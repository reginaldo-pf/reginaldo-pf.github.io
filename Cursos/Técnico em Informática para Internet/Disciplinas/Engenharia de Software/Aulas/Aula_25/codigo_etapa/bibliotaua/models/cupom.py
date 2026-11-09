"""
Entidade de Domínio: Cupom de Desconto (TASK-204 - Sprint 04)
Representa a regra de bonificação e promoção aplicável a pedidos de livros da BiblioTauá.
"""
from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
from typing import Optional, Union

from bibliotaua.exceptions import (
    CupomInativoError,
    CupomExpiradoError,
    CupomEsgotadoError,
    ValorMinimoNaoAtingidoError
)

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
        self.codigo = self.codigo.strip().upper()
        if not self.codigo:
            raise ValueError("O código do cupom não pode ser vazio.")
        if self.valor_desconto <= 0:
            raise ValueError("O valor de desconto deve ser estritamente positivo.")
        if self.tipo_desconto == TipoDesconto.PERCENTUAL and self.valor_desconto > 100:
            raise ValueError("O desconto percentual não pode ser superior a 100%.")
        if self.valor_minimo_pedido < 0:
            raise ValueError("O valor mínimo do pedido não pode ser negativo.")
        if self.limite_usos <= 0:
            raise ValueError("O limite de utilizações deve ser de no mínimo 1.")
        if self.usos_realizados < 0:
            raise ValueError("A contagem de utilizações não pode ser negativa.")

    def obter_data_validade(self) -> date:
        """Converte a validade para objeto date para comparação segura."""
        if isinstance(self.validade_ate, str):
            return datetime.strptime(self.validade_ate, "%Y-%m-%d").date()
        return self.validade_ate

    def esta_expirado(self, data_referencia: Optional[date] = None) -> bool:
        """Verifica se a data atual ultrapassou a validade estipulada."""
        hoje = data_referencia or date.today()
        return hoje > self.obter_data_validade()

    def atingiu_limite_usos(self) -> bool:
        """Verifica se todas as cotas do cupom já foram consumidas."""
        return self.usos_realizados >= self.limite_usos

    def pode_ser_aplicado_ao_pedido(self, subtotal: float, data_referencia: Optional[date] = None) -> None:
        """
        Valida todas as regras de negócio especificadas na DUC UC04.
        Lança exceções específicas para cada fluxo de exceção violado.
        """
        if not self.ativo:
            raise CupomInativoError(self.codigo)

        if self.esta_expirado(data_referencia):
            validade_str = self.obter_data_validade().strftime("%d/%m/%Y")
            raise CupomExpiradoError(self.codigo, validade_str)

        if self.atingiu_limite_usos():
            raise CupomEsgotadoError(self.codigo, self.limite_usos)

        if subtotal < self.valor_minimo_pedido:
            raise ValorMinimoNaoAtingidoError(self.codigo, self.valor_minimo_pedido, subtotal)

    def calcular_desconto(self, subtotal: float, data_referencia: Optional[date] = None) -> float:
        """
        Calcula o abatimento financeiro com base no tipo do cupom.
        Executa a validação prévia de todas as regras de negócio da DUC UC04.
        Garante que o desconto nunca ultrapasse o subtotal (não gera saldo negativo).
        """
        self.pode_ser_aplicado_ao_pedido(subtotal, data_referencia)

        if self.tipo_desconto == TipoDesconto.PERCENTUAL:
            desconto = (subtotal * self.valor_desconto) / 100.0
        else:
            desconto = self.valor_desconto

        # Regra de negócio: o desconto é limitado ao subtotal da compra
        return round(min(desconto, subtotal), 2)

    def registrar_uso(self) -> None:
        """Incrementa o contador de utilizações respeitando o limite."""
        if self.atingiu_limite_usos():
            raise CupomEsgotadoError(self.codigo, self.limite_usos)
        self.usos_realizados += 1
