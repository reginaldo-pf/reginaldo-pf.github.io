#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina: Banco de Dados Não-Relacionais (ADS16)
Aula 04: Modelo Chave-Valor com Redis (Arquitetura em Memória e Estruturas Nativas)
Docente: Prof. Me. Reginaldo Pereira Fernandes
=============================================================================

Este script implementa casos reais de mercado para o Redis:
1. Cache de Consultas de Busca (Search Query Cache) com Cache-Aside e TTL
2. Variações Avançadas de SET e GET (NX, XX, KEEPTTL, GETDEL, MSET, MGET)
3. Persistência em Disco (Inspeção de RDB Snapshotting e AOF)
4. Modelagem com as 5 Estruturas Nativas (Strings, Hashes, Lists, Sets, Sorted Sets)
5. Simulação de LangCache / Memória de Agentes de IA (Redis para LLMs)
6. Benchmarking e Geração de Gráfico Comparativo de Latência
=============================================================================
"""

import time
import json
import random
import redis
import matplotlib.pyplot as plt
import numpy as np

# Configuração de tema visual acessível e limpo para Matplotlib
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({
    'figure.figsize': (13, 8),
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'lines.linewidth': 2.2,
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica']
})


def conectar_redis():
    """Estabelece conexão com o servidor local do Redis."""
    try:
        r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        r.ping()
        print("✅ Conectado com sucesso ao Redis (localhost:6379)!\n")
        return r
    except redis.ConnectionError as err:
        print(f"❌ Erro ao conectar ao Redis: {err}")
        print("💡 Certifique-se de que o Redis está rodando via Docker, WSL ou serviço local.")
        exit(1)


# =============================================================================
# CASO REAL 1: SISTEMA DE BUSCA DE E-COMMERCE (SEARCH CACHE-ASIDE)
# =============================================================================
def busca_banco_relacional_mock(termo: str):
    """
    Simula uma consulta pesada em banco relacional (PostgreSQL/MySQL) ou
    orientado a documentos (MongoDB) com filtros complexos e agregação.
    Latência média simulada: 150 a 250 ms.
    """
    tempo_processamento = random.uniform(0.15, 0.25)
    time.sleep(tempo_processamento)
    
    catalogo = {
        "notebook dell": [
            {"id": 101, "nome": "Notebook Dell Inspiron 15", "preco": 3899.00, "estoque": 12},
            {"id": 102, "nome": "Notebook Dell Vostro 14", "preco": 4299.00, "estoque": 8}
        ],
        "fone bluetooth": [
            {"id": 201, "nome": "Fone Sony WH-1000XM5", "preco": 1999.00, "estoque": 25},
            {"id": 202, "nome": "Fone JBL Tune 520BT", "preco": 249.90, "estoque": 40}
        ],
        "monitor gamer": [
            {"id": 301, "nome": "Monitor LG UltraGear 27' 144Hz", "preco": 1299.00, "estoque": 15},
            {"id": 302, "nome": "Monitor Samsung Odyssey G3", "preco": 1149.00, "estoque": 20}
        ]
    }
    resultados = catalogo.get(termo.lower(), [
        {"id": 999, "nome": f"Produto Genérico para '{termo}'", "preco": 99.90, "estoque": 5}
    ])
    return resultados, tempo_processamento * 1000  # retorna dados e tempo em ms


def consultar_produtos_com_cache(r: redis.Redis, termo: str, ttl_segundos: int = 60):
    """
    Implementa o padrão Cache-Aside:
    1. Verifica se a chave existe no Redis (Cache Hit -> < 1 ms).
    2. Se não existir (Cache Miss), busca no banco lento e grava no Redis com TTL.
    """
    chave_cache = f"busca:catalogo:{termo.strip().lower().replace(' ', '_')}"
    
    inicio = time.perf_counter()
    dado_cache = r.get(chave_cache)
    
    if dado_cache:
        # Cache Hit: Resposta imediata da memória RAM
        duracao_ms = (time.perf_counter() - inicio) * 1000
        produtos = json.loads(dado_cache)
        ttl_restante = r.ttl(chave_cache)
        print(f"  ⚡ [CACHE HIT] Termo: '{termo}' | Latência: {duracao_ms:.3f} ms | TTL restante: {ttl_restante}s")
        # Incrementa contador atômico de pesquisas
        r.incr(f"stats:busca_hit:{termo}")
        r.zincrby("ranking:buscas_populares", 1, termo)
        return produtos, duracao_ms, "HIT"
    else:
        # Cache Miss: Busca na fonte primária (disco/relacional)
        print(f"  🐢 [CACHE MISS] Termo: '{termo}' -> Consultando banco relacional em disco...")
        produtos, duracao_db = busca_banco_relacional_mock(termo)
        
        # Grava no Redis com expiração configurada (SET com EX)
        # O valor é serializado em JSON (String no Redis)
        r.set(chave_cache, json.dumps(produtos), ex=ttl_segundos)
        
        duracao_total = (time.perf_counter() - inicio) * 1000
        print(f"  💾 Gravado no Redis com chave '{chave_cache}' (TTL={ttl_segundos}s) | Latência Total: {duracao_total:.2f} ms")
        r.zincrby("ranking:buscas_populares", 1, termo)
        return produtos, duracao_total, "MISS"


# =============================================================================
# CASO REAL 2: DEMONSTRAÇÃO PRÁTICA DAS VARIAÇÕES DE SET E GET
# =============================================================================
def demonstrar_variacoes_set_get(r: redis.Redis):
    """
    Apresenta em detalhes todas as variações de SET e GET exigidas no roteiro.
    """
    print("\n" + "="*70)
    print("🛠️ DEMONSTRAÇÃO DAS VARIAÇÕES AVANÇADAS DE SET E GET")
    print("="*70)
    
    # 1. SET simples e GET simples
    r.set("sistema:versao", "v2.4.0")
    print(f"1. SET / GET: sistema:versao = '{r.get('sistema:versao')}'")
    
    # 2. SET com EX (Expiração em Segundos)
    r.set("token:recuperacao:user_99", "xyz_789_segredo", ex=5)
    print(f"2. SET com EX 5: token criado. TTL imediato: {r.ttl('token:recuperacao:user_99')}s")
    
    # 3. SET com PX (Expiração em Milissegundos)
    r.set("alerta:temporario", "falha_rede", px=1500)
    print(f"3. SET com PX 1500: PTTL = {r.pttl('alerta:temporario')} ms")
    
    # 4. SET com NX (Not eXists - Trava Distribuída / Concorrência)
    # Cenário: Adquirir trava de estoque para impedir compra dupla
    lock_chave = "lock:estoque:produto_101"
    adquiriu_1 = r.set(lock_chave, "worker_worker_A", nx=True, ex=10)
    adquiriu_2 = r.set(lock_chave, "worker_worker_B", nx=True, ex=10)
    print(f"4. SET com NX (Distributed Lock):")
    print(f"   - Worker A tentou travar: {'SUCESSO (Retornou True)' if adquiriu_1 else 'FALHA'}")
    print(f"   - Worker B tentou travar simultaneamente: {'SUCESSO' if adquiriu_2 else 'BLOQUEADO (Retornou None/Nil)'}")
    r.delete(lock_chave)
    
    # 5. SET com XX (Only if eXists - Atualização estrita)
    r.delete("config:modo_manutencao")
    tentativa_xx1 = r.set("config:modo_manutencao", "ativo", xx=True)
    print(f"5. SET com XX (Apenas se já existir):")
    print(f"   - Tentativa em chave inexistente: {tentativa_xx1} (Não gravou)")
    r.set("config:modo_manutencao", "desativado")
    tentativa_xx2 = r.set("config:modo_manutencao", "ativo", xx=True)
    print(f"   - Tentativa após criar chave: {tentativa_xx2} (Atualizou para '{r.get('config:modo_manutencao')}')")
    
    # 6. SET com KEEPTTL (Atualiza valor preservando o tempo restante de vida)
    r.set("sessao:usuario_beta", "dados_v1", ex=30)
    time.sleep(1)
    ttl_antes = r.ttl("sessao:usuario_beta")
    r.set("sessao:usuario_beta", "dados_v2_atualizados", keepttl=True)
    ttl_depois = r.ttl("sessao:usuario_beta")
    print(f"6. SET com KEEPTTL: TTL antes = {ttl_antes}s | TTL após atualizar valor = {ttl_depois}s (Preservado!)")
    
    # 7. SET com GET (Define novo valor e retorna atomicamente o anterior)
    valor_anterior = r.set("metrica:requisicoes_minuto", "1540", get=True)
    print(f"7. SET com GET atômico: Valor retornado antigo = '{valor_anterior}', novo valor = '{r.get('metrica:requisicoes_minuto')}'")
    
    # 8. MSET e MGET (Multiplas chaves em um único Round-Trip de rede)
    r.mset({
        "moeda:usd_brl": "5.45",
        "moeda:eur_brl": "5.95",
        "moeda:btc_brl": "345000.00"
    })
    valores = r.mget(["moeda:usd_brl", "moeda:eur_brl", "moeda:btc_brl"])
    print(f"8. MSET / MGET (Operações em lote): USD={valores[0]}, EUR={valores[1]}, BTC={valores[2]}")
    
    # 9. GETDEL (Obtém o valor e deleta a chave atomicamente - Tokens de uso único)
    r.set("cupom:desconto_primeira_compra:user_50", "DESCONTO_IFCE_50", ex=60)
    cupom_resgatado = r.getdel("cupom:desconto_primeira_compra:user_50")
    print(f"9. GETDEL (Consumo atômico): Cupom resgatado = '{cupom_resgatado}', Verificação pós-GETDEL = {r.get('cupom:desconto_primeira_compra:user_50')}")
    
    # 10. GETEX (Obtém o valor e manipula o TTL na mesma operação)
    r.set("cache:sessao:user_88", "perfil_ativo", ex=10)
    dado_com_novo_ttl = r.getex("cache:sessao:user_88", ex=120)  # Renovou a sessão para 120s!
    print(f"10. GETEX (Leitura com renovação de sessão): Valor = '{dado_com_novo_ttl}', Novo TTL = {r.ttl('cache:sessao:user_88')}s")
    
    # 11. GETRANGE e STRLEN
    r.set("mensagem:boas_vindas", "Bem-vindo ao IFCE Campus Taua!")
    substring = r.getrange("mensagem:boas_vindas", 15, 29)
    comprimento = r.strlen("mensagem:boas_vindas")
    print(f"11. GETRANGE / STRLEN: Substring[15..29] = '{substring}' | Tamanho total = {comprimento} caracteres")


# =============================================================================
# CASO REAL 3: ARQUITETURA EM MEMÓRIA E PERSISTÊNCIA (RDB E AOF)
# =============================================================================
def demonstrar_persistencia(r: redis.Redis):
    """
    Explica a volatilidade da memória RAM e exibe o status de RDB e AOF.
    """
    print("\n" + "="*70)
    print("💾 ARQUITETURA EM MEMÓRIA E CONFIGURAÇÃO DE PERSISTÊNCIA (RDB & AOF)")
    print("="*70)
    
    info_persist = r.info("persistence")
    info_memory = r.info("memory")
    
    print("🧠 1. Status da Memória RAM (Volátil):")
    print(f"   - Memória utilizada: {info_memory['used_memory_human']}")
    print(f"   - Pico de memória: {info_memory['used_memory_peak_human']}")
    print(f"   - Taxa de fragmentação: {info_memory['mem_fragmentation_ratio']}")
    
    print("\n📸 2. Snapshotting RDB (Dump em Disco):")
    print(f"   - Último salvamento RDB (Unix Timestamp): {info_persist['rdb_last_save_time']}")
    data_formatada = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(info_persist['rdb_last_save_time']))
    print(f"   - Data legível do último RDB: {data_formatada}")
    print(f"   - Alterações na memória desde o último snapshot: {info_persist['rdb_changes_since_last_save']}")
    print(f"   - Status do último BGSAVE: {info_persist['rdb_last_bgsave_status']}")
    
    # Disparando um BGSAVE não-bloqueante
    try:
        resultado_bgsave = r.bgsave()
        print(f"   ⚡ Comando BGSAVE executado: {resultado_bgsave}")
    except redis.ResponseError as e:
        print(f"   ℹ️ BGSAVE já em andamento ou gerado recentemente: {e}")
        
    print("\n📜 3. Log de Operações AOF (Append-Only File):")
    print(f"   - AOF ativado: {'Sim' if info_persist.get('aof_enabled') == 1 else 'Não (Modo padrão: RDB ativo)'}")
    if info_persist.get('aof_enabled') == 1:
        print(f"   - Tamanho do arquivo AOF: {info_persist.get('aof_current_size', 0)} bytes")
        print(f"   - Modo fsync: {r.config_get('appendfsync').get('appendfsync')}")


# =============================================================================
# CASO REAL 4: AS 5 ESTRUTURAS NATIVAS DO REDIS
# =============================================================================
def demonstrar_estruturas_nativas(r: redis.Redis):
    """
    Demonstra as 5 estruturas fundamentais com problemas práticos:
    - Strings: Contadores e Cache
    - Hashes: Objetos e Perfis de Usuário
    - Lists: Fila de Tarefas FIFO e Histórico de Pesquisa
    - Sets: Tags Únicas e Operações de Conjunto (Interseção)
    - Sorted Sets: Leaderboards e Rankings com Scores
    """
    print("\n" + "="*70)
    print("🧩 AS 5 ESTRUTURAS DE DADOS NATIVAS DO REDIS EM CENÁRIOS REAIS")
    print("="*70)
    
    # 1. HASHES: Perfil de Aluno / Usuário
    aluno_key = "usuario:aluno:1042"
    r.hset(aluno_key, mapping={
        "nome": "Carlos Eduardo",
        "curso": "ADS IFCE Tauá",
        "semestre": "4",
        "pontos_desafio": "120"
    })
    r.hincrby(aluno_key, "pontos_desafio", 35) # Incrementa pontos atomicamente
    dados_aluno = r.hgetall(aluno_key)
    print(f"1. HASH (Objeto estruturado) '{aluno_key}':")
    print(f"   - Nome: {dados_aluno['nome']} | Pontos: {dados_aluno['pontos_desafio']}")
    
    # 2. LISTS: Histórico Recente de Buscas do Usuário (Capacidade limitada a 5)
    hist_key = "busca:historico:user_1042"
    r.delete(hist_key)
    termos_pesquisados = ["notebook dell", "mouse logitech", "teclado mecânico", "monitor ultrawide", "hub usb-c", "webcam full hd"]
    for termo in termos_pesquisados:
        r.lpush(hist_key, termo)      # Insere no topo (mais recente primeiro)
        r.ltrim(hist_key, 0, 4)       # Mantém apenas os 5 mais recentes
    historico_recente = r.lrange(hist_key, 0, -1)
    print(f"\n2. LIST (Histórico com LTRIM cap) '{hist_key}':")
    print(f"   - Últimas 5 pesquisas: {historico_recente}")
    
    # 3. SETS: Tags de Categorização e Recomendação por Interseção
    r.delete("tags:produto:notebook_dell", "tags:produto:desktop_gamer")
    r.sadd("tags:produto:notebook_dell", "portatil", "computador", "bivolt", "ssd", "usb-c")
    r.sadd("tags:produto:desktop_gamer", "desktop", "computador", "rgb", "ssd", "gpu_dedicada")
    tags_em_comum = r.sinter("tags:produto:notebook_dell", "tags:produto:desktop_gamer")
    print(f"\n3. SET (Conjuntos sem repetição e Álgebra de Conjuntos):")
    print(f"   - Tags em comum (SINTER): {tags_em_comum}")
    
    # 4. SORTED SETS: Leaderboard de Termos Mais Pesquisados da Semana
    ranking_key = "ranking:termos_quentes"
    r.delete(ranking_key)
    r.zadd(ranking_key, {"notebook dell": 150, "smartphone 5g": 210, "alexa": 95, "cadeira gamer": 180})
    r.zincrby(ranking_key, 75, "notebook dell") # O termo notebook disparou em buscas!
    top3 = r.zrevrange(ranking_key, 0, 2, withscores=True)
    print(f"\n4. SORTED SET (Ranking com pontuação atômica - ZREVRANGE):")
    for pos, (item, score) in enumerate(top3, 1):
        print(f"   #{pos} Termo: '{item}' com {int(score)} pesquisas")


# =============================================================================
# CASO REAL 5: MODERNIZAÇÃO - REDIS PARA IA / LANGCACHE & AGENT MEMORY
# =============================================================================
def simular_langcache_ia(r: redis.Redis):
    """
    Conecta o conceito com a imagem do Redis fornecida pelo usuário:
    - Cache across similar prompts (LangCache): Corta 40-80% de custo de LLM
    - Agent Memory: LLMs são stateless; Redis guarda memória entre turnos e sessões.
    """
    print("\n" + "="*70)
    print("🤖 MODERNIZAÇÃO: REDIS COMO CONTEXT ENGINE & LANGCACHE PARA IA")
    print("="*70)
    
    prompts_teste = [
        "Como configurar persistência RDB no Redis?",
        "Qual o teorema que aborda partições de rede?",
        "Como configurar persistência RDB no Redis?", # Repetido -> Hit imediato!
        "Qual o teorema que aborda partições de rede?"  # Repetido -> Hit imediato!
    ]
    
    respostas_llm_mock = {
        "Como configurar persistência RDB no Redis?": "Edite a diretiva 'save <segundos> <mudanças>' no redis.conf ou utilize o comando BGSAVE.",
        "Qual o teorema que aborda partições de rede?": "É o Teorema CAP (Brewer, 2000), complementado pelo Teorema PACELC (Abadi, 2012)."
    }
    
    for prompt in prompts_teste:
        prompt_hash = f"langcache:prompt:{hash(prompt)}"
        cached = r.get(prompt_hash)
        
        if cached:
            print(f"  ⚡ [LANGCACHE HIT] Prompt: \"{prompt[:35]}...\"")
            print(f"     Latência: 0.8 ms | Economia: $0.02 (Token de LLM economizado)")
        else:
            print(f"  🧠 [LLM COLD INFERENCE] Enviando para modelo generativo...")
            time.sleep(0.4) # Simula 400ms de inferência remota
            resposta = respostas_llm_mock[prompt]
            # Salva no Redis com TTL de 1 hora
            r.set(prompt_hash, resposta, ex=3600)
            print(f"     Latência: 400.0 ms | Resposta computada e armazenada no LangCache!")


# =============================================================================
# CASO REAL 6: BENCHMARKING E GERAÇÃO DE GRÁFICO DIDÁTICO
# =============================================================================
def executar_benchmark_e_gerar_grafico(r: redis.Redis):
    """
    Executa uma bateria de 60 consultas simuladas medindo a latência
    e plota um gráfico visual detalhado.
    """
    print("\n" + "="*70)
    print("📊 EXECUTANDO BENCHMARK E GERANDO GRÁFICO COMPARATIVO...")
    print("="*70)
    
    termos_pool = [
        "notebook dell", "fone bluetooth", "monitor gamer",
        "teclado mecanico", "mouse sem fio", "ssd nvme"
    ]
    
    latencias_db_direto = []
    latencias_cache_aside = []
    tipos_evento = [] # "MISS" ou "HIT"
    
    # Limpa caches anteriores de teste
    for t in termos_pool:
        r.delete(f"busca:catalogo:{t.replace(' ', '_')}")
    
    total_requisicoes = 40
    print(f"Simulando {total_requisicoes} buscas de usuários em sequência...")
    
    for i in range(total_requisicoes):
        # Seleciona termo (usando distribuição enviesada para simular termos populares)
        termo = random.choices(termos_pool, weights=[0.4, 0.25, 0.15, 0.1, 0.05, 0.05])[0]
        
        # Medição 1: Se fôssemos direto no banco em disco
        lat_db_estimada = random.uniform(160, 240)
        latencias_db_direto.append(lat_db_estimada)
        
        # Medição 2: Usando Redis Cache-Aside
        _, lat_cache, status = consultar_produtos_com_cache(r, termo, ttl_segundos=120)
        latencias_cache_aside.append(lat_cache)
        tipos_evento.append(status)
    
    # Métricas consolidadas
    media_db = np.mean(latencias_db_direto)
    hits_lat = [l for l, s in zip(latencias_cache_aside, tipos_evento) if s == "HIT"]
    misses_lat = [l for l, s in zip(latencias_cache_aside, tipos_evento) if s == "MISS"]
    media_hit = np.mean(hits_lat) if hits_lat else 0.5
    taxa_hit = (tipos_evento.count("HIT") / total_requisicoes) * 100
    fator_aceleracao = media_db / media_hit
    
    print("\n📈 RESULTADOS DO BENCHMARK:")
    print(f"  - Latência Média Banco Relacional/Disco: {media_db:.2f} ms")
    print(f"  - Latência Média Redis Cache Hit (RAM):  {media_hit:.3f} ms")
    print(f"  - Taxa de Acerto (Cache Hit Ratio):     {taxa_hit:.1f}%")
    print(f"  - Ganho de Performance (Speedup):       {fator_aceleracao:.1f}x mais rápido!")
    
    # Plotagem dos Gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Subplot 1: Comparativo de Barra de Latência Média (Escala Logarítmica)
    categorias = ['Banco em Disco\n(Sem Cache)', 'Cache Miss\n(Disco + Gravação)', 'Redis Cache Hit\n(Memória RAM)']
    medias = [media_db, np.mean(misses_lat), media_hit]
    cores = ['#DC2626', '#F59E0B', '#10B981']
    
    barras = ax1.bar(categorias, medias, color=cores, width=0.55, edgecolor='black', linewidth=1.2)
    ax1.set_yscale('log')
    ax1.set_ylabel('Tempo de Resposta em ms (Escala Logarítmica)')
    ax1.set_title('Impacto da Arquitetura em Memória na Latência', fontweight='bold')
    ax1.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Anotações de valores em cima das barras
    for barra, valor in zip(barras, medias):
        y_pos = valor * 1.2 if valor > 1 else valor * 2
        ax1.text(barra.get_x() + barra.get_width()/2, y_pos,
                 f"{valor:.2f} ms", ha='center', va='bottom', fontweight='bold', fontsize=11)
        
    ax1.text(0.5, 0.05, f"Ganho de Velocidade: {fator_aceleracao:.0f}x mais rápido!",
             transform=ax1.transAxes, ha='center', fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#DCFCE7', edgecolor='#16A34A', alpha=0.9))
    
    # Subplot 2: Evolução das Requisições ao Longo do Tempo (Hit vs Miss)
    indices = list(range(1, total_requisicoes + 1))
    ax2.plot(indices, latencias_db_direto, color='#DC2626', linestyle='--', alpha=0.5, label='Sem Cache (Banco Disco)')
    
    # Pontos de Cache Miss e Cache Hit
    x_miss = [i for i, s in zip(indices, tipos_evento) if s == "MISS"]
    y_miss = [l for l, s in zip(latencias_cache_aside, tipos_evento) if s == "MISS"]
    x_hit = [i for i, s in zip(indices, tipos_evento) if s == "HIT"]
    y_hit = [l for l, s in zip(latencias_cache_aside, tipos_evento) if s == "HIT"]
    
    ax2.scatter(x_miss, y_miss, color='#F59E0B', s=80, zorder=5, label=f'Cache Miss ({len(x_miss)})', marker='s')
    ax2.scatter(x_hit, y_hit, color='#10B981', s=90, zorder=6, label=f'Cache Hit ({len(x_hit)})', marker='o')
    ax2.plot(indices, latencias_cache_aside, color='#10B981', alpha=0.6, linewidth=1.5)
    
    ax2.set_xlabel('Número Sequencial da Requisição do Usuário')
    ax2.set_ylabel('Tempo de Resposta (ms)')
    ax2.set_title(f'Evolução Temporal: Aquecimento de Cache (Hit Ratio: {taxa_hit:.1f}%)', fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    caminho_grafico = "codigo/grafico_latencia_busca.png"
    plt.savefig(caminho_grafico, dpi=300)
    print(f"\n🖼️ Gráfico salvo com sucesso em: '{caminho_grafico}'!")
    
    # Também salva na pasta materiais/figuras para uso direto
    plt.savefig("materiais/figuras/grafico_latencia_busca.png", dpi=300)


def main():
    print("="*70)
    print("IFCE CAMPUS TAUÁ - ADS - BANCO DE DADOS NÃO-RELACIONAIS (ADS16)")
    print("AULA 04: MODELO CHAVE-VALOR & ARQUITETURA EM MEMÓRIA DO REDIS")
    print("Prof. Me. Reginaldo Pereira Fernandes")
    print("="*70)
    
    r = conectar_redis()
    
    # 1. Demonstração das variações de comandos
    demonstrar_variacoes_set_get(r)
    
    # 2. Demonstração de Persistência
    demonstrar_persistencia(r)
    
    # 3. As 5 estruturas nativas
    demonstrar_estruturas_nativas(r)
    
    # 4. Modernização: Redis para IA (LangCache)
    simular_langcache_ia(r)
    
    # 5. Benchmark e Geração do Gráfico de Latência
    executar_benchmark_e_gerar_grafico(r)
    
    print("\n✅ Demonstração prática concluída com êxito!")


if __name__ == "__main__":
    main()
