#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina: Banco de Dados Não-Relacionais (ADS16) — Aula 06
Docente: Prof. Me. Reginaldo Fernandes

Script: popular_catalogo_mongodb.py
Objetivo:
  1. Demonstrar na prática a diferença física entre JSON textual e BSON binário
     (usando o módulo nativo `bson` do PyMongo: ObjectId, Decimal128 e BSON.encode).
  2. Demonstrar o erro de ponto flutuante IEEE 754 (float) vs. precisão financeira
     exata com Decimal128.
  3. Criar e popular o banco 'ecommerce_shopgrids' no MongoDB aplicando:
     - Polimorfismo de Schema + Validação com $jsonSchema
     - Embedding 1:1 (Especificações Técnicas do Produto)
     - Embedding 1:Few (Endereços do Cliente)
     - Subset Pattern + Referencing 1:Many (Avaliações de Produtos)
     - Extended Reference + Snapshot Pattern (Pedidos Fiscais Imutáveis)
"""

import json
from datetime import datetime, timezone
from decimal import Decimal
import bson
from bson import BSON, ObjectId
from bson.decimal128 import Decimal128
from pymongo import MongoClient
from pymongo.errors import WriteError


def demonstrar_json_vs_bson():
    """Etapa 1: Compara JSON puro com BSON binário, ObjectId e Decimal128."""
    print("=" * 74)
    print(" ETAPA 1: RAIO-X DO BSON, OBJECTID (12 BYTES) E DECIMAL128 FINANCEIRO")
    print("=" * 74)

    # 1.1 O perigo do float binário (IEEE 754) em JSON puro para valores monetários
    soma_float = 0.1 + 0.2
    soma_decimal = Decimal("0.1") + Decimal("0.2")
    print(f"[Float IEEE 754] 0.1 + 0.2 = {soma_float:.17f}  <-- ERRO DE ARREDONDAMENTO!")
    print(f"[BSON Decimal128] 0.1 + 0.2 = {Decimal128(soma_decimal)}                <-- EXATO!")

    # 1.2 Inspecionando a anatomia dos 12 bytes de um ObjectId gerado localmente
    oid = ObjectId()
    raw_bytes = oid.binary
    ts_hex = raw_bytes[0:4].hex()
    random_hex = raw_bytes[4:9].hex()
    counter_hex = raw_bytes[9:12].hex()

    print("\n[Anatomia do ObjectId de 12 Bytes (24 hex chars)]:")
    print(f"  ObjectId Completo : {oid}")
    print(f"  - 4 Bytes Timestamp Unix : {ts_hex} -> {oid.generation_time.isoformat()}")
    print(f"  - 5 Bytes Random/Processo: {random_hex}")
    print(f"  - 3 Bytes Contador Atômico: {counter_hex}")

    # 1.3 Serializando um documento para JSON textual vs. BSON binário
    doc_python = {
        "_id": oid,
        "sku": "NOTE-ACER-15",
        "nome": "Notebook Gamer Acer Nitro V15",
        "preco": Decimal128("4599.90"),
        "estoque": 15,
        "criado_em": datetime.now(timezone.utc),
    }

    bytes_bson = BSON.encode(doc_python)
    texto_json = json.dumps(
        {
            "_id": str(oid),
            "sku": "NOTE-ACER-15",
            "nome": "Notebook Gamer Acer Nitro V15",
            "preco": 4599.90,
            "estoque": 15,
            "criado_em": doc_python["criado_em"].isoformat(),
        }
    ).encode("utf-8")

    print("\n[Comparativo de Serialização em Memória/Disco]:")
    print(f"  - Tamanho JSON Textual (UTF-8): {len(texto_json)} bytes (sem tipos ricos)")
    print(f"  - Tamanho BSON Binário Nativo : {len(bytes_bson)} bytes (com cabeçalho de salto O(1), ObjectId, Decimal128 e UTC Date)")


def popular_ecommerce_shopgrids():
    """Etapa 2: Conecta ao MongoDB e modela as coleções do ShopGrids."""
    print("\n" + "=" * 74)
    print(" ETAPA 2: MODELAGEM DE DADOS NO MONGODB (SHOPGRIDS E-COMMERCE)")
    print("=" * 74)

    # Conecta ao servidor MongoDB local na porta padrão 27017
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    db = client["ecommerce_shopgrids"]

    # Limpa a base para garantir execução determinística em laboratório
    client.drop_database("ecommerce_shopgrids")

    # -------------------------------------------------------------------------
    # 2.1 Criando a coleção 'produtos' com validação de governança ($jsonSchema)
    # -------------------------------------------------------------------------
    db.create_collection(
        "produtos",
        validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["sku", "nome", "categoria", "preco", "estoque"],
                "properties": {
                    "sku": {"bsonType": "string"},
                    "nome": {"bsonType": "string"},
                    "categoria": {"bsonType": "string"},
                    "preco": {"bsonType": ["decimal", "double"], "minimum": 0.01},
                    "estoque": {"bsonType": "int", "minimum": 0},
                    "especificacoes": {"bsonType": "object"},
                },
            }
        },
    )
    print("[OK] Coleção 'produtos' criada com validação nativa $jsonSchema.")

    # Testando a rejeição de um documento inválido pelo $jsonSchema
    try:
        db.produtos.insert_one({"sku": "INVALIDO-01", "nome": "Produto sem preço"})
    except WriteError as err:
        print(f"[OK] Validador $jsonSchema bloqueou inserção inválida (código {err.code}).")

    # -------------------------------------------------------------------------
    # 2.2 Inserindo Produtos Polimórficos (Embedding 1:1 + Subset Pattern)
    # -------------------------------------------------------------------------
    id_notebook = ObjectId()
    id_camiseta = ObjectId()
    id_livro = ObjectId()

    produtos = [
        {
            "_id": id_notebook,
            "sku": "NOTE-ACER-15",
            "nome": "Notebook Gamer Acer Nitro V15",
            "categoria": "Eletronicos",
            "preco": Decimal128("4599.90"),
            "estoque": 15,
            # EMBEDDING 1:1 — Especificações técnicas exclusivas de notebooks:
            "especificacoes": {
                "processador": "Intel Core i7-13620H",
                "memoria_ram_gb": 16,
                "ssd_nvme_gb": 512,
                "placa_video": "NVIDIA RTX 4050 6GB",
                "tensao": "Bivolt",
            },
            # SUBSET PATTERN — Apenas estatísticas e as últimas avaliações para a vitrine:
            "resumo_avaliacoes": {"media": 4.9, "total": 2},
            "ultimas_avaliacoes": [
                {
                    "autor": "Lucas Mendes",
                    "nota": 5,
                    "comentario": "Excelente para rodar containers Docker!",
                    "data": datetime(2026, 10, 25, 14, 30, tzinfo=timezone.utc),
                },
                {
                    "autor": "Marina Rocha",
                    "nota": 5,
                    "comentario": "SSD muito rápido e silencioso.",
                    "data": datetime(2026, 10, 26, 18, 15, tzinfo=timezone.utc),
                },
            ],
            "criado_em": datetime.now(timezone.utc),
        },
        {
            "_id": id_camiseta,
            "sku": "CAM-NOSQL-IFCE",
            "nome": "Camiseta Dev Polyglot Persistence IFCE",
            "categoria": "Vestuario",
            "preco": Decimal128("69.90"),
            "estoque": 80,
            # EMBEDDING 1:1 — Polimorfismo: atributos de vestuário sem colunas NULL!
            "especificacoes": {
                "tecido": "100% Algodão Egípcio",
                "cor": "Preta",
                "tamanhos": ["P", "M", "G", "GG"],
            },
            "resumo_avaliacoes": {"media": 5.0, "total": 1},
            "ultimas_avaliacoes": [
                {
                    "autor": "Pedro Alves",
                    "nota": 5,
                    "comentario": "Muito confortável!",
                    "data": datetime(2026, 10, 26, 10, 0, tzinfo=timezone.utc),
                }
            ],
            "criado_em": datetime.now(timezone.utc),
        },
        {
            "_id": id_livro,
            "sku": "LIV-NOSQL-FOWLER",
            "nome": "Livro NoSQL Essencial (Sadalage & Fowler)",
            "categoria": "Livros",
            "preco": Decimal128("94.50"),
            "estoque": 35,
            # EMBEDDING 1:1 — Polimorfismo: atributos editoriais!
            "especificacoes": {
                "autores": ["Pramod J. Sadalage", "Martin Fowler"],
                "editora": "Novatec",
                "paginas": 216,
                "isbn": "978-8575223383",
            },
            "resumo_avaliacoes": {"media": 4.8, "total": 0},
            "ultimas_avaliacoes": [],
            "criado_em": datetime.now(timezone.utc),
        },
    ]
    db.produtos.insert_many(produtos)
    print(f"[OK] {len(produtos)} produtos polimórficos inseridos em 'db.produtos'.")

    # -------------------------------------------------------------------------
    # 2.3 Coleção 'avaliacoes' (Referencing 1:Many para histórico ilimitado)
    # -------------------------------------------------------------------------
    db.avaliacoes.insert_many(
        [
            {
                "produto_id": id_notebook,  # Chave estrangeira manual (ObjectId)
                "sku_produto": "NOTE-ACER-15",
                "autor": "Lucas Mendes",
                "nota": 5,
                "comentario": "Excelente para rodar containers Docker!",
                "data": datetime(2026, 10, 25, 14, 30, tzinfo=timezone.utc),
            },
            {
                "produto_id": id_notebook,
                "sku_produto": "NOTE-ACER-15",
                "autor": "Marina Rocha",
                "nota": 5,
                "comentario": "SSD muito rápido e silencioso.",
                "data": datetime(2026, 10, 26, 18, 15, tzinfo=timezone.utc),
            },
        ]
    )
    print("[OK] Histórico completo de avaliações salvo em 'db.avaliacoes' (Referencing 1:Many).")

    # -------------------------------------------------------------------------
    # 2.4 Coleção 'clientes' (Embedding 1:Few de Endereços)
    # -------------------------------------------------------------------------
    id_cliente = ObjectId()
    cliente_ana = {
        "_id": id_cliente,
        "nome": "Ana Beatriz Costa",
        "email": "ana.costa@aluno.ifce.edu.br",
        "cpf": "123.456.789-00",
        # EMBEDDING 1:Few — Endereços pertencem exclusivamente ao cliente e são poucos
        "enderecos": [
            {
                "apelido": "Casa",
                "rua": "Av. Chermont Alves de Oliveira, 100",
                "cidade": "Tauá",
                "uf": "CE",
                "cep": "63660-000",
                "principal": True,
            },
            {
                "apelido": "IFCE Campus Tauá",
                "rua": "Rodovia CE-187, s/n - Colibris",
                "cidade": "Tauá",
                "uf": "CE",
                "cep": "63660-000",
                "principal": False,
            },
        ],
    }
    db.clientes.insert_one(cliente_ana)
    print("[OK] Cliente inserida com array de endereços embutido (Embedding 1:Few).")

    # -------------------------------------------------------------------------
    # 2.5 Coleção 'pedidos' (Extended Reference + Snapshot Pattern)
    # -------------------------------------------------------------------------
    pedido_doc = {
        "codigo_pedido": "PED-2026-0001",
        # EXTENDED REFERENCE: Referência ao _id + campos mais exibidos na tela de pedidos
        "cliente": {
            "cliente_id": id_cliente,
            "nome": cliente_ana["nome"],
            "cpf": cliente_ana["cpf"],
        },
        # SNAPSHOT DE ENDEREÇO: Cópia imutável do local de entrega no ato da compra
        "endereco_entrega_snapshot": cliente_ana["enderecos"][0],
        # EMBEDDING + SNAPSHOT DE PREÇO: Congela o preço pago na data da compra!
        "itens": [
            {
                "produto_id": id_notebook,
                "sku": "NOTE-ACER-15",
                "nome": "Notebook Gamer Acer Nitro V15",
                "preco_unitario_na_compra": Decimal128("4599.90"),
                "quantidade": 1,
                "subtotal": Decimal128("4599.90"),
            },
            {
                "produto_id": id_camiseta,
                "sku": "CAM-NOSQL-IFCE",
                "nome": "Camiseta Dev Polyglot Persistence IFCE",
                "preco_unitario_na_compra": Decimal128("69.90"),
                "quantidade": 2,
                "subtotal": Decimal128("139.80"),
            },
        ],
        "valor_total_pago": Decimal128("4739.70"),
        "status": "PAGO",
        "criado_em": datetime.now(timezone.utc),
    }
    db.pedidos.insert_one(pedido_doc)
    print("[OK] Pedido 'PED-2026-0001' gravado com Extended Reference e Snapshot de Preços!")


if __name__ == "__main__":
    demonstrar_json_vs_bson()
    popular_ecommerce_shopgrids()
