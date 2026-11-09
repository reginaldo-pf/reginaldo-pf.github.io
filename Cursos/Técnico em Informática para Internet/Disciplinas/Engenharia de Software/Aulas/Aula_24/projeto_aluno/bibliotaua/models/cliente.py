"""
Entidade de Domínio: Cliente (Leitor / Comprador da BiblioTauá)
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    id: Optional[int]
    nome: str
    email: str
    matricula: str
    ativo: bool = True

    def __post_init__(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        if not self.matricula or not self.matricula.strip():
            raise ValueError("A matrícula do aluno/cliente não pode ser vazia.")
