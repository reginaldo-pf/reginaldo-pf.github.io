"""
Entidade de Domínio: Pedido (Agregado Raiz da Compra de Livros)
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional

from bibliotaua.models.cliente import Cliente
from bibliotaua.models.cupom import Cupom
from bibliotaua.models.item_pedido import ItemPedido

class StatusPedido(str, Enum):
    CRIADO = "CRIADO"
    AGUARDANDO_PAGAMENTO = "AGUARDANDO_PAGAMENTO"
    PAGO = "PAGO"
    CANCELADO = "CANCELADO"
    FINALIZADO = "FINALIZADO"

@dataclass
class Pedido:
    cliente: Cliente
    itens: List[ItemPedido] = field(default_factory=list)
    cupom_aplicado: Optional[Cupom] = None
    desconto_aplicado: float = 0.0
    status: StatusPedido = StatusPedido.CRIADO
    data_criacao: datetime = field(default_factory=datetime.now)
    id: Optional[int] = None

    def adicionar_item(self, item: ItemPedido) -> None:
        self.itens.append(item)
        # Se um cupom já estiver aplicado, revalida o desconto com o novo subtotal
        if self.cupom_aplicado:
            self.aplicar_cupom(self.cupom_aplicado)

    @property
    def subtotal(self) -> float:
        """Soma o subtotal de todos os itens."""
        return round(sum(item.subtotal for item in self.itens), 2)

    @property
    def total(self) -> float:
        """Valor final líquido a pagar pelo cliente."""
        liquido = self.subtotal - self.desconto_aplicado
        return round(max(liquido, 0.0), 2)

    def aplicar_cupom(self, cupom: Cupom) -> None:
        """
        Aplica o cupom de desconto ao pedido após validação rigorosa.
        """
        if not self.itens:
            raise ValueError("Não é possível aplicar cupom a um pedido vazio sem itens.")

        # Valida as regras de negócio do cupom
        cupom.pode_ser_aplicado_ao_pedido(self.subtotal)

        # Calcula o abatimento e registra no pedido
        self.desconto_aplicado = cupom.calcular_desconto(self.subtotal)
        self.cupom_aplicado = cupom

    def remover_cupom(self) -> None:
        """Remove o cupom aplicado e restaura o total original."""
        self.cupom_aplicado = None
        self.desconto_aplicado = 0.0
