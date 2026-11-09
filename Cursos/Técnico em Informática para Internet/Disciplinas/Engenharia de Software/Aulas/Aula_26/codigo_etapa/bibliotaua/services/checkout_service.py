"""
Serviço de Aplicação: CheckoutService
Orquestra a criação do pedido, validação de regras de cupom e persistência transacional.
"""
from typing import List, Tuple, Optional
import sqlite3

from bibliotaua.models.cliente import Cliente
from bibliotaua.models.livro import Livro
from bibliotaua.models.item_pedido import ItemPedido
from bibliotaua.models.pedido import Pedido, StatusPedido
from bibliotaua.repositories.cupom_repository import CupomRepository
from bibliotaua.repositories.livro_repository import LivroRepository
from bibliotaua.repositories.pedido_repository import PedidoRepository
from bibliotaua.services.calculadora_desconto import CalculadoraDescontoService

class CheckoutService:
    def __init__(self, conexao: sqlite3.Connection):
        self.conn = conexao
        self.cupom_repo = CupomRepository(conexao)
        self.livro_repo = LivroRepository(conexao)
        self.pedido_repo = PedidoRepository(conexao)

    def realizar_checkout(
        self,
        cliente: Cliente,
        itens_solicitados: List[Tuple[int, int]], # Lista de (livro_id, quantidade)
        codigo_cupom: Optional[str] = None
    ) -> Pedido:
        """
        Executa a transação completa de checkout da livraria:
        1. Validação de estoque para cada livro.
        2. Montagem dos itens do pedido.
        3. Busca e aplicação do cupom promocional (se fornecido).
        4. Gravação atômica no SQLite (pedido, itens, baixa de estoque e incremento do cupom).
        """
        itens_pedido: List[ItemPedido] = []

        # 1 e 2. Validar estoques e montar itens
        for livro_id, qtd in itens_solicitados:
            livro = self.livro_repo.buscar_por_id(livro_id)
            if not livro:
                raise ValueError(f"Livro com ID {livro_id} não encontrado.")
            livro.debitar_estoque(qtd) # Lança EstoqueInsuficienteError se não houver
            itens_pedido.append(ItemPedido(livro=livro, quantidade=qtd, preco_unitario=livro.preco))

        pedido = Pedido(cliente=cliente, itens=itens_pedido, status=StatusPedido.PAGO)

        # 3. Aplicar cupom se fornecido
        cupom = None
        if codigo_cupom:
            cupom = self.cupom_repo.buscar_por_codigo(codigo_cupom)
            desconto = CalculadoraDescontoService.validar_e_calcular(cupom, pedido.subtotal)
            pedido.desconto_aplicado = desconto
            pedido.cupom_aplicado = cupom

        # 4. Persistir transacionalmente
        with self.conn:
            # Salvar o pedido e itens
            self.pedido_repo.salvar(pedido)

            # Atualizar estoques no banco
            for item in pedido.itens:
                self.livro_repo.atualizar_estoque(item.livro.id, item.livro.estoque)

            # Registrar utilização do cupom se aplicável
            if cupom:
                self.cupom_repo.registrar_uso(cupom.codigo)

        return pedido
