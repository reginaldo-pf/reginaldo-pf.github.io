#!/usr/bin/env bash
# ==============================================================================
# IFCE Campus Tauá - ADS16: Banco de Dados Não-Relacionais
# Comandos Rápidos de Linha de Comando (Revisão N1: Redis + MongoDB)
# ==============================================================================

echo "=== 1. REDIS CLI (Estruturas e Cache) ==="
echo "# Strings e TTL:"
echo "SET produto:SKU-001 '{\"nome\":\"Notebook\",\"preco\":3800}' EX 60"
echo "GET produto:SKU-001"
echo "TTL produto:SKU-001"
echo ""
echo "# Hashes (Carrinhos e Sessões):"
echo "HSET carrinho:cli_101 SKU-001 2 SKU-002 1"
echo "HINCRBY carrinho:cli_101 SKU-001 1"
echo "HGETALL carrinho:cli_101"
echo ""
echo "# Listas (Filas FIFO):"
echo "LPUSH fila:pedidos '{\"pedido_id\":\"PED-01\"}'"
echo "RPOP fila:pedidos"
echo ""

echo "=== 2. MONGODB SH (CRUD Atômico e ESR) ==="
echo "# Filtros e Atualizações Atômicas:"
echo "db.produtos.updateOne({ sku: 'SKU-001' }, { \$inc: { estoque: -1 } })"
echo "db.pedidos.find({ itens: { \$elemMatch: { preco_unitario: { \$gt: 200 }, quantidade: { \$gte: 2 } } } })"
echo ""
echo "# Índices e Regra ESR:"
echo "db.pedidos.createIndex({ status: 1, data_pedido: -1, valor_total: 1 })"
echo "db.pedidos.explain('executionStats').find({ status: 'entregue', valor_total: { \$gte: 500 } }).sort({ data_pedido: -1 })"
echo ""
echo "# Pipeline de Agregação:"
echo "db.pedidos.aggregate(["
echo "  { \$match: { status: 'entregue' } },"
echo "  { \$group: { _id: '\$canal', total: { \$sum: '\$valor_total' } } },"
echo "  { \$sort: { total: -1 } }"
echo "])"
