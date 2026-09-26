#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aula 10: Bootstrap e Testes A/B
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas -- IFCE Campus Tauá

Este script contém a implementação prática das funções de reamostragem (Bootstrap)
e intervalos de confiança para a realização de Testes A/B, organizados de forma
didática com exemplos práticos (sintéticos, dados de saúde e dados de negócios/conversão).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss
from statsmodels.distributions.empirical_distribution import ECDF

# Configurações de estilo para visualização didática
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({
    'figure.figsize': (12, 7),
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'lines.linewidth': 2.5
})

def despine(ax=None):
    """Remove as bordas superior e direita do gráfico para um visual mais limpo."""
    if ax is None:
        ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

# =====================================================================
# 1. FUNÇÕES CORE (ELEMENTOS DE USO)
# =====================================================================

def bootstrap_mean(df, column, n=5000, size=None):
    """
    Realiza o Bootstrap para estimar a distribuição da média amostral.
    
    Parâmetros:
    -----------
    df : pandas.DataFrame
        O dataframe contendo os dados.
    column : str
        A coluna na qual queremos calcular a média.
    n : int, padrão 5000
        O número de reamostragens (amostras bootstrap) a serem geradas.
    size : int, opcional
        O tamanho de cada reamostra. Por padrão, usa o mesmo tamanho do df original.
        
    Retorna:
    --------
    numpy.ndarray
        Vetor com as médias calculadas para cada uma das n reamostras.
    """
    if size is None:
        size = len(df)
    values = np.zeros(n)
    # Extrai os valores para otimizar a velocidade da amostragem com numpy
    data_array = df[column].to_numpy()
    for i in range(n):
        sample = np.random.choice(data_array, size=size, replace=True)
        values[i] = sample.mean()
    return values

def ic_bootstrap(df, column, n=5000, size=None, confidence=95.0):
    """
    Calcula o Intervalo de Confiança (IC) da média via percentis do Bootstrap.
    
    Parâmetros:
    -----------
    df : pandas.DataFrame
        O dataframe contendo os dados.
    column : str
        A coluna desejada.
    n : int, padrão 5000
        Número de reamostras bootstrap.
    size : int, opcional
        Tamanho de cada amostra bootstrap.
    confidence : float, padrão 95.0
        O nível de confiança desejado (ex: 95 para 95%).
        
    Retorna:
    --------
    tuple (float, float)
        Os limites inferior e superior do Intervalo de Confiança.
    """
    values = bootstrap_mean(df, column, n, size)
    lower_percentile = (100.0 - confidence) / 2.0
    upper_percentile = 100.0 - lower_percentile
    return (np.percentile(values, lower_percentile), np.percentile(values, upper_percentile))

def ic_classic(df, column, confidence=0.95):
    """
    Calcula o Intervalo de Confiança clássico usando o Teorema Central do Limite (TCL).
    
    Parâmetros:
    -----------
    df : pandas.DataFrame
        O dataframe contendo os dados.
    column : str
        A coluna desejada.
    confidence : float, padrão 0.95
        Nível de confiança (ex: 0.95 para 95%).
        
    Retorna:
    --------
    tuple (float, float)
        Limites inferior e superior do IC clássico.
    """
    data = df[column].dropna()
    mean = data.mean()
    std = data.std(ddof=1)
    n = len(data)
    se = std / np.sqrt(n)
    
    # Encontra o valor crítico z para a confiança desejada
    z = ss.norm.ppf((1 + confidence) / 2.0)
    return (mean - z * se, mean + z * se)

def bootstrap_diff(df1, df2, column, n=5000, size1=None, size2=None):
    """
    Realiza o Bootstrap para calcular a diferença entre as médias de dois grupos (A e B).
    Esta é a base do teste A/B computacional.
    
    Parâmetros:
    -----------
    df1 : pandas.DataFrame
        Dataframe do Grupo 1 (ex: Tratamento / Fumantes).
    df2 : pandas.DataFrame
        Dataframe do Grupo 2 (ex: Controle / Não Fumantes).
    column : str
        Coluna contendo a métrica numérica contínua a ser comparada.
    n : int, padrão 5000
        Número de reamostras bootstrap.
    
    Retorna:
    --------
    numpy.ndarray
        Vetor com a diferença de médias (Média_1 - Média_2) para cada reamostra.
    """
    if size1 is None:
        size1 = len(df1)
    if size2 is None:
        size2 = len(df2)
        
    data1 = df1[column].to_numpy()
    data2 = df2[column].to_numpy()
    
    diff_values = np.zeros(n)
    for i in range(n):
        sample1 = np.random.choice(data1, size=size1, replace=True)
        sample2 = np.random.choice(data2, size=size2, replace=True)
        diff_values[i] = sample1.mean() - sample2.mean()
        
    return diff_values

# =====================================================================
# 2. ROTEIROS DE EXECUÇÃO DIDÁTICA (EXEMPLOS)
# =====================================================================

def rodar_exemplo_sintetico():
    """
    Exemplo Sintético: Demonstração didática de como o Intervalo de Confiança
    Bootstrap converge para o clássico (via TCL) à medida que aumentamos
    o número de amostras bootstrap.
    """
    print("\n--- 1. Executando Exemplo Sintético (Convergência) ---")
    # População Normal teórica: média = 0, std = 1
    np.random.seed(42)
    pop_sample = np.random.normal(loc=0, scale=1, size=100)
    data = pd.DataFrame({'values': pop_sample})
    
    # Calcular tamanhos dos ICs variando o número de amostras bootstrap
    ns = np.arange(10, 1001, 10)
    ic_bootstrap_widths = []
    ic_classic_width = ic_classic(data, 'values')[1] - ic_classic(data, 'values')[0]
    
    for n in ns:
        ic_bs = ic_bootstrap(data, 'values', n=n)
        ic_bootstrap_widths.append(ic_bs[1] - ic_bs[0])
        
    plt.figure()
    plt.plot(ns, ic_bootstrap_widths, label='Tamanho IC Bootstrap', color='C0')
    plt.axhline(ic_classic_width, label='Tamanho IC Clássico (TCL)', color='C1', linestyle='--')
    plt.xlabel('Número de Amostras Bootstrap (n)')
    plt.ylabel('Tamanho do Intervalo de Confiança (IC)')
    plt.title('Convergência do Bootstrap para o IC Clássico')
    plt.legend()
    despine()
    plt.savefig('01_convergencia_sintetica.png')
    print("Gráfico '01_convergencia_sintetica.png' gerado com sucesso.")

def rodar_exemplo_peso_bebes():
    """
    Exemplo 2: Teste A/B com dados reais de saúde (Peso de bebês de mães
    fumantes vs. não fumantes).
    """
    print("\n--- 2. Executando Exemplo Real (Peso de Bebês) ---")
    url = 'https://media.githubusercontent.com/media/icd-ufmg/material/master/aulas/10-AB/baby.csv'
    try:
        df = pd.read_csv(url)
    except Exception as e:
        print(f"Erro ao carregar dados online: {e}")
        print("Criando dados simulados compatíveis para o exemplo...")
        # Simulação caso esteja sem internet
        np.random.seed(42)
        n_sim = 1174
        smokers_status = np.random.choice([True, False], size=n_sim, p=[0.4, 0.6])
        weights = np.where(smokers_status, np.random.normal(3.2, 0.5, size=n_sim), np.random.normal(3.5, 0.5, size=n_sim))
        df = pd.DataFrame({'Maternal Smoker': smokers_status, 'Birth Weight': weights / 0.0283495}) # Em onças
        
    # Converter unidades americanas (onças para kg, polegadas para cm)
    df['Birth Weight'] = 0.0283495 * df['Birth Weight'] # onças -> kg
    if 'Maternal Pregnancy Weight' in df.columns:
        df['Maternal Pregnancy Weight'] = 0.0283495 * df['Maternal Pregnancy Weight']
    if 'Maternal Height' in df.columns:
        df['Maternal Height'] = 0.0254 * df['Maternal Height']
        
    smokers = df[df['Maternal Smoker'] == True]
    no_smokers = df[df['Maternal Smoker'] == False]
    
    print(f"Quantidade de Mães Não Fumantes: {len(no_smokers)}")
    print(f"Quantidade de Mães Fumantes: {len(smokers)}")
    print(f"Média de peso (Não Fumantes): {no_smokers['Birth Weight'].mean():.3f} kg")
    print(f"Média de peso (Fumantes): {smokers['Birth Weight'].mean():.3f} kg")
    
    # Distribuição das médias via Bootstrap
    boot_smokers = bootstrap_mean(smokers, 'Birth Weight')
    boot_no_smokers = bootstrap_mean(no_smokers, 'Birth Weight')
    
    # Plot dos histogramas sobrepostos das médias bootstrap
    plt.figure()
    plt.hist(boot_no_smokers, bins=30, alpha=0.6, label='Médias Bootstrap - Não Fumantes (Grupo B)', color='C0', edgecolor='k')
    plt.hist(boot_smokers, bins=30, alpha=0.6, label='Médias Bootstrap - Fumantes (Grupo A)', color='C1', edgecolor='k')
    plt.xlabel('Peso Médio do Bebê (kg)')
    plt.ylabel('Frequência de Ocorrência')
    plt.title('Distribuição da Média Amostral (Bootstrap)')
    plt.legend()
    despine()
    plt.savefig('02_medias_bootstrap.png')
    
    # Cálculo da diferença de médias
    diffs = bootstrap_diff(smokers, no_smokers, 'Birth Weight')
    ic_diff = (np.percentile(diffs, 2.5), np.percentile(diffs, 97.5))
    print(f"Diferença observada das médias: {smokers['Birth Weight'].mean() - no_smokers['Birth Weight'].mean():.3f} kg")
    print(f"Intervalo de Confiança de 95% da Diferença: [{ic_diff[0]:.3f} kg, {ic_diff[1]:.3f} kg]")
    
    # Análise de significância
    if ic_diff[0] <= 0 <= ic_diff[1]:
        print("Conclusão: O valor zero ESTÁ contido no IC da diferença. Não podemos rejeitar a hipótese nula. As diferenças podem ser devido ao acaso.")
    else:
        print("Conclusão: O valor zero NÃO está contido no IC da diferença. Há evidência estatística significativa de que os bebês de mães fumantes nascem com peso inferior.")

    # Plot do Histograma da Diferença e ECDF
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    ax1.hist(diffs, bins=30, edgecolor='k', color='purple', alpha=0.7)
    ax1.axvline(0, color='red', linestyle='--', linewidth=2, label='Diferença Zero (H0)')
    ax1.axvline(ic_diff[0], color='black', linestyle=':', label='Limites IC 95%')
    ax1.axvline(ic_diff[1], color='black', linestyle=':')
    ax1.set_xlabel('Diferença de Médias (Fumantes - Não Fumantes)')
    ax1.set_ylabel('Frequência')
    ax1.set_title('Distribuição Bootstrap da Diferença')
    ax1.legend()
    despine(ax1)
    
    ecdf = ECDF(diffs)
    ax2.plot(ecdf.x, ecdf.y, color='purple', linewidth=3)
    ax2.axvline(0, color='red', linestyle='--', linewidth=2)
    ax2.axvline(ic_diff[0], color='black', linestyle=':')
    ax2.axvline(ic_diff[1], color='black', linestyle=':')
    ax2.set_xlabel('Diferença de Médias (Fumantes - Não Fumantes)')
    ax2.set_ylabel('Probabilidade Acumulada P(X <= x)')
    ax2.set_title('Função de Distribuição Acumulada Empírica (ECDF)')
    despine(ax2)
    
    plt.tight_layout()
    plt.savefig('03_diferenca_ecdf.png')
    print("Gráficos de diferença de médias e ECDF salvos em '03_diferenca_ecdf.png'.")

def rodar_novo_exemplo_ecommerce():
    """
    Exemplo 3 (Novo): Teste A/B Aplicado a Negócios e UX.
    Compara o valor de compra (ticket médio) de usuários sob duas versões de layout:
    - Versão A (Layout Clássico)
    - Versão B (Novo Layout com Checkout Expresso)
    """
    print("\n--- 3. Executando Novo Exemplo (Ticket Médio E-commerce) ---")
    np.random.seed(123)
    # Grupo A (Controle): N=250, média=45.0, desvio=12
    vendas_A = np.random.normal(loc=45.0, scale=12.0, size=250)
    # Grupo B (Tratamento): N=200, média=48.5, desvio=14
    vendas_B = np.random.normal(loc=48.5, scale=14.0, size=200)
    
    df_A = pd.DataFrame({'Ticket': vendas_A})
    df_B = pd.DataFrame({'Ticket': vendas_B})
    
    print(f"Layout A (Controle) - N={len(df_A)}, Média de Compra = R${df_A['Ticket'].mean():.2f}")
    print(f"Layout B (Tratamento) - N={len(df_B)}, Média de Compra = R${df_B['Ticket'].mean():.2f}")
    
    # 1. Gerar e salvar boxplot comparativo das amostras originais
    plt.figure()
    plt.boxplot([vendas_A, vendas_B], tick_labels=['Layout A (Controle)', 'Layout B (Tratamento)'], patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='C0'),
                medianprops=dict(color='red', linewidth=2))
    plt.ylabel('Valor da Compra (R$)')
    plt.title('Dispersao do Ticket Medio por Versao de Layout')
    despine()
    plt.savefig('05_boxplot_ecommerce.png')
    print("Gráfico '05_boxplot_ecommerce.png' gerado com sucesso.")

    diffs = bootstrap_diff(df_B, df_A, 'Ticket') # Diferença: B - A
    ic_diff = (np.percentile(diffs, 2.5), np.percentile(diffs, 97.5))
    
    print(f"Diferença observada (B - A): R${df_B['Ticket'].mean() - df_A['Ticket'].mean():.2f}")
    print(f"IC de 95% da diferença: [R${ic_diff[0]:.2f}, R${ic_diff[1]:.2f}]")
    
    plt.figure()
    plt.hist(diffs, bins=35, color='teal', alpha=0.7, edgecolor='k', label='Diferença (B - A)')
    plt.axvline(0, color='red', linestyle='--', linewidth=2, label='Zero (Sem Efeito)')
    plt.axvline(ic_diff[0], color='black', linestyle=':', label='IC 95%')
    plt.axvline(ic_diff[1], color='black', linestyle=':')
    plt.xlabel('Diferença no Valor de Compra (R$)')
    plt.ylabel('Frequência')
    plt.title('Teste A/B: Impacto do Novo Checkout Expresso no Ticket Médio')
    plt.legend()
    despine()
    plt.savefig('04_ab_teste_ecommerce.png')
    
    if ic_diff[0] > 0:
        print("Conclusão: O novo layout B gera um aumento estatisticamente significativo no ticket médio!")
    else:
        print("Conclusão: O intervalo inclui R$0. Não temos evidência estatística de que o novo layout é melhor.")

if __name__ == '__main__':
    rodar_exemplo_sintetico()
    rodar_exemplo_peso_bebes()
    rodar_novo_exemplo_ecommerce()
    print("\nTodos os exemplos executados. Arquivos de imagem gerados com sucesso no diretório.")
