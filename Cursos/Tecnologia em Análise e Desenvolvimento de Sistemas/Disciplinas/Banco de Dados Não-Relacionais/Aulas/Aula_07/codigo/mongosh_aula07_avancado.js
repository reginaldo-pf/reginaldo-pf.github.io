// =============================================================================
// Script de Aula: Operações CRUD Avançadas e Indexação de Alta Performance
// Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 07
// IFCE Campus Tauá - Prof. Me. Reginaldo Fernandes
// =============================================================================

// 1. Conexão com o Banco de Dados
use ecommerce_shopgrids

print("\n--- 1. DEMONSTRAÇÃO DO OPERADOR $elemMatch ---")
// Inserindo pedido para teste de falso positivo
db.pedidos.deleteOne({ codigo: "PED-MOSH-TESTE" })
db.pedidos.insertOne({
  codigo: "PED-MOSH-TESTE",
  cliente_id: 1001,
  status: "PENDENTE",
  itens: [
    { sku: "ITEM-A", preco: 250.0, qtd: 1, status_entrega: "PENDENTE" },
    { sku: "ITEM-B", preco: 30.0,  qtd: 6, status_entrega: "PENDENTE" }
  ],
  pagamento: { subtotal: 430.0, total_pago: 430.0 },
  data_criacao: new Date()
})

// Consulta Ingênua (Falso positivo: preço > 100 e qtd >= 5)
print("Consulta sem $elemMatch (Falso positivo retornado):")
printjson(db.pedidos.find({
  codigo: "PED-MOSH-TESTE",
  "itens.preco": { $gt: 100 },
  "itens.qtd": { $gte: 5 }
}))

// Consulta Correta com $elemMatch
print("Consulta correta com $elemMatch (Nenhum documento deve retornar):")
printjson(db.pedidos.find({
  codigo: "PED-MOSH-TESTE",
  itens: {
    $elemMatch: {
      preco: { $gt: 100 },
      qtd: { $gte: 5 }
    }
  }
}))

print("\n--- 2. OPERADOR $expr (COMPARAÇÃO ENTRE CAMPOS INTERNOS) ---")
// Localizar produtos com estoque atual abaixo do estoque mínimo
print("Produtos com estoque crítico ($estoque.atual < $estoque.minimo):")
printjson(db.produtos.find(
  { $expr: { $lt: ["$estoque.atual", "$estoque.minimo"] } },
  { titulo: 1, estoque: 1, _id: 0 }
).limit(2))

print("\n--- 3. ATUALIZAÇÕES ATÔMICAS: $inc, $push com $slice E arrayFilters ---")
// Atualização atômica de estoque
db.produtos.updateOne(
  { sku: "SKU-INF-000101" },
  { $inc: { "estoque.atual": -1 } }
)

// Inserção em array mantendo limite máximo de 5 itens ($slice: -5)
db.produtos.updateOne(
  { sku: "SKU-INF-000101" },
  {
    $push: {
      ultimas_avaliacoes: {
        $each: [{ nota: 5, autor: "Aluno ADS", comentario: "Testado via mongosh!" }],
        $slice: -5
      }
    }
  }
)

// Atualização posicional seletiva com arrayFilters
db.pedidos.updateOne(
  { codigo: "PED-MOSH-TESTE" },
  {
    $set: {
      "itens.$[alvo].status_entrega": "SEPARADO_EM_ESTOQUE",
      "itens.$[alvo].data_separacao": new Date()
    }
  },
  {
    arrayFilters: [ { "alvo.sku": "ITEM-A" } ]
  }
)
print("Pedido atualizado com arrayFilters:")
printjson(db.pedidos.findOne({ codigo: "PED-MOSH-TESTE" }))

print("\n--- 4. GESTÃO DE ÍNDICES E REGRA DE OURO ESR ---")
// Listar índices atuais
print("Índices existentes em 'produtos':")
printjson(db.produtos.getIndexes())

// Criar Índice Simples Único
db.produtos.createIndex({ sku: 1 }, { unique: true, name: "idx_sku_unico" })

// Criar Índice Composto seguindo rigorosamente ESR:
// E (Equality): status: 1
// S (Sort): data_cadastro: -1
// R (Range): preco: 1
db.produtos.createIndex(
  { status: 1, data_cadastro: -1, preco: 1 },
  { name: "idx_esr_produtos" }
)

print("\n--- 5. ÍNDICE TEXTUAL COM PESOS (FULL-TEXT SEARCH) ---")
// Criar índice textual composto ponderado
db.produtos.createIndex(
  { titulo: "text", tags: "text", descricao: "text" },
  {
    weights: { titulo: 10, tags: 5, descricao: 1 },
    default_language: "portuguese",
    name: "idx_text_produtos_full"
  }
)

// Consulta com escore de relevância
print("Busca textual por 'ergonômico sem fio' ordenada por relevância:")
printjson(db.produtos.find(
  { $text: { $search: "ergonômico sem fio" } },
  { titulo: 1, preco: 1, score: { $meta: "textScore" }, _id: 0 }
).sort({ score: { $meta: "textScore" } }).limit(3))

print("\n--- 6. ANÁLISE DE PLANO DE EXECUÇÃO COM explain('executionStats') ---")
// Analisando plano com índice ESR
var explicacao = db.produtos.find(
  { status: "ATIVO", preco: { $gte: 100, $lte: 800 } }
).sort({ data_cadastro: -1 }).limit(10).explain("executionStats")

print("Estágio de Execução : " + explicacao.executionStats.executionStages.stage)
print("Tempo de Execução   : " + explicacao.executionStats.executionTimeMillis + " ms")
print("Docs Examinados     : " + explicacao.executionStats.totalDocsExamined)
print("Docs Retornados     : " + explicacao.executionStats.nReturned)

print("\n--- 7. CONSULTA 100% COBERTA (COVERED QUERY) ---")
// Índice de cobertura total
db.produtos.createIndex(
  { categoria: 1, preco: 1, sku: 1 },
  { name: "idx_cobertura_total" }
)

var explicacaoCovered = db.produtos.find(
  { categoria: "Informática", preco: { $lte: 2000 } },
  { categoria: 1, preco: 1, sku: 1, _id: 0 } // _id: 0 é OBRIGATÓRIO para eliminar FETCH!
).limit(20).explain("executionStats")

print("Covered Query Docs Examinados: " + explicacaoCovered.executionStats.totalDocsExamined + " (Meta = 0)")
print("Covered Query Stage          : " + explicacaoCovered.executionStats.executionStages.stage)

print("\n✅ Script mongosh executado com sucesso!")
