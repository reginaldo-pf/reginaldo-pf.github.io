"""
=============================================================================
AULA 08 (PARTE 1) — CIÊNCIA DE DADOS PARA ADS
LABORATÓRIO PRÁTICO AO VIVO: PROPRIEDADES E INTERPRETAÇÃO DA MÉDIA
=============================================================================
Este script contém todos os exemplos numéricos, gráficos e aplicações da
Aula 08 (Parte 1) para execução durante a aula.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)

print("=" * 70)
print("1. EXEMPLO 1: A MÉDIA COMO 'EQUALIZADOR' (SMOOTHER)")
print("=" * 70)
# Coleção dos slides: 4 pessoas com $2, $3, $3 e $9
not_symmetric = np.array([2, 3, 3, 9])
total_dinheiro = np.sum(not_symmetric)
media_dinheiro = np.mean(not_symmetric)

print(f"Valores individuais nas carteiras: {not_symmetric}")
print(f"Total arrecadado no fundo comum:  R$ {total_dinheiro:.2f}")
print(f"Valor redistribuído (Média):     R$ {media_dinheiro:.2f}")
print()

print("=" * 70)
print("2. EXEMPLO 2: PROPORÇÕES SÃO MÉDIAS (DADOS BINÁRIOS / BOOLEANOS)")
print("=" * 70)
# Array binário [1, 1, 1, 0]
zero_one = np.array([1, 1, 1, 0])
print(f"Array Binário:            {zero_one}")
print(f"Soma dos 1s (Sucessos):   {np.sum(zero_one)}")
print(f"Média (Proporção de 1s):  {np.mean(zero_one):.2%}")

# Array booleano [True, True, True, False]
bool_array = np.array([True, True, True, False])
print(f"Média do Array Booleano:  {np.mean(bool_array):.2%}")
print()

# Aplicação Prática ADS: Taxa de Clique (CTR) em Log Web
np.random.seed(42)
cliques = np.random.choice([0, 1], size=1000, p=[0.85, 0.15])
df_web = pd.DataFrame({"usuario_id": range(1000), "clicou": cliques})
ctr = df_web["clicou"].mean()
print(f"▶ Aplicação ADS (Log Web com 1.000 requisições):")
print(f"   Total de cliques: {df_web['clicou'].sum()}")
print(f"   Taxa de Clique (CTR = df['clicou'].mean()): {ctr:.2%}")
print()

print("=" * 70)
print("3. EXEMPLO 3: A MÉDIA DEPENDE APENAS DA DISTRIBUIÇÃO RELATIVA")
print("=" * 70)
colecao_A = np.array([2, 3, 3, 9])
colecao_B = np.array([2, 2, 3, 3, 3, 3, 9, 9])

print(f"Coleção A (N={len(colecao_A)}): {colecao_A} -> Média = {np.mean(colecao_A)}")
print(f"Coleção B (N={len(colecao_B)}): {colecao_B} -> Média = {np.mean(colecao_B)}")
print("Conclusão: Duas coleções com a mesma distribuição proporcional possuem a MESMA média.")
print()

print("=" * 70)
print("4. EXEMPLO 4: MÉDIA VS. MEDIANA E O MITO DO 'ABAIXO DA MÉDIA'")
print("=" * 70)
simetrica = np.array([2, 3, 3, 4])
nao_simetrica = np.array([2, 3, 3, 9])

print(f"Simétrica {simetrica}:")
print(f"   Média = {np.mean(simetrica):.2f} | Mediana = {np.median(simetrica):.2f}")
print(f"Assimétrica {nao_simetrica}:")
print(f"   Média = {np.mean(nao_simetrica):.2f} | Mediana = {np.median(nao_simetrica):.2f}")
pct_abaixo = np.mean(nao_simetrica < np.mean(nao_simetrica))
print(f"   Proporção de elementos < Média (4.25): {pct_abaixo:.0%}")
print("   -> Na coleção assimétrica, 75% dos dados estão ABAIXO da média!")
print()

print("=" * 70)
print("5. ESTUDO DE CASO REAL: SALÁRIOS EM SAN FRANCISCO (SF 2015)")
print("=" * 70)
np.random.seed(42)
base_salarios = np.random.lognormal(mean=11.5, sigma=0.5, size=5000)
salarios_sf = base_salarios[(base_salarios >= 10000) & (base_salarios <= 700000)]

media_sf = np.mean(salarios_sf)
mediana_sf = np.median(salarios_sf)

print(f"Mediana do Salário: R$ {mediana_sf:,.2f}  (Salário Típico)")
print(f"Média do Salário:   R$ {media_sf:,.2f}  (Puxada pela cauda longa de altos salários)")
print(f"Diferença (Distorção): R$ {(media_sf - mediana_sf):,.2f}")
print()

print("=" * 70)
print("6. DESAFIO PRÁTICO DE ADS: LATÊNCIA DE API DE PAGAMENTO")
print("=" * 70)
np.random.seed(123)
# 95% requisições rápidas (50-150ms), 5% timeouts/lentas (2000-5000ms)
latencias_normais = np.random.normal(loc=100, scale=20, size=950)
latencias_lentas = np.random.uniform(low=2000, high=5000, size=50)
latencias_api = np.concatenate([latencias_normais, latencias_lentas])

media_lat = np.mean(latencias_api)
mediana_lat = np.median(latencias_api)

print(f"Média de Latência:   {media_lat:.2f} ms  (Distorcida pelos 5% de requisições lentas)")
print(f"Mediana de Latência: {mediana_lat:.2f} ms  (Reflete a latência do usuário típico)")
print("Recomendação para SLA em ADS: Usar Mediana (ou Percentil 95/99) para SLA de Usuário,")
print("e Média para Dimensionamento do Consumo Total do Servidor.")
print("=" * 70)

# Gerando gráfico do Centro de Gravidade
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Grafico 1: Centro de Gravidade {2, 3, 3, 9}
bins = np.arange(1.5, 10.5, 1)
ax1.hist(colecao_A, bins=bins, density=True, color="#0EA5E9", edgecolor="#1E293B", alpha=0.7, rwidth=0.9)
ax1.scatter(media_dinheiro, 0, color="#F59E0B", s=250, marker="^", zorder=5, label=f"Média = {media_dinheiro}")
ax1.axhline(0, color="black", linewidth=2)
ax1.set_xticks(range(2, 10))
ax1.set_title("1. Média como Centro de Gravidade {2, 3, 3, 9}", fontweight="bold")
ax1.set_xlabel("Valores")
ax1.set_ylabel("Proporção")
ax1.legend()

# Grafico 2: Assimetria Salários SF
sns.histplot(salarios_sf, bins=35, kde=True, ax=ax2, color="#0EA5E9", edgecolor="black")
ax2.axvline(mediana_sf, color="#E11D48", linestyle="--", linewidth=2.5, label=f"Mediana: R$ {mediana_sf:,.0f}")
ax2.axvline(media_sf, color="#F59E0B", linestyle="-", linewidth=2.5, label=f"Média: R$ {media_sf:,.0f}")
ax2.set_title("2. Distribuição de Salários (Right Skewed)", fontweight="bold")
ax2.set_xlabel("Salário (R$)")
ax2.set_ylabel("Frequência")
ax2.legend()

plt.tight_layout()
plt.savefig("graficos_pratica_aula.png", dpi=300)
print("▶ Gráfico salvo como 'graficos_pratica_aula.png'")
