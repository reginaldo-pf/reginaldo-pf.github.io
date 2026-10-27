"""
ShopGrids E-Commerce - Padrão Cache-Aside na Prática com Redis e TTL
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 05 (20/10/2026)
Prof. Me. Reginaldo Fernandes

Baseado no exemplo prático do vídeo:
"CACHE-ASIDE: Escalabilidade, Performance e Arquitetura de Software" (Renato Augusto)
https://www.youtube.com/watch?v=vRO0UfvsbDw

Roteiro Prático Demonstrado:
1. Sem Cache: Consulta direta ao banco SQL (SELECT * FROM categories WHERE is_featured = 1).
2. Cache-Aside Básico (GET + SET): Alívio do banco e resposta em < 1 ms, mas sem expiração.
3. O Problema da Inconsistência: Alteração na tabela categories não reflete no cache sem TTL.
4. Solução com TTL (SETEX 20s): Expiração automática e renovação transparente do cache.
"""

import json
import os
import sqlite3
import time
from flask import Flask, render_template, request, jsonify
import redis

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "shopgrids.db")
CACHE_KEY = "featured_categories"
DEFAULT_TTL = 20  # 20 segundos, exatamente como demonstrado no vídeo

# Conexão com o Redis (localhost:6379)
try:
    r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    r.ping()
    REDIS_ATIVO = True
except Exception as e:
    print(f"[AVISO] Redis não detectado em localhost:6379 ({e}).")
    REDIS_ATIVO = False


# ==============================================================================
# INICIALIZAÇÃO DO BANCO DE DADOS RELACIONAL (SQLITE - TABELA 'categories')
# ==============================================================================
CATEGORIAS_INICIAIS = [
    (1, "TV & Áudio", "fa-tv", 1),
    (2, "Desktop & Laptop", "fa-laptop", 1),
    (3, "Smartphones", "fa-mobile-screen-button", 1),
    (4, "Acessórios Gamer", "fa-gamepad", 1),
    (5, "Moda Inverno", "fa-mitten", 0),
    (6, "Aquecedores & Clima", "fa-temperature-arrow-up", 0),
    (7, "Câmeras & Drones", "fa-camera", 0),
    (8, "Smartwatches", "fa-clock", 0),
]


def init_db():
    """Cria a tabela 'categories' caso não exista e popula com os registros iniciais."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            image TEXT NOT NULL,
            is_featured INTEGER NOT NULL DEFAULT 0
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM categories")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO categories (id, name, image, is_featured) VALUES (?, ?, ?, ?)",
            CATEGORIAS_INICIAIS,
        )
        conn.commit()
    conn.close()


def buscar_categorias_destaque_no_banco():
    """
    Simula a consulta pesada ao Banco de Dados Relacional:
    SELECT id, name, image, is_featured FROM categories WHERE is_featured = 1
    """
    # Simula latência de I/O de disco e concorrência de conexões no banco relacional (~80 ms)
    time.sleep(0.08)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, image, is_featured FROM categories WHERE is_featured = 1 ORDER BY id"
    )
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return categorias


def listar_todas_categorias_no_banco():
    """Retorna todas as categorias cadastradas no banco para o painel de administração."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, image, is_featured FROM categories ORDER BY id")
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return categorias


# ==============================================================================
# ROTA PRINCIPAL DO EXEMPLO DO VÍDEO: GET /categories/featured
# ==============================================================================
@app.route("/categories/featured", methods=["GET"])
def get_featured_categories():
    """
    Endpoint consultado pelo Front-end / Postman para exibir as Categorias em Destaque.
    Suporta o parâmetro opcional ?estrategia=setex (padrão), ?estrategia=set ou ?estrategia=sem_cache
    para demonstrar ao vivo as etapas do vídeo.
    """
    inicio = time.time()
    estrategia = request.args.get("estrategia", "setex")  # 'setex' | 'set' | 'sem_cache'
    ttl_segundos = int(request.args.get("ttl", DEFAULT_TTL))

    # MODO 1: Sem Cache (Vai sempre direto ao banco de dados)
    if estrategia == "sem_cache" or not REDIS_ATIVO:
        categorias = buscar_categorias_destaque_no_banco()
        tempo_ms = round((time.time() - inicio) * 1000, 2)
        return jsonify({
            "origem": "BANCO_DE_DADOS (SQL)",
            "estrategia": "SEM_CACHE",
            "tempo_ms": tempo_ms,
            "ttl_restante": None,
            "total": len(categorias),
            "dados": categorias,
        })

    # MODO 2 e 3: Padrão Cache-Aside (Consulta o Redis primeiro!)
    cached_categories = r.get(CACHE_KEY)

    if cached_categories:
        # CACHE HIT: Encontrou na memória RAM do Redis! Nem encosta no banco SQL.
        categorias = json.loads(cached_categories)
        ttl_restante = r.ttl(CACHE_KEY)
        tempo_ms = round((time.time() - inicio) * 1000, 2)
        return jsonify({
            "origem": "CACHE_REDIS (Memória RAM)",
            "estrategia": estrategia.upper(),
            "tempo_ms": tempo_ms,
            "ttl_restante": ttl_restante,
            "total": len(categorias),
            "dados": categorias,
        })

    # CACHE MISS: Não existe no Redis -> Busca no Banco de Dados SQL
    categorias = buscar_categorias_destaque_no_banco()

    # Cria uma cópia dos dados dentro do Redis
    if estrategia == "set":
        # Etapa 2 do vídeo: SET simples sem TTL (gera problema de inconsistência!)
        r.set(CACHE_KEY, json.dumps(categorias))
        ttl_restante = -1  # -1 no Redis significa chave sem expiração (infinita)
    else:
        # Etapa 4 do vídeo: SETEX com TTL de 20 segundos (expiração automática!)
        r.setex(CACHE_KEY, ttl_segundos, json.dumps(categorias))
        ttl_restante = ttl_segundos

    tempo_ms = round((time.time() - inicio) * 1000, 2)
    return jsonify({
        "origem": "BANCO_DE_DADOS (SQL -> Salvo no Redis)",
        "estrategia": estrategia.upper(),
        "tempo_ms": tempo_ms,
        "ttl_restante": ttl_restante,
        "total": len(categorias),
        "dados": categorias,
    })


# ==============================================================================
# ROTAS DE ADMINISTRAÇÃO DO BANCO (SIMULAÇÃO DO TIME DE PRODUTO / MARKETING)
# ==============================================================================
@app.route("/categories", methods=["GET"])
def get_all_categories():
    """Lista todas as categorias da tabela SQL (marcadas ou não como destaque)."""
    categorias = listar_todas_categorias_no_banco()
    ttl = r.ttl(CACHE_KEY) if REDIS_ATIVO else -2
    existe_cache = bool(r.exists(CACHE_KEY)) if REDIS_ATIVO else False
    return jsonify({
        "total_banco": len(categorias),
        "cache_ativo": existe_cache,
        "ttl_restante": ttl,
        "categorias": categorias,
    })


@app.route("/categories/<int:cat_id>/toggle", methods=["POST", "PUT"])
def toggle_category_featured(cat_id: int):
    """
    Altera a coluna 'is_featured' diretamente no Banco de Dados SQL.
    IMPORTANTE: Assim como no vídeo, a tela de CRUD do time de produto altera APENAS
    o banco de dados (não toca no Redis), permitindo demonstrar a importância do TTL!
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT is_featured, name FROM categories WHERE id = ?", (cat_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    novo_status = 0 if row[0] == 1 else 1
    cursor.execute("UPDATE categories SET is_featured = ? WHERE id = ?", (novo_status, cat_id))
    conn.commit()
    conn.close()

    return jsonify({
        "status": "atualizado_no_banco",
        "id": cat_id,
        "name": row[1],
        "is_featured": novo_status,
        "aviso": "Alterado no Banco SQL! Se houver cache ativo no Redis, o Front-end só verá a mudança quando o TTL expirar (ou se o cache for deletado).",
    })


@app.route("/categories/preset/<nome_preset>", methods=["POST"])
def aplicar_preset_banco(nome_preset: str):
    """
    Atalhos rápidos para reproduzir os cenários do vídeo em 1 clique:
    - 'inicial': 4 categorias de tecnologia (TV, Laptop, Smartphones, Gamer)
    - 'inverno': Apenas 2 categorias (Moda Inverno e Aquecedores)
    - 'blackfriday': 6 categorias em destaque
    """
    presets = {
        "inicial": [1, 2, 3, 4],
        "inverno": [5, 6],
        "blackfriday": [1, 2, 3, 4, 7, 8],
    }
    ids_ativos = presets.get(nome_preset, [1, 2, 3, 4])

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE categories SET is_featured = 0")
    cursor.executemany(
        "UPDATE categories SET is_featured = 1 WHERE id = ?",
        [(i,) for i in ids_ativos],
    )
    conn.commit()
    conn.close()

    return jsonify({
        "status": "preset_aplicado_no_banco",
        "preset": nome_preset,
        "total_em_destaque_no_banco": len(ids_ativos),
        "ids_em_destaque": ids_ativos,
    })


@app.route("/categories/inverno", methods=["POST"])
def rota_inverno_atalho():
    """Atalho direto usado no roteiro da videoaula (Passo 6)."""
    return aplicar_preset_banco("inverno")


@app.route("/categories/blackfriday", methods=["POST"])
def rota_blackfriday_atalho():
    """Atalho direto usado no roteiro da videoaula (Passo 7)."""
    return aplicar_preset_banco("blackfriday")


@app.route("/cache/featured", methods=["DELETE", "POST"])
def deletar_cache():
    """Remove manualmente a chave 'featured_categories' do Redis (DEL featured_categories)."""
    if not REDIS_ATIVO:
        return jsonify({"erro": "Redis offline"}), 503

    removido = r.delete(CACHE_KEY)
    return jsonify({
        "status": "cache_removido",
        "chave": CACHE_KEY,
        "removido": bool(removido),
        "mensagem": "Chave 'featured_categories' apagada do Redis! A próxima consulta buscará do banco SQL.",
    })


@app.route("/")
def index():
    """Interface visual interativa que simula o Front-end ShopGrids + Banco SQL + Redis."""
    return render_template("index.html", redis_ativo=REDIS_ATIVO)


if __name__ == "__main__":
    init_db()
    print("=" * 70)
    print(" SHOPGRIDS - LABORATÓRIO CACHE-ASIDE COM REDIS (AULA 05 - IFCE TAUÁ)")
    print(" Endpoint principal: http://localhost:5000/categories/featured")
    print(" Painel interativo : http://localhost:5000")
    print("=" * 70)
    app.run(host="0.0.0.0", port=5000, debug=True)
