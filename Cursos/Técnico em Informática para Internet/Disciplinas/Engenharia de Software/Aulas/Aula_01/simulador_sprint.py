import numpy as np
import matplotlib.pyplot as plt

# Definicao de estilo visual de acordo com a skill cdd-aula-template
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({
    'figure.figsize': (12, 7),
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'lines.linewidth': 2.5,
    'font.size': 12
})

def despine(ax):
    """Remove as bordas superior e direita do grafico para um visual limpo."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def simular_monte_carlo(total_pontos_backlog, media_velocidade, desvio_padrao_velocidade, num_simulacoes=10000):
    """
    Simula a quantidade de sprints necessarias para concluir o backlog do produto
    usando o metodo de Monte Carlo.
    
    Argumentos:
        total_pontos_backlog (int): Total de Story Points do Product Backlog (ex: 80)
        media_velocidade (float): Media da velocidade da equipe por sprint (ex: 15)
        desvio_padrao_velocidade (float): Desvio padrao da velocidade da equipe (ex: 4)
        num_simulacoes (int): Numero de repeticoes da simulação
    
    Retorna:
        numpy.ndarray: Array com o numero de sprints necessarias em cada simulacao
    """
    sprints_necessarias = []
    
    for _ in range(num_simulacoes):
        pontos_concluidos = 0
        sprints = 0
        while pontos_concluidos < total_pontos_backlog:
            # Simular a velocidade da sprint atual usando distribuicao normal
            velocidade_sprint = np.random.normal(media_velocidade, desvio_padrao_velocidade)
            # A velocidade nao pode ser negativa
            velocidade_sprint = max(0, velocidade_sprint)
            pontos_concluidos += velocidade_sprint
            sprints += 1
        sprints_necessarias.append(sprints)
        
    return np.array(sprints_necessarias)

def plotar_resultados(sprints_simuladas, total_pontos):
    """Gera o grafico da ECDF (Funcao de Distribuicao Acumulada Empirica) para tomada de decisao."""
    fig, ax = plt.subplots()
    
    # Ordenar os dados para plotar a ECDF
    x = np.sort(sprints_simuladas)
    y = np.arange(1, len(x) + 1) / len(x)
    
    ax.plot(x, y, marker='.', linestyle='none', color='#1f77b4', alpha=0.5, label='Simulacoes Monte Carlo')
    
    # Adicionar linhas de decisao (percentis 50%, 80% e 90%)
    percentil_50 = np.percentile(sprints_simuladas, 50)
    percentil_80 = np.percentile(sprints_simuladas, 80)
    percentil_90 = np.percentile(sprints_simuladas, 90)
    
    ax.axhline(0.5, color='orange', linestyle='--', label=f'50% de Confianca ({percentil_50:.1f} Sprints)')
    ax.axhline(0.8, color='green', linestyle='--', label=f'80% de Confianca ({percentil_80:.1f} Sprints)')
    ax.axhline(0.9, color='red', linestyle='--', label=f'90% de Confianca ({percentil_90:.1f} Sprints)')
    
    ax.set_title(f'Simulacao de Monte Carlo: Prazo de Conclusao do Backlog ({total_pontos} SP)\n(Equipe de 5 Alunos - IFCE Campus Taua)', pad=20)
    ax.set_xlabel('Numero de Sprints para Concluir o Projeto')
    ax.set_ylabel('Probabilidade Acumulada (Confianca)')
    
    ax.legend(loc='lower right')
    ax.grid(True, linestyle=':', alpha=0.6)
    
    despine(ax)
    
    # Salvar o grafico para apresentacao
    plt.tight_layout()
    grafico_path = 'ecdf_simulacao_prazo.png'
    plt.savefig(grafico_path, dpi=300)
    plt.close()
    print(f"Grafico ECDF salvo com sucesso em: {grafico_path}")
    print(f"Resultados de Confianca:")
    print(f" - 50% de chance de concluir em ate {percentil_50:.1f} sprints.")
    print(f" - 80% de chance de concluir em ate {percentil_80:.1f} sprints.")
    print(f" - 90% de chance de concluir em ate {percentil_90:.1f} sprints.")

if __name__ == '__main__':
    # Backlog total estimado do MVP: 80 Story Points (SP)
    # Velocidade media estimada da equipe de 5 alunos: 15 SP por sprint
    # Desvio padrao da velocidade: 3.5 SP por sprint
    total_sp = 80
    media_vel = 15.0
    dp_vel = 3.5
    
    sprints = simular_monte_carlo(total_sp, media_vel, dp_vel)
    plotar_resultados(sprints, total_sp)
