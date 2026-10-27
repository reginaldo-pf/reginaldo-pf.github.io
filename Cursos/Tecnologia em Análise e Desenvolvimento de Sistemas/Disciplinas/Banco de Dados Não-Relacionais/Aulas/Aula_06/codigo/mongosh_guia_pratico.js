// ============================================================================
// IFCE CAMPUS TAUÁ - TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS (ADS)
// Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 06
// Docente: Prof. Me. Reginaldo Fernandes
// Arquivo: mongosh_guia_pratico.js
// Como executar: mongosh mongodb://localhost:27017/ecommerce_shopgrids mongosh_guia_pratico.js
// ============================================================================

print("\n======================================================================");
print(" 1. SELECIONANDO E LIMPANDO O BANCO DE DADOS 'ecommerce_shopgrids'");
print("======================================================================");

db = db.getSiblingDB("ecommerce_shopgrids");
db.dropDatabase();

// ----------------------------------------------------------------------------
// 2. GOVERNANÇA DE DADOS: CRIANDO A COLEÇÃO 'produtos' COM $jsonSchema
//    Garante que o núcleo do produto (sku, nome, categoria, preco > 0) seja
//    obrigatório, mas permite polimorfismo livre em 'especificacoes'.
// ----------------------------------------------------------------------------
print("\n======================================================================");
print(" 2. CRIANDO COLEÇÃO 'produtos' COM VALIDAÇÃO NATIVA ($jsonSchema)");
print("======================================================================");

db.createCollection("produtos", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["sku", "nome", "categoria", "preco", "estoque"],
      properties: {
        sku: {
          bsonType: "string",
          description: "Código único do produto (obrigatório)."
        },
        nome: {
          bsonType: "string",
          description: "Nome comercial do produto (obrigatório)."
        },
        categoria: {
          bsonType: "string",
          description: "Categoria de vitrine no ShopGrids."
        },
        preco: {
          bsonType: ["decimal", "double"],
          minimum: 0.01,
          description: "Preço unitário positivo em Decimal128 ou Double."
        },
        estoque: {
          bsonType: ["int", "long", "double"],
          minimum: 0,
          description: "Saldo de estoque não-negativo."
        },
        especificacoes: {
          bsonType: "object",
          description: "Subdocumento polimórfico (Embedding 1:1)."
        }
      }
    }
  }
});

// ----------------------------------------------------------------------------
// 3. POLIMORFISMO + EMBEDDING (1:1) + SUBSET PATTERN (Top Avaliações)
//    Inserindo produtos de categorias totalmente diferentes na mesma coleção!
// ----------------------------------------------------------------------------
print("\n======================================================================");
print(" 3. INSERINDO PRODUTOS POLIMÓRFICOS COM BSON (Decimal128 e ISODate)");
print("======================================================================");

const idNotebook = new ObjectId();
const idCamiseta = new ObjectId();
const idLivro = new ObjectId();

db.produtos.insertMany([
  {
    _id: idNotebook,
    sku: "NOTE-ACER-15",
    nome: "Notebook Gamer Acer Nitro V15",
    categoria: "Eletronicos",
    preco: NumberDecimal("4599.90"), // BSON Decimal128 (precisão financeira exata!)
    estoque: NumberInt(15),
    destaque_vitrine: true,
    // EMBEDDING 1:1 (Polimorfismo para Eletrônicos):
    especificacoes: {
      processador: "Intel Core i7-13620H",
      memoria_ram_gb: 16,
      armazenamento_ssd_gb: 512,
      gpu: "NVIDIA GeForce RTX 4050 6GB",
      tensao: "Bivolt"
    },
    // SUBSET PATTERN: guardamos o resumo e apenas as 2 avaliações mais recentes!
    resumo_avaliacoes: {
      nota_media: 4.9,
      total_avaliacoes: 2
    },
    ultimas_avaliacoes: [
      {
        autor: "Lucas Mendes",
        nota: NumberInt(5),
        comentario: "Excelente para rodar containers Docker e jogos pesados!",
        data: ISODate("2026-10-25T14:30:00Z")
      },
      {
        autor: "Marina Rocha",
        nota: NumberInt(5),
        comentario: "Tela 144Hz muito fluida e SSD super veloz.",
        data: ISODate("2026-10-26T18:15:00Z")
      }
    ],
    criado_em: new Date()
  },
  {
    _id: idCamiseta,
    sku: "CAM-NOSQL-IFCE",
    nome: "Camiseta Dev Polyglot Persistence IFCE",
    categoria: "Vestuario",
    preco: NumberDecimal("69.90"),
    estoque: NumberInt(80),
    destaque_vitrine: true,
    // EMBEDDING 1:1 (Polimorfismo para Vestuário — atributos completamente distintos!):
    especificacoes: {
      tecido: "100% Algodão Egípcio",
      cor: "Preta",
      tamanhos_disponiveis: ["P", "M", "G", "GG"],
      instrucoes_lavagem: ["Não usar alvejante", "Secar à sombra"]
    },
    resumo_avaliacoes: {
      nota_media: 5.0,
      total_avaliacoes: 1
    },
    ultimas_avaliacoes: [
      {
        autor: "Pedro Alves",
        nota: NumberInt(5),
        comentario: "Tecido muito confortável para maratonas de programação!",
        data: ISODate("2026-10-26T10:00:00Z")
      }
    ],
    criado_em: new Date()
  },
  {
    _id: idLivro,
    sku: "LIV-NOSQL-FOWLER",
    nome: "Livro NoSQL Essencial (Sadalage & Fowler)",
    categoria: "Livros",
    preco: NumberDecimal("94.50"),
    estoque: NumberInt(35),
    destaque_vitrine: false,
    // EMBEDDING 1:1 (Polimorfismo para Livros):
    especificacoes: {
      autores: ["Pramod J. Sadalage", "Martin Fowler"],
      editora: "Novatec",
      paginas: 216,
      isbn_13: "978-8575223383"
    },
    resumo_avaliacoes: {
      nota_media: 4.8,
      total_avaliacoes: 0
    },
    ultimas_avaliacoes: [],
    criado_em: new Date()
  }
]);

print("-> 3 produtos polimórficos inseridos com sucesso!");
print("-> Timestamp extraído dos 4 primeiros bytes do ObjectId do Notebook:", idNotebook.getTimestamp());

// ----------------------------------------------------------------------------
// 4. COLEÇÃO 'avaliacoes' (REFERENCING 1:Many para o Histórico Completo)
// ----------------------------------------------------------------------------
print("\n======================================================================");
print(" 4. POPULANDO COLEÇÃO 'avaliacoes' (REFERENCING 1:Many)");
print("======================================================================");

db.avaliacoes.insertMany([
  {
    produto_id: idNotebook, // Referência ao ObjectId do Produto
    sku_produto: "NOTE-ACER-15",
    autor: "Lucas Mendes",
    nota: NumberInt(5),
    comentario: "Excelente para rodar containers Docker e jogos pesados!",
    compra_verificada: true,
    data: ISODate("2026-10-25T14:30:00Z")
  },
  {
    produto_id: idNotebook,
    sku_produto: "NOTE-ACER-15",
    autor: "Marina Rocha",
    nota: NumberInt(5),
    comentario: "Tela 144Hz muito fluida e SSD super veloz.",
    compra_verificada: true,
    data: ISODate("2026-10-26T18:15:00Z")
  },
  {
    produto_id: idCamiseta,
    sku_produto: "CAM-NOSQL-IFCE",
    autor: "Pedro Alves",
    nota: NumberInt(5),
    comentario: "Tecido muito confortável para maratonas de programação!",
    compra_verificada: true,
    data: ISODate("2026-10-26T10:00:00Z")
  }
]);

// ----------------------------------------------------------------------------
// 5. COLEÇÃO 'clientes' (EMBEDDING 1:Few de Endereços)
// ----------------------------------------------------------------------------
print("\n======================================================================");
print(" 5. INSERINDO CLIENTE COM ENDEREÇOS EMBUTIDOS (EMBEDDING 1:Few)");
print("======================================================================");

const idClienteAna = new ObjectId();

db.clientes.insertOne({
  _id: idClienteAna,
  nome: "Ana Beatriz Costa",
  email: "ana.costa@aluno.ifce.edu.br",
  cpf: "123.456.789-00",
  telefone: "(88) 99999-1234",
  // EMBEDDING 1:Few: Um cliente tem poucos endereços (1 a 5) e eles são lidos juntos no checkout!
  enderecos: [
    {
      apelido: "Casa",
      logradouro: "Av. Chermont Alves de Oliveira, 100",
      bairro: "Tauazinho",
      cidade: "Tauá",
      uf: "CE",
      cep: "63660-000",
      principal: true
    },
    {
      apelido: "Campus IFCE",
      logradouro: "Rodovia CE-187, s/n",
      bairro: "Colibris",
      cidade: "Tauá",
      uf: "CE",
      cep: "63660-000",
      principal: false
    }
  ],
  criado_em: new Date()
});

print("-> Cliente Ana Beatriz inserida com 2 endereços embutidos!");

// ----------------------------------------------------------------------------
// 6. COLEÇÃO 'pedidos' (EXTENDED REFERENCE + SNAPSHOT PATTERN)
//    Congelamos o preço e o nome dos itens no instante da compra!
// ----------------------------------------------------------------------------
print("\n======================================================================");
print(" 6. REGISTRANDO PEDIDO COM EXTENDED REFERENCE E SNAPSHOT FISCAL");
print("======================================================================");

db.pedidos.insertOne({
  codigo_pedido: "PED-2026-0001",
  // Extended Reference: guardamos o _id do cliente + os campos vitais para a tela de pedidos
  cliente: {
    cliente_id: idClienteAna,
    nome: "Ana Beatriz Costa",
    cpf: "123.456.789-00"
  },
  // Snapshot do endereço de entrega (se o cliente mudar de casa no futuro, o histórico do pedido não muda!)
  endereco_entrega_snapshot: {
    logradouro: "Av. Chermont Alves de Oliveira, 100",
    bairro: "Tauazinho",
    cidade: "Tauá",
    uf: "CE",
    cep: "63660-000"
  },
  // Itens Embutidos com Referência ao Produto + Snapshot do Preço na Compra:
  itens: [
    {
      produto_id: idNotebook,
      sku: "NOTE-ACER-15",
      nome: "Notebook Gamer Acer Nitro V15",
      preco_unitario_na_compra: NumberDecimal("4599.90"),
      quantidade: NumberInt(1),
      subtotal: NumberDecimal("4599.90")
    },
    {
      produto_id: idCamiseta,
      sku: "CAM-NOSQL-IFCE",
      nome: "Camiseta Dev Polyglot Persistence IFCE",
      preco_unitario_na_compra: NumberDecimal("69.90"),
      quantidade: NumberInt(2),
      subtotal: NumberDecimal("139.80")
    }
  ],
  resumo_financeiro: {
    subtotal_itens: NumberDecimal("4739.70"),
    frete: NumberDecimal("0.00"),
    valor_total_pago: NumberDecimal("4739.70"),
    metodo_pagamento: "PIX"
  },
  status: "PAGO",
  criado_em: new Date()
});

print("-> Pedido PED-2026-0001 gravado com sucesso!");

// ----------------------------------------------------------------------------
// 7. PROVA DO SNAPSHOT PATTERN: REAJUSTANDO O PREÇO DO NOTEBOOK NO CATÁLOGO
// ----------------------------------------------------------------------------
print("\n======================================================================");
print(" 7. TESTE DE INTEGRIDADE: SUBINDO PREÇO DO NOTEBOOK PARA R$ 5.299,90");
print("======================================================================");

db.produtos.updateOne(
  { _id: idNotebook },
  { $set: { preco: NumberDecimal("5299.90") } }
);

const prodAtual = db.produtos.findOne({ _id: idNotebook });
const pedidoSalvo = db.pedidos.findOne({ codigo_pedido: "PED-2026-0001" });

print("-> Preço ATUAL na vitrine (db.produtos): R$", prodAtual.preco.toString());
print("-> Preço HISTÓRICO congelado na Nota Fiscal (db.pedidos): R$", pedidoSalvo.itens[0].preco_unitario_na_compra.toString());
print("======================================================================\n");
