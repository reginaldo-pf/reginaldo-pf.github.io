#!/usr/bin/env python3
"""
Povoamento de Dados para a Aula 08: MongoDB Aggregation Framework
Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
Professor: Prof. Me. Reginaldo Fernandes

Gera coleções realistas do e-commerce ShopGrids:
- clientes (500 documentos)
- produtos (50 documentos em 5 categorias)
- pedidos (10.000 documentos com subdocumentos de itens e múltiplos status)
- avaliações (1.500 avaliações com notas e comentários)
Também exporta uma amostra representativa em 'pedidos_amostra_aula08.json' para o Compass.
"""

import json
import random
from datetime import datetime, timedelta
from bson import ObjectId, json_util
from pymongo import MongoClient

def gerar_dados():
    random.seed(42)

    estados = ['CE', 'PI', 'RN', 'PB', 'PE', 'BA', 'SP', 'RJ', 'MG', 'RS']
    cidades = {
        'CE': ['Tauá', 'Fortaleza', 'Sobral', 'Juazeiro do Norte', 'Crateús', 'Iguatu'],
        'PI': ['Teresina', 'Picos', 'Parnaíba'],
        'RN': ['Natal', 'Mossoró'],
        'PB': ['João Pessoa', 'Campina Grande'],
        'PE': ['Recife', 'Caruaru'],
        'BA': ['Salvador', 'Feira de Santana'],
        'SP': ['São Paulo', 'Campinas', 'Santos'],
        'RJ': ['Rio de Janeiro', 'Niterói'],
        'MG': ['Belo Horizonte', 'Uberlândia'],
        'RS': ['Porto Alegre', 'Caxias do Sul']
    }
    segmentos = ['Varejo', 'Corporativo', 'VIP']

    # 1. Clientes
    clientes = []
    nomes_base = [
        'Ana Silva', 'Bruno Santos', 'Carlos Oliveira', 'Daniela Souza', 'Eduardo Lima',
        'Fernanda Pereira', 'Gabriel Costa', 'Helena Martins', 'Igor Ferreira', 'Juliana Rocha',
        'Lucas Alves', 'Mariana Ribeiro', 'Nicolas Dias', 'Olivia Mendes', 'Paulo Carvalho',
        'Quezia Gomes', 'Rafael Barbosa', 'Sabrina Castro', 'Tiago Moreira', 'Vanessa Cardoso'
    ]
    for i in range(500):
        uf = random.choice(estados)
        cidade = random.choice(cidades[uf])
        nome_completo = f"{random.choice(nomes_base)} {i+1}"
        cliente_id = ObjectId()
        data_cad = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 650))
        clientes.append({
            '_id': cliente_id,
            'nome': nome_completo,
            'email': f"cliente_{i+1}@shopgrids.com.br",
            'estado': uf,
            'cidade': cidade,
            'segmento': random.choices(segmentos, weights=[0.70, 0.20, 0.10])[0],
            'data_cadastro': data_cad
        })

    # 2. Produtos
    categorias = {
        'Eletrônicos': [
            ('Notebook Ultra 15', 3800.0, 2600.0),
            ('Monitor Curvo 27"', 1400.0, 950.0),
            ('Tablet Pro 11"', 2900.0, 1950.0),
            ('Smartphone X50', 2400.0, 1600.0),
            ('Smart TV 55" 4K', 2700.0, 1850.0)
        ],
        'Periféricos': [
            ('Teclado Mecânico RGB', 350.0, 180.0),
            ('Mouse Gamer Óptico', 190.0, 95.0),
            ('Headset Surround 7.1', 420.0, 220.0),
            ('Webcam Full HD 1080p', 280.0, 140.0),
            ('Microfone Condensador USB', 450.0, 240.0)
        ],
        'Móveis': [
            ('Cadeira Ergonômica Pro', 1100.0, 650.0),
            ('Mesa Regulável Standing Desk', 1800.0, 1100.0),
            ('Suporte Articulado para Monitor', 220.0, 110.0),
            ('Gaveteiro Volante 3 Gavetas', 380.0, 210.0),
            ('Estante Modular Aço/Madeira', 490.0, 280.0)
        ],
        'Acessórios': [
            ('Hub USB-C 8 em 1', 230.0, 105.0),
            ('Mousepad Extra Grande 90x40', 89.0, 35.0),
            ('Cabo HDMI 2.1 Ultra High Speed', 65.0, 22.0),
            ('Suporte de Alumínio para Notebook', 120.0, 50.0),
            ('Carregador Rápido 65W GaN', 180.0, 80.0)
        ],
        'Gamer': [
            ('Placa de Vídeo RTX 4070', 4500.0, 3400.0),
            ('Gabinete ATX Airflow', 520.0, 310.0),
            ('Water Cooler 240mm RGB', 480.0, 270.0),
            ('Memória RAM 16GB DDR5', 340.0, 190.0),
            ('SSD NVMe 1TB Gen4', 420.0, 230.0)
        ]
    }

    produtos = []
    prod_idx = 1
    for cat, lista in categorias.items():
        for nome_base, preco, custo in lista:
            for v in range(2):  # gera 2 variantes para totalizar 50 produtos
                sku = f"SKU-{cat[:3].upper()}-{prod_idx:03d}"
                sufixo = "" if v == 0 else " Plus"
                produtos.append({
                    '_id': ObjectId(),
                    'sku': sku,
                    'nome': f"{nome_base}{sufixo}",
                    'categoria': cat,
                    'preco': preco * (1.1 if v == 1 else 1.0),
                    'custo': custo * (1.1 if v == 1 else 1.0),
                    'estoque': random.randint(15, 180)
                })
                prod_idx += 1

    # 3. Pedidos (10.000 pedidos)
    status_opcoes = ['entregue', 'processando', 'cancelado', 'enviado']
    status_pesos = [0.75, 0.10, 0.05, 0.10]
    canais = ['web', 'mobile', 'loja_fisica']
    formas_pagamento = ['cartao_credito', 'pix', 'boleto']

    data_inicio = datetime(2025, 11, 1)
    pedidos = []

    for p in range(10000):
        cliente = random.choice(clientes)
        num_itens = random.choices([1, 2, 3, 4, 5], weights=[0.45, 0.30, 0.15, 0.07, 0.03])[0]
        itens_selecionados = random.sample(produtos, num_itens)

        itens_pedido = []
        valor_total = 0.0
        custo_total = 0.0
        desconto_total = 0.0

        for prod in itens_selecionados:
            qtd = random.choices([1, 2, 3, 4], weights=[0.7, 0.2, 0.07, 0.03])[0]
            desc_unit = round(random.choice([0.0, 5.0, 10.0, 15.0, 25.0]), 2)
            preco_unit = float(prod['preco'])
            custo_unit = float(prod['custo'])

            itens_pedido.append({
                'produto_id': prod['_id'],
                'sku': prod['sku'],
                'nome': prod['nome'],
                'categoria': prod['categoria'],
                'quantidade': qtd,
                'preco_unitario': preco_unit,
                'desconto_unitario': desc_unit,
                'subtotal': round(qtd * (preco_unit - desc_unit), 2)
            })

            valor_total += qtd * (preco_unit - desc_unit)
            custo_total += qtd * custo_unit
            desconto_total += qtd * desc_unit

        data_ped = data_inicio + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        status = random.choices(status_opcoes, weights=status_pesos)[0]

        pedidos.append({
            '_id': ObjectId(),
            'numero_pedido': f"PED-2026-{p+1:06d}",
            'cliente_id': cliente['_id'],
            'cliente_nome': cliente['nome'],
            'cliente_estado': cliente['estado'],
            'data_pedido': data_ped,
            'status': status,
            'canal': random.choice(canais),
            'forma_pagamento': random.choices(formas_pagamento, weights=[0.55, 0.35, 0.10])[0],
            'itens': itens_pedido,
            'valor_total': round(valor_total, 2),
            'custo_total': round(custo_total, 2),
            'desconto_total': round(desconto_total, 2),
            'lucro_bruto': round(valor_total - custo_total, 2)
        })

    # 4. Avaliações (1.500)
    avaliacoes = []
    comentarios_positivos = [
        "Produto excelente, superou as expectativas!",
        "Chegou super rápido no Ceará e muito bem embalado.",
        "Qualidade de construção impecável, recomendo fortemente.",
        "Ótimo custo-benefício para trabalho remoto."
    ]
    comentarios_medios = [
        "Atende ao anunciado, mas o manual poderia ser melhor.",
        "Bom produto, entrega demorou um pouco.",
        "Funciona bem, porém acabamento simples."
    ]
    comentarios_negativos = [
        "Não gostei do acabamento, esperava mais.",
        "Veio com pequeno detalhe na embalagem."
    ]

    for a in range(1500):
        prod = random.choice(produtos)
        cli = random.choice(clientes)
        nota = random.choices([5, 4, 3, 2, 1], weights=[0.55, 0.25, 0.10, 0.06, 0.04])[0]
        if nota >= 4:
            coment = random.choice(comentarios_positivos)
        elif nota == 3:
            coment = random.choice(comentarios_medios)
        else:
            coment = random.choice(comentarios_negativos)

        avaliacoes.append({
            '_id': ObjectId(),
            'produto_id': prod['_id'],
            'cliente_id': cli['_id'],
            'nota': nota,
            'comentario': coment,
            'data_avaliacao': datetime(2026, 1, 1) + timedelta(days=random.randint(0, 300))
        })

    return clientes, produtos, pedidos, avaliacoes

def salvar_amostra_json(pedidos, produtos):
    # Salva os primeiros 100 pedidos e os produtos para importação rápida no Compass
    amostra = {
        "produtos": produtos[:25],
        "pedidos": pedidos[:100]
    }
    with open('pedidos_amostra_aula08.json', 'w', encoding='utf-8') as f:
        f.write(json_util.dumps(pedidos[:50], indent=2, ensure_ascii=False))
    print("Amostra representativa exportada em: pedidos_amostra_aula08.json")

def inserir_mongodb(clientes, produtos, pedidos, avaliacoes, uri="mongodb://localhost:27017"):
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        db = client['ecommerce_shopgrids']

        print("Conectado ao MongoDB local! Limpando e povoando coleções...")
        db.clientes.drop()
        db.produtos.drop()
        db.pedidos.drop()
        db.avaliacoes.drop()

        db.clientes.insert_many(clientes)
        db.produtos.insert_many(produtos)
        db.pedidos.insert_many(pedidos)
        db.avaliacoes.insert_many(avaliacoes)

        print("Criando índices estratégicos para agregação e buscas...")
        db.pedidos.create_index([("data_pedido", 1), ("status", 1)])
        db.pedidos.create_index([("cliente_id", 1)])
        db.pedidos.create_index([("itens.produto_id", 1)])
        db.produtos.create_index([("categoria", 1)])

        print("Banco de dados 'ecommerce_shopgrids' povoado com sucesso:")
        print(f"  - Clientes:   {len(clientes)}")
        print(f"  - Produtos:   {len(produtos)}")
        print(f"  - Pedidos:    {len(pedidos)}")
        print(f"  - Avaliações: {len(avaliacoes)}")
    except Exception as e:
        print(f"MongoDB local offline ou inacessível ({e}).")
        print("Os dados foram gerados em memória e a amostra JSON foi salva.")

if __name__ == '__main__':
    print("Gerando dados sintéticos estruturados para o ecossistema ShopGrids...")
    cli, prods, peds, avals = gerar_dados()
    salvar_amostra_json(peds, prods)
    inserir_mongodb(cli, prods, peds, avals)
