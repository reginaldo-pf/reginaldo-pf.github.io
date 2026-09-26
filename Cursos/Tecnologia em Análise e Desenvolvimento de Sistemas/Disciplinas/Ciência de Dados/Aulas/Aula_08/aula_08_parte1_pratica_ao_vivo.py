"""
=============================================================================
AULA 08 (AULA 1 - 60 MINUTOS) — CIÊNCIA DE DADOS PARA ADS
LABORATÓRIO PRÁTICO: REVISÃO DE PROBABILIDADE, AMOSTRAGEM E MÉDIA
=============================================================================
Este script contém todos os exemplos numéricos, simulações de probabilidade,
amostragem e propriedades da média da Aula 1 (60 minutos).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)

print("=" * 70)
print("1. REVISÃO DE PROBABILIDADE: AXIOMAS, ADIÇÃO E MULTIPLICAÇÃO")
print("=" * 70)

# Simulação de 10.000 lançamentos de 2 moedas (HH, HT, TH, TT)
np.random.seed(42)
moeda1 = np.random.choice(['H', 'T'], size=10000)
moeda2 = np.random.choice(['H', 'T'], size=10000)

# Evento A: Pelo menos uma cara (H)
pelo_menos_uma_cara = (moeda1 == 'H') | (moeda2 == 'H')
prob_pelo_menos_uma_cara = np.mean(pelo_menos_uma_cara)

# Evento B: Exatamente uma cara e uma coroa (HT ou TH)
uma_cara_uma_coroa = (moeda1 != moeda2)
prob_uma_cara_uma_coroa = np.mean(uma_cara_uma_coroa)

print(f"P(Pelo menos uma Cara): {prob_pelo_menos_uma_cara:.2%} (Teórico: 3/4 = 75%)")
print(f"P(Exatamente 1H e 1T):   {prob_uma_cara_uma_coroa:.2%} (Teórico: 2/4 = 50%)")

# Regra da Adição: P(A u B) = P(A) + P(B) - P(A n B)
# P(17 anos) = 1.4%, P(18 anos) = 1.5% -> Mutuamente exclusivos
p_17 = 0.014
p_18 = 0.015
p_17_ou_18 = p_17 + p_18
print(f"P(Eleitor com 17 ou 18 anos): {p_17_ou_18:.1%} (Eventos Mutuamente Exclusivos)")

# Probabilidade Condicional e Multiplicação: Amostragem Sem Reposição
# Alunos {X, Y, Z}. P(Y primeiro e X segundo) = P(Y 1º) * P(X 2º | Y 1º) = (1/3) * (1/2) = 1/6
p_y_primeiro = 1/3
p_x_segundo_dado_y = 1/2
p_yx = p_y_primeiro * p_x_segundo_dado_y
print(f"P(Y primeiro E X segundo sem reposição): {p_yx:.4f} (1/6 = {1/6:.4f})")
print()

print("=" * 70)
print("2. AMOSTRAGEM ALEATÓRIA EM PYTHON (COM E SEM REPOSIÇÃO)")
print("=" * 70)

populacao_alunos = np.array(['Aluno_A', 'Aluno_B', 'Aluno_C', 'Aluno_D', 'Aluno_E'])

# Amostragem COM Reposição (Eventos Independentes)
amostra_com_reposicao = np.random.choice(populacao_alunos, size=3, replace=True)
print(f"Amostra COM Reposição (n=3): {amostra_com_reposicao}")

# Amostragem SEM Reposição (Eventos Dependentes)
amostra_sem_reposicao = np.random.choice(populacao_alunos, size=3, replace=False)
print(f"Amostra SEM Reposição (n=3): {amostra_sem_reposicao}")

# Amostragem em DataFrames do Pandas
df_usuarios = pd.DataFrame({
    'id': range(1, 1001),
    'plano': np.random.choice(['Free', 'Premium'], size=1000, p=[0.8, 0.2]),
    'ativo': np.random.choice([0, 1], size=1000, p=[0.3, 0.7])
})
amostra_df = df_usuarios.sample(n=5, random_state=42)
print("\nAmostra Aleatória de DataFrame Pandas (n=5):")
print(amostra_df)
print()

print("=" * 70)
print("3. PROPRIEDADES DA MÉDIA, PROPORÇÕES E HISTOGRAMA")
print("=" * 70)

not_symmetric = np.array([2, 3, 3, 9])
media = np.mean(not_symmetric)
mediana = np.median(not_symmetric)

print(f"Coleção {not_symmetric}:")
print(f"   Média (Smoother / Fundo Comum): R$ {media:.2f}")
print(f"   Mediana:                        R$ {mediana:.2f}")
print(f"   Proporção de dados < Média:     {np.mean(not_symmetric < media):.0%}")

# Proporção de Usuários Ativos (Média de Variável Binária)
taxa_retencao = df_usuarios['ativo'].mean()
print(f"▶ Taxa de Retenção de Usuários (df['ativo'].mean()): {taxa_retencao:.2%}")
print("=" * 70)
