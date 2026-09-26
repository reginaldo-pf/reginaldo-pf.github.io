import json

notebook = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Aula 08 (Parte 1) — Ciência de Dados para ADS\n",
        "## Laboratório Prático Ao Vivo: Propriedades e Interpretação da Média\n",
        "\n",
        "Este notebook contém todos os exemplos práticos abordados nos slides da **Aula 08 (Parte 1)**.\n",
        "Ele foi projetado para execução em sala de aula, permitindo ao professor e aos estudantes manipular os dados, gerar visualizações e compreender intuitivamente o comportamento da **Média**, das **Proporções** e da **Mediana** em sistemas de informação."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 1. Configuração do Ambiente e Bibliotecas\n",
        "Usaremos `numpy`, `pandas`, `matplotlib` e `seaborn` (padrão da indústria de Data Science)."
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
        "# Estilo dos graficos\n",
        "sns.set_theme(style=\"whitegrid\")\n",
        "plt.rcParams[\"figure.figsize\"] = (9, 5)\n",
        "print(\"✅ Ambiente configurado com sucesso!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 2. Exemplo 1: A Média como \"Equalizador\" (*Smoother*)\n",
        "**Cenário dos Slides:** 4 pessoas possuem nas suas carteiras os valores \$2, \$3, \$3 e \$9."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Colecao not_symmetric dos slides\n",
        "not_symmetric = np.array([2, 3, 3, 9])\n",
        "\n",
        "total_dinheiro = np.sum(not_symmetric)\n",
        "media_dinheiro = np.mean(not_symmetric)\n",
        "\n",
        "print(f\"Total arrecadado no fundo comum: R$ {total_dinheiro:.2f}\")\n",
        "print(f\"Valor redistribuido igualmente (Média): R$ {media_dinheiro:.2f}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 3. Exemplo 2: Proporções são Médias (Variáveis Booleanas em ADS)\n",
        "**Conceito:** Se uma coleção é formada apenas por `0`s e `1`s (ou `False` e `True`), a média é exatamente a **proporção de sucessos**."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Array binario [1, 1, 1, 0]\n",
        "zero_one = np.array([1, 1, 1, 0])\n",
        "print(\"Soma dos 1s:\", np.sum(zero_one))\n",
        "print(\"Media (Proporcao de 1s):\", np.mean(zero_one))\n",
        "\n",
        "# Array booleano [True, True, True, False]\n",
        "bool_array = np.array([True, True, True, False])\n",
        "print(\"Media de booleanos:\", np.mean(bool_array))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "#### 💻 Aplicação Prática em ADS: Log de Cliques em Web App (CTR)\n",
        "Vamos simular 1.000 requisições de um sistema web onde monitoramos se o usuário clicou em um anúncio (`1`) ou não (`0`)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "np.random.seed(42)\n",
        "cliques = np.random.choice([0, 1], size=1000, p=[0.85, 0.15]) # 15% de probabilidade de clique\n",
        "\n",
        "df_web = pd.DataFrame({\n",
        "    \"usuario_id\": range(1000),\n",
        "    \"clicou\": cliques\n",
        "})\n",
        "\n",
        "ctr = df_web[\"clicou\"].mean()\n",
        "print(f\"Taxa de Clique (Click-Through Rate - CTR): {ctr:.2%}\")\n",
        "print(f\"Total de cliques no sistema: {df_web[\'clicou\'].sum()}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 4. Exemplo 3: A Média Depende Apenas da Distribuição\n",
        "**Conceito:** Duas coleções com a mesma proporção relativa de valores possuem exatamente a mesma média, independente do número de elementos."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "colecao_A = np.array([2, 3, 3, 9])\n",
        "colecao_B = np.array([2, 2, 3, 3, 3, 3, 9, 9])\n",
        "\n",
        "print(\"Tamanho de A:\", len(colecao_A), \"| Media de A:\", np.mean(colecao_A))\n",
        "print(\"Tamanho de B:\", len(colecao_B), \"| Media de B:\", np.mean(colecao_B))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 5. Exemplo 4: Visualizando a Média como Centro de Gravidade (*Fulcrum*)\n",
        "Vamos plotar o histograma da coleção `{2, 3, 3, 9}` e marcar o ponto de equilíbrio no valor **4.25**."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "fig, ax = plt.subplots(figsize=(8, 4))\n",
        "\n",
        "bins = np.arange(1.5, 10.5, 1)\n",
        "counts, _, patches = ax.hist(colecao_A, bins=bins, density=True, color=\"#0EA5E9\", edgecolor=\"#1E293B\", alpha=0.7, rwidth=0.9)\n",
        "\n",
        "media = np.mean(colecao_A)\n",
        "\n",
        "# Plot do Ponto de Apoio (Fulcrum)\n",
        "ax.scatter(media, 0, color=\"#F59E0B\", s=250, marker=\"^\", zorder=5, label=f\"Média (Centro de Gravidade) = {media}\")\n",
        "ax.axhline(0, color=\"black\", linewidth=2)\n",
        "\n",
        "ax.set_xticks(range(2, 10))\n",
        "ax.set_title(\"Histograma de {2, 3, 3, 9} e seu Ponto de Apoio\", fontsize=14, fontweight=\"bold\")\n",
        "ax.set_xlabel(\"Valores\")\n",
        "ax.set_ylabel(\"Proporção (Frequência Relativa)\")\n",
        "ax.legend(loc=\"upper right\", frameon=True)\n",
        "plt.savefig(\"histograma_ponto_apoio.png\", dpi=300, bbox_inches=\"tight\")\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 6. Exemplo 5: Média vs. Mediana e o Mito do \"Abaixo da Média\"\n",
        "Compare a distribuição simétrica `{2, 3, 3, 4}` com a assimétrica `{2, 3, 3, 9}`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "simetrica = np.array([2, 3, 3, 4])\n",
        "nao_simetrica = np.array([2, 3, 3, 9])\n",
        "\n",
        "df_comp = pd.DataFrame({\n",
        "    \"Conjunto\": [\"Simétrico {2,3,3,4}\", \"Assimétrico {2,3,3,9}\"],\n",
        "    \"Média\": [np.mean(simetrica), np.mean(nao_simetrica)],\n",
        "    \"Mediana\": [np.median(simetrica), np.median(nao_simetrica)],\n",
        "    \"% dados < Média\": [\n",
        "        f\"{np.mean(simetrica < np.mean(simetrica)):.0%}\",\n",
        "        f\"{np.mean(nao_simetrica < np.mean(nao_simetrica)):.0%}\"\n",
        "    ]\n",
        "})\n",
        "display(df_comp)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 7. Estudo de Caso Real: Salários e Compensações (San Francisco 2015)\n",
        "Vamos carregar ou simular o conjunto de dados de salários de San Francisco para observar o comportamento da **Média** e da **Mediana** sob assimetria acentuada (*Right Skewed*)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "np.random.seed(42)\n",
        "# Simulacao fiel da distribuicao de salarios de SF 2015 (Compensacao Total > $10.000)\n",
        "base_salarios = np.random.lognormal(mean=11.5, sigma=0.5, size=5000)\n",
        "salarios_sf = base_salarios[(base_salarios >= 10000) & (base_salarios <= 700000)]\n",
        "\n",
        "media_sf = np.mean(salarios_sf)\n",
        "mediana_sf = np.median(salarios_sf)\n",
        "\n",
        "print(f\"Mediana do Salário: R$ {mediana_sf:,.2f}  (Salário Típico)\")\n",
        "print(f\"Média do Salário:   R$ {media_sf:,.2f}  (Puxada pela cauda longa)\")\n",
        "print(f\"Diferença:          R$ {(media_sf - mediana_sf):,.2f}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "fig, ax = plt.subplots(figsize=(10, 5))\n",
        "\n",
        "sns.histplot(salarios_sf, bins=40, kde=True, ax=ax, color=\"#0EA5E9\", edgecolor=\"black\")\n",
        "\n",
        "ax.axvline(mediana_sf, color=\"#E11D48\", linestyle=\"--\", linewidth=2.5, label=f\"Mediana: R$ {mediana_sf:,.0f}\")\n",
        "ax.axvline(media_sf, color=\"#F59E0B\", linestyle=\"-\", linewidth=2.5, label=f\"Média: R$ {media_sf:,.0f}\")\n",
        "\n",
        "ax.set_title(\"Distribuição de Salários (San Francisco 2015) - Assimetria à Direita\", fontsize=14, fontweight=\"bold\")\n",
        "ax.set_xlabel(\"Compensação Total (R\$)\")\n",
        "ax.set_ylabel(\"Frequência\")\n",
        "ax.legend(fontsize=12)\n",
        "plt.savefig(\"salarios_sf_assimetria.png\", dpi=300, bbox_inches=\"tight\")\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "### 8. Desafio Prático de ADS (Live Coding em Sala!)\n",
        "**Cenário em Engenharia de Software:**\n",
        "Você é o engenheiro de dados responsável pelo monitoramento de performance de uma API de pagamento.\n",
        "Abaixo temos o log do tempo de resposta (latência em milissegundos) de 1.000 requisições."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "np.random.seed(123)\n",
        "# 95% das requisicoes respondem rapido (50ms - 150ms), 5% sofrem timeout/delay alto (2000ms - 5000ms)\n",
        "latencias_normais = np.random.normal(loc=100, scale=20, size=950)\n",
        "latencias_lentas = np.random.uniform(low=2000, high=5000, size=50)\n",
        "latencias_api = np.concatenate([latencias_normais, latencias_lentas])\n",
        "\n",
        "print(\"Primeiras 10 latencias:\", latencias_api[:10].round(1))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "**PERGUNTA PARA A TURMA:**\n",
        "1. Calcule a média e a mediana do tempo de resposta da API.\n",
        "2. Qual métrica você colocaria no SLA do painel de monitoramento do sistema para refletir a experiência típica do usuário?\n",
        "3. Qual métrica você usaria para projetar o consumo total de banda/processador do servidor?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# RESPOSTA DO EXERCÍCIO DA TURMA\n",
        "media_lat = np.mean(latencias_api)\n",
        "mediana_lat = np.median(latencias_api)\n",
        "\n",
        "print(f\"Média de Latência:   {media_lat:.2f} ms  (Afetada drasticamente pelos 5% de requisições lentas)\")\n",
        "print(f\"Mediana de Latência: {mediana_lat:.2f} ms  (Reflete a latência do usuário típico)\")"
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

with open('/home/reginaldo/CDD/aula_8/aula_08_pratica_ao_vivo.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print("Jupyter Notebook aula_08_pratica_ao_vivo.ipynb criado!")
