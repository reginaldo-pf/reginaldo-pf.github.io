import numpy as np
import pandas as pd
import matplotlib.pyplot as plots

# Configuracoes visuais do matplotlib
plots.style.use('seaborn-v0_8-colorblind')
plots.rcParams.update({
    'figure.figsize': (10, 6),
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'lines.linewidth': 2.5
})

def despine(ax):
    """Remove as bordas superior e direita do grafico para um visual mais limpo."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

def criar_dataset():
    """Gera o arquivo bta.csv no formato esperado pelo notebook."""
    dados = []
    # 16 pacientes no grupo de controle (2 recuperaram, 14 nao)
    for _ in range(2):
        dados.append({'Group': 'Control', 'Result': 1})
    for _ in range(14):
        dados.append({'Group': 'Control', 'Result': 0})
    # 15 pacientes no grupo de tratamento (9 recuperaram, 6 nao)
    for _ in range(9):
        dados.append({'Group': 'Treatment', 'Result': 1})
    for _ in range(6):
        dados.append({'Group': 'Treatment', 'Result': 0})
        
    df = pd.DataFrame(dados)
    df.to_csv('/home/reginaldo-fernandes/CDD/aula12/bta.csv', index=False)
    return df

def plotar_barras(df):
    """Gera um grafico de barras comparando as proporcoes de recuperacao."""
    proporcoes = df.groupby('Group')['Result'].mean()
    
    fig, ax = plots.subplots()
    bars = ax.bar(proporcoes.index, proporcoes.values, color=['#0066cc', '#009966'], width=0.4)
    
    # Adicionar rotulos de valores nas barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.02, f'{yval:.1%}', ha='center', va='bottom', fontsize=12, fontweight='bold')
        
    ax.set_title('Proporcao de Alivio da Dor por Grupo (HUWC Ceará)')
    ax.set_xlabel('Grupo de Estudo')
    ax.set_ylabel('Proporcao de Recuperacao')
    ax.set_ylim(0, 0.7)
    despine(ax)
    plots.tight_layout()
    plots.savefig('/home/reginaldo-fernandes/CDD/aula12/02_causalidade_barras.png', dpi=150)
    plots.close()

def executar_simulacao(df, repeticoes=20000, seed=42):
    """Executa a simulacao de permutacoes (embaralhar rotulos)."""
    np.random.seed(seed)
    
    resultados = df['Result'].values
    tamanho_tratamento = df[df['Group'] == 'Treatment'].shape[0] # 15
    tamanho_controle = df[df['Group'] == 'Control'].shape[0] # 16
    
    distancias_simuladas = np.zeros(repeticoes)
    
    for i in range(repeticoes):
        # Embaralha os resultados (rotulos sao fixos, embaralhamos os resultados)
        embaralhado = np.random.permutation(resultados)
        
        sim_controle = embaralhado[:tamanho_controle]
        sim_tratamento = embaralhado[tamanho_controle:]
        
        prop_controle = np.mean(sim_controle)
        prop_tratamento = np.mean(sim_tratamento)
        
        distancias_simuladas[i] = np.abs(prop_tratamento - prop_controle)
        
    return distancias_simuladas

def plotar_histograma(distancias, observado_dist):
    """Gera o histograma da distribuicao nula com a linha do valor observado."""
    fig, ax = plots.subplots()
    bins = np.arange(0, 0.7, 0.05)
    
    # Histograma
    n, bins_out, patches = ax.hist(distancias, bins=bins, edgecolor='white', color='#2c3e50', density=True, label='Sob a Hipótese Nula')
    
    # Destacar a cauda a partir do observado_dist em dourado/amarelo
    for patch in patches:
        if (patch.get_x() + patch.get_width()) > observado_dist:
            patch.set_facecolor('#ff9900')
            
    # Adicionar patch fake para legenda do destaque
    ax.axvline(observado_dist, color='#e74c3c', linestyle='dashed', linewidth=3, label=f'Diferença Observada ({observado_dist:.3f})')
    
    # Adiciona patch ficticio na legenda para o dourado
    from matplotlib.patches import Patch
    legenda_patches = [
        Patch(facecolor='#2c3e50', edgecolor='white', label='Valores sob H0'),
        Patch(facecolor='#ff9900', label='Diferença igual ou maior que a Obs.'),
        ax.lines[0]
    ]
    
    ax.legend(handles=legenda_patches)
    ax.set_title('Previsao do Distanciamento sob a Hipotese Nula')
    ax.set_xlabel('Distancia entre Proporcoes (Valor Absoluto)')
    ax.set_ylabel('Densidade')
    
    despine(ax)
    plots.tight_layout()
    plots.savefig('/home/reginaldo-fernandes/CDD/aula12/01_causalidade_histograma.png', dpi=150)
    plots.close()

if __name__ == "__main__":
    # 1. Cria o dataset bta.csv
    df = criar_dataset()
    print("Dataset criado com sucesso!")
    print(df.groupby('Group').agg(Soma_Recuperados=('Result', 'sum'), Total_Pacientes=('Result', 'count'), Taxa_Recuperacao=('Result', 'mean')))
    
    # 2. Plotar o grafico de barras comparativo
    plotar_barras(df)
    print("Grafico de barras 02_causalidade_barras.png gerado!")
    
    # 3. Executar o teste de permutacao
    obs_dist = np.abs(0.600 - 0.125)
    distancias = executar_simulacao(df, repeticoes=20000)
    
    # 4. Calcular o P-valor empírico
    p_valor = np.count_nonzero(distancias >= obs_dist) / len(distancias)
    print(f"Diferenca observada: {obs_dist:.3f}")
    print(f"P-valor empírico obtido: {p_valor:.5f} (Esperado: ~0.009)")
    
    # 5. Plotar histograma
    plotar_histograma(distancias, obs_dist)
    print("Histograma da distribuicao nula 01_causalidade_histograma.png gerado!")
