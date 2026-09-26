# -*- coding: utf-8 -*-
"""
Código de Apoio Didático - Aula 14 (Parte 2): Verossimilhança
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Instituição: IFCE Campus Tauá
Disciplina: Ciência de Dados / Estatística Computacional

Este script implementa a modelagem e visualização da Função de Verossimilhança
para o caso discreto (Bernoulli) e contínuo (Normal), em consonância com o notebook
utilizado em sala. Salva as imagens para os slides da aula.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

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
    """Remove as bordas superior e direita do gráfico para limpeza visual."""
    if ax is None:
        ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# -------------------------------------------------------------------------
# 2. Caso Discreto: Experimento de Bernoulli (Lançamento de Moeda)
# -------------------------------------------------------------------------
def gerar_graficos_bernoulli():
    """Calcula e gera a curva de verossimilhança e log-verossimilhança para Bernoulli."""
    # Dados reais do experimento: 4 caras (1) e 9 coroas (0), total N=13
    dados = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    N = len(dados)
    sucessos = np.sum(dados)
    fracassos = N - sucessos
    
    # Proporção empírica (MLE)
    mle_proporcao = sucessos / N
    
    # Grid de valores de theta
    thetas = np.linspace(0.001, 0.999, 100)
    
    # Função de verossimilhança e log-verossimilhança
    veros = (thetas ** sucessos) * ((1 - thetas) ** fracassos)
    log_veros = sucessos * np.log(thetas) + fracassos * np.log(1 - thetas)
    
    # Plot da verossimilhança
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(thetas, veros, color='steelblue', label=r'L($\theta$) = $\theta^{4}(1-\theta)^{9}$')
    ax.axvline(x=mle_proporcao, color='crimson', linestyle='--', 
               label=f'MLE: $\hat{{\theta}}$ = {mle_proporcao:.4f}')
    ax.set_xlabel(r'Parâmetro Candidato ($\theta$)')
    ax.set_ylabel('Verossimilhança')
    ax.set_title('Função de Verossimilhança de Bernoulli (Lançamentos de Moeda)')
    ax.legend()
    aplicar_despine(ax)
    plt.tight_layout()
    plt.savefig('verossimilhanca_bernoulli.png', dpi=300)
    plt.close()
    
    # Plot da log-verossimilhança
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(thetas, log_veros, color='purple', label=r'$\ln L(\theta)$')
    ax.axvline(x=mle_proporcao, color='crimson', linestyle='--', 
               label=f'MLE: $\hat{{\theta}}$ = {mle_proporcao:.4f}')
    ax.set_xlabel(r'Parâmetro Candidato ($\theta$)')
    ax.set_ylabel('Log-Verossimilhança')
    ax.set_title('Função de Log-Verossimilhança de Bernoulli')
    ax.legend()
    aplicar_despine(ax)
    plt.tight_layout()
    plt.savefig('log_verossimilhanca_bernoulli.png', dpi=300)
    plt.close()
    
    print("Gráficos de Bernoulli salvos com sucesso.")
    return mle_proporcao

# -------------------------------------------------------------------------
# 3. Caso Contínuo: Distribuição Normal (Gaussiana)
# -------------------------------------------------------------------------
def gerar_graficos_normal():
    """Calcula e gera o plot de log-verossimilhança para a distribuição Normal."""
    # Amostra de 170 elementos contida no notebook de sala
    dados = np.array([
        41, 27, 33, 58, 24, 65, 48, 72, 36, 29,
        54, 67, 21, 46, 38, 25, 31, 43, 59, 50,
        63, 35, 44, 22, 68, 26, 55, 61, 28, 73,
        47, 39, 70, 53, 32, 66, 30, 64, 56, 37,
        34, 62, 42, 51, 71, 57, 69, 23, 45, 40,
        75, 20, 74, 49, 19, 60, 52, 77, 78, 43,
        65, 26, 31, 48, 33, 68, 28, 37, 63, 24,
        36, 27, 39, 42, 44, 54, 57, 21, 30, 46,
        62, 50, 70, 29, 25, 58, 60, 55, 34, 40,
        67, 41, 71, 32, 66, 35, 23, 59, 49, 22,
        47, 73, 38, 64, 20, 45, 68, 72, 74, 63,
        43, 33, 31, 53, 28, 26, 24, 61, 36, 56,
        52, 25, 27, 34, 40, 50, 65, 29, 46, 38,
        66, 30, 32, 35, 37, 44, 39, 68, 67, 41,
        60, 42, 69, 45, 54, 48, 70, 22, 71, 23,
        49, 43, 73, 31, 64, 33, 28, 58, 20, 63,
        55, 56, 72, 26, 24, 74, 25, 62, 27, 61
    ])
    
    N = len(dados)
    mle_mu = np.mean(dados)
    mle_sigma = np.std(dados)  # MLE da variância divide por N (std padrão no NumPy)
    
    print("=== ANÁLISE DO MODELO CONTINUO (NORMAL) ===")
    print(f"Tamanho da Amostra (N): {N}")
    print(f"Média Amostral (MLE de mu): {mle_mu:.4f}")
    print(f"Desvio Padrão MLE (MLE de sigma): {mle_sigma:.4f}")
    
    # Avaliar log-verossimilhança para um grid de mu, mantendo sigma fixo no ótimo
    mu_vals = np.linspace(mle_mu - 5, mle_mu + 5, 100)
    log_veros_mu = []
    
    for mu in mu_vals:
        # ln L(mu, sigma) = -N/2 * ln(2*pi*sigma^2) - sum((x_i - mu)^2) / (2*sigma^2)
        pdf = ss.norm.pdf(dados, loc=mu, scale=mle_sigma)
        log_veros_mu.append(np.sum(np.log(pdf)))
        
    # Plot do log-verossimilhança de mu
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(mu_vals, log_veros_mu, color='teal', label=r'$\ln L(\mu, \hat{\sigma})$')
    ax.axvline(x=mle_mu, color='crimson', linestyle='--', 
               label=f'MLE: $\hat{{\mu}}$ = {mle_mu:.4f}')
    ax.set_xlabel(r'Média Candidata ($\mu$)')
    ax.set_ylabel('Log-Verossimilhança')
    ax.set_title('Log-Verossimilhança da Média (Dados de Alturas/Medições)')
    ax.legend()
    aplicar_despine(ax)
    plt.tight_layout()
    plt.savefig('log_verossimilhanca_normal_mu.png', dpi=300)
    plt.close()
    
    print("Gráfico do log-verossimilhança normal de mu salvo com sucesso.")
    return mle_mu, mle_sigma

if __name__ == '__main__':
    gerar_graficos_bernoulli()
    gerar_graficos_normal()
    print("Todas as simulações e plots foram gerados com sucesso no diretório atual.")
