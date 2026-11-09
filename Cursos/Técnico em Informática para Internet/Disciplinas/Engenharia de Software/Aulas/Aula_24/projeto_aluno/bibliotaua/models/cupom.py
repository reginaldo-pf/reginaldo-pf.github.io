"""
Entidade de Domínio: Cupom de Desconto (TASK-204 - Sprint 04)
Representa a regra de bonificação e promoção aplicável a pedidos de livros da BiblioTauá.

Instruções para o Aluno (Aula 24):
Consulte os Slides 13, 14 e 15 e o guia_desenvolvedor.md para implementar:
1. Validações de integridade no __post_init__
2. Métodos de domínio: esta_expirado, atingiu_limite_usos, pode_ser_aplicado_ao_pedido,
   calcular_desconto e registrar_uso.
"""
from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
from typing import Optional, Union

# Import das exceções (implementadas pelo aluno em bibliotaua/exceptions.py)
try:
    from bibliotaua.exceptions import (
        CupomInvalidoError,
        CupomInativoError,
        CupomExpiradoError,
        CupomEsgotadoError,
        ValorMinimoNaoAtingidoError
    )
except ImportError:
    pass

class TipoDesconto(str, Enum):
    """Enumeração para categorizar a modalidade matemática de desconto."""
    PERCENTUAL = "PERCENTUAL"
    VALOR_FIXO = "VALOR_FIXO"


@dataclass
class Cupom:
    """
    Entidade Cupom construída a partir da especificação DUC UC04 e do Diagrama de Classes.
    """
    codigo: str
    tipo_desconto: TipoDesconto
    valor_desconto: float
    valor_minimo_pedido: float = 0.0
    limite_usos: int = 100
    usos_realizados: int = 0
    validade_ate: Union[str, date] = "2026-12-31"
    ativo: bool = True
    id: Optional[int] = None

    def __post_init__(self):
        # Normalização do código
        self.codigo = self.codigo.strip().upper()

        # ==============================================================================
        # TODO: [ALUNO - TAREFA 2.1] Validações de integridade dos atributos (Slide 13)
        # ==============================================================================
        # 1. Se self.codigo for vazio -> raise ValueError("O código do cupom não pode ser vazio.")
        # 2. Se self.valor_desconto <= 0 -> raise ValueError("O valor de desconto deve ser estritamente positivo.")
        # 3. Se tipo PERCENTUAL e valor_desconto > 100 -> raise ValueError("O desconto percentual não pode ser superior a 100%.")
        # 4. Se self.valor_minimo_pedido < 0 -> raise ValueError("O valor mínimo do pedido não pode ser negativo.")
        # 5. Se self.limite_usos <= 0 -> raise ValueError("O limite de utilizações deve ser de no mínimo 1.")
        # 6. Se self.usos_realizados < 0 -> raise ValueError("A contagem de utilizações não pode ser negativa.")
        pass

    def obter_data_validade(self) -> date:
        """Converte a validade para objeto date para comparação segura."""
        if isinstance(self.validade_ate, str):
            return datetime.strptime(self.validade_ate, "%Y-%m-%d").date()
        return self.validade_ate

    def esta_expirado(self, data_referencia: Optional[date] = None) -> bool:
        """
        TODO: [ALUNO - TAREFA 2.2]
        Verifica se a data atual (ou data_referencia) ultrapassou a data estipulada em obter_data_validade().
        Retorna True se estiver expirado, False caso contrário. (Slide 14)
        """
        raise NotImplementedError("TODO: Implementar método esta_expirado")

    def atingiu_limite_usos(self) -> bool:
        """
        TODO: [ALUNO - TAREFA 2.3]
        Verifica se a quantidade de usos realizados atingiu ou superou o limite de usos permitidos.
        Retorna True se esgotado, False caso contrário. (Slide 14)
        """
        raise NotImplementedError("TODO: Implementar método atingiu_limite_usos")

    def pode_ser_aplicado_ao_pedido(self, subtotal: float, data_referencia: Optional[date] = None) -> None:
        """
        TODO: [ALUNO - TAREFA 2.4]
        Valida todas as regras de negócio especificadas na DUC UC04.
        Lança exceções específicas para cada fluxo de exceção violado:
        - Se not self.ativo -> raise CupomInativoError(self.codigo)
        - Se self.esta_expirado(data_referencia) -> raise CupomExpiradoError(...)
        - Se self.atingiu_limite_usos() -> raise CupomEsgotadoError(...)
        - Se subtotal < self.valor_minimo_pedido -> raise ValorMinimoNaoAtingidoError(...)
        (Consulte o Slide 15)
        """
        raise NotImplementedError("TODO: Implementar método pode_ser_aplicado_ao_pedido")

    def calcular_desconto(self, subtotal: float, data_referencia: Optional[date] = None) -> float:
        """
        TODO: [ALUNO - TAREFA 2.5]
        1. Invoca self.pode_ser_aplicado_ao_pedido(subtotal, data_referencia)
        2. Se tipo_desconto == PERCENTUAL -> desconto = (subtotal * valor_desconto) / 100.0
           Senão -> desconto = valor_desconto
        3. Retorna round(min(desconto, subtotal), 2), garantindo teto no subtotal.
        (Consulte o Slide 15)
        """
        raise NotImplementedError("TODO: Implementar método calcular_desconto")

    def registrar_uso(self) -> None:
        """
        TODO: [ALUNO - TAREFA 2.6]
        Incrementa o contador usos_realizados em 1 se não atingiu o limite.
        (Consulte o Slide 14)
        """
        raise NotImplementedError("TODO: Implementar método registrar_uso")
