# 🔒 Roteiro do Professor: Aula 06 — Do CRUD Básico e Python (`PyMongo`) à Modelagem de Documentos BSON

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá
* **Disciplina:** Banco de Dados Não-Relacionais (ADS16)
* **Docente:** Prof. Me. Reginaldo Fernandes
* **Arquivos de Apoio:** `materiais/main.pdf` (26 slides), `tutorial_construcao_passo_a_passo.md` e pasta `codigo/`.

---

## Bloco 1: Fundamentos Teóricos — RDBMS, Documentos e BSON (Slides 1 a 7)

### Slides 1 a 5: Do RDBMS ao Modelo de Documentos e Ferramentas
* Apresentar por que os bancos relacionais aplicam as Formas Normais (1NF a 5NF): evitar redundâncias e anomalias de atualização (*Update Anomalies*), ao custo de múltiplos `JOINs` pesados na leitura.
* Mostrar que no MongoDB a unidade básica é o **Documento BSON** (até **100 níveis** de aninhamento e **16 MB**), permitindo agrupar dados relacionados em subdocumentos e arrays.
* Destacar na tabela comparativa os conceitos (`Database`, `Collection`, `Document`, `Field`, `_id`) e as três ferramentas oficiais que usaremos na aula: **MongoDB Compass (GUI)**, **`mongosh`** e o driver **Python (`PyMongo`)**.

### Slides 6 e 7: Os 3 Pilares do BSON, `ObjectId` e Extended JSON no Compass
* Explicar as **3 características de projeto do BSON**:
  1. **Lightweight (Leve):** Baixa sobrecarga espacial.
  2. **Traversable (Percorrível):** Cabeçalhos com tamanho em bytes permitem saltar campos em $\mathcal{O}(1)$ sem ler caractere por caractere.
  3. **Efficient (Eficiente):** Codificação/decodificação rápida em tipos binários nativos (`ObjectId` de 12 bytes, `Decimal128` para moeda sem erro de ponto flutuante, `ISODate`, `Int32`, `Int64`).
* Mostrar a diferença prática para não dar erro no Compass: na janela **Insert Document (`VIEW {}`)** do Compass, usamos **Extended JSON** com chaves entre aspas duplas (`"_id": { "$oid": "..." }`, `"preco": { "$numberDecimal": "..." }`).

---

## Bloco 2: Aprendendo do Zero — CRUD Passo a Passo no Compass e `mongosh` (Slides 8 a 12)

### Slide 9: Criando o Banco `mongodb_books` e Consultando as Coleções
1. Abrir o **MongoDB Compass** (`mongodb://localhost:27017`).
2. Clicar em **`+` (*Create database*)** no menu esquerdo:
   * **Database Name:** `mongodb_books`
   * **Collection Name:** `books`
3. **Consultar a lista de coleções no Compass:** Clicar em `mongodb_books` no menu lateral e mostrar `books` listada na aba **Collections** (e mostrar o comando equivalente `show dbs`, `use mongodb_books`, `show collections` / `db.getCollectionNames()` no `mongosh`).

### Slide 10: Inserindo (`insertOne`) e Consultando (`find`) o 1.º Documento
1. Abrir a coleção **`books`**, clicar em **Add Data $\to$ Insert Document** e colar o 1.º livro:
   ```json
   {
     "isbn": "101",
     "name": "MongoDB 7.0 Guia Pratico",
     "price": 30
   }
   ```
2. **Consultar a lista de documentos no Compass:** Mostrar o `_id: ObjectId(...)` gerado automaticamente e alternar entre as visões **List**, **JSON** e **Table**.

### Slide 11: Subdocumento `meta` e Busca com *Dot Notation*, `$gt` e `$regex`
1. Em **Add Data $\to$ Insert Document**, inserir o livro de ISBN `"201"` com o subdocumento `"meta": { "version": "MongoDB 6.0" }` e o livro `"202"` com `"meta": { "version": "MongoDB 7.0" }`.
2. **Consultar a lista de documentos no Compass**, expandir `meta: Object` e testar na barra **Filter** do Compass:
   * `{ "isbn": "101" }`
   * `{ "meta.version": "MongoDB 6.0" }` (*Dot Notation*)
   * `{ "price": { "$gt": 35 } }`
   * `{ "name": { "$regex": "mongo", "$options": "i" } }`
3. Clicar em **Reset** na barra *Filter*.

### Slide 12: Atualizando (`updateOne` / `$set`), Removendo (`deleteOne`) e Lote (`bulkWrite`)
1. Editar o preço do livro `"101"` para `45` clicando no ícone de lápis (**Edit Document**) no Compass e **consultar a lista de documentos** (destacando o retorno `matchedCount: 1, modifiedCount: 1` do `updateOne` com `$set`).
2. Excluir o livro `"201"` clicando no ícone de lixeira (**Delete Document**) no Compass e **consultar a lista de documentos**.

---

## Bloco 3: CRUD Passo a Passo com Python (`PyMongo`) (Slides 13 a 16)

### Slides 14 a 16: Executando o Script `crud_pymongo.py`
1. Mostrar nos slides como o `PyMongo` conecta com `MongoClient("mongodb://localhost:27017/")`, testa com `client.admin.command("ping")` e manipula dicionários Python com:
   * `books.insert_one(...)` (ISBN `"301"`) e `books.insert_many(...)` (ISBN `"302"` e `"303"`).
   * `books.find(...)` com filtro simples, *dot notation* + `$regex` (`"meta.version"`), comparação (`"$gt": 50`), condição `AND` e operador `"$or"`.
   * `books.update_one(..., {"$set": {"price": 75}})`, `books.delete_one({"isbn": "303"})` e `books.bulk_write(...)`.
2. Executar no terminal:
   ```bash
   cd codigo
   python3 crud_pymongo.py
   ```
3. Voltar ao **MongoDB Compass**, clicar em **Refresh** na coleção `books` (e também inspecionar as coleções `users`, `professors` e `courses` criadas pelo script) para **consultar a lista de coleções e documentos**.

---

## Bloco 4: Teoria de Schema Design e Construção do `ecommerce_shopgrids` (Slides 17 a 26)

### Slides 17 a 20: *Embedding*, *Referencing*, *Read-Write Ratio* e Padrões de Modelagem
* Explicar as 3 estratégias de modelagem (*Embedded Data*, *References*, *Denormalization*) e a métrica **Read-Write Ratio**.
* Analisar o diagrama comparativo no Slide 19 e a tabela de padrões no Slide 20 (*Polymorphic*, *Subset*, *Extended Reference*, *Computed*) além do risco de *Unbounded Arrays* (limite de **16 MB**).

### Slide 22: Criando `ecommerce_shopgrids` e a Coleção `produtos` no Compass
1. No Compass, clicar em **`+` (*Create database*)**:
   * **Database Name:** `ecommerce_shopgrids`
   * **Collection Name:** `produtos`
2. **Consultar a lista de coleções no Compass** clicando em `ecommerce_shopgrids`.
3. Em `produtos`, inserir manualmente via **Add Data $\to$ Insert Document** o 1.º produto (`NOTE-ACER-15`, Eletrônicos), **consultar a lista de documentos**, inserir o 2.º produto (`CAM-TECH-ADS`, Vestuário), **consultar a lista de documentos** e aplicar a regra `$jsonSchema` na aba **Validation**.

### Slides 23 e 24: Coleções `clientes`, `avaliacoes` e `pedidos` Passo a Passo no Compass
1. **Coleção `clientes`:** Criar a coleção `clientes` $\to$ **consultar a lista de coleções** $\to$ inserir manualmente o 1.º registro (`Ana Costa` com array `enderecos`) $\to$ **consultar a lista de documentos no Compass**.
2. **Coleção `avaliacoes`:** Criar a coleção `avaliacoes` $\to$ **consultar a lista de coleções** $\to$ inserir manualmente a 1.ª avaliação referenciada (`produto_id` apontando para o Notebook) $\to$ **consultar a lista de documentos no Compass**.
3. **Coleção `pedidos`:** Criar a coleção `pedidos` $\to$ **consultar a lista de coleções** $\to$ inserir manualmente o 1.º pedido (`PED-2026-0001` com `cliente` e `itens` congelando `preco_unit: 4599.90`) $\to$ **consultar a lista de documentos no Compass** e demonstrar a edição do preço do Notebook em `produtos` sem afetar a nota fiscal em `pedidos`.

### Slide 25: Exercício Final — Povoamento em Lote
* Orientar os alunos a importar os lotes JSON no Compass (**Add Data $\to$ Import JSON or CSV file**: `produtos_lote.json`, `clientes_lote.json`, `avaliacoes_lote.json`, `pedidos_lote.json`) ou executar `python3 popular_catalogo_mongodb.py`, consultando a lista de documentos de cada coleção no Compass ao finalizar.
