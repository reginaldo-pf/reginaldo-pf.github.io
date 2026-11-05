#!/usr/bin/env python3
"""
Gabarito Comentado do Simulado N1 (Redis + MongoDB)
Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
Professor: Prof. Me. Reginaldo Fernandes

Este arquivo serve como material de apoio ao docente e gabarito de referência
para os discentes após a realização do laboratório preparatório para a AVP1.
"""

import json
import redis
from pymongo import MongoClient

# Conexões
r = redis.Redis(host="localhost", port=6379, decode_responses=True)
client = MongoClient("mongodb://localhost:27017")
db = client["ecommerce_shopgrids"]

def solucao_desafio_1_cache_aside(sku: str, ttl: int = 60) -> dict:
    """
    Padrão Cache-Aside (Lazy Loading):
    - O cliente consulta a memória RAM do Redis primeiro (latência < 0.1 ms).
    - Somente em caso de falha (Cache Miss), lê o MongoDB (disco / WiredTiger).
    - Escreve no cache com TTL expirável para garantir liberação de RAM (evitando vazamentos).
    """
    chave = f"produto:{sku}"
    cached = r.get(chave)
    if cached:
        return json.loads(cached)

    doc = db.produtos.find_one({"sku": sku})
    if not doc:
        return None

    # Serializa BSON para JSON
    doc["_id"] = str(doc["_id"])
    r.setex(chave, ttl, json.dumps(doc))
    return doc

def solucao_desafio_2_invalidacao_estoque(sku: str, delta: int) -> bool:
    """
    Invalidação de Cache no Write-Path:
    - O MongoDB é atualizado atomicamente com $inc (prevenindo race conditions).
    - A chave do Redis é sumariamente deletada para que a próxima leitura busque
      o dado fresco no banco de documentos, eliminando 'stale reads' (leituras desatualizadas).
    """
    res = db.produtos.update_one(
        {"sku": sku},
        {"$inc": {"estoque": delta}}
    )
    if res.modified_count > 0:
        r.delete(f"produto:{sku}")
        return True
    return False

def solucao_desafio_3_carrinho_hashes(cliente_id: str, sku: str, qtd: int):
    """
    Gerenciamento de Estado Transiente com Hashes:
    - Hashes agrupam múltiplos campos sob a mesma chave na memória.
    - HINCRBY opera com complexidade O(1) e atomicidade no servidor Redis.
    - EXPIRE renova o tempo de vida do carrinho de compras ativo.
    """
    chave = f"carrinho:{cliente_id}"
    total_item = r.hincrby(chave, sku, qtd)
    r.expire(chave, 1200) # 20 minutos de inatividade
    return total_item, r.hgetall(chave)

def solucao_desafio_4_indice_esr():
    """
    Regra de Ouro ESR (Equality, Sort, Range):
    - Equality: { status: 1 } -> filtra exato
    - Sort: { data_pedido: -1 } -> permite ordenação pelo índice sem usar buffer de RAM (SORT)
    - Range: { valor_total: 1 } -> percorre a faixa contígua das folhas da árvore B-Tree
    """
    return db.pedidos.create_index([
        ("status", 1),
        ("data_pedido", -1),
        ("valor_total", 1)
    ], name="idx_pedidos_esr")

def solucao_desafio_5_pipeline_analitico():
    """
    Pipeline de Agregação de Vendas com Otimização de Memória:
    1. $match no início: descarta pedidos cancelados/processando usando índice B-Tree.
    2. $unwind: expande o array de itens para documentos individuais.
    3. $group: acumula somatórios por categoria.
    4. $sort: ordena pelo faturamento final.
    """
    pipeline = [
        {"$match": {"status": "entregue"}},
        {"$unwind": "$itens"},
        {
            "$group": {
                "_id": "$itens.categoria",
                "faturamento": {"$sum": "$itens.subtotal"},
                "itens_vendidos": {"$sum": "$itens.quantidade"}
            }
        },
        {"$sort": {"faturamento": -1}}
    ]
    return list(db.pedidos.aggregate(pipeline))

if __name__ == "__main__":
    print("Gabarito das soluções integradas pronto para consulta docente e discente.")
