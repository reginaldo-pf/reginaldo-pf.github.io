"""
Repositório de Persistência SQLite: PedidoRepository
"""
import sqlite3
from typing import Optional, List
from bibliotaua.models.pedido import Pedido, StatusPedido
from bibliotaua.models.cliente import Cliente
from bibliotaua.models.item_pedido import ItemPedido
from bibliotaua.models.livro import Livro
from bibliotaua.models.cupom import Cupom, TipoDesconto

class PedidoRepository:
    def __init__(self, conexao: sqlite3.Connection):
        self.conn = conexao

    def salvar(self, pedido: Pedido) -> Pedido:
        with self.conn:
            cupom_id = pedido.cupom_aplicado.id if pedido.cupom_aplicado else None
            cursor = self.conn.execute("""
                INSERT INTO pedidos (
                    cliente_id, cupom_id, subtotal, desconto_aplicado, total, status, data_criacao
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                pedido.cliente.id,
                cupom_id,
                pedido.subtotal,
                pedido.desconto_aplicado,
                pedido.total,
                pedido.status.value,
                pedido.data_criacao.strftime("%Y-%m-%d %H:%M:%S")
            ))
            pedido.id = cursor.lastrowid

            # Salva os itens do pedido
            for item in pedido.itens:
                self.conn.execute("""
                    INSERT INTO itens_pedido (pedido_id, livro_id, quantidade, preco_unitario, subtotal)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    pedido.id,
                    item.livro.id,
                    item.quantidade,
                    item.preco_unitario,
                    item.subtotal
                ))
        return pedido

    def buscar_por_id(self, pedido_id: int) -> Optional[Pedido]:
        cursor = self.conn.execute("""
            SELECT p.*, c.nome as cliente_nome, c.email as cliente_email, c.matricula as cliente_matricula,
                   cup.codigo as cupom_codigo, cup.tipo_desconto as cupom_tipo, cup.valor_desconto as cupom_valor
            FROM pedidos p
            JOIN clientes c ON p.cliente_id = c.id
            LEFT JOIN cupons cup ON p.cupom_id = cup.id
            WHERE p.id = ?
        """, (pedido_id,))
        row = cursor.fetchone()
        if not row:
            return None

        cliente = Cliente(
            id=row["cliente_id"],
            nome=row["cliente_nome"],
            email=row["cliente_email"],
            matricula=row["cliente_matricula"]
        )

        cupom = None
        if row["cupom_id"]:
            cupom = Cupom(
                id=row["cupom_id"],
                codigo=row["cupom_codigo"],
                tipo_desconto=TipoDesconto(row["cupom_tipo"]),
                valor_desconto=float(row["cupom_valor"])
            )

        # Buscar itens
        itens_cursor = self.conn.execute("""
            SELECT ip.*, l.titulo, l.autor, l.isbn, l.preco, l.estoque, l.categoria
            FROM itens_pedido ip
            JOIN livros l ON ip.livro_id = l.id
            WHERE ip.pedido_id = ?
        """, (pedido_id,))

        itens = []
        for i_row in itens_cursor.fetchall():
            livro = Livro(
                id=i_row["livro_id"],
                titulo=i_row["titulo"],
                autor=i_row["autor"],
                isbn=i_row["isbn"],
                preco=float(i_row["preco"]),
                estoque=int(i_row["estoque"]),
                categoria=i_row["categoria"]
            )
            itens.append(ItemPedido(livro=livro, quantidade=i_row["quantidade"], preco_unitario=i_row["preco_unitario"]))

        pedido = Pedido(
            id=row["id"],
            cliente=cliente,
            itens=itens,
            cupom_aplicado=cupom,
            desconto_aplicado=float(row["desconto_aplicado"]),
            status=StatusPedido(row["status"])
        )
        return pedido
