"""
Script para geração dos gráficos de carros (dados em português)
para a Aula 1: Associação Linear e Correlação.
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
IFCE Campus Tauá
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração do Estilo Visual (Colorblind-friendly e limpo)
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({
    'figure.figsize': (10, 6),
    'axes.labelsize': 13,
    'axes.titlesize': 15,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'lines.linewidth': 2.5,
    'legend.fontsize': 11
})

def aplicar_despine(ax=None):
    sns.despine(ax=ax, top=True, right=True, left=False, bottom=False)

def main():
    # 1. Carregar e traduzir os dados
    df = pd.read_csv('data/hybrid.csv')
    
    # Criar colunas traduzidas
    df_pt = pd.DataFrame()
    df_pt['Veículo'] = df['vehicle']
    df_pt['Ano'] = df['year']
    df_pt['Preço (mil USD)'] = df['msrp'] / 1000.0
    df_pt['Aceleração (s)'] = df['acceleration']
    df_pt['Consumo (mpg)'] = df['mpg']
    
    # Traduzir classes
    traducao_classe = {
        'Compact': 'Compacto',
        'Two Seater': 'Dois Lugares',
        'Minivan': 'Minivan',
        'SUV': 'SUV',
        'Midsize': 'Médio',
        'Pickup Truck': 'Picape'
    }
    df_pt['Classe'] = df['class'].map(traducao_classe)
    
    # Salvar uma cópia traduzida dos dados (primeiras 5 linhas) para exibição nos slides
    print(df_pt.head().to_latex(index=False))
    
    # 2. Gráfico 1: Aceleração vs Preço (MSRP)
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df_pt, x='Aceleração (s)', y='Preço (mil USD)', alpha=0.7, color='steelblue', s=50)
    plt.title("Aceleração vs. Preço do Veículo")
    plt.xlabel("Aceleração (tempo de 0-100 km/h em segundos)")
    plt.ylabel("Preço Sugerido (milhares de USD)")
    aplicar_despine()
    plt.tight_layout()
    plt.savefig('car_aceleracao_vs_preco.png', dpi=300)
    plt.close()
    
    # 3. Gráfico 2: Consumo (mpg) vs Aceleração
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df_pt, x='Consumo (mpg)', y='Aceleração (s)', alpha=0.7, color='darkorange', s=50)
    plt.title("Consumo vs. Aceleração (Não-Linear)")
    plt.xlabel("Consumo (milhas por galão - mpg)")
    plt.ylabel("Aceleração (segundos)")
    aplicar_despine()
    plt.tight_layout()
    plt.savefig('car_consumo_vs_aceleracao.png', dpi=300)
    plt.close()
    
    # 4. Gráfico 3: Covariância e Correlação (Lado a Lado)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Covariância e Correlação de Consumo vs Aceleração
    corr_1 = df_pt['Consumo (mpg)'].corr(df_pt['Aceleração (s)'])
    cov_1 = df_pt['Consumo (mpg)'].cov(df_pt['Aceleração (s)'])
    sns.scatterplot(data=df_pt, x='Consumo (mpg)', y='Aceleração (s)', alpha=0.7, color='darkorange', s=50, ax=axes[0])
    axes[0].set_title(f"Consumo vs. Aceleração\ncov = {cov_1:.1f} | corr = {corr_1:.2f}")
    axes[0].set_xlabel("Consumo (mpg)")
    axes[0].set_ylabel("Aceleração (s)")
    aplicar_despine(axes[0])
    
    # Covariância e Correlação de Aceleração vs Preço
    corr_2 = df_pt['Aceleração (s)'].corr(df_pt['Preço (mil USD)'])
    cov_2 = df_pt['Aceleração (s)'].cov(df_pt['Preço (mil USD)'])
    sns.scatterplot(data=df_pt, x='Aceleração (s)', y='Preço (mil USD)', alpha=0.7, color='steelblue', s=50, ax=axes[1])
    axes[1].set_title(f"Aceleração vs. Preço\ncov = {cov_2:.1f} | corr = {corr_2:.2f}")
    axes[1].set_xlabel("Aceleração (s)")
    axes[1].set_ylabel("Preço (mil USD)")
    aplicar_despine(axes[1])
    
    plt.tight_layout()
    plt.savefig('car_cov_vs_corr.png', dpi=300)
    plt.close()
    
    # 5. Gráfico 4: Plot de Pares (Pair Plot)
    cols_pair = ['Ano', 'Preço (mil USD)', 'Aceleração (s)', 'Consumo (mpg)']
    g = sns.pairplot(df_pt[cols_pair], diag_kind='hist', plot_kws={'alpha': 0.6, 's': 40})
    g.fig.suptitle("Plot de Pares (Matriz de Dispersão)", y=1.02, fontsize=16)
    g.savefig('car_pairplot.png', dpi=300)
    plt.close()
    
    print("Gráficos de carros gerados com sucesso!")

if __name__ == '__main__':
    main()
