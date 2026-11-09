"""
Entidade de Domínio: ItemPedido (Linha de Composição do Pedido)
"""
from dataclasses import dataclass
from bibliotaua.models.livro import Livro

@dataclass
class ItemPedido:
    livro: Livro
    quantidade: int
    preco_unitario: float

    def __post_init__(self):
        if self.quantidade <= 0:
            raise ValueError("A quantidade do item deve ser no mínimo 1.")
        if self.preco_unitario < 0:
            raise ValueError("O preço unitário não pode ser negativo.")

    @property
    def subtotal(self) -> float:
        return round(self.quantidade * self.preco_unitario, 2)
