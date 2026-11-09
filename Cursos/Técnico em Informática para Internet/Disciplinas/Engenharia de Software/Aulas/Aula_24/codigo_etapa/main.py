"""
Ponto de Entrada e Teste da Implementação - Aula 24
Livraria BiblioTauá (Sprint 04 - TASK-204)
"""
from datetime import date, timedelta
from bibliotaua.models.cupom import Cupom, TipoDesconto
from bibliotaua.exceptions import ValorMinimoNaoAtingidoError

def main():
    print("--- Testando a Entidade Cupom (BiblioTauá) ---")

    # 1. Instanciando cupom de 10% (mínimo R$ 50)
    cupom = Cupom(
        codigo="BEMVINDO10",
        tipo_desconto=TipoDesconto.PERCENTUAL,
        valor_desconto=10.0,
        valor_minimo_pedido=50.0,
        validade_ate=date.today() + timedelta(days=5)
    )
    print(f"Cupom: {cupom.codigo} ({cupom.valor_desconto}% OFF)")

    # 2. Teste válido (R$ 100.00)
    desconto = cupom.calcular_desconto(100.0)
    print(f"Subtotal R$ 100.00 -> Desconto: R$ {desconto:.2f}")

    # 3. Teste abaixo do mínimo (R$ 30.00)
    try:
        cupom.calcular_desconto(30.0)
    except ValorMinimoNaoAtingidoError as erro:
        print(f"Subtotal R$ 30.00  -> Bloqueado: {erro}")

if __name__ == "__main__":
    main()
