import json

notebook = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Aula 08 (Aula 1 - 60 Minutos) — Ciência de Dados para ADS\n",
        "## Laboratório Prático: Revisão de Probabilidade, Amostragem e Propriedades da Média\n",
        "\n",
        "Este notebook atende à necessidade de reforço em **Probabilidade e Amostragem** para a turma de ADS, unindo a fundamentação matemática a exemplos práticos em Python (`numpy` e `pandas`)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 1. Configuração do Ambiente\n",
        "Importando as bibliotecas essenciais para análise de dados."
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
        "\n",
        "sns.set_theme(style=\"whitegrid\")\n",
        "plt.rcParams[\"figure.figsize\"] = (9, 5)\n",
        "print(\"✅ Ambiente configurado para a Aula 1 (60 min)!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 2. Módulo 1: Revisão Essencial de Probabilidade para Ciência de Dados\n",
        "**Conceitos:** Espaço Amostral ($\\Omega$), Eventos Equiprováveis, Regra da Adição (Eventos Mutuamente Exclusivos vs. Não-Exclusivos) e Regra da Multiplicação (Probabilidade Condicional $P(B|A)$ e Independência)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 1. Experimento: Lancamento de 2 Moedas (HH, HT, TH, TT)\n",
        "np.random.seed(42)\n",
        "m1 = np.random.choice(['H', 'T'], size=10000)\n",
        "m2 = np.random.choice(['H', 'T'], size=10000)\n",
        "\n",
        "# P(Pelo menos uma Cara) = 3/4 = 75%\n",
        "prob_pelo_menos_uma_cara = np.mean((m1 == 'H') | (m2 == 'H'))\n",
        "print(f\"P(Pelo menos uma Cara): {prob_pelo_menos_uma_cara:.2%}\")\n",
        "\n",
        "# 2. Regra da Adição: Eventos Mutuamente Exclusivos\n",
        "# P(17 anos) = 1.4%, P(18 anos) = 1.5% -> P(17 ou 18 anos) = 1.4% + 1.5% = 2.9%\n",
        "p_17, p_18 = 0.014, 0.015\n",
        "print(f\"P(17 ou 18 anos): {p_17 + p_18:.1%}\")\n",
        "\n",
        "# 3. Probabilidade Condicional e Amostragem Sem Reposição\n",
        "# Sorteando 2 alunos de {X, Y, Z} sem reposição. P(Y primeiro E X segundo) = (1/3) * (1/2) = 1/6\n",
        "p_yx = (1/3) * (1/2)\n",
        "print(f\"P(Y 1º e X 2º sem reposição): {p_yx:.4f} (1/6)\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 3. Módulo 2: Amostragem Aleatória em Python (Com e Sem Reposição)\n",
        "**Conceito:** A amostragem **com reposição** gera eventos independentes, enquanto a amostragem **sem reposição** altera o espaço amostral a cada passo (eventos dependentes)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "alunos = np.array(['Aluno_A', 'Aluno_B', 'Aluno_C', 'Aluno_D', 'Aluno_E'])\n",
        "\n",
        "# Sorteio COM reposicao (replace=True)\n",
        "amostra_com = np.random.choice(alunos, size=3, replace=True)\n",
        "print(\"Amostra COM Reposição:\", amostra_com)\n",
        "\n",
        "# Sorteio SEM reposicao (replace=False)\n",
        "amostra_sem = np.random.choice(alunos, size=3, replace=False)\n",
        "print(\"Amostra SEM Reposição:\", amostra_sem)\n",
        "\n",
        "# Amostragem aleatoria em DataFrames com df.sample()\n",
        "df_users = pd.DataFrame({\n",
        "    'id': range(1, 101),\n",
        "    'ativo': np.random.choice([0, 1], size=100, p=[0.3, 0.7])\n",
        "})\n",
        "display(df_users.sample(n=5, random_state=42))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 4. Módulo 3: A Média e suas Propriedades Fundamentais\n",
        "**Exemplo:** Coleção `{2, 3, 3, 9}` (Média = 4.25, Ponto de Equilíbrio / Smoother)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "not_symmetric = np.array([2, 3, 3, 9])\n",
        "media = np.mean(not_symmetric)\n",
        "mediana = np.median(not_symmetric)\n",
        "\n",
        "print(f\"Média: {media:.2f} | Mediana: {mediana:.2f}\")\n",
        "print(f\"Proporção de dados < Média: {np.mean(not_symmetric < media):.0%}\")\n",
        "\n",
        "# Proporção em DataFrames (df['ativo'].mean())\n",
        "taxa_ativos = df_users['ativo'].mean()\n",
        "print(f\"Taxa de Usuários Ativos (Proporção): {taxa_ativos:.2%}\")"
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

with open('/home/reginaldo/CDD/aula_8/aula_08_parte1_pratica_ao_vivo.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print("✅ Notebook aula_08_parte1_pratica_ao_vivo.ipynb gerado com sucesso!")
