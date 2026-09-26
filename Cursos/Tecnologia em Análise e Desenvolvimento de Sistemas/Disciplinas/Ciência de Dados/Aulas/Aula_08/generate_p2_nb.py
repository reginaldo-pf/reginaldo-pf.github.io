import json

notebook = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Aula 08 (Parte 2) — Ciência de Dados para ADS\n",
        "## Laboratório Prático Ao Vivo: Variabilidade, Curva Normal, TLC e Tamanho de Amostra\n",
        "\n",
        "Este notebook contém todos os exemplos práticos abordados nos slides da **Aula 08 (Parte 2)**.\n",
        "Ele foi projetado para execução em sala de aula, permitindo compreender a medição da variabilidade através do **Desvio Padrão (SD)**, a **Curva Normal**, o **Teorema do Limite Central (TLC)**, a **Lei da Raiz Quadrada** e o cálculo do **Tamanho de Amostra** para pesquisas e sistemas."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 1. Configuração do Ambiente\n",
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
        "print(\"✅ Ambiente configurado para a Parte 2!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 2. Módulo 1: Calculando o Desvio Padrão (SD) e Unidades Padrão (Z-Score)\n",
        "**Exemplo:** Coleção simples `any_numbers = [1, 2, 2, 10]`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "any_numbers = np.array([1, 2, 2, 10])\n",
        "media = np.mean(any_numbers)\n",
        "desvios = any_numbers - media\n",
        "desvios_quad = desvios ** 2\n",
        "variancia = np.mean(desvios_quad)\n",
        "sd = np.sqrt(variancia)\n",
        "\n",
        "df_sd = pd.DataFrame({\n",
        "    \"x\": any_numbers,\n",
        "    \"x - media\": desvios,\n",
        "    \"(x - media)^2\": desvios_quad,\n",
        "    \"Z-Score (Standard Units)\": (any_numbers - media) / sd\n",
        "})\n",
        "display(df_sd)\n",
        "print(f\"Média: {media:.2f} | Variância: {variancia:.2f} | SD (np.std): {sd:.2f}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 3. Módulo 2: A Curva Normal e a Regra Empírica (68% - 95% - 99.7%)\n",
        "Utilizando a função acumulada `scipy.stats.norm.cdf`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Calculando probabilidades acumuladas sob a Curva Normal Padrao\n",
        "area_1sd = stats.norm.cdf(1) - stats.norm.cdf(-1)\n",
        "area_2sd = stats.norm.cdf(2) - stats.norm.cdf(-2)\n",
        "area_3sd = stats.norm.cdf(3) - stats.norm.cdf(-3)\n",
        "\n",
        "print(f\"Área entre Media ± 1 SD: {area_1sd:.2%}\")\n",
        "print(f\"Área entre Media ± 2 SD: {area_2sd:.2%}\")\n",
        "print(f\"Área entre Media ± 3 SD: {area_3sd:.2%}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Plotando a Curva Normal e os Intervalos de SD\n",
        "x = np.linspace(-4, 4, 1000)\n",
        "y = stats.norm.pdf(x)\n",
        "\n",
        "fig, ax = plt.subplots(figsize=(9, 4.5))\n",
        "ax.plot(x, y, color=\"#1E293B\", linewidth=2.5, label=\"Normal Padrão N(0,1)\")\n",
        "ax.fill_between(x, y, where=(x >= -1) & (x <= 1), color=\"#0EA5E9\", alpha=0.5, label=\"68% (±1 SD)\")\n",
        "ax.fill_between(x, y, where=(x >= -2) & (x <= 2), color=\"#0EA5E9\", alpha=0.2, label=\"95% (±2 SD)\")\n",
        "ax.set_title(\"A Curva Normal Padrão e os Pontos de Inflexão (±1 SD)\", fontsize=14, fontweight=\"bold\")\n",
        "ax.set_xlabel(\"Unidades Padrão (Z-Scores)\")\n",
        "ax.set_ylabel(\"Densidade\")\n",
        "ax.legend()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 4. Módulo 3: O Teorema do Limite Central (TLC) na Prática\n",
        "**Fenômeno:** Não importa quão assimétrica seja a população original (ex: atrasos de voos), a **distribuição das médias amostrais** de tamanho $N$ grande será sempre aproximada por uma Curva Normal!"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "np.random.seed(42)\n",
        "populacao = np.random.exponential(scale=15, size=10000)\n",
        "\n",
        "fig, axes = plt.subplots(1, 3, figsize=(15, 4))\n",
        "\n",
        "for idx, n in enumerate([5, 25, 100]):\n",
        "    amostras = np.random.choice(populacao, size=(10000, n))\n",
        "    medias = np.mean(amostras, axis=1)\n",
        "    sns.histplot(medias, bins=30, kde=True, ax=axes[idx], color=\"#0EA5E9\", edgecolor=\"black\")\n",
        "    axes[idx].set_title(f\"Médias Amostrais (N={n})\", fontsize=12, fontweight=\"bold\")\n",
        "    axes[idx].set_xlabel(f\"SD Observado: {np.std(medias):.2f}\")\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 5. Módulo 4: A Lei da Raiz Quadrada e Acurácia\n",
        "$$SD(\\text{média amostral}) = \\frac{SD_{\\text{populacional}}}{\\sqrt{n}}$$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "sd_pop = np.std(populacao)\n",
        "sd_n25 = sd_pop / np.sqrt(25)\n",
        "sd_n100 = sd_pop / np.sqrt(100)\n",
        "\n",
        "print(f\"SD da População Original:          {sd_pop:.2f}\")\n",
        "print(f\"SD das Médias Amostrais (N=25):   {sd_n25:.2f}\")\n",
        "print(f\"SD das Médias Amostrais (N=100):  {sd_n100:.2f}\")\n",
        "print(f\"Aumento de precisão (Fator):      {sd_n25 / sd_n100:.2f}x (Multiplicar N por 4 divide SD por 2)\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 6. Módulo 5: Tamanho de Amostra Mínimo em Pesquisas\n",
        "**Cenário:** Estimar a intenção de voto do Candidato A com margem de erro total máxima de 1% (largura total do intervalo de 95% $\\le 0.01$).\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "sd_max = 0.5\n",
        "largura_intervalo = 0.01\n",
        "n_necessario = (4 * sd_max / largura_intervalo) ** 2\n",
        "print(f\"Tamanho mínimo de amostra necessário: {n_necessario:,.0f} pessoas\")"
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

with open('/home/reginaldo/CDD/aula_8/aula_08_parte2_pratica_ao_vivo.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print("Notebook aula_08_parte2_pratica_ao_vivo.ipynb gerado com sucesso!")
