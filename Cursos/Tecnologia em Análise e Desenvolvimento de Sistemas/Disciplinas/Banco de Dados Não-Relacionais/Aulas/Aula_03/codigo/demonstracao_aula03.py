#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS16)
Disciplina: Banco de Dados Não-Relacionais
Aula 03 (Sábado Letivo) - Prática Autônoma: MongoDB, Redis e Padrão Cache-Aside
Docente: Prof. Me. Reginaldo Pereira Fernandes
================================================================================
Este script implementa uma demonstração prática e autônoma da integração
arquitetural moderna entre um Banco Orientado a Documentos (MongoDB) e um
Banco Chave-Valor em Memória (Redis), aplicando o padrão Cache-Aside Pattern
com medição estatística de latência e geração de gráfico didático.
================================================================================
"""

import sys
import os
import time
import json
import random
from typing import Dict, Any, Optional

# Visualização de Dados (Seguindo cdd-aula-template)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Tentativa de importação dos drivers oficiais
try:
    import pymongo
    from pymongo.collection import Collection
    HAS_PYMONGO = True
except ImportError:
    HAS_PYMONGO = False

try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False


# ==============================================================================
# CONFIGURAÇÃO DE ESTILO GRÁFICO (cdd-aula-template)
# ==============================================================================
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({
    'figure.figsize': (11, 6),
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'lines.linewidth': 2.2,
    'font.family': 'sans-serif'
})

def despine(ax):
    """Remove bordas superiores e direitas para acabamento visual limpo."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


# ==============================================================================
# CLIENTES MOCK / FALLBACK (Garante execução mesmo se banco estiver offline)
# ==============================================================================
class MockMongoClient:
    """Simulador em memória do MongoDB para garantir execução sem falhas."""
    def __init__(self):
        self._dbs = {}

    def __getitem__(self, db_name):
        if db_name not in self._dbs:
            self._dbs[db_name] = MockDatabase(db_name)
        return self._dbs[db_name]


class MockDatabase:
    def __init__(self, name):
        self.name = name
        self._collections = {}

    def __getitem__(self, col_name):
        if col_name not in self._collections:
            self._collections[col_name] = MockCollection(col_name)
        return self._collections[col_name]


class MockCollection:
    def __init__(self, name):
        self.name = name
        self.docs = []

    def drop(self):
        self.docs = []

    def insert_one(self, doc):
        d = dict(doc)
        if '_id' not in d:
            d['_id'] = f"mock_{len(self.docs)+1}"
        self.docs.append(d)
        time.sleep(0.008)  # Simula latência de rede/disco do MongoDB (~8ms)
        class Res:
            inserted_id = d['_id']
        return Res()

    def insert_many(self, docs):
        res_ids = []
        for doc in docs:
            r = self.insert_one(doc)
            res_ids.append(r.inserted_id)
        return res_ids

    def find_one(self, filter_dict, projection=None):
        time.sleep(0.009)  # Simula latência de consulta no MongoDB (~9ms)
        for doc in self.docs:
            match = True
            for k, v in filter_dict.items():
                if doc.get(k) != v:
                    match = False
                    break
            if match:
                res = dict(doc)
                if projection and '_id' in projection and projection['_id'] == 0:
                    res.pop('_id', None)
                return res
        return None

    def find(self, filter_dict=None, projection=None):
        time.sleep(0.012)
        results = []
        filter_dict = filter_dict or {}
        for doc in self.docs:
            match = True
            for k, v in filter_dict.items():
                if doc.get(k) != v:
                    match = False
                    break
            if match:
                res = dict(doc)
                if projection and '_id' in projection and projection['_id'] == 0:
                    res.pop('_id', None)
                results.append(res)
        return results

    def update_one(self, filter_dict, update_dict):
        time.sleep(0.008)
        for doc in self.docs:
            match = True
            for k, v in filter_dict.items():
                if doc.get(k) != v:
                    match = False
                    break
            if match:
                if '$set' in update_dict:
                    doc.update(update_dict['$set'])
                if '$inc' in update_dict:
                    for k, inc_val in update_dict['$inc'].items():
                        doc[k] = doc.get(k, 0) + inc_val
                return True
        return False

    def delete_many(self, filter_dict):
        time.sleep(0.007)
        initial = len(self.docs)
        self.docs = [d for d in self.docs if not all(d.get(k) == v for k, v in filter_dict.items())]
        class DelRes:
            deleted_count = initial - len(self.docs)
        return DelRes()


class MockRedisClient:
    """Simulador em memória do Redis com TTL e estruturas básicas."""
    def __init__(self):
        self.store = {}
        self.ttls = {}
        self.hashes = {}
        self.lists = {}
        self.zsets = {}

    def ping(self):
        return True

    def set(self, key, value, ex=None):
        time.sleep(0.0004)  # Simula latência de memória Redis (~0.4ms)
        self.store[key] = str(value)
        if ex:
            self.ttls[key] = time.time() + ex
        return True

    def get(self, key):
        time.sleep(0.0003)  # Simula latência de leitura Redis (~0.3ms)
        if key in self.ttls and time.time() > self.ttls[key]:
            del self.store[key]
            del self.ttls[key]
            return None
        val = self.store.get(key)
        return val.encode('utf-8') if val is not None else None

    def delete(self, *keys):
        for k in keys:
            self.store.pop(k, None)
            self.ttls.pop(k, None)
            self.hashes.pop(k, None)
            self.lists.pop(k, None)
            self.zsets.pop(k, None)
        return len(keys)

    def ttl(self, key):
        if key in self.ttls:
            remaining = int(self.ttls[key] - time.time())
            return remaining if remaining > 0 else -2
        return -1 if key in self.store else -2

    def incr(self, key):
        val = int(self.store.get(key, 0)) + 1
        self.store[key] = str(val)
        return val

    def hset(self, name, key=None, value=None, mapping=None):
        if name not in self.hashes:
            self.hashes[name] = {}
        if mapping:
            self.hashes[name].update(mapping)
        elif key is not None and value is not None:
            self.hashes[name][key] = str(value)
        return True

    def hget(self, name, key):
        return self.hashes.get(name, {}).get(key)

    def hgetall(self, name):
        return {k.encode(): v.encode() if isinstance(v, str) else str(v).encode()
                for k, v in self.hashes.get(name, {}).items()}

    def rpush(self, name, *values):
        if name not in self.lists:
            self.lists[name] = []
        self.lists[name].extend(values)
        return len(self.lists[name])

    def lpop(self, name):
        if name in self.lists and self.lists[name]:
            return self.lists[name].pop(0)
        return None

    def lrange(self, name, start, end):
        lst = self.lists.get(name, [])
        if end == -1:
            return lst[start:]
        return lst[start:end+1]


# ==============================================================================
# CONEXÕES E INICIALIZAÇÃO
# ==============================================================================
def inicializar_bancos():
    """Conecta ao MongoDB e Redis reais ou inicializa fallbacks simulados."""
    mongo_client = None
    redis_client = None

    # Tenta conectar ao MongoDB
    if HAS_PYMONGO:
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1500)
            client.admin.command('ping')
            mongo_client = client
            print("  [OK] MongoDB conectado com sucesso via localhost:27017.")
        except Exception:
            print("  [AVISO] MongoDB offline em localhost:27017. Usando MockMongoClient didático.")
            mongo_client = MockMongoClient()
    else:
        print("  [AVISO] Driver pymongo não instalado. Usando MockMongoClient.")
        mongo_client = MockMongoClient()

    # Tenta conectar ao Redis
    if HAS_REDIS:
        try:
            r = redis.Redis(host='localhost', port=6379, db=0, socket_timeout=1.5)
            r.ping()
            redis_client = r
            print("  [OK] Redis conectado com sucesso via localhost:6379.")
        except Exception:
            print("  [AVISO] Redis offline em localhost:6379. Usando MockRedisClient didático.")
            redis_client = MockRedisClient()
    else:
        print("  [AVISO] Driver redis-py não instalado. Usando MockRedisClient.")
        redis_client = MockRedisClient()

    return mongo_client, redis_client


# ==============================================================================
# SEÇÃO 1: CRUD NO MONGODB
# ==============================================================================
def demonstrar_mongodb_crud(mongo_db):
    """Executa o ciclo CRUD completo no MongoDB."""
    print("\n" + "="*70)
    print(" 1. CICLO CRUD NO MONGODB (Banco Orientado a Documentos)")
    print("="*70)

    produtos_col = mongo_db["produtos"]
    produtos_col.drop()

    catalogo = [
        {
            "sku": "NOT-DEL-01",
            "nome": "Notebook Dell Inspiron 15",
            "categoria": "Informatica",
            "preco": 4299.90,
            "estoque": 14,
            "especificacoes": {"processador": "Core i7", "ram_gb": 16, "ssd_gb": 512},
            "tags": ["trabalho", "desenvolvimento", "bivolt"],
            "ativo": True
        },
        {
            "sku": "MOU-LOG-02",
            "nome": "Mouse Sem Fio Logitech MX Master 3S",
            "categoria": "Perifericos",
            "preco": 589.00,
            "estoque": 25,
            "especificacoes": {"dpi": 8000, "conexao": "Bluetooth"},
            "tags": ["ergonomia", "produtividade"],
            "ativo": True
        },
        {
            "sku": "TEC-MEC-03",
            "nome": "Teclado Mecanico Keychron K2",
            "categoria": "Perifericos",
            "preco": 699.50,
            "estoque": 8,
            "especificacoes": {"switch": "Gateron Brown", "layout": "75%"},
            "tags": ["mecanico", "desenvolvimento"],
            "ativo": True
        },
        {
            "sku": "MON-LG-04",
            "nome": "Monitor Ultrawide LG 29",
            "categoria": "Monitores",
            "preco": 1290.00,
            "estoque": 6,
            "especificacoes": {"resolucao": "2560x1080", "painel": "IPS"},
            "tags": ["ultrawide", "produtividade"],
            "ativo": True
        }
    ]

    # Create (Insert Many)
    print("\n[CREATE] Inserindo 4 produtos no MongoDB...")
    produtos_col.insert_many(catalogo)
    print("-> 4 documentos inseridos com sucesso.")

    # Read (Find One)
    print("\n[READ] Consultando produto por SKU (NOT-DEL-01):")
    p = produtos_col.find_one({"sku": "NOT-DEL-01"}, {"_id": 0, "nome": 1, "preco": 1, "especificacoes": 1})
    print(f"-> Resultado: {json.dumps(p, indent=2)}")

    # Update (Update One com $set e $inc)
    print("\n[UPDATE] Atualizando preco para R$ 3999.00 e incrementando estoque em +5...")
    produtos_col.update_one(
        {"sku": "NOT-DEL-01"},
        {"$set": {"preco": 3999.00}, "$inc": {"estoque": 5}}
    )
    p_atualizado = produtos_col.find_one({"sku": "NOT-DEL-01"}, {"_id": 0, "nome": 1, "preco": 1, "estoque": 1})
    print(f"-> Documento atualizado: {p_atualizado}")


# ==============================================================================
# SEÇÃO 2: OPERAÇÕES CHAVE-VALOR NO REDIS
# ==============================================================================
def demonstrar_redis_estruturas(redis_cli):
    """Executa manipulação das principais estruturas de dados do Redis."""
    print("\n" + "="*70)
    print(" 2. ESTRUTURAS DE DADOS NO REDIS (Banco Chave-Valor em Memória)")
    print("="*70)

    # 1. Strings e Expiração (TTL)
    print("\n[STRINGS & TTL] Gravando token de sessão com expiração de 60s:")
    redis_cli.set("session:token:taua_ads", "jwt_user_reginaldo_ifce", ex=60)
    val = redis_cli.get("session:token:taua_ads")
    ttl = redis_cli.ttl("session:token:taua_ads")
    print(f"-> Chave 'session:token:taua_ads' = {val.decode() if isinstance(val, bytes) else val} (TTL restante: {ttl}s)")

    # 2. Contadores Atômicos
    print("\n[CONTADORES] Incrementando visualizações de página:")
    redis_cli.set("views:NOT-DEL-01", 100)
    v1 = redis_cli.incr("views:NOT-DEL-01")
    print(f"-> Novo contador após INCR: {v1}")

    # 3. Hashes (Carrinho de compras)
    print("\n[HASHES] Armazenando carrinho de compras do usuário (SKU -> Qtd):")
    cart_key = "cart:user:42"
    redis_cli.hset(cart_key, "NOT-DEL-01", 1)
    redis_cli.hset(cart_key, "MOU-LOG-02", 2)
    cart_items = redis_cli.hgetall(cart_key)
    print(f"-> Itens no carrinho: {cart_items}")

    # 4. Lists (Fila FIFO de Mensagens)
    print("\n[LISTS] Enfileirando pedidos para processamento em background (RPUSH / LPOP):")
    queue_key = "queue:pedidos_taua"
    redis_cli.delete(queue_key)
    redis_cli.rpush(queue_key, "PED-2026-001", "PED-2026-002", "PED-2026-003")
    fila_inicial = redis_cli.lrange(queue_key, 0, -1)
    print(f"-> Fila criada: {fila_inicial}")
    processado = redis_cli.lpop(queue_key)
    print(f"-> Worker retirou para processar: {processado}")
    fila_restante = redis_cli.lrange(queue_key, 0, -1)
    print(f"-> Fila remanescente: {fila_restante}")


# ==============================================================================
# SEÇÃO 3: PADRÃO CACHE-ASIDE (INTEGRAÇÃO MONGODB + REDIS)
# ==============================================================================
class CacheAsideService:
    """Implementa o padrão Cache-Aside Pattern ligando MongoDB e Redis."""
    def __init__(self, mongo_db, redis_cli, cache_ttl_seconds=60):
        self.mongo_col = mongo_db["produtos"]
        self.redis = redis_cli
        self.ttl = cache_ttl_seconds

    def obter_produto(self, sku: str) -> tuple[Dict[str, Any], str, float]:
        """
        Retorna o produto pelo SKU, o status do cache (HIT ou MISS)
        e a latência da operação em milissegundos.
        """
        inicio = time.perf_counter()
        cache_key = f"cache:produto:{sku}"

        # 1. Tenta buscar no Redis (In-Memory Cache)
        dado_cache = self.redis.get(cache_key)
        if dado_cache:
            latencia_ms = (time.perf_counter() - inicio) * 1000.0
            if isinstance(dado_cache, bytes):
                dado_cache = dado_cache.decode('utf-8')
            return json.loads(dado_cache), "CACHE_HIT", latencia_ms

        # 2. Se não encontrou no Cache -> CACHE MISS: Busca no MongoDB
        produto_db = self.mongo_col.find_one({"sku": sku}, {"_id": 0})
        if not produto_db:
            latencia_ms = (time.perf_counter() - inicio) * 1000.0
            return {}, "NOT_FOUND", latencia_ms

        # 3. Popula o cache no Redis para próximas requisições
        self.redis.set(cache_key, json.dumps(produto_db), ex=self.ttl)
        latencia_ms = (time.perf_counter() - inicio) * 1000.0
        return produto_db, "CACHE_MISS", latencia_ms

    def atualizar_preco(self, sku: str, novo_preco: float):
        """Atualiza no MongoDB e invalida o cache correspondente no Redis."""
        self.mongo_col.update_one({"sku": sku}, {"$set": {"preco": novo_preco}})
        cache_key = f"cache:produto:{sku}"
        self.redis.delete(cache_key)
        print(f"  [INVALIDAÇÃO] Preço atualizado no MongoDB. Chave '{cache_key}' removida do Redis.")


def simular_benchmark_cache_aside(servico: CacheAsideService):
    """Executa teste de carga medindo latência de Cache Miss vs Cache Hit."""
    print("\n" + "="*70)
    print(" 3. BENCHMARKING DO PADRÃO CACHE-ASIDE (Latência MongoDB vs Redis)")
    print("="*70)

    sku_alvo = "NOT-DEL-01"

    # Garante que o cache começa limpo
    servico.redis.delete(f"cache:produto:{sku_alvo}")

    # 1ª Leitura (Gera CACHE MISS)
    doc_miss, status_miss, lat_miss = servico.obter_produto(sku_alvo)
    print(f"\n1ª Leitura: Status = {status_miss} | Latência = {lat_miss:.3f} ms")
    print(f"-> Produto recuperado do MongoDB: {doc_miss.get('nome')} | R$ {doc_miss.get('preco')}")

    # 2ª Leitura (Gera CACHE HIT)
    doc_hit, status_hit, lat_hit = servico.obter_produto(sku_alvo)
    print(f"\n2ª Leitura: Status = {status_hit} | Latência = {lat_hit:.3f} ms")
    print(f"-> Produto recuperado do Redis: {doc_hit.get('nome')} | R$ {doc_hit.get('preco')}")

    aceleracao = lat_miss / lat_hit if lat_hit > 0 else 1.0
    print(f"-> Ganho de Velocidade (Speedup): {aceleracao:.1f}x mais rápido no Cache!")

    # Execução estatística de 100 requisições
    print("\nSimulando 100 requisições consecutivas para análise estatística...")
    latencias_hit = []
    latencias_miss = [lat_miss]

    for _ in range(100):
        _, status, lat = servico.obter_produto(sku_alvo)
        latencias_hit.append(lat)

    # Invalidação de Cache
    print("\nDemonstrando Invalidação de Cache ao atualizar dados:")
    servico.atualizar_preco(sku_alvo, 3750.00)
    # 3ª Leitura pós-invalidação (Gera novo CACHE MISS)
    doc_fresco, status_pos, lat_pos = servico.obter_produto(sku_alvo)
    latencias_miss.append(lat_pos)
    print(f"Leitura pós-invalidação: Status = {status_pos} | Preço Atualizado = R$ {doc_fresco.get('preco')} | Latência = {lat_pos:.3f} ms")

    # Resumo Estatístico
    media_miss = np.mean(latencias_miss)
    media_hit = np.mean(latencias_hit)
    desvio_hit = np.std(latencias_hit)

    print("\n" + "-"*50)
    print(" RESUMO ESTATÍSTICO DE DESEMPENHO")
    print("-"*50)
    print(f"Latência Média CACHE MISS (MongoDB): {media_miss:.3f} ms")
    print(f"Latência Média CACHE HIT  (Redis):   {media_hit:.3f} ms (±{desvio_hit:.3f} ms)")
    print(f"Aceleração Geral Média:              {media_miss / media_hit:.1f}x")

    return latencias_miss, latencias_hit


# ==============================================================================
# SEÇÃO 4: GERAÇÃO DO GRÁFICO DIDÁTICO
# ==============================================================================
def gerar_grafico_latencias(latencias_miss, latencias_hit, arquivo_saida):
    """Gera visualização comparativa de latência seguindo o padrão IFCE."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Gráfico 1: Barras de Média
    categorias = ['Cache Miss\n(Busca MongoDB)', 'Cache Hit\n(Memória Redis)']
    medias = [np.mean(latencias_miss), np.mean(latencias_hit)]
    cores = ['#D97706', '#059669']  # Amber e Emerald

    barras = ax1.bar(categorias, medias, color=cores, width=0.5, edgecolor='black', linewidth=1.2)
    despine(ax1)
    ax1.set_ylabel('Latência Média (milissegundos - ms)')
    ax1.set_title('Comparativo de Latência de Acesso')
    ax1.grid(axis='y', linestyle='--', alpha=0.5)

    for b in barras:
        altura = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2., altura + 0.2,
                 f'{altura:.2f} ms', ha='center', va='bottom', fontweight='bold', fontsize=11)

    speedup = medias[0] / medias[1] if medias[1] > 0 else 1.0
    ax1.text(0.5, max(medias)*0.6, f'Aceleração: {speedup:.1f}x mais rápido\ncom Redis em memória',
             ha='center', va='center', bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="#059669", lw=1.5),
             fontsize=10, fontweight='bold', color='#059669')

    # Gráfico 2: Distribuição Temporal das 100 requisições
    reqs = list(range(1, len(latencias_hit) + 1))
    ax2.plot(reqs, latencias_hit, color='#059669', marker='o', markersize=4, linestyle='-', alpha=0.8, label='Cache Hit (Redis)')
    ax2.axhline(medias[0], color='#D97706', linestyle='--', linewidth=2, label=f'Média Cache Miss ({medias[0]:.2f} ms)')
    despine(ax2)
    ax2.set_xlabel('Número da Requisição')
    ax2.set_ylabel('Latência (ms)')
    ax2.set_title('Estabilidade de Resposta ao Longo de 100 Requisições')
    ax2.legend(loc='upper right')
    ax2.grid(True, linestyle='--', alpha=0.4)

    plt.suptitle('IFCE Campus Tauá • ADS16 - Banco de Dados Não-Relacionais (Aula 03)', fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(arquivo_saida, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\n[GRÁFICO] Figura didática salva com sucesso em: {arquivo_saida}")


# ==============================================================================
# EXECUÇÃO PRINCIPAL
# ==============================================================================
if __name__ == "__main__":
    print("="*70)
    print(" INICIANDO LABORATÓRIO DA AULA 03: MONGODB + REDIS + CACHE-ASIDE")
    print(" IFCE Campus Tauá - Prof. Me. Reginaldo Pereira Fernandes")
    print("="*70)

    mongo_client, redis_client = inicializar_bancos()
    mongo_db = mongo_client["ecommerce_taua"]

    # 1. Demonstração MongoDB CRUD
    demonstrar_mongodb_crud(mongo_db)

    # 2. Demonstração Redis Estruturas
    demonstrar_redis_estruturas(redis_client)

    # 3. Padrão Cache-Aside & Benchmarking
    servico_cache = CacheAsideService(mongo_db, redis_client, cache_ttl_seconds=120)
    lats_miss, lats_hit = simular_benchmark_cache_aside(servico_cache)

    # 4. Geração de Gráfico Didático
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_grafico = os.path.join(dir_atual, "grafico_latencia_cache.png")
    gerar_grafico_latencias(lats_miss, lats_hit, caminho_grafico)

    print("\n" + "="*70)
    print(" LABORATÓRIO CONCLUÍDO COM 100% DE SUCESSO!")
    print("="*70)
