import json
notebook = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Aula 09 \u2014 Ci\u00eancia de Dados para ADS\n",
        "## Laborat\u00f3rio Pr\u00e1tico Ao Vivo: Intervalos de Confian\u00e7a Param\u00e9tricos e Testes de Hip\u00f3teses\n",
        "\n",
        "Este notebook cont\u00e9m todas as simula\u00e7\u00f5es emp\u00edricas e equa\u00e7\u00f5es param\u00e9tricas da **Aula 09**.\n",
        "Ele aborda o Teste de Hip\u00f3teses da **Moeda Viesada** (via simula\u00e7\u00e3o/percentis), o Intervalo de Confian\u00e7a do **RSG de Alunos da UFMG** (via Teorema do Limite Central), a an\u00e1lise do **Estudo da COVID-19 da UFPel**, e um **Desafio Pr\u00e1tico de ADS** para calculadoras de ICs de lat\u00eancia de software."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 1. Configura\u00e7\u00e3o do Ambiente e Importa\u00e7\u00f5es\n",
        "Importando `numpy`, `pandas`, `matplotlib`, `seaborn` e `scipy.stats`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
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
        "print(\"\u2705 Ambiente da Aula 09 configurado com sucesso!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 2. Abordagem 1: Teste de Hip\u00f3tese Emp\u00edrico via Simula\u00e7\u00e3o (Moeda Viesada)\n",
        "**Problema:** Lan\u00e7amos uma moeda 30 vezes e obtivemos **22 caras**. A moeda \u00e9 justa ou tem vi\u00e9s?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "np.random.seed(42)\n",
        "# Simulando 10.000 experimentos de 30 lancamentos sob H0 (Moeda Justa, p=0.5)\n",
        "simulacoes_moeda = np.random.binomial(n=30, p=0.5, size=10000)\n",
        "\n",
        "# Percentis empiricos de 95% (2.5% e 97.5%)\n",
        "ic_low = np.percentile(simulacoes_moeda, 2.5)\n",
        "ic_high = np.percentile(simulacoes_moeda, 97.5)\n",
        "p_valor = np.mean(simulacoes_moeda >= 22)\n",
        "\n",
        "print(f\"Intervalo Empirico de 95% sob H0: [{ic_low:.0f}, {ic_high:.0f}] caras\")\n",
        "print(f\"P-Valor (Probabilidade de observar >= 22 caras): {p_valor:.4f} ({p_valor:.2%})\")\n",
        "print(\"Conclusao: Rejeitamos H0 com p < 0.05. A moeda tem vies significante!\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Plotando a Distribuicao Empirica das Simulacoes\n",
        "fig, ax = plt.subplots(figsize=(9, 4.5))\n",
        "sns.histplot(simulacoes_moeda, discrete=True, ax=ax, color=\"#0EA5E9\", edgecolor=\"black\")\n",
        "ax.axvline(22, color=\"#E11D48\", linestyle=\"--\", linewidth=2.5, label=\"Observado: 22 Caras (p = 0.69%)\")\n",
        "ax.axvline(15, color=\"#F59E0B\", linestyle=\"-\", linewidth=2, label=\"Esperado sob H0: 15 Caras\")\n",
        "ax.set_title(\"Distribui\u00e7\u00e3o Emp\u00edrica de 10.000 Experimentos de 30 Moedas\", fontsize=13, fontweight=\"bold\")\n",
        "ax.set_xlabel(\"N\u00famero de Caras\")\n",
        "ax.legend()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 3. Abordagem 2: Intervalo de Confian\u00e7a Param\u00e9trico via TCL (RSG da UFMG)\n",
        "$$\\text{IC}_{95\\%} = \\bar{x} \\pm z^* \\cdot \\frac{s}{\\sqrt{n}}$$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Dados da Pesquisa UFMG (n=50, mean=3.2, s=1.74)\n",
        "n = 50\n",
        "xbar = 3.2\n",
        "s = 1.74\n",
        "\n",
        "se = s / np.sqrt(n) # Erro Padrao\n",
        "z_95 = stats.norm.ppf(0.975) # 1.96\n",
        "margem = z_95 * se\n",
        "\n",
        "ic_inf = xbar - margem\n",
        "ic_sup = xbar + margem\n",
        "\n",
        "print(f\"Erro Padr\u00e3o (SE): {se:.4f}\")\n",
        "print(f\"Margem de Erro (1.96 * SE): {margem:.4f}\")\n",
        "print(f\"Intervalo de Confian\u00e7a 95%: ({ic_inf:.2f}, {ic_sup:.2f})\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 4. An\u00e1lise do Estudo da COVID-19 (UFPel 2020)\n",
        "**Contexto:** Estudo de preval\u00eancia de anticorpos encontrou **1,9%** de infectados com IC 95% de **[1,7%, 2,1%]**.\n",
        "**Hip\u00f3tese de Imunidade de Rebanho:** Necessita de $\\ge 50\\%$ de soropositivos.\n",
        "**Conclus\u00e3o Estat\u00edstica:** Como 50% est\u00e1 fora do IC [1,7%, 2,1%], rejeita-se H0 com p < 0.05."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 5. An\u00e1lise de Sensibilidade: Varia\u00e7\u00e3o de N\u00edvel de Confian\u00e7a ($z^*$) e Amostra ($n$)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "confs = [0.90, 0.95, 0.98, 0.99]\n",
        "tabela = []\n",
        "for c in confs:\n",
        "    z = stats.norm.ppf(1 - (1 - c)/2)\n",
        "    me = z * se\n",
        "    tabela.append({\n",
        "        \"N\u00edvel de Confian\u00e7a\": f\"{c:.0%}\",\n",
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
        "### 6. Desafio Pr\u00e1tico para ADS: Fun\u00e7\u00e3o de IC Param\u00e9trico Automatizada"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
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
        "# Exemplo com latencias de rede de um microservico\n",
        "np.random.seed(123)\n",
        "latencias = np.random.normal(loc=120, scale=25, size=60)\n",
        "media_api, (ic_l, ic_h), me_api = calcular_ic(latencias, nivel_confianca=0.95)\n",
        "print(f\"M\u00e9dia da Lat\u00eancia: {media_api:.2f} ms | IC 95%: ({ic_l:.2f} ms, {ic_h:.2f} ms)\")"
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
with open("/home/reginaldo/CDD/aula_09/aula_09_pratica_ao_vivo.ipynb", "w") as fp:
    json.dump(notebook, fp, indent=2)
print("Notebook Aula 09 gerado com sucesso!")
