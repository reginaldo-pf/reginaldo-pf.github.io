"""
Serviço de Domínio: CalculadoraDescontoService (TASK-204)
Encapsula o motor de regras de negócio de aplicação e cálculo de abatimentos da BiblioTauá.
"""
from datetime import date
from typing import Optional
from bibliotaua.models.cupom import Cupom

class CalculadoraDescontoService:
    @staticmethod
    def validar_e_calcular(
        cupom: Cupom,
        subtotal: float,
        data_referencia: Optional[date] = None
    ) -> float:
        """
        Valida a elegibilidade do cupom e calcula o valor em Reais a ser descontado.
        Lança exceções de domínio apropriadas caso as regras sejam violadas.
        """
        cupom.pode_ser_aplicado_ao_pedido(subtotal, data_referencia=data_referencia)
        return cupom.calcular_desconto(subtotal)
