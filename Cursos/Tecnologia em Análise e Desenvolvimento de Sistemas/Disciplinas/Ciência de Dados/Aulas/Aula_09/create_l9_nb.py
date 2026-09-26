import json

notebook = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Aula 09 — Ciência de Dados para ADS\n",
        "## Laboratório Prático Ao Vivo: Intervalos de Confiança Paramétricos e Testes de Hipóteses\n",
        "\n",
        "Este notebook contém todas as simulações empíricas e equações paramétricas da **Aula 09**.\n",
        "Ele aborda o Teste de Hipóteses da **Moeda Viesada** (via simulação/percentis), o Intervalo de Confiança do **RSG de Alunos da UFMG** (via Teorema do Limite Central), a análise do **Estudo da COVID-19 da UFPel**, e um **Desafio Prático de ADS** para calculadoras de ICs de latência de software."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 1. Configuração do Ambiente e Importações\n",
        "Importando `numpy`, `pandas`, `matplotlib`, `seaborn` e `scipy.stats`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from scipy import stats\n",
        "\n",
        "sns.set_theme(style=\"whitegrid\")\n",
        "plt.rcParams[\"figure.figsize\"] = (9, 5)\n",
        "print(\"✅ Ambiente da Aula 09 configurado com sucesso!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 2. Abordagem 1: Teste de Hipótese Empírico via Simulação (Moeda Viesada)\n",
        "**Problema:** Lançamos uma moeda 30 vezes e obtivemos **22 caras**. A moeda é justa ou tem viés?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "np.random.seed(42)\n",
        "simulacoes_moeda = np.random.binomial(n=30, p=0.5, size=10000)\n",
        "\n",
        "ic_low = np.percentile(simulacoes_moeda, 2.5)\n",
        "ic_high = np.percentile(simulacoes_moeda, 97.5)\n",
        "p_valor = np.mean(simulacoes_moeda >= 22)\n",
        "\n",
        "print(f\"Intervalo Empírico de 95% sob H0: [{ic_low:.0f}, {ic_high:.0f}] caras\")\n",
        "print(f\"P-Valor (Probabilidade de observar >= 22 caras): {p_valor:.4f} ({p_valor:.2%})\")\n",
        "print(\"Conclusão: Rejeitamos H0 com p < 0.05. A moeda tem viés significante!\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "fig, ax = plt.subplots(figsize=(9, 4.5))\n",
        "sns.histplot(simulacoes_moeda, discrete=True, ax=ax, color=\"#0EA5E9\", edgecolor=\"black\")\n",
        "ax.axvline(22, color=\"#E11D48\", linestyle=\"--\", linewidth=2.5, label=\"Observado: 22 Caras (p = 0.69%)\")\n",
        "ax.axvline(15, color=\"#F59E0B\", linestyle=\"-\", linewidth=2, label=\"Esperado sob H0: 15 Caras\")\n",
        "ax.set_title(\"Distribuição Empírica de 10.000 Experimentos de 30 Moedas\", fontsize=13, fontweight=\"bold\")\n",
        "ax.set_xlabel(\"Número de Caras\")\n",
        "ax.legend()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 3. Abordagem 2: Intervalo de Confiança Paramétrico via TCL (RSG da UFMG)\n",
        "$$\\text{IC}_{95\\%} = \\bar{x} \\pm z^* \\cdot \\frac{s}{\\sqrt{n}}$$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "n = 50\n",
        "xbar = 3.2\n",
        "s = 1.74\n",
        "\n",
        "se = s / np.sqrt(n)\n",
        "z_95 = stats.norm.ppf(0.975)\n",
        "margem = z_95 * se\n",
        "\n",
        "ic_inf = xbar - margem\n",
        "ic_sup = xbar + margem\n",
        "\n",
        "print(f\"Erro Padrão (SE): {se:.4f}\")\n",
        "print(f\"Margem de Erro (1.96 * SE): {margem:.4f}\")\n",
        "print(f\"Intervalo de Confiança 95%: ({ic_inf:.2f}, {ic_sup:.2f})\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 4. Análise do Estudo da COVID-19 (UFPel 2020)\n",
        "**Contexto:** Estudo de prevalência de anticorpos encontrou **1,9%** de infectados com IC 95% de **[1,7%, 2,1%]**.\n",
        "**Hipótese de Imunidade de Rebanho:** Necessita de $\\ge 50\\%$ de soropositivos.\n",
        "**Conclusão Estatística:** Como 50% está fora do IC [1,7%, 2,1%], rejeita-se H0 com p < 0.05."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 5. Análise de Sensibilidade: Variação de Nível de Confiança ($z^*$) e Amostra ($n$)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "confs = [0.90, 0.95, 0.98, 0.99]\n",
        "tabela = []\n",
        "for c in confs:\n",
        "    z = stats.norm.ppf(1 - (1 - c)/2)\n",
        "    me = z * se\n",
        "    tabela.append({\n",
        "        \"Nível de Confiança\": f\"{c:.0%}\",\n",
        "        \"z*\": round(z, 3),\n",
        "        \"Margem de Erro\": round(me, 3),\n",
        "        \"IC (\": f\"({xbar - me:.2f}, {xbar + me:.2f})\"\n",
        "    })\n",
        "display(pd.DataFrame(tabela))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 6. Desafio Prático para ADS: Função de IC Paramétrico Automatizada"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "def calcular_ic(dados, nivel_confianca=0.95):\n",
        "    n_elem = len(dados)\n",
        "    media_elem = np.mean(dados)\n",
        "    sd_elem = np.std(dados, ddof=1)\n",
        "    se_elem = sd_elem / np.sqrt(n_elem)\n",
        "    z_cr = stats.norm.ppf(1 - (1 - nivel_confianca)/2)\n",
        "    me_elem = z_cr * se_elem\n",
        "    return media_elem, (media_elem - me_elem, media_elem + me_elem), me_elem\n",
        "\n",
        "np.random.seed(123)\n",
        "latencias = np.random.normal(loc=120, scale=25, size=60)\n",
        "media_api, (ic_l, ic_h), me_api = calcular_ic(latencias, nivel_confianca=0.95)\n",
        "print(f\"Média da Latência: {media_api:.2f} ms | IC 95%: ({ic_l:.2f} ms, {ic_h:.2f} ms)\")"
      ]
    }
  ],
  "metadata": {
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}

with open('/home/reginaldo/CDD/aula_09/aula_09_pratica_ao_vivo.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print("Notebook aula_09_pratica_ao_vivo.ipynb gerado!")
