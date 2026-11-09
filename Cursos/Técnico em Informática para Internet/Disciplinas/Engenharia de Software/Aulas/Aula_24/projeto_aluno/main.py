"""
Ponto de Entrada e Teste da Implementação - Aula 24
Livraria BiblioTauá (Sprint 04 - TASK-204)

Instruções para o Aluno:
Após implementar bibliotaua/exceptions.py e bibliotaua/models/cupom.py,
complete o código abaixo conforme apresentado no Slide 15 para testar o cupom.
"""
from datetime import date, timedelta
from bibliotaua.models.cupom import Cupom, TipoDesconto
from bibliotaua.exceptions import ValorMinimoNaoAtingidoError

def main():
    print("--- Testando a Entidade Cupom (BiblioTauá) ---")

    # TODO: [ALUNO] 1. Instancie o cupom 'BEMVINDO10' (10%, mínimo R$ 50.00, validade 5 dias)
    # TODO: [ALUNO] 2. Teste o cálculo de desconto para subtotal de R$ 100.00
    # TODO: [ALUNO] 3. Teste a regra de valor mínimo para subtotal de R$ 30.00 dentro de try/except

if __name__ == "__main__":
    main()
