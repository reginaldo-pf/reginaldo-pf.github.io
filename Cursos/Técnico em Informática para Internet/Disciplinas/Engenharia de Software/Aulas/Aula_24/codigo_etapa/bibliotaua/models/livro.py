"""
Entidade de Domínio: Livro (Acervo e Catálogo da BiblioTauá)
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Livro:
    id: Optional[int]
    titulo: str
    autor: str
    isbn: str
    preco: float
    estoque: int
    categoria: str = "Didático"

    def __post_init__(self):
        if self.preco < 0:
            raise ValueError("O preço do livro não pode ser negativo.")
        if self.estoque < 0:
            raise ValueError("O estoque do livro não pode ser negativo.")

    def debitar_estoque(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade a debitar deve ser maior que zero.")
        if self.estoque < quantidade:
            from bibliotaua.exceptions import EstoqueInsuficienteError
            raise EstoqueInsuficienteError(self.titulo, self.estoque, quantidade)
        self.estoque -= quantidade

    def repor_estoque(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade a repor deve ser positiva.")
        self.estoque += quantidade
