"""
FastCommerce NoSQL - Aplicação Web Prática com Redis
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 05 (20/10/2026)
Prof. Me. Reginaldo Fernandes

Objetivos Práticos Demonstrados:
1. Cache-Aside com TTL (catálogo de produtos e medição de latência Hit vs Miss).
2. Gerenciamento de Sessão de Usuário em Memória com Expiração Automática.
3. Carrinho de Compras Atômico utilizando Hashes do Redis (HINCRBY, HGETALL, HDEL).
4. Fila Assíncrona de Checkout utilizando Listas do Redis (LPUSH) e consumo com BRPOP.
"""

import json
import time
import uuid
from typing import Dict, Any, List
from flask import Flask, render_template, request, jsonify, make_response
import redis

app = Flask(__name__)

# Conexão com o Redis (padrão localhost:6379)
try:
    r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    r.ping()
    REDIS_ATIVO = True
except Exception as e:
    print(f"[AVISO] Não foi possível conectar ao Redis: {e}")
    REDIS_ATIVO = False

# ==============================================================================
# BASE DE DADOS SIMULADA (MOCK DO BANCO RELACIONAL / DISCO)
# NA AULA 06: Este catálogo passará a ser uma coleção de documentos no MongoDB!
# ==============================================================================
CATALOGO_PRODUTOS_ORIGINAL = [
    {
        "id": "prod_1",
        "nome": "Notebook Dell Inspiron 15",
        "categoria": "Informática",
        "preco": 3899.90,
        "imagem": "fa-laptop",
        "estoque": 14,
        "descricao": "Processador Intel Core i7, 16GB RAM, SSD 512GB NVMe, Tela FHD 15.6 polegadas."
    },
    {
        "id": "prod_2",
        "nome": "Monitor UltraWide LG 29\"",
        "categoria": "Monitores",
        "preco": 1249.00,
        "imagem": "fa-desktop",
        "estoque": 8,
        "descricao": "Resolução 2560x1080 IPS, 75Hz, HDR10 com suporte a Split Screen multitarefa."
    },
    {
        "id": "prod_3",
        "nome": "Teclado Mecânico Keychron K2",
        "categoria": "Periféricos",
        "preco": 620.00,
        "imagem": "fa-keyboard",
        "estoque": 25,
        "descricao": "Switches Gateron Brown, Bluetooth 5.1 e USB-C, compatível com Mac e Windows."
    },
    {
        "id": "prod_4",
        "nome": "Mouse Sem Fio Logitech MX Master 3S",
        "categoria": "Periféricos",
        "preco": 579.90,
        "imagem": "fa-computer-mouse",
        "estoque": 19,
        "descricao": "Sensor óptico 8K DPI silencioso, roda MagSpeed de aço e rolagem horizontal."
    },
    {
        "id": "prod_5",
        "nome": "Headset Gamer HyperX Cloud II",
        "categoria": "Áudio",
        "preco": 489.00,
        "imagem": "fa-headphones",
        "estoque": 30,
        "descricao": "Som Surround 7.1 virtual, drivers de 53mm e microfone com cancelamento de ruído."
    },
    {
        "id": "prod_6",
        "nome": "SSD NVMe Kingston KC3000 1TB",
        "categoria": "Armazenamento",
        "preco": 699.00,
        "imagem": "fa-hard-drive",
        "estoque": 42,
        "descricao": "Interface PCIe 4.0 NVMe, velocidades de leitura de até 7000 MB/s."
    }
]

PRODUTOS_POR_ID = {p["id"]: p for p in CATALOGO_PRODUTOS_ORIGINAL}


# ==============================================================================
# HELPERS DE SESSÃO DO USUÁRIO NO REDIS
# ==============================================================================
def obter_ou_criar_sessao(request_obj) -> str:
    """Recupera o token de sessão do cookie ou gera um novo."""
    session_id = request_obj.cookies.get("fastcommerce_session")
    if not session_id:
        session_id = str(uuid.uuid4())
    
    if REDIS_ATIVO:
        chave_sessao = f"session:{session_id}"
        # Se a sessão não existir no Redis, cria com dados padrão e TTL de 30 minutos (1800s)
        if not r.exists(chave_sessao):
            dados_usuario = {
                "id_usuario": f"usr_{session_id[:8]}",
                "nome": "Estudante ADS Tauá",
                "nivel": "Cliente VIP",
                "criado_em": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            r.setex(chave_sessao, 1800, json.dumps(dados_usuario))
        else:
            # Renova o TTL a cada acesso da sessão ativa (sliding expiration)
            r.expire(chave_sessao, 1800)
    return session_id


# ==============================================================================
# ROTAS PRINCIPAIS (FRONT-END E API)
# ==============================================================================
@app.route("/")
def index():
    """Página principal da loja com vitrine e carrinho."""
    session_id = obter_ou_criar_sessao(request)
    resp = make_response(render_template("index.html", session_id=session_id))
    resp.set_cookie("fastcommerce_session", session_id, max_age=1800)
    return resp


@app.route("/api/session", methods=["GET"])
def get_session():
    """Retorna os dados da sessão do usuário e o TTL restante no Redis."""
    session_id = obter_ou_criar_sessao(request)
    if not REDIS_ATIVO:
        return jsonify({"status": "error", "message": "Redis inativo"}), 503

    chave_sessao = f"session:{session_id}"
    ttl_restante = r.ttl(chave_sessao)
    dados_raw = r.get(chave_sessao)
    dados = json.loads(dados_raw) if dados_raw else {}

    return jsonify({
        "session_id": session_id,
        "ttl_segundos": ttl_restante,
        "usuario": dados
    })


@app.route("/api/produtos", methods=["GET"])
def get_produtos():
    """
    Demonstração do Padrão Cache-Aside com TTL:
    1. Verifica se a chave 'cache:catalogo_produtos' existe no Redis.
    2. Se existir: CACHE HIT (retorno ultra rápido em < 1 ms).
    3. Se não existir: CACHE MISS (simula busca em disco ~150 ms e grava no Redis com TTL).
    """
    tempo_inicio = time.time()
    chave_cache = "cache:catalogo_produtos"

    if REDIS_ATIVO and r.exists(chave_cache):
        # CACHE HIT
        dados_json = r.get(chave_cache)
        produtos = json.loads(dados_json)
        ttl = r.ttl(chave_cache)
        latencia_ms = round((time.time() - tempo_inicio) * 1000, 2)
        origem = "CACHE_HIT (RAM Redis)"
    else:
        # CACHE MISS (Simula leitura pesada de disco/SQL)
        time.sleep(0.12)  # Simula 120 ms de gargalo de banco relacional
        produtos = CATALOGO_PRODUTOS_ORIGINAL
        
        # Armazena no Redis com TTL de 45 segundos
        if REDIS_ATIVO:
            r.setex(chave_cache, 45, json.dumps(produtos))
            ttl = 45
        else:
            ttl = 0

        latencia_ms = round((time.time() - tempo_inicio) * 1000, 2)
        origem = "CACHE_MISS (Simulação de Disco/SGBD)"

    return jsonify({
        "origem": origem,
        "latencia_ms": latencia_ms,
        "ttl_cache_segundos": ttl,
        "total_produtos": len(produtos),
        "produtos": produtos
    })


@app.route("/api/cache/invalidar", methods=["POST"])
def invalidar_cache():
    """Permite ao estudante forçar a invalidação do cache para ver o próximo CACHE MISS."""
    if not REDIS_ATIVO:
        return jsonify({"status": "error"}), 503

    chave_cache = "cache:catalogo_produtos"
    deletado = r.delete(chave_cache)
    return jsonify({
        "status": "success",
        "chave": chave_cache,
        "invalidados": deletado,
        "mensagem": "Chave de cache removida! A próxima busca incorrerá em CACHE MISS proposital."
    })


@app.route("/api/carrinho", methods=["GET"])
def get_carrinho():
    """
    Retorna o carrinho de compras armazenado como HASH no Redis:
    Chave: cart:<session_id>
    Campos: { prod_1: 2, prod_3: 1 }
    """
    session_id = obter_ou_criar_sessao(request)
    if not REDIS_ATIVO:
        return jsonify({"itens": [], "subtotal": 0.0})

    chave_carrinho = f"cart:{session_id}"
    itens_hash = r.hgetall(chave_carrinho)
    ttl_carrinho = r.ttl(chave_carrinho)

    itens = []
    subtotal = 0.0

    for prod_id, qtd_str in itens_hash.items():
        qtd = int(qtd_str)
        if prod_id in PRODUTOS_POR_ID:
            prod = PRODUTOS_POR_ID[prod_id]
            total_item = round(prod["preco"] * qtd, 2)
            subtotal += total_item
            itens.append({
                "id": prod_id,
                "nome": prod["nome"],
                "preco_unitario": prod["preco"],
                "quantidade": qtd,
                "total_item": total_item
            })

    return jsonify({
        "session_id": session_id,
        "chave_redis": chave_carrinho,
        "ttl_segundos": ttl_carrinho,
        "itens": itens,
        "subtotal": round(subtotal, 2)
    })


@app.route("/api/carrinho/adicionar", methods=["POST"])
def adicionar_ao_carrinho():
    """
    Adiciona um item ao carrinho via HINCRBY atômico:
    Incrementa a quantidade sem necessidade de leitura prévia (operações atômicas).
    """
    session_id = obter_ou_criar_sessao(request)
    data = request.get_json() or {}
    prod_id = data.get("produto_id")
    qtd = int(data.get("quantidade", 1))

    if prod_id not in PRODUTOS_POR_ID:
        return jsonify({"status": "error", "message": "Produto inexistente"}), 404

    if not REDIS_ATIVO:
        return jsonify({"status": "error", "message": "Redis indisponível"}), 503

    chave_carrinho = f"cart:{session_id}"
    # HINCRBY: operação atômica de incremento no Hash
    nova_qtd = r.hincrby(chave_carrinho, prod_id, qtd)
    # Define TTL de 1 hora para o carrinho
    r.expire(chave_carrinho, 3600)

    return jsonify({
        "status": "success",
        "produto_id": prod_id,
        "quantidade_atual": nova_qtd,
        "mensagem": f"Item '{PRODUTOS_POR_ID[prod_id]['nome']}' adicionado ao carrinho!"
    })


@app.route("/api/carrinho/remover", methods=["POST"])
def remover_do_carrinho():
    """Remove um item do carrinho usando HDEL."""
    session_id = obter_ou_criar_sessao(request)
    data = request.get_json() or {}
    prod_id = data.get("produto_id")

    if not REDIS_ATIVO:
        return jsonify({"status": "error"}), 503

    chave_carrinho = f"cart:{session_id}"
    r.hdel(chave_carrinho, prod_id)

    return jsonify({
        "status": "success",
        "produto_id": prod_id,
        "mensagem": "Item removido do carrinho com HDEL."
    })


@app.route("/api/checkout", methods=["POST"])
def checkout():
    """
    Finaliza a compra e enfileira na LISTA do Redis (LPUSH fila:pedidos):
    1. Lê os itens do Hash cart:<session_id>.
    2. Serializa o pedido em JSON com ID único.
    3. Dá LPUSH na fila de processamento assíncrono.
    4. Deleta o carrinho com DEL cart:<session_id>.
    """
    session_id = obter_ou_criar_sessao(request)
    if not REDIS_ATIVO:
        return jsonify({"status": "error", "message": "Redis inativo"}), 503

    chave_carrinho = f"cart:{session_id}"
    itens_hash = r.hgetall(chave_carrinho)

    if not itens_hash:
        return jsonify({"status": "error", "message": "Carrinho vazio!"}), 400

    itens_pedido = []
    total_pedido = 0.0
    for pid, qtd_str in itens_hash.items():
        qtd = int(qtd_str)
        if pid in PRODUTOS_POR_ID:
            p = PRODUTOS_POR_ID[pid]
            sub = round(p["preco"] * qtd, 2)
            total_pedido += sub
            itens_pedido.append({
                "produto_id": pid,
                "nome": p["nome"],
                "quantidade": qtd,
                "preco_unitario": p["preco"],
                "total": sub
            })

    pedido = {
        "id_pedido": f"PED-{int(time.time())}-{uuid.uuid4().hex[:6].upper()}",
        "session_id": session_id,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total": round(total_pedido, 2),
        "itens": itens_pedido,
        "status": "ENFILEIRADO_AGUARDANDO_WORKER"
    }

    # Enfileira na Lista do Redis (LPUSH)
    chave_fila = "fila:pedidos"
    posicao_fila = r.lpush(chave_fila, json.dumps(pedido))

    # Limpa o carrinho de compras do Redis
    r.delete(chave_carrinho)

    return jsonify({
        "status": "success",
        "pedido": pedido,
        "posicao_na_fila": posicao_fila,
        "mensagem": "Pedido enviado com sucesso para a fila assíncrona do Redis (LPUSH)!"
    })


@app.route("/api/pedidos/fila", methods=["GET"])
def get_fila_pedidos():
    """Retorna os pedidos que estão na fila aguardando o worker."""
    if not REDIS_ATIVO:
        return jsonify({"tamanho": 0, "pedidos": []})

    chave_fila = "fila:pedidos"
    tamanho = r.llen(chave_fila)
    # Pega até os últimos 10 itens da lista sem removê-los
    itens_raw = r.lrange(chave_fila, 0, 9)
    pedidos = [json.loads(p) for p in itens_raw]

    return jsonify({
        "tamanho_fila": tamanho,
        "pedidos_recentes": pedidos
    })


@app.route("/api/telemetria", methods=["GET"])
def telemetria():
    """Retorna estatísticas operacionais do Redis para o painel de monitoramento."""
    if not REDIS_ATIVO:
        return jsonify({"status": "offline"})

    try:
        info_mem = r.info("memory")
        info_stats = r.info("stats")
        info_clients = r.info("clients")
        chaves_existentes = r.keys("*")

        return jsonify({
            "status": "online",
            "memoria_usada_humana": info_mem.get("used_memory_human", "N/A"),
            "memoria_pico_humana": info_mem.get("used_memory_peak_human", "N/A"),
            "conexoes_ativas": info_clients.get("connected_clients", 1),
            "total_comandos_executados": info_stats.get("total_commands_processed", 0),
            "total_chaves": len(chaves_existentes),
            "chaves_amostra": chaves_existentes[:15]
        })
    except Exception as err:
        return jsonify({"status": "error", "message": str(err)})


if __name__ == "__main__":
    print("=" * 80)
    print("INICIANDO SERVIDOR WEB FASTCOMMERCE (AULA 05 - BANCO DE DADOS NÃO-RELACIONAIS)")
    print("Acesse no navegador: http://localhost:5000")
    print("Conexão Redis: localhost:6379 -> Status:", "ONLINE" if REDIS_ATIVO else "OFFLINE")
    print("=" * 80)
    app.run(host="0.0.0.0", port=5000, debug=True)
