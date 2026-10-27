#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina: Banco de Dados Não-Relacionais (ADS16) — Aula 06
Docente: Prof. Me. Reginaldo Fernandes

Script: comparativo_embedding_vs_referencing.py
Objetivo:
  Comprovar empiricamente duas decisões críticas de modelagem no MongoDB:
  1. PERFORMANCE DE LEITURA (Single-Query Read vs. Multi-Query Join Manual):
     Compara o tempo para carregar 200 páginas de detalhes de produtos quando
     usamos Referencing excessivo (3 coleções separadas, imitando tabelas SQL)
     versus Embedding + Subset Pattern (1 único documento autocontido).
  2. INTEGRIDADE FISCAL (Snapshot Pattern vs. Referencing Puro de Preço):
     Demonstra como um pedido modelado apenas com referência ao ID do produto
     sofre adulteração retroativa de valor fiscal quando o preço do produto
     sobe no catálogo, e como o Snapshot Pattern protege a nota fiscal.
"""

import time
from decimal import Decimal
from bson import ObjectId
from bson.decimal128 import Decimal128
from pymongo import MongoClient


def executar_benchmark_leitura(db, total_leituras=200):
    """Compara o tempo de leitura de 200 exibições de página de produto."""
    print("=" * 74)
    print(" EXPERIMENTO 1: EMBEDDING (1 QUERY) vs. REFERENCING PURO (3 QUERIES)")
    print("=" * 74)

    # Limpa coleções de teste do benchmark
    db.bench_prod_ref.drop()
    db.bench_espec_ref.drop()
    db.bench_aval_ref.drop()
    db.bench_prod_emb.drop()

    prod_id = ObjectId()

    # 1. Configura o modelo Fragmentado (Anti-padrão: imitando 3 tabelas SQL no MongoDB)
    db.bench_prod_ref.insert_one(
        {"_id": prod_id, "sku": "NOTE-ACER-15", "nome": "Notebook Nitro V15", "preco": 4599.90}
    )
    db.bench_espec_ref.insert_one(
        {"produto_id": prod_id, "cpu": "Core i7", "ram_gb": 16, "ssd_gb": 512}
    )
    db.bench_aval_ref.insert_many(
        [
            {"produto_id": prod_id, "autor": "Lucas", "nota": 5, "texto": "Excelente!"},
            {"produto_id": prod_id, "autor": "Marina", "nota": 5, "texto": "Muito rápido!"},
        ]
    )

    # 2. Configura o modelo Orientado a Agregados (Embedding 1:1 + Subset Pattern)
    db.bench_prod_emb.insert_one(
        {
            "_id": prod_id,
            "sku": "NOTE-ACER-15",
            "nome": "Notebook Nitro V15",
            "preco": 4599.90,
            "especificacoes": {"cpu": "Core i7", "ram_gb": 16, "ssd_gb": 512},
            "ultimas_avaliacoes": [
                {"autor": "Lucas", "nota": 5, "texto": "Excelente!"},
                {"autor": "Marina", "nota": 5, "texto": "Muito rápido!"},
            ],
        }
    )

    # Medição A: Modelo Fragmentado (Referencing excessivo -> 3 queries por visita)
    t0 = time.perf_counter()
    for _ in range(total_leituras):
        p = db.bench_prod_ref.find_one({"_id": prod_id})
        e = db.bench_espec_ref.find_one({"produto_id": prod_id})
        a = list(db.bench_aval_ref.find({"produto_id": prod_id}).limit(2))
        _pagina = {**p, "especificacoes": e, "ultimas_avaliacoes": a}
    tempo_ref_ms = (time.perf_counter() - t0) * 1000

    # Medição B: Modelo Incorporado (Embedding + Subset -> 1 única query por visita)
    t0 = time.perf_counter()
    for _ in range(total_leituras):
        _pagina = db.bench_prod_emb.find_one({"_id": prod_id})
    tempo_emb_ms = (time.perf_counter() - t0) * 1000

    ganho = tempo_ref_ms / max(tempo_emb_ms, 0.001)

    print(f"Total de páginas renderizadas : {total_leituras} visitas")
    print(f"  [A] Referencing Puro (600 queries em 3 coleções): {tempo_ref_ms:.2f} ms")
    print(f"  [B] Embedding + Subset (200 queries em 1 doc)   : {tempo_emb_ms:.2f} ms")
    print(f"  --> GANHO DE VELOCIDADE (Speedup): {ganho:.2f}x mais rápido com Embedding!")


def demonstrar_integridade_snapshot(db):
    """Mostra o bug fiscal do Referencing puro em pedidos vs. Snapshot Pattern."""
    print("\n" + "=" * 74)
    print(" EXPERIMENTO 2: INTEGRIDADE FISCAL EM PEDIDOS (SNAPSHOT vs. REFERENCING)")
    print("=" * 74)

    db.teste_produtos.drop()
    db.teste_pedidos_errado.drop()
    db.teste_pedidos_correto.drop()

    id_prod = ObjectId()
    db.teste_produtos.insert_one(
        {
            "_id": id_prod,
            "sku": "NOTE-ACER-15",
            "nome": "Notebook Gamer Acer Nitro V15",
            "preco": Decimal128("4599.90"),
        }
    )

    # Pedido ERRADO (Referencing puro: guarda apenas produto_id e quantidade)
    db.teste_pedidos_errado.insert_one(
        {
            "codigo": "PED-ERRADO-01",
            "itens": [{"produto_id": id_prod, "quantidade": 1}],
        }
    )

    # Pedido CORRETO (Extended Reference + Snapshot: congela o preço na compra)
    prod_atual = db.teste_produtos.find_one({"_id": id_prod})
    db.teste_pedidos_correto.insert_one(
        {
            "codigo": "PED-CORRETO-01",
            "itens": [
                {
                    "produto_id": id_prod,
                    "sku": prod_atual["sku"],
                    "nome": prod_atual["nome"],
                    "preco_congelado": prod_atual["preco"],
                    "quantidade": 1,
                }
            ],
        }
    )

    print("1. Cliente finalizou a compra hoje pagando R$ 4.599,90 no PIX.")
    print("2. Passou 1 semana e o preço do Notebook no catálogo subiu para R$ 5.299,90!")

    # Atualiza o preço no catálogo
    db.teste_produtos.update_one(
        {"_id": id_prod}, {"$set": {"preco": Decimal128("5299.90")}}
    )

    # Consultando os dois pedidos após o reajuste de preço:
    ped_errado = db.teste_pedidos_errado.find_one({"codigo": "PED-ERRADO-01"})
    prod_buscado = db.teste_produtos.find_one({"_id": ped_errado["itens"][0]["produto_id"]})
    valor_calculado_errado = prod_buscado["preco"]

    ped_correto = db.teste_pedidos_correto.find_one({"codigo": "PED-CORRETO-01"})
    valor_congelado_correto = ped_correto["itens"][0]["preco_congelado"]

    print("\n[Auditoria Fiscal 1 Semana Depois]:")
    print(f"  - Pedido SEM Snapshot (Referencing Puro) : R$ {valor_calculado_errado}  <-- CORRUPÇÃO FISCAL! Mudou o passado!")
    print(f"  - Pedido COM Snapshot (Híbrido Correto)  : R$ {valor_congelado_correto}  <-- ÍNTEGRO! Preserva o valor pago!")
    print("=" * 74)


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    db_shopgrids = client["ecommerce_shopgrids"]
    executar_benchmark_leitura(db_shopgrids)
    demonstrar_integridade_snapshot(db_shopgrids)
