"""
Código de Apoio Didático - Aula 1: Correlação Linear e Associação
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Instituição: IFCE Campus Tauá
Disciplina: Ciência de Dados / Estatística Computacional

Este script fornece as funções de cálculo e as rotinas de visualização para a
Aula 1. Ele foi construído utilizando um estilo visual acessível e limpo,
conforme as especificações de design do curso.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# -------------------------------------------------------------------------
# 1. Configuração do Estilo Visual (Acessibilidade e Limpeza)
# -------------------------------------------------------------------------
plt.style.use('seaborn-v0_8-colorblind')  # Tema de cores acessível
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
    """
    Remove as bordas superior e direita do gráfico para limpeza visual (despine).
    """
    sns.despine(ax=ax, top=True, right=True, left=False, bottom=False)

# -------------------------------------------------------------------------
# 2. Exemplo Pareado: Cálculo Manual vs. Computacional de Pearson (r)
# -------------------------------------------------------------------------
def calcular_r_passo_a_passo(x, y):
    """
    Calcula o Coeficiente de Correlação de Pearson (r) passo a passo,
    retornando as etapas intermediárias (médias, desvios e covariância)
    para fins didáticos.
    
    Parâmetros:
      x, y: Listas ou arrays unidimensionais de tamanho N.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    N = len(x)
    
    if N != len(y):
        raise ValueError("Os vetores x e y devem possuir o mesmo tamanho.")
        
    # Passo 1: Calcular as Médias Amostrais (X_barra, Y_barra)
    media_x = np.mean(x)
    media_y = np.mean(y)
    
    # Passo 2: Calcular os Desvios em relação à Média
    desvios_x = x - media_x
    desvios_y = y - media_y
    
    # Passo 3: Produto dos Desvios e Covariância Amostral
    produtos_desvios = desvios_x * desvios_y
    soma_produtos = np.sum(produtos_desvios)
    covariancia = soma_produtos / (N - 1)
    
    # Passo 4: Desvios Padrão Amostrais (s_x, s_y)
    s_x = np.sqrt(np.sum(desvios_x**2) / (N - 1))
    s_y = np.sqrt(np.sum(desvios_y**2) / (N - 1))
    
    # Passo 5: Coeficiente de Correlação de Pearson (r)
    r = covariancia / (s_x * s_y)
    
    return {
        'N': N,
        'Média X': media_x,
        'Média Y': media_y,
        'Covariância Amostral': covariancia,
        'Desvio Padrão X': s_x,
        'Desvio Padrão Y': s_y,
        'Pearson r': r
    }

# -------------------------------------------------------------------------
# 3. Visualização de Relações Não Lineares: Pearson vs. Spearman
# -------------------------------------------------------------------------
def plotar_comparacao_pearson_spearman():
    """
    Gera um gráfico demonstrativo comparando a sensibilidade do Coeficiente
    de Correlação de Pearson (r) e da Correlação de Postos de Spearman (r_s)
    para uma relação estritamente não-linear monótona.
    """
    # Gerando dados não lineares monótonos (cúbicos)
    x = np.linspace(-3, 3, 100)
    y = x**3 + np.random.normal(0, 1.5, size=100)  # Relação cúbica com ruído
    
    # Cálculo das correlações
    corr_pearson, _ = stats.pearsonr(x, y)
    corr_spearman, _ = stats.spearmanr(x, y)
    
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.7, color='steelblue', label='Observações')
    
    # Linha de tendência não linear ilustrativa
    ax.plot(x, x**3, color='crimson', linestyle='--', label='Relação Funcional (Monótona)')
    
    ax.set_title("Comparação de Métricas de Associação\n"
                 f"Pearson r = {corr_pearson:.3f} | Spearman r_s = {corr_spearman:.3f}")
    ax.set_xlabel("Variável Independente (X)")
    ax.set_ylabel("Variável Dependente (Y)")
    ax.legend()
    aplicar_despine(ax)
    
    plt.tight_layout()
    plt.savefig('grafico_pearson_vs_spearman.png', dpi=300)
    plt.close()
    print("Gráfico 'grafico_pearson_vs_spearman.png' gerado com sucesso.")

# -------------------------------------------------------------------------
# 4. Simulação Visual do Paradoxo de Simpson
# -------------------------------------------------------------------------
def simular_paradoxo_simpson():
    """
    Simula e plota o Paradoxo de Simpson usando o exemplo clássico de
    Nível de Colesterol vs. Horas de Exercício Físico por faixas etárias.
    Gera dois gráficos: um agregado (mostrando uma correlação espúria positiva)
    e um estratificado (mostrando a real correlação negativa intragrupo).
    """
    np.random.seed(42)
    n_por_grupo = 40
    
    # Criando três faixas etárias (Jovens, Adultos, Idosos)
    # Cada grupo tem média de exercício e colesterol diferentes
    
    # Jovens: Exercitam-se mais, têm colesterol mais baixo no geral
    ex_jovens = np.random.normal(8, 1.5, n_por_grupo)
    col_jovens = 180 - 4 * ex_jovens + np.random.normal(0, 8, n_por_grupo)
    grupo_jovens = ['Jovens (20-35 anos)'] * n_por_grupo
    
    # Adultos: Exercitam-se moderadamente, colesterol médio
    ex_adultos = np.random.normal(5, 1.5, n_por_grupo)
    col_adultos = 220 - 4 * ex_adultos + np.random.normal(0, 8, n_por_grupo)
    grupo_adultos = ['Adultos (36-55 anos)'] * n_por_grupo
    
    # Idosos: Exercitam-se menos, colesterol mais alto
    ex_idosos = np.random.normal(3, 1.5, n_por_grupo)
    col_idosos = 260 - 4 * ex_idosos + np.random.normal(0, 8, n_por_grupo)
    grupo_idosos = ['Idosos (56+ anos)'] * n_por_grupo
    
    # Consolidando em um DataFrame
    df = pd.DataFrame({
        'Exercicio': np.concatenate([ex_jovens, ex_adultos, ex_idosos]),
        'Colesterol': np.concatenate([col_jovens, col_adultos, col_idosos]),
        'Faixa Etaria': grupo_jovens + grupo_adultos + grupo_idosos
    })
    
    # Correlação agregada (geral)
    r_geral, _ = stats.pearsonr(df['Exercicio'], df['Colesterol'])
    
    # 1. Gráfico Agregado
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Exercicio', y='Colesterol', color='dimgray', alpha=0.8, s=60, label='Dados Agregados')
    sns.regplot(data=df, x='Exercicio', y='Colesterol', scatter=False, color='black', 
                label=f'Ajuste Geral: r = {r_geral:.3f}')
    plt.title("Nível de Colesterol vs. Exercício Físico (Agregado)\n"
              "O Paradoxo: Exercício parece estar associado a MAIOR colesterol!")
    plt.xlabel("Horas de Atividade Física / Semana")
    plt.ylabel("Nível de Colesterol (mg/dL)")
    plt.legend()
    aplicar_despine()
    plt.tight_layout()
    plt.savefig('simpson_agregado.png', dpi=300)
    plt.close()
    
    # 2. Gráfico Estratificado (Revelando a Realidade por Faixa Etária)
    plt.figure(figsize=(10, 6))
    
    # Loop pelos grupos para calcular correlação intragrupo e plotar
    cores = ['#009E73', '#D55E00', '#0072B2'] # Cores colorblind-friendly
    for i, grupo in enumerate(df['Faixa Etaria'].unique()):
        sub_df = df[df['Faixa Etaria'] == grupo]
        r_grupo, _ = stats.pearsonr(sub_df['Exercicio'], sub_df['Colesterol'])
        
        sns.scatterplot(data=sub_df, x='Exercicio', y='Colesterol', 
                        color=cores[i], label=f'{grupo} (r = {r_grupo:.3f})', s=60, alpha=0.9)
        # Traçar reta de regressão para cada subgrupo
        sns.regplot(data=sub_df, x='Exercicio', y='Colesterol', scatter=False, color=cores[i])
        
    plt.title("Nível de Colesterol vs. Exercício Físico (Estratificado por Idade)\n"
              "A Realidade: Exercício reduz o colesterol em todas as faixas etárias.")
    plt.xlabel("Horas de Atividade Física / Semana")
    plt.ylabel("Nível de Colesterol (mg/dL)")
    plt.legend()
    aplicar_despine()
    plt.tight_layout()
    plt.savefig('simpson_estratificado.png', dpi=300)
    plt.close()
    print("Gráficos do Paradoxo de Simpson gerados: 'simpson_agregado.png' e 'simpson_estratificado.png'.")

# -------------------------------------------------------------------------
# Execução de Demonstração
# -------------------------------------------------------------------------
if __name__ == '__main__':
    # Exemplo Pareado com os dados fictícios calculados à mão
    x_exemplo = [1, 2, 3, 4, 5]
    y_exemplo = [2, 4, 5, 4, 5]
    
    res = calcular_r_passo_a_passo(x_exemplo, y_exemplo)
    print("=== Exemplo Pareado: Cálculo de Pearson ===")
    for k, v in res.items():
        print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")
    print("===========================================")
    
    # Geração dos gráficos de suporte aos slides
    plotar_comparacao_pearson_spearman()
    simular_paradoxo_simpson()
