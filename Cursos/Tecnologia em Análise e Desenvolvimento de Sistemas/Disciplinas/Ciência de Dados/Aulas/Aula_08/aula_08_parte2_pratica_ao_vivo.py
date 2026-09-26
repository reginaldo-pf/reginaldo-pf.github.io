"""
=============================================================================
AULA 08 (PARTE 2) — CIÊNCIA DE DADOS PARA ADS
LABORATÓRIO PRÁTICO AO VIVO: VARIABILIDADE, CURVA NORMAL, TLC E TAMANHO DE AMOSTRA
=============================================================================
Este script contém todos os exemplos numéricos, simulações estatísticas,
gráficos e desafios de código da Aula 08 (Parte 2).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configuração visual dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)

print("=" * 70)
print("1. MÓDULO 1: CÁLCULO DO DESVIO PADRÃO (SD) E SCORE-Z")
print("=" * 70)

# Array simples any_numbers dos slides
any_numbers = np.array([1, 2, 2, 10])
media = np.mean(any_numbers)
desvios = any_numbers - media
desvios_quad = desvios ** 2
variancia = np.mean(desvios_quad)
sd = np.sqrt(variancia)

print(f"Valores:           {any_numbers}")
print(f"Média:             {media:.2f}")
print(f"Desvios (x - xbar):{desvios}")
print(f"Desvios²:          {desvios_quad}")
print(f"Variância (msd):   {variancia:.2f}")
print(f"Desvio Padrão (SD):{sd:.2f} (np.std = {np.std(any_numbers):.2f})")

# Unidades Padrão (Z-Scores)
z_scores = (any_numbers - media) / sd
print(f"Z-Scores:          {z_scores.round(2)}")
print()

print("=" * 70)
print("2. MÓDULO 2: CURVA NORMAL E REGRA EMPÍRICA (68-95-99.7)")
print("=" * 70)

# Exemplo de alturas de mães (Média = 64 polegadas, SD = 2.5 polegadas)
np.random.seed(42)
alturas_maes = np.random.normal(loc=64, scale=2.5, size=1174)

media_mae = np.mean(alturas_maes)
sd_mae = np.std(alturas_maes)

print(f"Média das Alturas: {media_mae:.2f} polegadas")
print(f"SD das Alturas:    {sd_mae:.2f} polegadas")

# Probabilidades acumuladas com a CDF (norm.cdf)
pct_1sd = stats.norm.cdf(1) - stats.norm.cdf(-1)
pct_2sd = stats.norm.cdf(2) - stats.norm.cdf(-2)
pct_3sd = stats.norm.cdf(3) - stats.norm.cdf(-3)

print(f"Área em Média ± 1 SD: {pct_1sd:.2%} (Esperado: ~68%)")
print(f"Área em Média ± 2 SD: {pct_2sd:.2%} (Esperado: ~95%)")
print(f"Área em Média ± 3 SD: {pct_3sd:.2%} (Esperado: ~99.7%)")
print()

print("=" * 70)
print("3. MÓDULO 3: TEOREMA DO LIMITE CENTRAL (TLC) NA PRÁTICA")
print("=" * 70)

# População altamente assimétrica (Atrasos de Voos em minutos)
pop_atrasos = np.random.exponential(scale=15, size=10000)

# Simulando o TLC: Extrair 10.000 amostras aleatórias de tamanho N=100
tamanhos_amostra = [5, 30, 100]
medias_amostrais = {}

for n in tamanhos_amostra:
    # Extrai 10.000 médias de amostras de tamanho n
    amostras = np.random.choice(pop_atrasos, size=(10000, n))
    medias_amostrais[n] = np.mean(amostras, axis=1)

print(f"Média Populacional Real: {np.mean(pop_atrasos):.2f} min")
print(f"SD Populacional Real:    {np.std(pop_atrasos):.2f} min")
print()
for n in tamanhos_amostra:
    print(f"N={n:3d} -> Média das Médias: {np.mean(medias_amostrais[n]):.2f} | SD das Médias: {np.std(medias_amostrais[n]):.2f}")
print()

print("=" * 70)
print("4. MÓDULO 4: A LEI DA RAIZ QUADRADA (ACCURACY VS SAMPLE SIZE)")
print("=" * 70)

sd_pop = np.std(pop_atrasos)
sd_teorico_25 = sd_pop / np.sqrt(25)
sd_teorico_100 = sd_pop / np.sqrt(100)

print(f"SD da População:                  {sd_pop:.2f}")
print(f"SD das Médias Amostrais (N=25):   {sd_teorico_25:.2f}")
print(f"SD das Médias Amostrais (N=100):  {sd_teorico_100:.2f}")
print(f"Fator de Redução do SD ao quadruplicar N (de 25 para 100): {sd_teorico_25 / sd_teorico_100:.2f}x (sqrt(4) = 2)")
print()

print("=" * 70)
print("5. MÓDULO 5: ESCOLHA DO TAMANHO DE AMOSTRA (CANDIDATO A)")
print("=" * 70)

# O SD máximo para uma variável binária (0-1) ocorre quando P = 0.5 -> SD = 0.5
sd_max_binario = 0.5
margem_erro_desejada = 0.01 # 1% de largura total = +/- 0.5% (4 * SD / sqrt(n) <= 0.01)

# 4 * (0.5 / sqrt(n)) <= 0.01  => sqrt(n) >= 200 => n >= 40.000
n_minimo = (4 * sd_max_binario / margem_erro_desejada) ** 2

print(f"Margem de Erro de Largura Total Tolerada: {margem_erro_desejada:.1%}")
print(f"SD Máximo Possível para População 0-1:    {sd_max_binario}")
print(f"Tamanho de Amostra Mínimo Garantido (N): {n_minimo:,.0f} eleitores")
print("=" * 70)

# Gerando gráficos explicativos da Parte 2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: TLC em Ação (População Assimétrica vs Distribuição das Médias)
sns.histplot(pop_atrasos, bins=30, kde=True, ax=ax1, color="#F59E0B", edgecolor="black")
ax1.set_title("1. População Original (Fortemente Assimétrica)", fontweight="bold")
ax1.set_xlabel("Atraso de Voos (minutos)")

sns.histplot(medias_amostrais[100], bins=30, kde=True, ax=ax2, color="#0EA5E9", edgecolor="black")
ax2.set_title("2. Distribuição das Médias Amostrais (N=100) -> NORMAL!", fontweight="bold")
ax2.set_xlabel("Média Amostral de Atrasos (minutos)")

plt.tight_layout()
plt.savefig("graficos_pratica_aula_parte2.png", dpi=300)
print("▶ Gráfico salvo como 'graficos_pratica_aula_parte2.png'")
