/**
 * Scripts Interativos no MongoSH - Aula 08
 * MongoDB Aggregation Framework
 * Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
 * Docente: Prof. Me. Reginaldo Fernandes
 */

use ecommerce_shopgrids;

// ==============================================================================
// 1. PIPELINE BÁSICO: $match, $group, $project e $sort
// Relatório de Vendas e Ticket Médio por Mês
// ==============================================================================
print("\n--- 1. Relatório Mensal de Faturamento ---");

db.pedidos.aggregate([
  {
    $match: {
      status: "entregue"
    }
  },
  {
    $group: {
      _id: {
        ano: { $year: "$data_pedido" },
        mes: { $month: "$data_pedido" }
      },
      faturamento_total: { $sum: "$valor_total" },
      lucro_total: { $sum: "$lucro_bruto" },
      ticket_medio: { $avg: "$valor_total" },
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
      lucro_total: { $round: ["$lucro_total", 2] },
      ticket_medio: { $round: ["$ticket_medio", 2] },
      total_pedidos: 1
    }
  },
  {
    $sort: { mes_ano: 1 }
  }
]);

// ==============================================================================
// 2. DESCONSTRUÇÃO DE ARRAYS: $unwind
// Top 5 Produtos Mais Vendidos por Volume e Receita
// ==============================================================================
print("\n--- 2. Top 5 Produtos com $unwind ---");

db.pedidos.aggregate([
  { $match: { status: "entregue" } },
  { $unwind: "$itens" },
  {
    $group: {
      _id: {
        sku: "$itens.sku",
        nome: "$itens.nome",
        categoria: "$itens.categoria"
      },
      unidades_vendidas: { $sum: "$itens.quantidade" },
      receita_total: { $sum: "$itens.subtotal" }
    }
  },
  {
    $project: {
      _id: 0,
      sku: "$_id.sku",
      produto: "$_id.nome",
      categoria: "$_id.categoria",
      unidades_vendidas: 1,
      receita_total: { $round: ["$receita_total", 2] }
    }
  },
  { $sort: { receita_total: -1 } },
  { $limit: 5 }
]);

// ==============================================================================
// 3. JUNÇÃO EXTERNA: $lookup
// Cruzando Catálogo de Produtos com Avaliações
// ==============================================================================
print("\n--- 3. Cruzamento de Produtos com Avaliações ($lookup) ---");

db.produtos.aggregate([
  {
    $lookup: {
      from: "avaliacoes",
      localField: "_id",
      foreignField: "produto_id",
      as: "avaliacoes_recebidas"
    }
  },
  {
    $project: {
      sku: 1,
      nome: 1,
      categoria: 1,
      preco: 1,
      quantidade_avaliacoes: { $size: "$avaliacoes_recebidas" },
      nota_media: {
        $cond: [
          { $gt: [{ $size: "$avaliacoes_recebidas" }, 0] },
          { $round: [{ $avg: "$avaliacoes_recebidas.nota" }, 1] },
          0.0
        ]
      }
    }
  },
  { $sort: { nota_media: -1, quantidade_avaliacoes: -1 } },
  { $limit: 5 }
]);

// ==============================================================================
// 4. MULTI-PERSPECTIVA: $facet
// Dashboard Executivo em Operação Única
// ==============================================================================
print("\n--- 4. Dashboard Executivo com $facet ---");

db.pedidos.aggregate([
  { $match: { status: "entregue" } },
  {
    $facet: {
      resumo_geral: [
        {
          $group: {
            _id: null,
            faturamento: { $sum: "$valor_total" },
            ticket_medio: { $avg: "$valor_total" },
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
      por_canal: [
        {
          $group: {
            _id: "$canal",
            total_vendas: { $sum: 1 },
            faturamento: { $sum: "$valor_total" }
          }
        },
        { $sort: { faturamento: -1 } }
      ]
    }
  }
]);

// ==============================================================================
// 5. INSPEÇÃO DO PLANO DE EXECUÇÃO: explain("executionStats")
// ==============================================================================
print("\n--- 5. Plano de Execução do Pipeline ---");

db.pedidos.explain("executionStats").aggregate([
  { $match: { status: "entregue" } },
  {
    $group: {
      _id: "$canal",
      faturamento: { $sum: "$valor_total" }
    }
  }
]);
