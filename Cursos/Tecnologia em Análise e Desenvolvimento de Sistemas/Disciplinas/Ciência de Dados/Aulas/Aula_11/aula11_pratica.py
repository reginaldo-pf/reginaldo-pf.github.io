import numpy as np
import matplotlib.pyplot as plots
import seaborn as sns

# Configurando o estilo visual dos graficos de acordo com as diretrizes da disciplina
plots.style.use('seaborn-v0_8-colorblind')
plots.rcParams.update({
    'figure.figsize': (10, 6),
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'lines.linewidth': 2.5
})

def despine(ax):
    """Remove as bordas superior e direita do grafico para um visual limpo."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# ==========================================
# 1. Swain vs. Alabama (Selecao de Juri)
# ==========================================
def simular_swain(pop_proporcoes, tamanho_amostra, repeticoes=10000, seed=42):
    """
    Simula o juri sob a hipotese nula (selecao uniforme).
    pop_proporcoes: lista com as proporcoes da populacao [negra, branca]
    """
    np.random.seed(seed)
    # Gerando os counts da categoria de interesse (negros) usando numpy
    # sample_proportions sob a hipotese nula: P(Negro) = 0.26
    simulacoes = np.random.binomial(n=tamanho_amostra, p=pop_proporcoes[0], size=repeticoes)
    return simulacoes

def plotar_swain(simulacoes, observado):
    fig, ax = plots.subplots()
    # Histograma das contagens simuladas
    ax.hist(simulacoes, bins=np.arange(min(simulacoes)-0.5, max(simulacoes)+1.5, 1), 
            edgecolor='white', color='#34495e', density=True)
    ax.axvline(observado, color='#e74c3c', linestyle='dashed', linewidth=3, 
               label=f'Observado ({observado})')
    
    ax.set_title('Swain vs. Alabama: Distribuiçao Sob a Hipotese Nula')
    ax.set_xlabel('Numero de Jurados Negros no Painel (N = 100)')
    ax.set_ylabel('Densidade de Probabilidade')
    ax.legend()
    despine(ax)
    plots.tight_layout()
    plots.savefig('/home/reginaldo-fernandes/CDD/aula11/01_swain_histograma.png', dpi=150)
    plots.close()

# ==========================================
# 2. Alameda County (Juri com Multiplas Categorias)
# ==========================================
def calcular_tvd(prop_amostra, prop_esperada):
    """
    Calcula a Distancia de Variacao Total (TVD) entre duas distribuicoes categoricas.
    """
    return 0.5 * np.sum(np.abs(prop_amostra - prop_esperada))

def simular_alameda(prop_elegivel, tamanho_painel, repeticoes=10000, seed=42):
    """
    Simula paineis de juri sob a hipotese nula e calcula a TVD para cada painel.
    """
    np.random.seed(seed)
    tvds = np.zeros(repeticoes)
    for i in range(repeticoes):
        # Gerar uma amostra multinomial sob a proporcao de elegiveis
        contagens = np.random.multinomial(tamanho_painel, prop_elegivel)
        prop_simulada = contagens / tamanho_painel
        tvds[i] = calcular_tvd(prop_simulada, prop_elegivel)
    return tvds

def plotar_alameda(tvds, observado_tvd):
    fig, ax = plots.subplots()
    ax.hist(tvds, bins=30, edgecolor='white', color='#2c3e50', density=True)
    ax.axvline(observado_tvd, color='#e74c3c', linestyle='dashed', linewidth=3, 
               label=f'TVD Observado ({observado_tvd:.3f})')
    
    ax.set_title('Alameda County: Distribuçao do TVD Sob a Hipotese Nula')
    ax.set_xlabel('Distancia de Variacao Total (TVD)')
    ax.set_ylabel('Densidade')
    ax.legend()
    despine(ax)
    plots.tight_layout()
    plots.savefig('/home/reginaldo-fernandes/CDD/aula11/02_alameda_tvd.png', dpi=150)
    plots.close()

def plotar_comparacao_alameda(prop_elegivel, prop_painel):
    """
    Plota um grafico de barras comparando a populacao elegivel e os paineis observados.
    """
    etnias = ['Asiatico', 'Negro', 'Branco', 'Hispanico', 'Outro']
    x = np.arange(len(etnias))
    largura = 0.35
    
    fig, ax = plots.subplots()
    # Barra da populacao elegivel (pop)
    ax.bar(x - largura/2, prop_elegivel, largura, label='pop', color='#0066cc')
    # Barra dos paineis observados (sample)
    ax.bar(x + largura/2, prop_painel, largura, label='sample', color='#009966')
    
    ax.set_title('Composiçao dos Paineis de Juri em Alameda County')
    ax.set_xlabel('Etnia')
    ax.set_ylabel('Proporçao')
    ax.set_xticks(x)
    ax.set_xticklabels(etnias)
    ax.legend()
    despine(ax)
    plots.tight_layout()
    plots.savefig('/home/reginaldo-fernandes/CDD/aula11/06_alameda_comparacao.png', dpi=150)
    plots.close()

def plotar_comparacao_aleatoria(prop_elegivel, seed=42):
    """
    Plota um grafico de barras comparando a populacao elegivel e uma amostra verdadeiramente aleatoria de tamanho 1453.
    """
    np.random.seed(seed)
    contagens_random = np.random.multinomial(1453, prop_elegivel)
    prop_random = contagens_random / 1453
    
    tvd_random = calcular_tvd(prop_random, prop_elegivel)
    print(f"TVD da Amostra Aleatoria: {tvd_random:.4f}")
    print(f"Proporcoes da Amostra Aleatoria: {prop_random}")
    
    etnias = ['Asiatico', 'Negro', 'Branco', 'Hispanico', 'Outro']
    x = np.arange(len(etnias))
    largura = 0.35
    
    fig, ax = plots.subplots()
    ax.bar(x - largura/2, prop_elegivel, largura, label='pop', color='#0066cc')
    ax.bar(x + largura/2, prop_random, largura, label='random sample', color='#ff9900')
    
    ax.set_title('Painel Aleatorio (Simulado) vs. Populacao Elegivel')
    ax.set_xlabel('Etnia')
    ax.set_ylabel('Proporçao')
    ax.set_xticks(x)
    ax.set_xticklabels(etnias)
    ax.legend()
    despine(ax)
    plots.tight_layout()
    plots.savefig('/home/reginaldo-fernandes/CDD/aula11/07_alameda_random_comparacao.png', dpi=150)
    plots.close()
    
    return prop_random, tvd_random

# ==========================================
# 3. Gregor Mendel's Pea Plants (Gregor Mendel)
# ==========================================
def simular_mendel(prob_roxa, tamanho_amostra, observado_roxo, repeticoes=10000, seed=42):
    """
    Simula os experimentos de Mendel para flores roxas.
    """
    np.random.seed(seed)
    # Estatistica: | porcentagem simulada de flores roxas - 75% |
    simulados = np.random.binomial(n=tamanho_amostra, p=prob_roxa, size=repeticoes)
    percents_simulados = (simulados / tamanho_amostra) * 100
    estatisticas = np.abs(percents_simulados - 75.0)
    
    observado_percent = (observado_roxo / tamanho_amostra) * 100
    estatistica_observada = np.abs(observado_percent - 75.0)
    
    return estatisticas, estatistica_observada

def plotar_mendel(estatisticas, observado_dist):
    fig, ax = plots.subplots()
    ax.hist(estatisticas, bins=25, edgecolor='white', color='#8e44ad', density=True)
    ax.axvline(observado_dist, color='#e74c3c', linestyle='dashed', linewidth=3, 
               label=f'Observado ({observado_dist:.3f}%)')
    
    ax.set_title("Mendel: Distribuçao do Desvio Percentual Sob a Hipotese Nula")
    ax.set_xlabel("Distancia entre Percentual de Flores Roxas e 75%")
    ax.set_ylabel("Densidade")
    ax.legend()
    despine(ax)
    plots.tight_layout()
    plots.savefig('/home/reginaldo-fernandes/CDD/aula11/03_mendel_histograma.png', dpi=150)
    plots.close()

# ==========================================
# 4. Testes A/B por Permutacao
# ==========================================
def testar_permutacao_diferenca_medias(grupo_a, grupo_b, repeticoes=10000, seed=42):
    """
    Realiza um teste de permutacao para a diferenca de medias entre dois grupos.
    """
    np.random.seed(seed)
    observado_diff = np.mean(grupo_b) - np.mean(grupo_a)
    
    conjunto = np.concatenate([grupo_a, grupo_b])
    tamanho_a = len(grupo_a)
    
    diferencas = np.zeros(repeticoes)
    for i in range(repeticoes):
        # Embaralha os dados
        embaralhado = np.random.permutation(conjunto)
        sim_a = embaralhado[:tamanho_a]
        sim_b = embaralhado[tamanho_a:]
        diferencas[i] = np.mean(sim_b) - np.mean(sim_a)
        
    return diferencas, observado_diff

def plotar_permutacao(diferencas, observado_diff, titulo, nome_arquivo):
    fig, ax = plots.subplots()
    ax.hist(diferencas, bins=30, edgecolor='white', color='#16a085', density=True)
    ax.axvline(observado_diff, color='#e74c3c', linestyle='dashed', linewidth=3, 
               label=f'Diferenca Observada ({observado_diff:.3f})')
    
    ax.set_title(titulo)
    ax.set_xlabel('Diferenca entre as Medias (Grupo B - Grupo A)')
    ax.set_ylabel('Densidade')
    ax.legend()
    despine(ax)
    plots.tight_layout()
    plots.savefig(nome_arquivo, dpi=150)
    plots.close()

if __name__ == "__main__":
    # 1. Swain vs. Alabama
    # Proporcao populacional de negros elegiveis: 26%
    sim_swain = simular_swain(pop_proporcoes=[0.26, 0.74], tamanho_amostra=100)
    plotar_swain(sim_swain, observado=8)
    p_swain = np.count_nonzero(sim_swain <= 8) / len(sim_swain)
    print(f"Swain vs. Alabama P-Valor: {p_swain:.5f} (Esperado: muito baixo, menor que 0.05)")
    
    # 1b. Intervalo de Confianca Bootstrap para Swain vs. Alabama
    np.random.seed(42)
    amostra_swain = np.array([1]*8 + [0]*92)
    medias_boot_swain = np.array([np.random.choice(amostra_swain, size=100).mean() for _ in range(10000)])
    ic_inf_swain = np.percentile(medias_boot_swain, 2.5)
    ic_sup_swain = np.percentile(medias_boot_swain, 97.5)
    print(f"IC 95% Bootstrap Swain: [{ic_inf_swain:.4f}; {ic_sup_swain:.4f}] (Esperado: [0.0300; 0.1400])")
    
    # 2. Alameda County
    prop_elegivel = np.array([0.15, 0.18, 0.54, 0.12, 0.01]) # Asian, Black, Caucasian, Hispanic, Other
    prop_painel = np.array([0.26, 0.08, 0.54, 0.08, 0.04])
    obs_tvd = calcular_tvd(prop_painel, prop_elegivel)
    tvds_alameda = simular_alameda(prop_elegivel, tamanho_painel=1453)
    plotar_alameda(tvds_alameda, obs_tvd)
    plotar_comparacao_alameda(prop_elegivel, prop_painel)
    plotar_comparacao_aleatoria(prop_elegivel)
    p_alameda = np.count_nonzero(tvds_alameda >= obs_tvd) / len(tvds_alameda)
    print(f"Alameda County P-Valor: {p_alameda:.5f} (Esperado: 0.0)")

    # 3. Gregor Mendel
    estatisticas_mendel, obs_mendel = simular_mendel(prob_roxa=0.75, tamanho_amostra=929, observado_roxo=705)
    plotar_mendel(estatisticas_mendel, obs_mendel)
    p_mendel = np.count_nonzero(estatisticas_mendel >= obs_mendel) / len(estatisticas_mendel)
    print(f"Mendel P-Valor: {p_mendel:.5f} (Esperado: ~0.34-0.38)")

    # 4. Testes A/B: Smoking vs. Birth Weight (em kg)
    # Simulando pesos de bebes com base nas estatisticas reais (1 oz = 0.0283495 kg)
    # Grupo A (Fumantes): media = 3.23 kg, std = 0.52 kg, n = 459
    # Grupo B (Nao Fumantes): media = 3.49 kg, std = 0.49 kg, n = 715
    np.random.seed(42)
    grupo_fumantes = np.random.normal(loc=3.23, scale=0.52, size=459)
    grupo_nao_fumantes = np.random.normal(loc=3.49, scale=0.49, size=715)
    
    diffs_peso, obs_diff_peso = testar_permutacao_diferenca_medias(grupo_fumantes, grupo_nao_fumantes)
    plotar_permutacao(diffs_peso, obs_diff_peso, 'Teste de Permutacao: Peso de Recem-Nascidos (kg)', '/home/reginaldo-fernandes/CDD/aula11/04_permutacao_peso.png')
    p_peso = np.count_nonzero(diffs_peso >= obs_diff_peso) / len(diffs_peso)
    print(f"Peso do Bebe P-Valor: {p_peso:.5f} (Esperado: 0.0)")

    # 5. Testes A/B: NBA Salaries (Cleveland vs. Houston)
    # Cleveland Cavaliers: media = 10.23M, Houston Rockets: media = 7.10M
    # Simulando salarios em milhoes de dolares
    grupo_cleveland = np.random.normal(loc=10.23, scale=11.0, size=15)
    grupo_houston = np.random.normal(loc=7.10, scale=11.0, size=15)
    
    # Queremos testar se a diferenca e diferente de zero (teste bicaudal) ou se Cleveland > Houston
    diffs_nba, obs_diff_nba = testar_permutacao_diferenca_medias(grupo_houston, grupo_cleveland)
    plotar_permutacao(diffs_nba, obs_diff_nba, 'Teste de Permutacao: Salarios NBA (Cavs vs. Rockets)', '/home/reginaldo-fernandes/CDD/aula11/05_permutacao_nba.png')
    p_nba = np.count_nonzero(np.abs(diffs_nba) >= np.abs(obs_diff_nba)) / len(diffs_nba)
    print(f"NBA Salaries P-Valor: {p_nba:.5f} (Esperado: ~0.16)")
