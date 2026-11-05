#!/usr/bin/env python3
"""
Pipelines Analíticos de Inteligência de Negócio no MongoDB
Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
Professor: Prof. Me. Reginaldo Fernandes

Demonstração prática dos 5 pipelines essenciais de agregação:
1. Faturamento por Mês e Ticket Médio ($match, $group, $project, $sort)
2. Top 5 Produtos Mais Vendidos com Desconstrução de Array ($unwind, $group, $sort, $limit)
3. Enriquecimento de Dados com Junção Externa ($lookup, $project)
4. Segmentação RFM de Clientes ($group, $project com expressões de data)
5. Painel Executivo Consolidado com Multi-Perspectiva ($facet)
"""

from datetime import datetime
from pymongo import MongoClient

def conectar_mongodb(uri="mongodb://localhost:27017"):
    client = MongoClient(uri, serverSelectionTimeoutMS=2000)
    db = client['ecommerce_shopgrids']
    return db

def pipeline_1_faturamento_mensal(db):
    """
    Relatório 1: Faturamento Mensal, Lucro e Ticket Médio
    Equivalente SQL:
      SELECT DATE_TRUNC('month', data_pedido) AS mes,
             SUM(valor_total) AS faturamento,
             AVG(valor_total) AS ticket_medio,
             COUNT(*) AS total_pedidos
      FROM pedidos
      WHERE status = 'entregue'
      GROUP BY mes ORDER BY mes ASC;
    """
    print("\n" + "="*70)
    print("PIPELINE 1: Faturamento Mensal e Ticket Médio ($match, $group, $project, $sort)")
    print("="*70)

    pipeline = [
        # Estágio 1: Filtragem seletiva (usa índice {status: 1, data_pedido: 1})
        {
            "$match": {
                "status": "entregue"
            }
        },
        # Estágio 2: Agrupamento pelo ano-mês da data do pedido
        {
            "$group": {
                "_id": {
                    "ano": {"$year": "$data_pedido"},
                    "mes": {"$month": "$data_pedido"}
                },
                "faturamento_total": {"$sum": "$valor_total"},
                "lucro_total": {"$sum": "$lucro_bruto"},
                "ticket_medio": {"$avg": "$valor_total"},
                "quantidade_pedidos": {"$sum": 1}
            }
        },
        # Estágio 3: Projeção e formatação de saída
        {
            "$project": {
                "_id": 0,
                "periodo": {
                    "$concat": [
                        {"$toString": "$_id.ano"}, "-",
                        {"$cond": [
                            {"$lt": ["$_id.mes", 10]},
                            {"$concat": ["0", {"$toString": "$_id.mes"}]},
                            {"$toString": "$_id.mes"}
                        ]}
                    ]
                },
                "faturamento_total": {"$round": ["$faturamento_total", 2]},
                "lucro_total": {"$round": ["$lucro_total", 2]},
                "ticket_medio": {"$round": ["$ticket_medio", 2]},
                "quantidade_pedidos": 1
            }
        },
        # Estágio 4: Ordenação cronológica crescente
        {
            "$sort": {"periodo": 1}
        }
    ]

    resultados = list(db.pedidos.aggregate(pipeline))
    for r in resultados[:6]:
        print(f"Período: {r['periodo']} | Faturamento: R$ {r['faturamento_total']:>10.2f} | "
              f"Ticket Médio: R$ {r['ticket_medio']:>7.2f} | Pedidos: {r['quantidade_pedidos']}")
    return resultados

def pipeline_2_top_produtos_unwind(db):
    """
    Relatório 2: Top 5 Produtos e Categorias Mais Vendidas
    Necessita de $unwind para desmembrar o array 'itens' de cada pedido.
    """
    print("\n" + "="*70)
    print("PIPELINE 2: Top 5 Produtos Mais Vendidos ($unwind, $group, $sort, $limit)")
    print("="*70)

    pipeline = [
        {"$match": {"status": "entregue"}},
        # Desconstrói cada item do array de pedidos em documento individual
        {"$unwind": "$itens"},
        # Agrupa pelo SKU e Nome do produto
        {
            "$group": {
                "_id": {
                    "sku": "$itens.sku",
                    "nome": "$itens.nome",
                    "categoria": "$itens.categoria"
                },
                "unidades_vendidas": {"$sum": "$itens.quantidade"},
                "receita_gerada": {"$sum": "$itens.subtotal"}
            }
        },
        # Projeta formato limpo
        {
            "$project": {
                "_id": 0,
                "sku": "$_id.sku",
                "produto": "$_id.nome",
                "categoria": "$_id.categoria",
                "unidades_vendidas": 1,
                "receita_gerada": {"$round": ["$receita_gerada", 2]}
            }
        },
        # Ordena pelo volume financeiro decrescente
        {"$sort": {"receita_gerada": -1}},
        # Limita aos top 5
        {"$limit": 5}
    ]

    resultados = list(db.pedidos.aggregate(pipeline))
    for i, r in enumerate(resultados, 1):
        print(f"{i}º | {r['sku']} | {r['produto']:<30} | {r['categoria']:<12} | "
              f"Qtd: {r['unidades_vendidas']:>4} | Receita: R$ {r['receita_gerada']:>9.2f}")
    return resultados

def pipeline_3_lookup_catalogo_avaliacoes(db):
    """
    Relatório 3: Junção ($lookup) de Produtos com Estatísticas de Avaliações
    Equivalente SQL:
      SELECT p.nome, p.preco, p.estoque,
             AVG(a.nota) AS media_avaliacoes,
             COUNT(a.id) AS total_avaliacoes
      FROM produtos p
      LEFT JOIN avaliacoes a ON p.id = a.produto_id
      GROUP BY p.id;
    """
    print("\n" + "="*70)
    print("PIPELINE 3: Cruzamento Analítico de Catálogo com Avaliações ($lookup)")
    print("="*70)

    pipeline = [
        # Junção com a coleção de avaliações
        {
            "$lookup": {
                "from": "avaliacoes",
                "localField": "_id",
                "foreignField": "produto_id",
                "as": "historico_avaliacoes"
            }
        },
        # Estágio de projeção calculando média diretamente do array agregado
        {
            "$project": {
                "sku": 1,
                "nome": 1,
                "categoria": 1,
                "preco": 1,
                "estoque": 1,
                "total_avaliacoes": {"$size": "$historico_avaliacoes"},
                "media_nota": {
                    "$cond": [
                        {"$gt": [{"$size": "$historico_avaliacoes"}, 0]},
                        {"$round": [{"$avg": "$historico_avaliacoes.nota"}, 1]},
                        0.0
                    ]
                }
            }
        },
        # Ordena pelos produtos mais bem avaliados com estoque
        {"$sort": {"media_nota": -1, "total_avaliacoes": -1}},
        {"$limit": 5}
    ]

    resultados = list(db.produtos.aggregate(pipeline))
    for r in resultados:
        print(f"[{r['sku']}] {r['nome']:<30} | Cat: {r['categoria']:<12} | "
              f"Preço: R$ {r['preco']:>7.2f} | Nota Média: {r['media_nota']} ⭐ ({r['total_avaliacoes']} reviews)")
    return resultados

def pipeline_4_dashboard_facet(db):
    """
    Relatório 4: Painel Executivo Multi-Facetado em Única Execução ($facet)
    Gera múltiplos relatórios analíticos a partir do mesmo fluxo de dados.
    """
    print("\n" + "="*70)
    print("PIPELINE 4: Dashboard Multi-Perspectiva com $facet (KPIs + Vendas)")
    print("="*70)

    pipeline = [
        {"$match": {"status": "entregue"}},
        {
            "$facet": {
                # Sub-pipeline A: Resumo Global de Métricas (KPIs)
                "metricas_globais": [
                    {
                        "$group": {
                            "_id": None,
                            "faturamento": {"$sum": "$valor_total"},
                            "lucro": {"$sum": "$lucro_bruto"},
                            "total_vendas": {"$sum": 1},
                            "ticket_medio": {"$avg": "$valor_total"}
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "faturamento": {"$round": ["$faturamento", 2]},
                            "lucro": {"$round": ["$lucro", 2]},
                            "total_vendas": 1,
                            "ticket_medio": {"$round": ["$ticket_medio", 2]}
                        }
                    }
                ],
                # Sub-pipeline B: Distribuição por Forma de Pagamento
                "por_pagamento": [
                    {
                        "$group": {
                            "_id": "$forma_pagamento",
                            "total_pedidos": {"$sum": 1},
                            "volume_financeiro": {"$sum": "$valor_total"}
                        }
                    },
                    {
                        "$project": {
                            "forma": "$_id",
                            "_id": 0,
                            "total_pedidos": 1,
                            "volume_financeiro": {"$round": ["$volume_financeiro", 2]}
                        }
                    },
                    {"$sort": {"volume_financeiro": -1}}
                ],
                # Sub-pipeline C: Distribuição Regional (Top 5 Estados)
                "por_estado": [
                    {
                        "$group": {
                            "_id": "$cliente_estado",
                            "pedidos": {"$sum": 1},
                            "receita": {"$sum": "$valor_total"}
                        }
                    },
                    {"$sort": {"receita": -1}},
                    {"$limit": 5}
                ]
            }
        }
    ]

    resultado = list(db.pedidos.aggregate(pipeline))[0]
    print("\n--- RESUMO GERAL (KPIs) ---")
    kpis = resultado['metricas_globais'][0]
    print(f"Faturamento Global: R$ {kpis['faturamento']:,.2f}")
    print(f"Lucro Bruto Total:  R$ {kpis['lucro']:,.2f}")
    print(f"Total de Vendas:    {kpis['total_vendas']}")
    print(f"Ticket Médio Geral: R$ {kpis['ticket_medio']:,.2f}")

    print("\n--- DISTRIBUIÇÃO POR FORMA DE PAGAMENTO ---")
    for pag in resultado['por_pagamento']:
        print(f"  • {pag['forma']:<16}: R$ {pag['volume_financeiro']:>11.2f} ({pag['total_pedidos']} transações)")

    print("\n--- TOP 5 ESTADOS EM FATURAMENTO ---")
    for est in resultado['por_estado']:
        print(f"  • {est['_id']}: R$ {est['receita']:>11.2f} ({est['pedidos']} pedidos)")

    return resultado

if __name__ == '__main__':
    try:
        db = conectar_mongodb()
        db.command('ping')
        pipeline_1_faturamento_mensal(db)
        pipeline_2_top_produtos_unwind(db)
        pipeline_3_lookup_catalogo_avaliacoes(db)
        pipeline_4_dashboard_facet(db)
        print("\nTodos os pipelines executados com êxito!")
    except Exception as e:
        print(f"Aviso: Não foi possível conectar ao MongoDB local ({e}).")
        print("Para executar este script, inicie o container com 'docker compose up -d' e execute 'povoar_dados_aula08.py'.")
