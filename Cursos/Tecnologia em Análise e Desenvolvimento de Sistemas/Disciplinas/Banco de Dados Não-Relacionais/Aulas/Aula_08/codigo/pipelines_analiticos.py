#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pipelines Analíticos de Inteligência de Negócio no MongoDB
Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
Professor: Prof. Me. Reginaldo Fernandes

Demonstração prática dos 6 pipelines essenciais de agregação sobre o banco 'ecommerce_shopgrids':
1. Faturamento por Mês e Ticket Médio ($match, $group, $project, $sort)
2. Top 5 Produtos Mais Vendidos com Desconstrução de Array ($unwind, $group, $sort, $limit)
3. Cruzamento de Pedidos com Catálogo de Produtos ($lookup com 'produtos')
4. Enriquecimento de Pedidos com Dados do Cliente e Localização ($lookup com 'clientes')
5. Análise de Catálogo com Nota Média e Total de Avaliações ($lookup com 'avaliacoes')
6. Painel Executivo Consolidado Multi-Perspectiva ($facet com KPIs e Vendas por Estado)
"""

from pymongo import MongoClient

def conectar_mongodb(uri="mongodb://localhost:27017"):
    client = MongoClient(uri, serverSelectionTimeoutMS=2000)
    db = client['ecommerce_shopgrids']
    return db

def pipeline_1_faturamento_mensal(db):
    """
    Relatório 1: Faturamento Mensal e Ticket Médio
    Equivalente SQL:
      SELECT DATE_TRUNC('month', data_criacao) AS mes,
             SUM(pagamento.total_pago) AS faturamento,
             AVG(pagamento.total_pago) AS ticket_medio,
             COUNT(*) AS total_pedidos
      FROM pedidos
      WHERE status = 'ENTREGUE'
      GROUP BY mes ORDER BY mes ASC;
    """
    print("\n" + "="*75)
    print("PIPELINE 1: Faturamento Mensal e Ticket Médio ($match, $group, $project, $sort)")
    print("="*75)

    pipeline = [
        {"$match": {"status": "ENTREGUE"}},
        {
            "$group": {
                "_id": {
                    "ano": {"$year": "$data_criacao"},
                    "mes": {"$month": "$data_criacao"}
                },
                "faturamento_total": {"$sum": "$pagamento.total_pago"},
                "desconto_total": {"$sum": {"$subtract": ["$pagamento.subtotal", "$pagamento.total_pago"]}},
                "ticket_medio": {"$avg": "$pagamento.total_pago"},
                "quantidade_pedidos": {"$sum": 1}
            }
        },
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
                "desconto_total": {"$round": ["$desconto_total", 2]},
                "ticket_medio": {"$round": ["$ticket_medio", 2]},
                "quantidade_pedidos": 1
            }
        },
        {"$sort": {"periodo": 1}}
    ]

    resultados = list(db.pedidos.aggregate(pipeline))
    for r in resultados[:6]:
        print(f"Período: {r['periodo']} | Faturamento: R$ {r['faturamento_total']:>11.2f} | "
              f"Ticket Médio: R$ {r['ticket_medio']:>8.2f} | Pedidos: {r['quantidade_pedidos']}")
    return resultados

def pipeline_2_top_produtos_unwind(db):
    """
    Relatório 2: Top 5 Produtos Mais Vendidos por Volume e Receita
    Usa $unwind para desmembrar o array 'itens' de cada pedido.
    """
    print("\n" + "="*75)
    print("PIPELINE 2: Top 5 Produtos Mais Vendidos ($unwind, $group, $sort, $limit)")
    print("="*75)

    pipeline = [
        {"$match": {"status": "ENTREGUE"}},
        {"$unwind": "$itens"},
        {
            "$group": {
                "_id": "$itens.sku",
                "unidades_vendidas": {"$sum": "$itens.qtd"},
                "receita_gerada": {"$sum": {"$multiply": ["$itens.preco", "$itens.qtd"]}}
            }
        },
        {"$sort": {"receita_gerada": -1}},
        {"$limit": 5},
        {
            "$project": {
                "_id": 0,
                "sku": "$_id",
                "unidades_vendidas": 1,
                "receita_gerada": {"$round": ["$receita_gerada", 2]}
            }
        }
    ]

    resultados = list(db.pedidos.aggregate(pipeline))
    for i, r in enumerate(resultados, 1):
        print(f"{i}º | SKU: {r['sku']:<18} | Qtd: {r['unidades_vendidas']:>4} un | "
              f"Receita Total: R$ {r['receita_gerada']:>10.2f}")
    return resultados

def pipeline_3_lookup_pedidos_produtos(db):
    """
    Relatório 3: Junção Externa ($lookup) entre Itens de Pedidos e Catálogo de Produtos
    """
    print("\n" + "="*75)
    print("PIPELINE 3: Cruzamento de Itens de Pedidos com Catálogo ($lookup 'produtos')")
    print("="*75)

    pipeline = [
        {"$match": {"status": "ENTREGUE"}},
        {"$unwind": "$itens"},
        {
            "$lookup": {
                "from": "produtos",
                "localField": "itens.sku",
                "foreignField": "sku",
                "as": "prod"
            }
        },
        {"$unwind": "$prod"},
        {
            "$project": {
                "_id": 0,
                "codigo": 1,
                "sku": "$itens.sku",
                "titulo": "$prod.titulo",
                "categoria": "$prod.categoria",
                "preco": "$itens.preco",
                "qtd": "$itens.qtd"
            }
        },
        {"$limit": 5}
    ]

    resultados = list(db.pedidos.aggregate(pipeline))
    for r in resultados:
        print(f"[{r['codigo']}] SKU: {r['sku']} | {r['titulo'][:30]:<30} | "
              f"Cat: {r['categoria']:<12} | R$ {r['preco']:>7.2f} (x{r['qtd']})")
    return resultados

def pipeline_4_lookup_pedidos_clientes(db):
    """
    Relatório 4: Enriquecimento de Pedidos com Cadastro de Clientes e Localização
    Demonstra junção 1:N entre a coleção 'pedidos' e a coleção 'clientes'.
    """
    print("\n" + "="*75)
    print("PIPELINE 4: Enriquecimento de Pedidos com Cadastro de Clientes ($lookup 'clientes')")
    print("="*75)

    pipeline = [
        {"$match": {"status": "ENTREGUE"}},
        {"$sort": {"pagamento.total_pago": -1}},
        {"$limit": 5},
        {
            "$lookup": {
                "from": "clientes",
                "localField": "cliente_id",
                "foreignField": "cliente_id",
                "as": "cliente"
            }
        },
        {"$unwind": "$cliente"},
        {
            "$project": {
                "_id": 0,
                "codigo": 1,
                "cliente_nome": "$cliente.nome",
                "cidade_uf": {"$concat": ["$cliente.cidade", "/", "$cliente.estado"]},
                "segmento": "$cliente.segmento",
                "total_pago": "$pagamento.total_pago"
            }
        }
    ]

    resultados = list(db.pedidos.aggregate(pipeline))
    for i, r in enumerate(resultados, 1):
        print(f"{i}º | [{r['codigo']}] {r['cliente_nome']:<25} | "
              f"Local: {r['cidade_uf']:<20} | Seg: {r['segmento']:<11} | R$ {r['total_pago']:>10.2f}")
    return resultados

def pipeline_5_lookup_produtos_avaliacoes(db):
    """
    Relatório 5: Análise de Catálogo com Nota Média e Total de Avaliações
    Cruza 'produtos' com a coleção 'avaliacoes' usando o identificador 'sku'.
    """
    print("\n" + "="*75)
    print("PIPELINE 5: Catálogo com Avaliações de Clientes ($lookup 'avaliacoes')")
    print("="*75)

    pipeline = [
        {"$match": {"categoria": "Informática", "status": "ATIVO"}},
        {
            "$lookup": {
                "from": "avaliacoes",
                "localField": "sku",
                "foreignField": "sku",
                "as": "avaliacoes"
            }
        },
        {
            "$project": {
                "_id": 0,
                "sku": 1,
                "titulo": 1,
                "preco": 1,
                "total_avaliacoes": {"$size": "$avaliacoes"},
                "nota_media": {"$round": [{"$avg": "$avaliacoes.nota"}, 1]}
            }
        },
        {"$match": {"total_avaliacoes": {"$gte": 2}}},
        {"$sort": {"nota_media": -1, "total_avaliacoes": -1}},
        {"$limit": 5}
    ]

    resultados = list(db.produtos.aggregate(pipeline))
    for r in resultados:
        print(f"SKU: {r['sku']} | {r['titulo'][:35]:<35} | R$ {r['preco']:>8.2f} | "
              f"Avaliações: {r['total_avaliacoes']:>2} | Nota Média: {r['nota_media']} ★")
    return resultados

def pipeline_6_dashboard_facet(db):
    """
    Relatório 6: Painel Executivo Multi-Facetado em Única Execução ($facet)
    Gera múltiplos relatórios analíticos a partir do mesmo fluxo de dados.
    """
    print("\n" + "="*75)
    print("PIPELINE 6: Dashboard Multi-Perspectiva com $facet (KPIs + Maiores Pedidos)")
    print("="*75)

    pipeline = [
        {"$match": {"status": "ENTREGUE"}},
        {
            "$facet": {
                # Sub-pipeline A: Resumo Global de Métricas (KPIs)
                "metricas_globais": [
                    {
                        "$group": {
                            "_id": None,
                            "faturamento": {"$sum": "$pagamento.total_pago"},
                            "total_vendas": {"$sum": 1},
                            "ticket_medio": {"$avg": "$pagamento.total_pago"}
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "faturamento": {"$round": ["$faturamento", 2]},
                            "total_vendas": 1,
                            "ticket_medio": {"$round": ["$ticket_medio", 2]}
                        }
                    }
                ],
                # Sub-pipeline B: Maiores Pedidos Concluídos
                "maiores_pedidos": [
                    {"$sort": {"pagamento.total_pago": -1}},
                    {"$limit": 5},
                    {
                        "$project": {
                            "_id": 0,
                            "codigo": 1,
                            "cliente_id": 1,
                            "total_pago": "$pagamento.total_pago"
                        }
                    }
                ]
            }
        }
    ]

    resultado = list(db.pedidos.aggregate(pipeline))[0]
    print("\n--- RESUMO GERAL (KPIs) ---")
    kpis = resultado['metricas_globais'][0]
    print(f"Faturamento Global: R$ {kpis['faturamento']:,.2f}")
    print(f"Total de Vendas:    {kpis['total_vendas']}")
    print(f"Ticket Médio Geral: R$ {kpis['ticket_medio']:,.2f}")

    print("\n--- TOP 5 MAIORES PEDIDOS ---")
    for ped in resultado['maiores_pedidos']:
        print(f"  • {ped['codigo']} (Cliente {ped['cliente_id']}): R$ {ped['total_pago']:>10.2f}")

    return resultado

if __name__ == '__main__':
    try:
        db = conectar_mongodb()
        db.command('ping')
        pipeline_1_faturamento_mensal(db)
        pipeline_2_top_produtos_unwind(db)
        pipeline_3_lookup_pedidos_produtos(db)
        pipeline_4_lookup_pedidos_clientes(db)
        pipeline_5_lookup_produtos_avaliacoes(db)
        pipeline_6_dashboard_facet(db)
        print("\nTodos os 6 pipelines executados com pleno êxito!")
    except Exception as e:
        print(f"Erro ao executar pipelines no MongoDB ({e}).")
