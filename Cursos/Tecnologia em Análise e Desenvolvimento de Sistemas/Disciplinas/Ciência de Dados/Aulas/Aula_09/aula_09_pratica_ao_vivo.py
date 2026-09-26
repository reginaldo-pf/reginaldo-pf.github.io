"""
=============================================================================
AULA 09 — CIÊNCIA DE DADOS PARA ADS
LABORATÓRIO PRÁTICO AO VIVO: INTERVALOS DE CONFIANÇA E TESTES DE HIPÓTESES
=============================================================================
Este script contém a implementação em Python para a Aula 09, cobrindo:
1. Simulação Empírica (Bootstrap / Percentis) para o Teste da Moeda Viesada
2. Cálculo de Intervalos de Confiança Paramétricos (TCL) para o RSG de Alunos
3. Visualização da Distribuição Amostral e do Intervalo de Confiança
4. Sensibilidade do IC ao Nível de Confiança (z*) e ao Tamanho da Amostra (n)
5. Desafio de Código: Calculadora Automática de IC para Dados de ADS
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
print("1. ABORDAGEM EMPÍRICA: TESTE DA MOEDA VIESADA (22 CARAS EM 30 JOGADAS)")
print("=" * 70)

# Experimento: Moeda justa (P = 0.5), 30 lançamentos, 10.000 simulações
np.random.seed(42)
simulacoes_moeda = np.random.binomial(n=30, p=0.5, size=10000)

# Percentis empíricos de 95% (2.5% e 97.5%)
ic_empirico_low = np.percentile(simulacoes_moeda, 2.5)
ic_empirico_high = np.percentile(simulacoes_moeda, 97.5)

# Calculando o P-valor empírico de observar 22 ou mais caras
p_valor_empirico = np.mean(simulacoes_moeda >= 22)

print(f"Número de Caras Observado:     22 caras")
print(f"Média Esperada sob H0:         15 caras (30 * 0.5)")
print(f"Intervalo Empírico de 95%:     [{ic_empirico_low:.0f}, {ic_empirico_high:.0f}] caras")
print(f"P-Valor Observado (P >= 22):  {p_valor_empirico:.4f} ({p_valor_empirico:.2%})")

if p_valor_empirico < 0.05:
    print("▶ DECISÃO: Rejeitamos a hipótese nula (H0)! A moeda tem viés estatisticamente significante.")
else:
    print("▶ DECISÃO: Não rejeitamos a hipótese nula (H0).")
print()

print("=" * 70)
print("2. ABORDAGEM PARAMÉTRICA (TCL): IC DO RSG DOS ALUNOS DA UFMG")
print("=" * 70)

# Dados do Estudo de Caso da UFMG (n=50, mean=3.2, s=1.74)
n_alunos = 50
media_rsg = 3.2
sd_rsg = 1.74

# Passo 1: Erro Padrão (SE) = s / sqrt(n)
se_rsg = sd_rsg / np.sqrt(n_alunos)

# Passo 2: Nível de Confiança de 95% (z* = 1.96)
z_95 = stats.norm.ppf(0.975) # 1.95996
margem_erro = z_95 * se_rsg

# Passo 3: Limites do Intervalo de Confiança
ic_low = media_rsg - margem_erro
ic_high = media_rsg + margem_erro

print(f"Amostra (n):                   {n_alunos} alunos")
print(f"Média Amostral (xbar):         {media_rsg:.2f}")
print(f"Desvio Padrão Amostral (s):   {sd_rsg:.2f}")
print(f"Erro Padrão da Média (SE):    {se_rsg:.4f}")
print(f"Z-Score para 95% (z*):         {z_95:.4f}")
print(f"Margem de Erro (z* * SE):      {margem_erro:.4f}")
print(f"Intervalo de Confiança 95%:    ({ic_low:.2f}, {ic_high:.2f})")
print()

print("=" * 70)
print("3. ANÁLISE DE SENSIBILIDADE DO IC (VARIAÇÃO DE CONFIANÇA E N)")
print("=" * 70)

# Comparando Níveis de Confiança: 90%, 95%, 98%, 99%
niveis_confianca = [0.90, 0.95, 0.98, 0.99]
tabela_sensibilidade = []

for conf in niveis_confianca:
    z_val = stats.norm.ppf(1 - (1 - conf)/2)
    me = z_val * se_rsg
    tabela_sensibilidade.append({
        "Nível de Confiança": f"{conf:.0%}",
        "Valor Crítico (z*)": round(z_val, 3),
        "Margem de Erro": round(me, 3),
        "Intervalo de Confiança": f"({media_rsg - me:.2f}, {media_rsg + me:.2f})",
        "Largura Total do IC": round(2 * me, 3)
    })

df_sensibilidade = pd.DataFrame(tabela_sensibilidade)
print(df_sensibilidade.to_string(index=False))
print()

print("=" * 70)
print("4. DESAFIO PRÁTICO DE ADS: CALCULADORA AUTOMÁTICA DE IC")
print("=" * 70)

def calcular_ic_parametro(dados, confianca=0.95):
    """Calcula o Intervalo de Confiança paramétrico via TCL para um array de dados."""
    n = len(dados)
    xbar = np.mean(dados)
    s = np.std(dados, ddof=1) # Desvio amostral
    se = s / np.sqrt(n)
    z = stats.norm.ppf(1 - (1 - confianca)/2)
    margem = z * se
    return xbar, (xbar - margem, xbar + margem), margem

# Teste com dados simulados de tempo de resposta de API (ms)
np.random.seed(123)
tempo_resposta_api = np.random.normal(loc=120, scale=25, size=60)
mean_api, (ic_inf, ic_sup), me_api = calcular_ic_parametro(tempo_resposta_api, confianca=0.95)

print(f"Média Amostral da API:        {mean_api:.2f} ms")
print(f"IC de 95% do Tempo Médio:    ({ic_inf:.2f} ms, {ic_sup:.2f} ms)")
print(f"Margem de Erro:               ±{me_api:.2f} ms")
print("=" * 70)

# Gerando gráfico ilustrativo da Aula 09
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Simulação da Moeda Viesada e P-Valor
sns.histplot(simulacoes_moeda, discrete=True, ax=ax1, color="#0EA5E9", edgecolor="black")
ax1.axvline(22, color="#E11D48", linestyle="--", linewidth=2.5, label="Observado: 22 Caras (p < 0.05)")
ax1.axvline(15, color="#F59E0B", linestyle="-", linewidth=2, label="Esperado sob H0: 15 Caras")
ax1.set_title("1. Teste da Moeda Viesada (Abordagem Empírica)", fontweight="bold")
ax1.set_xlabel("Número de Caras em 30 Lançamentos")
ax1.set_ylabel("Frequência")
ax1.legend()

# Gráfico 2: Intervalo de Confiança do RSG (UFMG)
x_curve = np.linspace(2.0, 4.4, 500)
y_curve = stats.norm.pdf(x_curve, loc=media_rsg, scale=se_rsg)
ax2.plot(x_curve, y_curve, color="#1E293B", linewidth=2.5, label="Distribuição Amostral das Médias")
ax2.fill_between(x_curve, y_curve, where=(x_curve >= ic_low) & (x_curve <= ic_high), color="#0EA5E9", alpha=0.4, label="IC 95%: (2.71, 3.69)")
ax2.axvline(media_rsg, color="#F59E0B", linestyle="-", linewidth=2, label=f"Média Amostral = {media_rsg}")
ax2.set_title("2. Intervalo de Confiança Paramétrico (RSG UFMG)", fontweight="bold")
ax2.set_xlabel("Média Estimada do RSG")
ax2.set_ylabel("Densidade")
ax2.legend()

plt.tight_layout()
plt.savefig("/home/reginaldo/CDD/aula_09/graficos_aula_09.png", dpi=300)
print("▶ Gráfico salvo como 'graficos_aula_09.png'")
