#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CRUD Avançado: Filtros Complexos e Atualizações Atômicas no MongoDB
Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 07
IFCE Campus Tauá - Prof. Me. Reginaldo Fernandes
"""

import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def conectar():
    try:
        client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=2000)
        client.admin.command("ping")
        return client["ecommerce_shopgrids"]
    except ConnectionFailure:
        print("❌ Erro de conexão com o MongoDB. Suba o serviço com 'docker compose up -d'.")
        sys.exit(1)

def demonstrar_elem_match(db):
    print("=" * 70)
    print("1. DEMONSTRAÇÃO DO OPERADOR $elemMatch (Evitando Falsos Positivos)")
    print("=" * 70)

    # Inserir um documento didático específico para teste de falso positivo
    doc_teste = {
        "codigo": "PED-TESTE-FALSO-POSITIVO",
        "cliente_id": 9999,
        "status": "PENDENTE",
        "itens": [
            {"sku": "ITEM-CARO-UNICO", "preco": 300.0, "qtd": 1, "status_entrega": "PENDENTE"},
            {"sku": "ITEM-BARATO-LOTE", "preco": 15.0, "qtd": 8, "status_entrega": "PENDENTE"}
        ],
        "pagamento": {"subtotal": 420.0, "total_pago": 420.0},
        "data_criacao": datetime.now()
    }
    db.pedidos.delete_one({"codigo": "PED-TESTE-FALSO-POSITIVO"})
    db.pedidos.insert_one(doc_teste)

    # Consulta 1: Abordagem Ingênua (Falso Positivo)
    filtro_ingenuo = {
        "codigo": "PED-TESTE-FALSO-POSITIVO",
        "itens.preco": {"$gt": 100},
        "itens.qtd": {"$gte": 5}
    }
    retorno_ingenuo = db.pedidos.find_one(filtro_ingenuo)
    print("\n🔍 A) Consulta Ingênua (Sem $elemMatch):")
    print(f"Filtro: {filtro_ingenuo}")
    print(f"Retornou documento? {' SIM (Falso Positivo!)' if retorno_ingenuo else ' NÃO'}")
    print("-> Explicação: O item 1 satisfez o preco > 100 e o item 2 satisfez a qtd >= 5.")

    # Consulta 2: Abordagem Correta com $elemMatch
    filtro_correto = {
        "codigo": "PED-TESTE-FALSO-POSITIVO",
        "itens": {
            "$elemMatch": {
                "preco": {"$gt": 100},
                "qtd": {"$gte": 5}
            }
        }
    }
    retorno_correto = db.pedidos.find_one(filtro_correto)
    print("\n🔍 B) Consulta Rigorosa (Com $elemMatch):")
    print(f"Filtro: {filtro_correto}")
    print(f"Retornou documento? {' SIM' if retorno_correto else ' NÃO (Correto! Nenhum item atende a ambos os critérios)'}")

def demonstrar_expr(db):
    print("\n" + "=" * 70)
    print("2. DEMONSTRAÇÃO DO OPERADOR $expr (Comparação Entre Campos Internos)")
    print("=" * 70)

    # Busca produtos em que o estoque atual é inferior ao estoque mínimo
    query_estoque_baixo = {
        "$expr": {
            "$lt": ["$estoque.atual", "$estoque.minimo"]
        }
    }
    total_repor = db.produtos.count_documents(query_estoque_baixo)
    print(f"📦 Produtos com estoque crítico ($estoque.atual < $estoque.minimo): {total_repor:,}")
    
    exemplo = db.produtos.find_one(query_estoque_baixo, {"titulo": 1, "estoque": 1, "_id": 0})
    if exemplo:
        print(f"   Exemplo: {exemplo['titulo']}")
        print(f"   Estoque Atual: {exemplo['estoque']['atual']} | Estoque Mínimo: {exemplo['estoque']['minimo']}")

def demonstrar_arrays_all_size(db):
    print("\n" + "=" * 70)
    print("3. OPERADORES DE LISTA: $all E $size")
    print("=" * 70)

    # Produtos que possuem ambas as tags 'gamer' e 'sem fio'
    query_all = {"tags": {"$all": ["gamer", "sem fio"]}}
    total_all = db.produtos.count_documents(query_all)
    print(f"🎮 Produtos com tags 'gamer' E 'sem fio' simultaneamente ($all): {total_all:,}")

    # Pedidos com exatamente 1 item
    query_size = {"itens": {"$size": 1}}
    total_size = db.pedidos.count_documents(query_size)
    print(f"📋 Pedidos com exatamente 1 item ($size: 1): {total_size:,}")

def demonstrar_atualizacoes_atomicas(db):
    print("\n" + "=" * 70)
    print("4. ATUALIZAÇÕES ATÔMICAS: $inc, $min, $max E $push com $slice")
    print("=" * 70)

    # Localizar um produto para atualizar
    prod = db.produtos.find_one({"status": "ATIVO"})
    if not prod:
        print("Nenhum produto encontrado.")
        return
    sku = prod["sku"]
    estoque_antes = prod["estoque"]["atual"]

    # 1. $inc: Decrementar estoque em 3 unidades de forma atômica
    db.produtos.update_one(
        {"sku": sku},
        {"$inc": {"estoque.atual": -3}}
    )
    prod_depois = db.produtos.find_one({"sku": sku})
    print(f"📉 $inc atômico no SKU {sku}:")
    print(f"   Estoque Anterior: {estoque_antes} -> Estoque Novo: {prod_depois['estoque']['atual']}")

    # 2. $push com $slice: Adicionar avaliação mantendo no máximo 5 no array
    nova_avaliacao = {
        "nota": 5,
        "autor": "Prof. Reginaldo",
        "comentario": "Excelente acabamento e resposta rápida!",
        "data": datetime.now()
    }
    db.produtos.update_one(
        {"sku": sku},
        {
            "$push": {
                "ultimas_avaliacoes": {
                    "$each": [nova_avaliacao],
                    "$slice": -5 # Mantém apenas as 5 últimas avaliações!
                }
            }
        }
    )
    prod_avaliado = db.produtos.find_one({"sku": sku})
    print(f"⭐ $push com $slice (-5) aplicado no SKU {sku}:")
    print(f"   Total de avaliações mantidas: {len(prod_avaliado.get('ultimas_avaliacoes', []))}")

def demonstrar_array_filters(db):
    print("\n" + "=" * 70)
    print("5. MODIFICAÇÃO SELETIVA EM ARRAYS COM arrayFilters E $[<identificador>]")
    print("=" * 70)

    # Inserir pedido modelo
    codigo_pedido = "PED-DEMO-FILTERS-2026"
    db.pedidos.delete_one({"codigo": codigo_pedido})
    db.pedidos.insert_one({
        "codigo": codigo_pedido,
        "status": "PROCESSANDO",
        "itens": [
            {"sku": "PROD-TECLADO", "status_entrega": "PENDENTE", "qtd": 1},
            {"sku": "PROD-MOUSE", "status_entrega": "PENDENTE", "qtd": 2},
            {"sku": "PROD-PAD", "status_entrega": "PENDENTE", "qtd": 1}
        ]
    })

    print(f"Pedido criado: {codigo_pedido} com 3 itens PENDENTES.")

    # Atualizar exclusivamente o item 'PROD-MOUSE' para 'SEPARADO_EM_ESTOQUE'
    resultado = db.pedidos.update_one(
        {"codigo": codigo_pedido},
        {
            "$set": {
                "itens.$[alvo].status_entrega": "SEPARADO_EM_ESTOQUE",
                "itens.$[alvo].data_separacao": datetime.now().isoformat()
            }
        },
        array_filters=[{"alvo.sku": "PROD-MOUSE"}]
    )

    pedido_atualizado = db.pedidos.find_one({"codigo": codigo_pedido})
    print(f"Modificados: {resultado.modified_count} documento(s).")
    print("Status atualizado dos itens:")
    for item in pedido_atualizado["itens"]:
        print(f"  - SKU: {item['sku']:<15} | Status: {item['status_entrega']}")

def main():
    db = conectar()
    print("🚀 Executando Demonstrações de CRUD Avançado e Atualizações Atômicas...")
    demonstrar_elem_match(db)
    demonstrar_expr(db)
    demonstrar_arrays_all_size(db)
    demonstrar_atualizacoes_atomicas(db)
    demonstrar_array_filters(db)
    print("\n✅ Todas as demonstrações de CRUD Avançado foram concluídas com sucesso!\n")

if __name__ == "__main__":
    main()
