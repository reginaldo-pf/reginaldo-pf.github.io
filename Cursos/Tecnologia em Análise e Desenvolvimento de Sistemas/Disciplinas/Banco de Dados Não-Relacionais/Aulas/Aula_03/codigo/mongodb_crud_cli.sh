#!/usr/bin/env bash
# ==============================================================================
# IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS16)
# Disciplina: Banco de Dados Não-Relacionais
# Aula 03 (Sábado Letivo) - Prática de Terminal CLI com MongoDB (mongosh)
# Docente: Prof. Me. Reginaldo Pereira Fernandes
# ==============================================================================
# Este script contém o roteiro completo de comandos do mongosh para estudo em casa.
# Você pode executá-lo diretamente ou copiar comando por comando no terminal mongosh.
# ==============================================================================

set -e

# Configurações de Conexão (Ajuste conforme seu ambiente: Docker, Atlas ou Local)
# Se estiver usando Docker local com credenciais:
MONGO_URI="${MONGO_URI:-mongodb://localhost:27017}"

echo "======================================================================"
echo " [IFCE TAUÁ] Laboratório CLI MongoDB: mongosh"
echo " Conectando a: $MONGO_URI"
echo "======================================================================"

mongosh "$MONGO_URI" --quiet << 'EOF'
// 1. CRIAÇÃO E SELEÇÃO DE BANCO DE DADOS
print("\n>>> 1. Selecionando a base de dados: ecommerce_taua");
use ecommerce_taua;

// Limpeza de coleções anteriores para garantir idempotência do laboratório
db.produtos.drop();
db.pedidos.drop();

// 2. CREATE (Inserção de Documentos - insertOne e insertMany)
print("\n>>> 2. Inserindo Documentos no Catálogo de Produtos (insertOne / insertMany)...");

// Inserção individual (insertOne)
db.produtos.insertOne({
  sku: "NOT-DEL-01",
  nome: "Notebook Dell Inspiron 15",
  categoria: "Informatica",
  preco: 4299.90,
  estoque: 14,
  especificacoes: {
    processador: "Intel Core i7 13ª Ger",
    memoria_gb: 16,
    ssd_gb: 512,
    sistema: "Ubuntu Linux 24.04"
  },
  tags: ["trabalho", "desenvolvimento", "bivolt"],
  ativo: true,
  cadastrado_em: new Date()
});

// Inserção em lote (insertMany)
db.produtos.insertMany([
  {
    sku: "MOU-LOG-02",
    nome: "Mouse Sem Fio Logitech MX Master 3S",
    categoria: "Perifericos",
    preco: 589.00,
    estoque: 25,
    especificacoes: { dpi: 8000, conexao: "Bluetooth / Bolt", bateria: "Recarregavel" },
    tags: ["ergonomia", "produtividade"],
    ativo: true,
    cadastrado_em: new Date()
  },
  {
    sku: "TEC-MEC-03",
    nome: "Teclado Mecanico Keychron K2 RGB",
    categoria: "Perifericos",
    preco: 699.50,
    estoque: 8,
    especificacoes: { switch: "Gateron Brown", layout: "ANSI 75%", conexao: "Hibrido" },
    tags: ["mecanico", "desenvolvimento", "mac_friendly"],
    ativo: true,
    cadastrado_em: new Date()
  },
  {
    sku: "MON-LG-04",
    nome: "Monitor Ultrawide LG 29 polegadas",
    categoria: "Monitores",
    preco: 1290.00,
    estoque: 6,
    especificacoes: { resolucao: "2560x1080", taxa_hz: 75, painel: "IPS" },
    tags: ["ultrawide", "produtividade"],
    ativo: true,
    cadastrado_em: new Date()
  },
  {
    sku: "CAB-USBC-05",
    nome: "Cabo USB-C Trancado 2 metros",
    categoria: "Acessorios",
    preco: 45.00,
    estoque: 50,
    especificacoes: { potencia_w: 100, dados: "480Mbps" },
    tags: ["carga_rapida", "acessorio"],
    ativo: false,
    cadastrado_em: new Date()
  }
]);

// 3. READ (Consultas, Projeções e Operadores de Comparação)
print("\n>>> 3. Executando Consultas Básicas e Avançadas (find)...");

print("\na) Listar todos os produtos com projeção (apenas nome, preco e sku):");
db.produtos.find(
  {},
  { _id: 0, sku: 1, nome: 1, preco: 1, categoria: 1 }
).forEach(printjson);

print("\nb) Filtrar periféricos com preço menor que R$ 650.00 ($lt):");
db.produtos.find(
  { categoria: "Perifericos", preco: { $lt: 650.00 } },
  { _id: 0, nome: 1, preco: 1 }
).forEach(printjson);

print("\nc) Filtrar produtos com tag 'desenvolvimento' em array ($in / correspondência de array):");
db.produtos.find(
  { tags: "desenvolvimento" },
  { _id: 0, nome: 1, tags: 1 }
).forEach(printjson);

print("\nd) Filtrar por atributo aninhado (especificacoes.memoria_gb >= 16):");
db.produtos.find(
  { "especificacoes.memoria_gb": { $gte: 16 } },
  { _id: 0, nome: 1, especificacoes: 1 }
).forEach(printjson);

// 4. UPDATE (Modificação com Operadores Atômicos $set, $inc, $push)
print("\n>>> 4. Atualizações Atômicas no Catálogo (updateOne / updateMany)...");

print("\na) Aplicar 10% de desconto no Notebook e adicionar tag 'promocao' ($set e $push):");
db.produtos.updateOne(
  { sku: "NOT-DEL-01" },
  {
    $set: { preco: 3869.91, em_promocao: true },
    $push: { tags: "promocao_outubro" }
  }
);

print("\nb) Incrementar estoque do Monitor em +4 unidades ($inc):");
db.produtos.updateOne(
  { sku: "MON-LG-04" },
  { $inc: { estoque: 4 } }
);

print("\nc) Exibir produto atualizado:");
printjson(db.produtos.findOne({ sku: "NOT-DEL-01" }, { _id: 0, nome: 1, preco: 1, estoque: 1, tags: 1 }));

// 5. DELETE (Remoção de Documentos - deleteOne / deleteMany)
print("\n>>> 5. Remoção de Documentos (deleteOne / deleteMany)...");

print("\na) Remover produtos inativos (ativo = false):");
let deleteResult = db.produtos.deleteMany({ ativo: false });
print("Documentos inativos removidos: " + deleteResult.deletedCount);

// 6. INDEXAÇÃO E MEDIÇÃO DE PERFORMANCE
print("\n>>> 6. Criando Índice Secundário na Categoria:");
db.produtos.createIndex({ categoria: 1 });
print("Indices na colecao produtos:");
printjson(db.produtos.getIndexes());

print("\nLaboratório CLI de MongoDB concluído com êxito!");
EOF
