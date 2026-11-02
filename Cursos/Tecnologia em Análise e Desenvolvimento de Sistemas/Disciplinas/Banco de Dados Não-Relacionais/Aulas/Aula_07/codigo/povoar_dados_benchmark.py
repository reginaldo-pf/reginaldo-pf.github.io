#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Povoamento em Lote para Testes de Carga e Benchmark de Índices
Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 07
IFCE Campus Tauá - Prof. Me. Reginaldo Fernandes

Gera 50.000 produtos e 10.000 pedidos realistas para demonstrar o impacto do COLLSCAN vs IXSCAN.
"""

import sys
import random
from datetime import datetime, timedelta
from pymongo import MongoClient, InsertOne
from pymongo.errors import ConnectionFailure

CATEGORIAS = [
    "Informática", "Eletrônicos", "Periféricos", "Smartphones", 
    "Gamer", "Acessórios", "Áudio", "Armazenamento", "Redes", "Monitores"
]

SUBSTANTIVOS = [
    "Teclado", "Mouse", "Monitor", "Headset", "SSD NVMe", "Placa de Vídeo",
    "Processador", "Memória RAM", "Gabinete", "Fonte ATX", "Roteador Wi-Fi",
    "Cadeira", "Webcam HD", "Microfone", "Hub USB-C", "Carregador Rápido"
]

ADJETIVOS = [
    "Gamer Pro", "Ergonômico", "Sem Fio", "Bluetooth 5.3", "RGB Ultra",
    "Mecânico RGB", "Silencioso", "Compacto", "Alta Performance", "Metálico",
    "UltraWide 4K", "Modular", "Resistente à Água", "Profissional", "Customizável"
]

DESCRICOES = [
    "Equipamento de ponta projetado para produtividade extrema e jogabilidade profissional.",
    "Design ergonômico premiado com descanso para punho e switches duráveis de resposta tátil.",
    "Conectividade estável de baixa latência com bateria de longa duração e recarga ultra rápida.",
    "Estrutura robusta em alumínio aeroespacial com iluminação RGB personalizável via software.",
    "Sensor óptico de alta precisão com ajuste dinâmico de sensibilidade e memória interna."
]

TAGS_POOL = [
    "gamer", "promocao", "sem fio", "ergonomico", "rgb", "bluetooth",
    "usb-c", "mecanico", "4k", "alta performance", "black friday", "lancamento"
]

STATUS_PRODUTO = ["ATIVO", "ATIVO", "ATIVO", "INATIVO", "ESGOTADO"]
STATUS_PEDIDO = ["PENDENTE", "PAGO", "EM_TRANSPORTE", "ENTREGUE", "CANCELADO"]

def conectar_mongo(uri="mongodb://localhost:27017"):
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        client.admin.command("ping")
        print(" Conectado com sucesso ao servidor MongoDB!")
        return client
    except ConnectionFailure:
        print(" ERRO: Não foi possível conectar ao MongoDB em", uri)
        print("Certifique-se de que o contêiner está rodando: 'docker compose up -d'")
        sys.exit(1)

def gerar_lote_produtos(qtd=50000):
    print(f"📦 Gerando {qtd:,} documentos sintéticos de produtos em memória...")
    produtos = []
    base_data = datetime.now() - timedelta(days=730)

    for i in range(1, qtd + 1):
        cat = random.choice(CATEGORIAS)
        sub = random.choice(SUBSTANTIVOS)
        adj = random.choice(ADJETIVOS)
        titulo = f"{sub} {adj} {random.randint(100, 9900)}"
        preco = round(random.uniform(29.90, 8999.00), 2)
        estoque_min = random.randint(5, 20)
        estoque_atual = random.randint(0, 150)
        tags = list(set(random.sample(TAGS_POOL, k=random.randint(2, 4))))
        data_cad = base_data + timedelta(minutes=random.randint(0, 1051200))
        status = random.choice(STATUS_PRODUTO)

        produtos.append({
            "sku": f"SKU-{cat[:3].upper()}-{i:06d}",
            "titulo": titulo,
            "descricao": random.choice(DESCRICOES),
            "categoria": cat,
            "preco": preco,
            "estoque": {
                "atual": estoque_atual,
                "minimo": estoque_min
            },
            "status": status,
            "tags": tags,
            "data_cadastro": data_cad,
            "ultimas_avaliacoes": [
                {"nota": random.randint(3, 5), "autor": f"Cliente_{random.randint(1, 999)}"}
                for _ in range(random.randint(1, 3))
            ]
        })
    return produtos

def gerar_lote_pedidos(qtd=10000):
    print(f"📦 Gerando {qtd:,} pedidos sintéticos em memória...")
    pedidos = []
    base_data = datetime.now() - timedelta(days=180)

    for i in range(1, qtd + 1):
        num_itens = random.randint(1, 4)
        itens = []
        subtotal = 0.0
        for _ in range(num_itens):
            preco_item = round(random.uniform(50.0, 1500.0), 2)
            qtd_item = random.randint(1, 3)
            subtotal += preco_item * qtd_item
            itens.append({
                "sku": f"SKU-INF-{random.randint(1, 50000):06d}",
                "preco": preco_item,
                "qtd": qtd_item,
                "status_entrega": "PENDENTE"
            })
        
        desconto = round(random.choice([0.0, 10.0, 25.0, 50.0]), 2)
        total_pago = max(subtotal - desconto, 10.0)

        pedidos.append({
            "codigo": f"PED-2026-{i:06d}",
            "cliente_id": random.randint(1001, 3500),
            "status": random.choice(STATUS_PEDIDO),
            "itens": itens,
            "pagamento": {
                "subtotal": round(subtotal, 2),
                "total_pago": round(total_pago, 2)
            },
            "data_criacao": base_data + timedelta(minutes=random.randint(0, 259200))
        })
    return pedidos

def povoar_banco(total_produtos=50000, total_pedidos=10000):
    client = conectar_mongo()
    db = client["ecommerce_shopgrids"]

    print("\n🧹 Limpando coleções anteriores no banco 'ecommerce_shopgrids'...")
    db.produtos.drop()
    db.pedidos.drop()

    # 1. Inserir Produtos em lotes de 5000
    produtos = gerar_lote_produtos(total_produtos)
    batch_size = 5000
    total_inseridos = 0
    print(f"\n🚀 Inserindo produtos no MongoDB em lotes de {batch_size} via bulk_write...")
    
    for idx in range(0, len(produtos), batch_size):
        chunk = produtos[idx : idx + batch_size]
        operacoes = [InsertOne(doc) for doc in chunk]
        db.produtos.bulk_write(operacoes, ordered=False)
        total_inseridos += len(chunk)
        print(f"  -> {total_inseridos:,} / {total_produtos:,} produtos inseridos...")

    # 2. Inserir Pedidos em lotes de 5000
    pedidos = gerar_lote_pedidos(total_pedidos)
    print(f"\n🚀 Inserindo pedidos no MongoDB em lotes de {batch_size}...")
    total_ped_inseridos = 0
    for idx in range(0, len(pedidos), batch_size):
        chunk = pedidos[idx : idx + batch_size]
        operacoes = [InsertOne(doc) for doc in chunk]
        db.pedidos.bulk_write(operacoes, ordered=False)
        total_ped_inseridos += len(chunk)
        print(f"  -> {total_ped_inseridos:,} / {total_pedidos:,} pedidos inseridos...")

    print(f"\n Povoamento concluído com absoluto sucesso!")
    print(f"  Total Produtos na Coleção: {db.produtos.count_documents({}):,}")
    print(f"  Total Pedidos na Coleção : {db.pedidos.count_documents({}):,}")
    print(f"  Banco de Dados: 'ecommerce_shopgrids'\n")

if __name__ == "__main__":
    qtd_prod = 50000
    qtd_ped = 10000
    if len(sys.argv) > 1:
        try:
            qtd_prod = int(sys.argv[1])
        except ValueError:
            pass
    povoar_banco(qtd_prod, qtd_ped)
