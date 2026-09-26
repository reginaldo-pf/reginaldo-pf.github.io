"""
Código de Apoio Didático - Aula 2: Regressão Linear Simples
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Instituição: IFCE Campus Tauá
Disciplina: Ciência de Dados / Estatística Computacional

Este script implementa os métodos numéricos e visuais para a Aula 2.
Fornece algoritmos de otimização de perda (RMSE), cálculo analítico
da reta nas unidades originais, geração de gráficos de resíduos para
diagnósticos e estimação de intervalos de confiança via Bootstrap.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
import statsmodels.api as sm
from scipy import stats

# -------------------------------------------------------------------------
# 1. Configuração do Estilo Visual (Acessibilidade e Limpeza)
# -------------------------------------------------------------------------
plt.style.use('seaborn-v0_8-colorblind')  # Tema acessível
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
# 2. Perda e Otimização Numérica (Bloco 2.1)
# -------------------------------------------------------------------------
def calcular_rmse(coeficientes, x, y):
    """
    Calcula a Raiz do Erro Quadrático Médio (RMSE) para dados z-normalizados
    considerando uma reta que passa pela origem (y_estimado = beta * x).
    
    Parâmetros:
      coeficientes: Vetor contendo [beta].
      x, y: Variáveis preditora e resposta (normalizadas).
    """
    beta = coeficientes[0]
    y_estimado = beta * x
    erro_quadratico = (y - y_estimado) ** 2
    rmse = np.sqrt(np.mean(erro_quadratico))
    return rmse

def otimizar_reta_normalizada(x, y):
    """
    Minimiza numericamente a função de perda RMSE para dados normalizados.
    Demonstra a concordância entre o beta otimizado e o coeficiente r de Pearson.
    """
    # Z-normalização (Unidades Padrão)
    x_su = (x - np.mean(x)) / np.std(x, ddof=1)
    y_su = (y - np.mean(y)) / np.std(y, ddof=1)
    
    # Chute inicial para beta
    chute_inicial = [0.0]
    
    # Otimização por minimização numérica da perda (RMSE)
    resultado = minimize(calcular_rmse, chute_inicial, args=(x_su, y_su), method='BFGS')
    beta_otimizado = resultado.x[0]
    
    # Coeficiente r de Pearson analítico
    r_analitico, _ = stats.pearsonr(x, y)
    
    return {
        'Beta Otimizado (RMSE)': beta_otimizado,
        'Pearson r (Analítico)': r_analitico,
        'Diferença': abs(beta_otimizado - r_analitico)
    }

# -------------------------------------------------------------------------
# 3. Equação Analítica nas Unidades Originais (Bloco 2.2)
# -------------------------------------------------------------------------
def calcular_regressao_analitica(x, y):
    """
    Calcula analiticamente o Slope (beta) e Intercepto (alfa) nas unidades
    originais dos dados, bem como estatísticas de qualidade de ajuste.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    # Médias Amostrais
    media_x = np.mean(x)
    media_y = np.mean(y)
    
    # Desvios Padrão Amostrais
    s_x = np.std(x, ddof=1)
    s_y = np.std(y, ddof=1)
    
    # Coeficiente de Pearson r
    r, _ = stats.pearsonr(x, y)
    
    # Parâmetros da reta
    beta = r * (s_y / s_x)
    alfa = media_y - beta * media_x
    
    # Predições e Resíduos
    y_estimado = beta * x + alfa
    residuos = y - y_estimado
    
    # Métricas de Ajuste
    soma_erros_quadrados = np.sum(residuos**2)
    variabilidade_total = np.sum((y - media_y)**2)
    r_quadrado = 1 - (soma_erros_quadrados / variabilidade_total)
    
    # Desvio Padrão dos Resíduos
    sd_residuos = np.sqrt(soma_erros_quadrados / (len(x) - 2)) # Ajustado pelos graus de liberdade
    sd_residuos_teorico = np.sqrt(1 - r**2) * s_y
    
    return {
        'Slope (Beta)': beta,
        'Intercepto (Alfa)': alfa,
        'R-Quadrado (R2)': r_quadrado,
        'Média dos Resíduos': np.mean(residuos),
        'SD dos Resíduos (Amostral)': sd_residuos,
        'SD dos Resíduos (Teórico)': sd_residuos_teorico
    }

# -------------------------------------------------------------------------
# 4. Bootstrap de Pares para Inferência (Intervalo de Confiança do Slope)
# -------------------------------------------------------------------------
def bootstrap_slope(x, y, repeticoes=2000, alpha_ic=0.05):
    """
    Realiza Bootstrap de pares para construir o Intervalo de Confiança (IC)
    amostral do Slope (coeficiente angular beta) da reta de regressão.
    Utiliza álgebra de vetores rápida no NumPy.
    """
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    slopes_bootstrap = np.zeros(repeticoes)
    
    # Loop de reamostragem otimizado com NumPy
    for i in range(repeticoes):
        # Seleciona índices com reposição
        indices = np.random.choice(n, size=n, replace=True)
        x_resampled = x[indices]
        y_resampled = y[indices]
        
        # Regressão linear rápida de uma linha (fórmula de mínimos quadrados)
        cov_xy = np.cov(x_resampled, y_resampled)[0, 1]
        var_x = np.var(x_resampled, ddof=1)
        slopes_bootstrap[i] = cov_xy / var_x
        
    # Percentis para o Intervalo de Confiança
    percentil_inf = 100 * (alpha_ic / 2.0)
    percentil_sup = 100 * (1 - alpha_ic / 2.0)
    
    ic_inferior = np.percentile(slopes_bootstrap, percentil_inf)
    ic_superior = np.percentile(slopes_bootstrap, percentil_sup)
    
    return slopes_bootstrap, (ic_inferior, ic_superior)

# -------------------------------------------------------------------------
# 5. Geração de Plots Diagnósticos (Não-Linearidade e Heterocedasticidade)
# -------------------------------------------------------------------------
def gerar_graficos_diagnostico():
    """
    Gera dados artificiais ilustrando o comportamento correto dos resíduos
    (homocedástico), resíduos de modelo não-linear e resíduos heterocedásticos.
    Salva os gráficos para suporte aos slides.
    """
    np.random.seed(42)
    n = 150
    x = np.linspace(1, 10, n)
    
    # 1. Caso Linear Homocedástico (Ideal)
    y_linear = 2.5 * x + 5 + np.random.normal(0, 1.5, n)
    # 2. Caso Não-Linear (Falta termo quadrático)
    y_nao_linear = 0.5 * (x - 5)**2 + 10 + np.random.normal(0, 0.8, n)
    # 3. Caso Heterocedástico (Variância cresce com X)
    y_hetero = 2.5 * x + 5 + np.random.normal(0, 0.4 * x, n)
    
    modelos = [('linear', y_linear), ('nao_linear', y_nao_linear), ('heterocedastico', y_hetero)]
    
    for nome, y in modelos:
        # Ajusta a reta
        slope, intercept, r_val, p_val, std_err = stats.linregress(x, y)
        y_pred = slope * x + intercept
        residuos = y - y_pred
        
        # Plot do Ajuste e Resíduos
        fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
        
        # Painel esquerdo: Ajuste linear
        sns.scatterplot(x=x, y=y, ax=axes[0], color='steelblue', alpha=0.8)
        axes[0].plot(x, y_pred, color='crimson', label=f'Ajuste Linear ($R^2$ = {r_val**2:.2f})')
        axes[0].set_title(f"Ajuste de Regressão ({nome.capitalize()})")
        axes[0].set_xlabel("Variável Preditora (X)")
        axes[0].set_ylabel("Variável Resposta (Y)")
        axes[0].legend()
        aplicar_despine(axes[0])
        
        # Painel direito: Gráfico de resíduos
        sns.scatterplot(x=x, y=residuos, ax=axes[1], color='dimgray', alpha=0.8)
        axes[1].axhline(y=0, color='crimson', linestyle='--')
        axes[1].set_title(f"Gráfico de Resíduos ({nome.capitalize()})")
        axes[1].set_xlabel("Variável Preditora (X)")
        axes[1].set_ylabel("Resíduos (Erro)")
        aplicar_despine(axes[1])
        
        plt.tight_layout()
        filename = f'diagnostico_{nome}.png'
        plt.savefig(filename, dpi=300)
        plt.close()
        print(f"Gráfico '{filename}' gerado com sucesso.")

def gerar_grafico_linha_45():
    """
    Gera uma nuvem de pontos sintética padronizada (Z-scores) com uma reta de 45 graus
    para ilustrar a reta de 45 graus versus a reta de regressão.
    """
    np.random.seed(42)
    n = 4000
    x = np.random.normal(0, 1, n)
    r = 0.6
    y = r * x + np.sqrt(1 - r**2) * np.random.normal(0, 1, n)
    
    # Garantir unidades padrão (Z-scores)
    x_su = (x - np.mean(x)) / np.std(x)
    y_su = (y - np.mean(y)) / np.std(y)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x_su, y_su, alpha=0.5, color='#0072B2', s=4)
    ax.plot([-4, 4], [-4, 4], color='crimson', linewidth=2.5)
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("x in standard units")
    ax.set_ylabel("y in standard units")
    ax.grid(True, linestyle='-', alpha=0.15)
    aplicar_despine(ax)
    
    plt.tight_layout()
    plt.savefig('grafico_linha_45.png', dpi=300)
    plt.close()
    print("Gráfico 'grafico_linha_45.png' gerado com sucesso.")

# -------------------------------------------------------------------------
# Execução Principal (Demonstração Didática com o Caso dos Gambás)
# -------------------------------------------------------------------------
if __name__ == '__main__':
    # Simulação realista do dataset "Possum" (Gambás) - 140 observações
    # Preditora (X): Comprimento do corpo (cm)
    # Resposta (Y): Comprimento da cabeça (mm)
    np.random.seed(140)
    comprimento_corpo = np.random.normal(87.5, 4.2, 140)
    comprimento_cabeca = 42.0 + 0.58 * comprimento_corpo + np.random.normal(0, 2.1, 140)
    
    # 1. Demonstração da Minimização Numérica (Unidades Padrão)
    print("=== Bloco 2.1: Minimização Numérica da Perda (RMSE) ===")
    res_otim = otimizar_reta_normalizada(comprimento_corpo, comprimento_cabeca)
    for k, v in res_otim.items():
        print(f"{k}: {v:.6f}")
    print("========================================================\n")
    
    # 2. Ajuste Analítico do Modelo
    print("=== Bloco 2.2: Ajuste Analítico e Qualidade do Modelo ===")
    res_reg = calcular_regressao_analitica(comprimento_corpo, comprimento_cabeca)
    for k, v in res_reg.items():
        print(f"{k}: {v:.5f}")
    print("========================================================\n")
    
    # 3. Inferência do Slope via Bootstrap
    print("=== Bloco 2.2: Inferência via Bootstrap (Repetições = 2000) ===")
    slopes_boot, ic_boot = bootstrap_slope(comprimento_corpo, comprimento_cabeca)
    print(f"Intervalo de Confiança de 95% para o Slope (Bootstrap): [{ic_boot[0]:.4f}, {ic_boot[1]:.4f}]")
    print("========================================================\n")
    
    # 4. Ajuste no Statsmodels para validação estatística padrão
    print("=== Bloco 2.2: Validação com Statsmodels (Estatística Clássica) ===")
    X_sm = sm.add_constant(comprimento_corpo)
    modelo_sm = sm.OLS(comprimento_cabeca, X_sm).fit()
    print(modelo_sm.summary().tables[1])
    print(f"R-quadrado do Statsmodels: {modelo_sm.rsquared:.5f}")
    print("========================================================\n")
    
    # Geração dos arquivos de imagens para os slides Beamer
    gerar_graficos_diagnostico()
    gerar_grafico_linha_45()
