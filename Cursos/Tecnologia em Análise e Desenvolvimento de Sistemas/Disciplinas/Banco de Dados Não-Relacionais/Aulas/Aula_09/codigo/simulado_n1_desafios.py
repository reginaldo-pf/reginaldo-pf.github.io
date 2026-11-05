#!/usr/bin/env python3
"""
Simulado Prático Preparatório para a AVP1 (Laboratório Integrado N1)
Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
Professor: Prof. Me. Reginaldo Fernandes

Instruções para o Estudante:
1. Complete a implementação das 5 funções abaixo conforme a especificação de cada desafio.
2. Execute este script para rodar a suíte de testes automatizados de validação:
   $ python3 simulado_n1_desafios.py
3. Para consultar o gabarito comentado, abra o arquivo 'solucao_simulado_n1.py'.
"""

import json
import redis
from pymongo import MongoClient

def get_conexoes():
    """Retorna conexões ativas com o Redis e MongoDB locais."""
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    m = MongoClient("mongodb://localhost:27017")
    db = m["ecommerce_shopgrids"]
    return r, db

# ==============================================================================
# DESAFIO 1: Padrão Cache-Aside (Lazy Loading) com TTL no Redis
# ==============================================================================
def buscar_produto_com_cache(r: redis.Redis, db, sku: str, ttl_segundos: int = 60) -> dict:
    """
    Especificação:
    1. Verifica se a chave 'produto:{sku}' existe no Redis.
    2. Se existir (Cache Hit): desserializa a string JSON e retorna o dicionário.
    3. Se não existir (Cache Miss): busca o documento na coleção 'produtos' do MongoDB.
    4. Se o produto existir no MongoDB, serializa em JSON, grava no Redis com TTL
       de expiração e retorna o dicionário.
    5. Se não existir em nenhum dos dois, retorna None.
    """
    # TODO: Implemente a lógica do Cache-Aside abaixo
    chave_cache = f"produto:{sku}"
    dados_cache = r.get(chave_cache)
    if dados_cache:
        produto = json.loads(dados_cache)
        produto["_fonte"] = "REDIS_CACHE_HIT"
        return produto

    doc = db.produtos.find_one({"sku": sku})
    if doc:
        doc_serializavel = dict(doc)
        doc_serializavel["_id"] = str(doc_serializavel["_id"])
        r.setex(chave_cache, ttl_segundos, json.dumps(doc_serializavel))
        doc_serializavel["_fonte"] = "MONGODB_CACHE_MISS"
        return doc_serializavel

    return None

# ==============================================================================
# DESAFIO 2: Invalidação Imediata de Cache na Atualização de Estoque
# ==============================================================================
def atualizar_estoque_com_invalidacao(r: redis.Redis, db, sku: str, delta_quantidade: int) -> bool:
    """
    Especificação:
    1. Executa atualização atômica no MongoDB usando o operador $inc no campo 'estoque'.
    2. Imediatamente remove a chave 'produto:{sku}' do Redis para evitar Stale Reads.
    3. Retorna True se o documento foi modificado com sucesso, ou False caso o SKU não exista.
    """
    resultado = db.produtos.update_one(
        {"sku": sku},
        {"$inc": {"estoque": delta_quantidade}}
    )
    if resultado.modified_count > 0:
        r.delete(f"produto:{sku}")
        return True
    return False

# ==============================================================================
# DESAFIO 3: Carrinho de Compras em Hashes do Redis
# ==============================================================================
def adicionar_ao_carrinho(r: redis.Redis, cliente_id: str, sku: str, quantidade: int) -> int:
    """
    Especificação:
    1. Utiliza uma Hash do Redis com chave 'carrinho:{cliente_id}'.
    2. Incrementa atomicamente a quantidade do item usando HINCRBY.
    3. Define uma expiração de 1200 segundos (20 min) no carrinho caso seja nova chave.
    4. Retorna a quantidade total atual do item no carrinho.
    """
    chave = f"carrinho:{cliente_id}"
    nova_qtd = r.hincrby(chave, sku, quantidade)
    r.expire(chave, 1200)
    return nova_qtd

def obter_carrinho(r: redis.Redis, cliente_id: str) -> dict:
    """Retorna um dicionário com todos os itens e quantidades da Hash 'carrinho:{cliente_id}'."""
    return r.hgetall(f"carrinho:{cliente_id}")

# ==============================================================================
# DESAFIO 4: Consulta Otimizada no MongoDB (Regra ESR)
# ==============================================================================
def criar_indice_pedidos_esr(db):
    """
    Especificação:
    Cria um índice composto na coleção 'pedidos' para otimizar consultas que filtram
    por igualdade de status, ordenam por data_pedido descendente e filtram por faixa de valor_total.
    Regra ESR: Equality ('status'), Sort ('data_pedido'), Range ('valor_total').
    """
    return db.pedidos.create_index([
        ("status", 1),
        ("data_pedido", -1),
        ("valor_total", 1)
    ], name="idx_pedidos_esr_status_data_valor")

# ==============================================================================
# DESAFIO 5: Pipeline de Agregação de Vendas
# ==============================================================================
def relatorio_vendas_por_categoria(db) -> list:
    """
    Especificação:
    Construa um pipeline de agregação que:
    1. Filtre apenas pedidos com status 'entregue' ($match precoce).
    2. Desconstrua o array de itens ($unwind).
    3. Agrupe pela categoria do item ($group), calculando faturamento total e peças vendidas.
    4. Ordene pelo maior faturamento descendente ($sort).
    5. Retorne a lista de categorias agregadas.
    """
    pipeline = [
        {"$match": {"status": "entregue"}},
        {"$unwind": "$itens"},
        {
            "$group": {
                "_id": "$itens.categoria",
                "faturamento_total": {"$sum": "$itens.subtotal"},
                "total_unidades": {"$sum": "$itens.quantidade"}
            }
        },
        {"$sort": {"faturamento_total": -1}}
    ]
    return list(db.pedidos.aggregate(pipeline))

# ==============================================================================
# SUÍTE DE TESTES AUTOMATIZADOS (Validação em Laboratório)
# ==============================================================================
def executar_testes():
    print("="*70)
    print("INICIANDO VALIDAÇÃO DO SIMULADO N1 (Redis + MongoDB)")
    print("="*70)

    try:
        r, db = get_conexoes()
        r.ping()
        db.command("ping")
        print("✓ Conexões locais com Redis e MongoDB confirmadas com sucesso!\n")
    except Exception as e:
        print(f"❌ Falha de infraestrutura: Verifique se os containers estão ativos ({e}).")
        print("Execute: docker compose up -d")
        return

    # Teste 1: Cache-Aside
    print("[Teste 1] Testando Padrão Cache-Aside...")
    sku_teste = "SKU-ELE-001"
    # Garante que um produto existe
    db.produtos.update_one(
        {"sku": sku_teste},
        {"$setOnInsert": {"sku": sku_teste, "nome": "Notebook Ultra 15", "categoria": "Eletrônicos", "preco": 3800.0, "estoque": 20}},
        upsert=True
    )
    r.delete(f"produto:{sku_teste}")

    p1 = buscar_produto_com_cache(r, db, sku_teste)
    assert p1 is not None and p1["_fonte"] == "MONGODB_CACHE_MISS", "Deveria ter ocorrido Cache Miss na primeira busca!"
    p2 = buscar_produto_com_cache(r, db, sku_teste)
    assert p2 is not None and p2["_fonte"] == "REDIS_CACHE_HIT", "Deveria ter ocorrido Cache Hit na segunda busca!"
    print("✓ Teste 1 passou: Cache-Aside operando corretamente com Hit e Miss.\n")

    # Teste 2: Invalidação de Cache
    print("[Teste 2] Testando Invalidação de Cache...")
    atualizar_estoque_com_invalidacao(r, db, sku_teste, delta_quantidade=-2)
    assert r.get(f"produto:{sku_teste}") is None, "A chave deveria ter sido removida do Redis após atualização!"
    print("✓ Teste 2 passou: Invalidação imediata protege contra leituras de dados obsoletos.\n")

    # Teste 3: Carrinho em Hash Redis
    print("[Teste 3] Testando Carrinho de Compras em Hash...")
    cliente_id = "cli_999"
    r.delete(f"carrinho:{cliente_id}")
    qtd1 = adicionar_ao_carrinho(r, cliente_id, "SKU-PER-005", 2)
    qtd2 = adicionar_ao_carrinho(r, cliente_id, "SKU-PER-005", 1)
    assert qtd2 == 3, f"A quantidade esperada era 3, mas obteve {qtd2}"
    carrinho = obter_carrinho(r, cliente_id)
    assert "SKU-PER-005" in carrinho and int(carrinho["SKU-PER-005"]) == 3
    print("✓ Teste 3 passou: Hashes do Redis gerenciam estados transientes com atomicidade.\n")

    # Teste 4: Regra ESR
    print("[Teste 4] Testando Índice ESR no MongoDB...")
    nome_indice = criar_indice_pedidos_esr(db)
    indices_existentes = db.pedidos.index_information()
    assert nome_indice in indices_existentes, f"Índice {nome_indice} não encontrado na coleção!"
    print("✓ Teste 4 passou: Índice composto ESR criado com sucesso.\n")

    # Teste 5: Agregação
    print("[Teste 5] Testando Pipeline Analítico de Vendas...")
    relatorio = relatorio_vendas_por_categoria(db)
    assert isinstance(relatorio, list), "O relatório deve retornar uma lista."
    if len(relatorio) > 0:
        assert "faturamento_total" in relatorio[0], "Campo faturamento_total ausente no resultado da agregação."
        print(f"  • Top Categoria Identificada: {relatorio[0]['_id']} (Faturamento: R$ {relatorio[0]['faturamento_total']:,.2f})")
    print("✓ Teste 5 passou: Pipeline de agregação estruturado e funcional.\n")

    print("="*70)
    print("🎉 PARABÉNS! Todos os testes do Simulado N1 foram concluídos com êxito!")
    print("="*70)

if __name__ == "__main__":
    executar_testes()
