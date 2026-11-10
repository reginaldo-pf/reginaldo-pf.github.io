/**
 * Scripts Interativos no MongoSH - Aula 08
 * MongoDB Aggregation Framework
 * Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
 * Docente: Prof. Me. Reginaldo Fernandes
 */

db = db.getSiblingDB("ecommerce_shopgrids");

// ==============================================================================
// 1. PIPELINE BÁSICO: $match, $group, $project e $sort
// Relatório de Vendas e Ticket Médio por Mês
// ==============================================================================
print("\n--- 1. Relatório Mensal de Faturamento ---");

printjson(db.pedidos.aggregate([
  {
    $match: {
      status: "ENTREGUE"
    }
  },
  {
    $group: {
      _id: {
        ano: { $year: "$data_criacao" },
        mes: { $month: "$data_criacao" }
      },
      faturamento_total: { $sum: "$pagamento.total_pago" },
      ticket_medio: { $avg: "$pagamento.total_pago" },
      total_pedidos: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      mes_ano: {
        $concat: [
          { $toString: "$_id.ano" }, "-",
          {
            $cond: [
              { $lt: ["$_id.mes", 10] },
              { $concat: ["0", { $toString: "$_id.mes" }] },
              { $toString: "$_id.mes" }
            ]
          }
        ]
      },
      faturamento_total: { $round: ["$faturamento_total", 2] },
      ticket_medio: { $round: ["$ticket_medio", 2] },
      total_pedidos: 1
    }
  },
  {
    $sort: { mes_ano: 1 }
  }
]).toArray());

// ==============================================================================
// 2. DESCONSTRUÇÃO DE ARRAYS: $unwind
// Top 5 Produtos Mais Vendidos por Volume e Receita
// ==============================================================================
print("\n--- 2. Top 5 Produtos com $unwind ---");

printjson(db.pedidos.aggregate([
  { $match: { status: "ENTREGUE" } },
  { $unwind: "$itens" },
  {
    $group: {
      _id: "$itens.sku",
      unidades_vendidas: { $sum: "$itens.qtd" },
      receita_total: { $sum: { $multiply: ["$itens.preco", "$itens.qtd"] } }
    }
  },
  {
    $project: {
      _id: 0,
      sku: "$_id",
      unidades_vendidas: 1,
      receita_total: { $round: ["$receita_total", 2] }
    }
  },
  { $sort: { receita_total: -1 } },
  { $limit: 5 }
]).toArray());

// ==============================================================================
// 3. JUNÇÃO EXTERNA: $lookup entre Pedidos e Catálogo de Produtos
// ==============================================================================
print("\n--- 3. Cruzamento de Pedidos com Produtos ($lookup 'produtos') ---");

printjson(db.pedidos.aggregate([
  { $match: { status: "ENTREGUE" } },
  { $unwind: "$itens" },
  {
    $lookup: {
      from: "produtos",
      localField: "itens.sku",
      foreignField: "sku",
      as: "prod"
    }
  },
  { $unwind: "$prod" },
  {
    $project: {
      _id: 0,
      codigo: 1,
      sku: "$itens.sku",
      titulo: "$prod.titulo",
      categoria: "$prod.categoria",
      preco: "$itens.preco",
      qtd: "$itens.qtd"
    }
  },
  { $limit: 5 }
]).toArray());

// ==============================================================================
// 4. JUNÇÃO EXTERNA: $lookup entre Pedidos e Cadastro de Clientes
// Enriquecimento com Dados Cadastrais e Localização
// ==============================================================================
print("\n--- 4. Enriquecimento de Pedidos com Clientes ($lookup 'clientes') ---");

printjson(db.pedidos.aggregate([
  { $match: { status: "ENTREGUE" } },
  { $sort: { "pagamento.total_pago": -1 } },
  { $limit: 5 },
  {
    $lookup: {
      from: "clientes",
      localField: "cliente_id",
      foreignField: "cliente_id",
      as: "cliente"
    }
  },
  { $unwind: "$cliente" },
  {
    $project: {
      _id: 0,
      codigo: 1,
      cliente_nome: "$cliente.nome",
      localizacao: { $concat: ["$cliente.cidade", "/", "$cliente.estado"] },
      segmento: "$cliente.segmento",
      total_pago: "$pagamento.total_pago"
    }
  }
]).toArray());

// ==============================================================================
// 5. JUNÇÃO EXTERNA: $lookup entre Produtos e Avaliações
// Média de Avaliações e Volume de Reviews por SKU
// ==============================================================================
print("\n--- 5. Catálogo com Avaliações ($lookup 'avaliacoes') ---");

printjson(db.produtos.aggregate([
  { $match: { categoria: "Informática", status: "ATIVO" } },
  {
    $lookup: {
      from: "avaliacoes",
      localField: "sku",
      foreignField: "sku",
      as: "avaliacoes"
    }
  },
  {
    $project: {
      _id: 0,
      sku: 1,
      titulo: 1,
      preco: 1,
      total_avaliacoes: { $size: "$avaliacoes" },
      nota_media: { $round: [{ $avg: "$avaliacoes.nota" }, 1] }
    }
  },
  { $match: { total_avaliacoes: { $gte: 2 } } },
  { $sort: { nota_media: -1, total_avaliacoes: -1 } },
  { $limit: 5 }
]).toArray());

// ==============================================================================
// 6. MULTI-PERSPECTIVA: $facet
// Dashboard Executivo em Operação Única
// ==============================================================================
print("\n--- 6. Dashboard Executivo com $facet ---");

printjson(db.pedidos.aggregate([
  { $match: { status: "ENTREGUE" } },
  {
    $facet: {
      resumo_geral: [
        {
          $group: {
            _id: null,
            faturamento: { $sum: "$pagamento.total_pago" },
            ticket_medio: { $avg: "$pagamento.total_pago" },
            pedidos: { $sum: 1 }
          }
        },
        {
          $project: {
            _id: 0,
            faturamento: { $round: ["$faturamento", 2] },
            ticket_medio: { $round: ["$ticket_medio", 2] },
            pedidos: 1
          }
        }
      ],
      maiores_pedidos: [
        { $sort: { "pagamento.total_pago": -1 } },
        { $limit: 3 },
        {
          $project: {
            _id: 0,
            codigo: 1,
            cliente_id: 1,
            total_pago: "$pagamento.total_pago"
          }
        }
      ]
    }
  }
]).toArray());

// ==============================================================================
// 7. INSPEÇÃO DO PLANO DE EXECUÇÃO: explain("executionStats")
// ==============================================================================
print("\n--- 7. Plano de Execução do Pipeline ---");

printjson(db.pedidos.explain("executionStats").aggregate([
  { $match: { status: "ENTREGUE" } },
  {
    $group: {
      _id: "$status",
      faturamento: { $sum: "$pagamento.total_pago" }
    }
  }
]));
