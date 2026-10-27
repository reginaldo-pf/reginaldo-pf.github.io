# Guia Passo a Passo: Do CRUD Básico e Python (`PyMongo`) à Modelagem de Documentos no MongoDB

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá
* **Disciplina:** Banco de Dados Não-Relacionais (ADS16) — Aula 06
* **Docente:** Prof. Me. Reginaldo Fernandes

---

## Parte 1: Fundamentos Teóricos — Do RDBMS ao Modelo de Documentos e BSON

### 1.1 Por que Normalizamos no SQL e Como o MongoDB Modela Dados
Nos bancos de dados relacionais (RDBMS), armazenar dados de entidades relacionadas em uma única tabela gera **redundância de dados** e **anomalias de atualização (*Update Anomalies*)**: se um aluno participa de três cursos e seu endereço muda, é necessário atualizar três linhas diferentes; se uma linha falhar, o banco fica inconsistente. Para evitar isso, o modelo relacional aplica as **Formas Normais (1NF a 5NF)**, dividindo os dados em várias tabelas conectadas por chaves estrangeiras (`FOREIGN KEY`) e recompondo-os na leitura por meio de cláusulas `JOIN`.

No **MongoDB**, a unidade básica de armazenamento não é uma linha plana de tabela, mas um **Documento BSON** capaz de conter subdocumentos (objetos aninhados) e listas (*arrays*) com até **100 níveis de profundidade** e tamanho máximo de **16 MB por documento**. Em vez de fragmentar uma entidade em diversas tabelas, agrupamos os dados que são lidos juntos pela aplicação em um mesmo documento autocontido.

| Conceito Relacional (SQL) | Equivalente no MongoDB | Papel na Arquitetura |
| :--- | :--- | :--- |
| `Database` | `Database` | Agrupador lógico de coleções (`mongodb_books`, `ecommerce_shopgrids`). |
| `Table` (Tabela) | `Collection` (Coleção) | Conjunto de documentos com esquema dinâmico (`books`, `produtos`, `pedidos`). |
| `Row / Tuple` (Linha) | `Document` (Documento BSON) | Objeto estruturado (até **16 MB** e **100 níveis** de aninhamento). |
| `Column` (Coluna) | `Field` (Campo) | Par `chave: valor` (suporta tipos escalares, subdocumentos e arrays). |
| `Primary Key` (PK) | Campo `_id` | Identificador único obrigatório na coleção (por padrão, `ObjectId` de 12 bytes). |
| `JOIN` | **Embedding** / `$lookup` | Incorporação direta de subdocumentos/arrays ou junção em pipeline de agregação. |

---

### 1.2 As Três Características do BSON e Seus Tipos de Dados
Embora escrevamos documentos usando a sintaxe JSON, o motor de armazenamento **WiredTiger** do MongoDB persiste e trafega dados em **BSON (*Binary JSON*)**. O formato BSON foi desenhado sobre três pilares:
1. **Lightweight (Leve):** Mantém a sobrecarga espacial mínima, ideal para tráfego em rede e armazenamento em disco.
2. **Traversable (Percorrível):** Diferente do JSON textual (que exige ler caractere por caractere para encontrar um campo), o BSON grava prefixos de tamanho em bytes no início de cada campo e subdocumento, permitindo ao motor saltar diretamente para o campo desejado sem fazer *parse* do restante do documento.
3. **Efficient (Eficiente):** A codificação para BSON e a decodificação de volta para estruturas nativas da linguagem (como dicionários Python) ocorrem em altíssima velocidade usando tipos binários de máquina.

#### Principais Tipos BSON e Anatomia do `ObjectId` (12 Bytes)
* **`ObjectId` (12 bytes):** Composto por **4 bytes de *timestamp*** (segundos desde a Unix Epoch, permitindo ordenar documentos cronologicamente pelo próprio `_id`), **5 bytes aleatórios** (únicos por máquina/processo) e **3 bytes de contador incremental**. Pode ser gerado no cliente Python sem trava centralizada (*lock*) no servidor.
* **Tipos Numéricos:** `Int32` (inteiro de 32 bits), `Int64 / Long` (inteiro de 64 bits), `Double` (ponto flutuante IEEE 754 de 64 bits) e **`Decimal128`** (decimal de 128 bits com precisão exata, indispensável para valores monetários e fiscais onde `0.1 + 0.2` não pode sofrer imprecisão binária).
* **Outros Tipos Nativo-Binários:** `String` (UTF-8), `Object` (subdocumento embutido), `Array` (lista), `Boolean` (`true`/`false`), `Date` (`ISODate` em milissegundos UTC), `Null`, `Regular Expression` (PCRE) e `Binary Data` (`BinData`).

> **Diferença de Sintaxe entre o MongoDB Compass (`VIEW {}`) e o Terminal `mongosh`:**
> * Na janela **Insert Document** do **MongoDB Compass**, o editor utiliza o analisador **JSON estrito (*Extended JSON*)**: todas as chaves devem estar entre **aspas duplas** (`"isbn"`, `"price"`) e tipos BSON específicos são escritos como objetos JSON (`{"$oid": "..."}`, `{"$numberDecimal": "4599.90"}`).
> * Já no terminal **`mongosh`** (e na barra *Filter* do Compass), o ambiente é um interpretador JavaScript (Node.js REPL), que aceita chaves sem aspas e construtores como `ObjectId("...")` e `NumberDecimal("...")`.

---

## Parte 2: Aprendendo do Zero — CRUD Passo a Passo no Compass e no `mongosh`

Antes de modelarmos múltiplas coleções, vamos aprender a operar o MongoDB **do zero, passo a passo**, utilizando o banco `mongodb_books` e a coleção `books`.

### Passo 1: Conectando, Criando o Banco `mongodb_books` e Consultando as Coleções

1. Certifique-se de que o contêiner do MongoDB está em execução na porta `27017`:
   ```bash
   cd codigo
   docker compose up -d
   ```
2. Abra o **MongoDB Compass** e conecte em `mongodb://localhost:27017`.
3. No painel lateral esquerdo (*Databases*), clique no botão **`+` (*Create database*)**.
4. Preencha os campos:
   * **Database Name:** `mongodb_books`
   * **Collection Name:** `books`
5. Clique em **Create Database**.

#### Consultando a Lista de Coleções no Compass
* Clique sobre o banco **`mongodb_books`** no menu lateral esquerdo do Compass.
* Na aba central **Collections**, verifique que a coleção **`books`** aparece listada com `0` documentos.

#### Equivalente no Terminal `mongosh`
Se quiser acompanhar simultaneamente no terminal interativo (ou na aba `_MONGOSH` na base do Compass):
```javascript
// Listar todos os bancos de dados com dados gravados:
show dbs

// Selecionar o banco mongodb_books:
use mongodb_books

// Consultar a lista de colecoes do banco atual:
show collections
// Equivalente em JavaScript puro:
db.getCollectionNames()
```

---

### Passo 2: Inserindo Manualmente o Primeiro Documento (*Create* — `insertOne`)

#### Exemplo 1: Cadastrando o Primeiro Livro no Compass
1. No menu lateral esquerdo do Compass, clique na coleção **`books`** (dentro de `mongodb_books`).
2. Clique no botão verde **Add Data $\to$ Insert Document**.
3. Apague o conteúdo padrão da janela, cole o JSON abaixo e clique em **Insert**:

```json
{
  "isbn": "101",
  "name": "MongoDB 7.0 Guia Pratico",
  "price": 30
}
```

#### Consultando a Lista de Documentos no Compass
* Observe a aba **Documents** da coleção `books`: o documento foi gravado e o MongoDB gerou automaticamente a chave primária `_id: ObjectId("...")`!
* No canto superior direito da lista de documentos, alterne entre os três modos de visualização do Compass: **List** (árvore visual), **JSON** (documento Extended JSON) e **Table** (visão tabular).

#### Equivalente no `mongosh`
```javascript
db.books.insertOne({
  isbn: "101",
  name: "MongoDB 7.0 Guia Pratico",
  price: 30
})
// Retorno do servidor:
// { acknowledged: true, insertedId: ObjectId("...") }

// Consultar todos os documentos da colecao books:
db.books.find()
```

---

### Passo 3: Inserindo Subdocumentos (`meta`) e Filtrando com *Dot Notation* (*Read* — `find`)

No MongoDB, um campo pode conter outro documento inteiro (subdocumento embutido). Vamos inserir documentos que possuem o subdocumento `meta`.

#### Exemplo 2: Inserindo Livros com Subdocumento `meta` no Compass
1. Na coleção **`books`**, clique em **Add Data $\to$ Insert Document**.
2. Cole o documento abaixo e clique em **Insert**:

```json
{
  "isbn": "201",
  "name": "Modelagem de Documentos NoSQL",
  "meta": {
    "version": "MongoDB 6.0"
  },
  "price": 50
}
```

3. Clique mais uma vez em **Add Data $\to$ Insert Document**, cole o terceiro livro e clique em **Insert**:

```json
{
  "isbn": "202",
  "name": "Arquitetura de Bancos NoSQL",
  "meta": {
    "version": "MongoDB 7.0"
  },
  "price": 60
}
```

#### Consultando a Lista de Documentos e Filtrando no Compass
1. Na aba **Documents** da coleção `books`, verifique que agora existem **3 documentos** listados. Clique na seta ao lado de `meta: Object` para expandir o campo interno `version`.
2. Na barra **Filter** no topo da aba *Documents* do Compass, teste cada uma das consultas abaixo (clique em **Find** após digitar cada filtro):
   * **Busca por campo de primeiro nível:**
     ```json
     { "isbn": "101" }
     ```
   * **Busca em subdocumento usando *Dot Notation* (Notação de Ponto):** Para consultar um campo dentro de um objeto aninhado, juntamos o nome do objeto pai e do campo filho com um ponto (`"meta.version"` entre aspas):
     ```json
     { "meta.version": "MongoDB 7.0" }
     ```
   * **Busca com operador de comparação (`$gt` = maior que):**
     ```json
     { "price": { "$gt": 40 } }
     ```
   * **Busca com Expressão Regular PCRE case-insensitive (`$regex`):**
     ```json
     { "name": { "$regex": "nosql", "$options": "i" } }
     ```
3. Ao terminar os testes de filtro, clique no botão **Reset** na barra *Filter* para voltar a listar todos os 3 documentos da coleção `books`.

---

### Passo 4: Atualizando Documentos (*Update* — `updateOne` e `$set`)

Para modificar campos específicos de um documento sem sobrescrever o documento inteiro, utilizamos o operador atômico **`$set`**.

#### Exemplo 3: Atualizando o Preço de um Livro no Compass e no `mongosh`
1. **No MongoDB Compass:**
   * Na lista de documentos da coleção **`books`**, passe o mouse sobre o livro de `"isbn": "101"` e clique no ícone de lápis (**Edit Document**).
   * Dê duplo clique no valor `30` do campo `price`, altere para `45` e clique no botão amarelo **Update**.
   * **Consulte a lista de documentos** na aba *Documents* para confirmar que o preço foi alterado para `45`.
2. **Equivalente no `mongosh`:**
   ```javascript
   db.books.updateOne(
     { isbn: "101" },          // 1.º argumento: filtro de busca
     { $set: { price: 45 } }   // 2.º argumento: operador $set com o novo valor
   )
   ```
   O MongoDB retorna um documento de confirmação explicando exatamente o que ocorreu:
   ```javascript
   {
     acknowledged: true,
     insertedId: null,
     matchedCount: 1,   // Quantos documentos atenderam ao filtro { isbn: "101" }
     modifiedCount: 1,  // Quantos documentos tiveram seu valor efetivamente alterado
     upsertedCount: 0
   }
   ```
   *(Se você rodar exatamente o mesmo comando `updateOne` uma segunda vez seguida com `price: 45`, `matchedCount` será `1`, mas `modifiedCount` será `0`, pois o valor já era `45`!)*

---

### Passo 5: Removendo Documentos (*Delete* — `deleteOne`)

#### Exemplo 4: Excluindo um Documento no Compass e no `mongosh`
1. **No MongoDB Compass:**
   * Na coleção **`books`**, passe o mouse sobre o livro de `"isbn": "201"` e clique no ícone de lixeira (**Delete Document**).
   * Confirme clicando no botão vermelho **Delete**.
   * **Consulte a lista de documentos** na aba *Documents*: verifique que restaram apenas os livros de ISBN `"101"` e `"202"`.
2. **Equivalente no `mongosh`:**
   ```javascript
   // Remove apenas o primeiro documento que corresponder ao filtro:
   db.books.deleteOne({ isbn: "201" })
   // Retorno: { acknowledged: true, deletedCount: 1 }

   // Para remover multiplos documentos que atendam a um filtro:
   // db.books.deleteMany({ price: { $lt: 20 } })
   ```

---

## Parte 3: Operações CRUD com o Driver Oficial Python (`PyMongo`)

Agora que dominamos o fluxo visual no Compass e no `mongosh`, vamos realizar as operações CRUD usando a linguagem **Python** e o driver oficial **`PyMongo`**.

> Você pode executar todo o código abaixo rodando o script pronto `codigo/crud_pymongo.py`:
> ```bash
> cd codigo
> python3 crud_pymongo.py
> ```

### Passo 1: Conectando ao MongoDB com `MongoClient` e Testando com `ping`

```python
from pprint import pprint
from pymongo import MongoClient

# Conecta ao servidor MongoDB local na porta 27017:
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

# Envia um comando 'ping' ao banco admin para confirmar a conexao:
try:
    client.admin.command("ping")
    print("Conectado ao MongoDB com sucesso!")
except Exception as e:
    print("Erro de conexao:", e)

# Seleciona o banco 'mongodb_books' e a colecao 'books':
books = client.mongodb_books.books
```

---

### Passo 2: Inserindo Documentos com `insert_one` e `insert_many`

No `PyMongo`, documentos BSON são representados diretamente como **dicionários Python (`dict`)**:

```python
# 1. Inserindo um unico documento com insert_one():
book = {
    "isbn": "301",
    "name": "Python and MongoDB",
    "meta": {"version": "MongoDB 7.0"},
    "price": 60
}
insert_result = books.insert_one(book)
print("ObjectId gerado pelo insert_one:", insert_result.inserted_id)

# 2. Inserindo mais dois livros para consultas comparativas:
books.insert_many([
    {
        "isbn": "302",
        "name": "Python and MongoDB",
        "meta": {"version": "MongoDB 7.0"},
        "price": 60
    },
    {
        "isbn": "303",
        "name": "Advanced MongoDB Techniques",
        "price": 70
    }
])
```

#### Consultando a Lista de Documentos no Compass
* Volte à janela do **MongoDB Compass**, abra a coleção **`books`** em `mongodb_books` e clique no botão **Refresh** (ícone de atualizar ao lado do botão *Reset*): os livros de ISBN `"301"`, `"302"` e `"303"` inseridos pelo Python aparecerão imediatamente na tela!

---

### Passo 3: Consultando Documentos no Python (`find`, *Dot Notation*, `$regex`, `$gt`, `AND` e `$or`)

```python
# 1. Busca por atributo de primeiro nivel:
print("\n--- 1. Livros com name = 'Python and MongoDB' ---")
for document in books.find({"name": "Python and MongoDB"}):
    pprint(document)

# 2. Busca em subdocumento com Dot Notation ('meta.version') e $regex:
print("\n--- 2. Busca no subdocumento meta.version com $regex ---")
query_regex = {
    "meta.version": {
        "$regex": r".*?g.*?7\.0$",
        "$options": "i"
    }
}
for document in books.find(query_regex):
    pprint(document)

# 3. Operador de comparacao $gt (price > 50):
print("\n--- 3. Livros com price > 50 ($gt) ---")
for document in books.find({"price": {"$gt": 50}}):
    pprint(document)

# 4. Condicao logica AND (multiplas chaves no mesmo dicionario):
print("\n--- 4. Condicao logica AND ---")
query_and = {
    "name": "Advanced MongoDB Techniques",
    "price": 70
}
for document in books.find(query_and):
    pprint(document)

# 5. Condicao logica OR ($or):
print("\n--- 5. Condicao logica $or (Advanced MongoDB Techniques OU isbn 301) ---")
query_or = {
    "$or": [
        {"name": "Advanced MongoDB Techniques"},
        {"isbn": "301"}
    ]
}
for document in books.find(query_or):
    pprint(document)
```

---

### Passo 4: Atualizando (`update_one`) e Removendo (`delete_one`) no Python

```python
# 1. Atualizando o preco de "Advanced MongoDB Techniques" para 75:
update_result = books.update_one(
    {"name": "Advanced MongoDB Techniques"},
    {"$set": {"price": 75}}
)
print("\nResultado do update_one:", update_result.raw_result)

# Buscando o documento com find_one() para verificar a alteracao:
updated_document = books.find_one({"name": "Advanced MongoDB Techniques"})
pprint(updated_document)

# 2. Removendo o livro de ISBN '303' com delete_one():
isbn_to_delete = "303"
delete_result = books.delete_one({"isbn": isbn_to_delete})
print("\nResultado do delete_one:", delete_result.raw_result)
```

#### Consultando a Lista de Documentos no Compass
* Clique em **Refresh** na coleção **`books`** do Compass e verifique que o livro de ISBN `"303"` foi removido pelo script Python!

---

## Parte 4: Modelagem de Dados (*Schema Design*) Passo a Passo no Compass

Modelar um banco orientado a documentos exige combinar três técnicas fundamentais de acordo com a **proporção de leitura vs. escrita (*Read-Write Ratio*)** e a cardinalidade dos dados:
1. **Incorporação (*Embedded Data*):** Aninhar objetos ou listas dentro do documento pai (ideal para relações `1:1` e `1:Poucos`, quando os dados são sempre lidos juntos na mesma tela).
2. **Referenciamento (*References*):** Armazenar o `ObjectId` de um documento em outra coleção (ideal para relações `1:Muitos`, `1:Milhões` e `N:N`, evitando que arrays cresçam sem limite e estourem os **16 MB** do BSON).
3. **Desnormalização e Padrões de Projeto (*Design Patterns*):**
   * **Polymorphic Pattern:** Documentos de categorias diferentes compartilhando uma coleção com um núcleo comum de campos e subdocumentos específicos.
   * **Subset Pattern:** Embutir apenas as últimas avaliações no produto e guardar o histórico completo em outra coleção.
   * **Computed Pattern:** Armazenar métricas pré-calculadas (como média e total de avaliações) junto ao documento para evitar recálculos a cada leitura.
   * **Extended Reference + Snapshot Pattern:** Copiar no pedido apenas os campos essenciais do cliente e congelar o preço unitário do produto no momento da compra.

Vamos construir agora o banco **`ecommerce_shopgrids`** no **MongoDB Compass**, criando cada coleção, consultando a lista de coleções, inserindo manualmente o primeiro registro e consultando os documentos!

---

### 4.1 Criando o Banco `ecommerce_shopgrids` e a Coleção `produtos`

1. No painel lateral esquerdo do **MongoDB Compass**, clique no botão **`+` (*Create database*)**.
2. Preencha:
   * **Database Name:** `ecommerce_shopgrids`
   * **Collection Name:** `produtos`
3. Clique em **Create Database**.

#### Consultando a Lista de Coleções no Compass
* Clique sobre o banco **`ecommerce_shopgrids`** no menu lateral esquerdo do Compass e verifique na aba **Collections** que a coleção **`produtos`** foi criada com `0` documentos.

#### Exemplo 1: Inserindo Manualmente o Primeiro Produto (Categoria Eletrônicos)
1. Clique na coleção **`produtos`** e selecione **Add Data $\to$ Insert Document**.
2. Apague o conteúdo padrão, cole o JSON abaixo e clique em **Insert**:

```json
{
  "_id": { "$oid": "671ec880a1b2c3d4e5f60001" },
  "sku": "NOTE-ACER-15",
  "nome": "Notebook Gamer Nitro V15",
  "categoria": "Eletronicos",
  "preco": { "$numberDecimal": "4599.90" },
  "estoque": 15,
  "especificacoes": {
    "cpu": "Intel Core i7-13620H",
    "ram_gb": 16,
    "gpu": "RTX 4050 6GB"
  },
  "garantia_meses": 12
}
```

#### Consultando a Lista de Documentos no Compass
* Na aba **Documents** da coleção `produtos`, visualize o Notebook inserido, expanda `especificacoes: Object` e observe os tipos `ObjectId` e `Decimal128` nas visões **List**, **JSON** e **Table**.

#### Exemplo 2: Inserindo Manualmente o Segundo Produto Polimórfico (Categoria Vestuário)
1. Ainda na coleção **`produtos`**, clique em **Add Data $\to$ Insert Document**.
2. Cole o JSON da camiseta e clique em **Insert**:

```json
{
  "_id": { "$oid": "671ec880a1b2c3d4e5f60002" },
  "sku": "CAM-TECH-ADS",
  "nome": "Camiseta Dev NoSQL IFCE",
  "categoria": "Vestuario",
  "preco": { "$numberDecimal": "69.90" },
  "estoque": 80,
  "especificacoes": {
    "tecido": "100% Algodao Egipcio",
    "cor": "Preta",
    "tamanhos": ["P", "M", "G", "GG"]
  },
  "lavagem": ["Nao usar alvejante"]
}
```

#### Consultando a Lista de Documentos no Compass
* Na aba **Documents** de `produtos`, compare os 2 documentos lado a lado: ambos possuem `sku`, `nome`, `categoria`, `preco` e `estoque`, mas `especificacoes` se adapta ao tipo de produto (*Polymorphic Pattern*).

#### Exemplo 3: Adicionando Validação de Esquema no Compass
1. Clique na aba superior **Validation** da coleção **`produtos`**.
2. Clique em **Add Rule**, cole o esquema abaixo e clique em **Update**:

```json
{
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["sku", "nome", "preco"],
    "properties": {
      "sku": { "bsonType": "string" },
      "nome": { "bsonType": "string" },
      "preco": { "bsonType": ["decimal", "double"], "minimum": 0.01 },
      "especificacoes": { "bsonType": "object" }
    }
  }
}
```

---

### 4.2 Coleção `clientes`: Incorporação de Endereços (*Embedded Data 1:Few*)

#### Criando a Coleção `clientes` e Consultando as Coleções
1. No menu lateral esquerdo do Compass, passe o mouse sobre **`ecommerce_shopgrids`** e clique no botão **`+` (*Create collection*)**.
2. Digite `clientes` e clique em **Create Collection**.
3. Clique sobre o banco **`ecommerce_shopgrids`** no menu lateral para **consultar a lista de coleções** na aba **Collections**: confirme que agora aparecem `produtos` (2 documentos) e `clientes` (0 documentos).

#### Exemplo: Inserindo Manualmente o Primeiro Cliente com Endereços Embutidos
1. Abra a coleção **`clientes`** e clique em **Add Data $\to$ Insert Document**.
2. Cole o JSON abaixo e clique em **Insert**:

```json
{
  "_id": { "$oid": "671ec880a1b2c3d4e5f60010" },
  "nome": "Ana Costa",
  "email": "ana.costa@aluno.ifce.edu.br",
  "cpf": "123.456.789-00",
  "enderecos": [
    {
      "apelido": "Casa",
      "rua": "Av. Chermont, 100",
      "cidade": "Taua-CE"
    },
    {
      "apelido": "IFCE",
      "rua": "CE-187, Taua-CE",
      "cidade": "Taua-CE"
    }
  ]
}
```

#### Consultando a Lista de Documentos no Compass
* Na aba **Documents** de `clientes`, expanda `enderecos: Array (2)` e os itens `0: Object` e `1: Object`.
* Na barra **Filter** do Compass, consulte usando *dot notation* em arrays: `{ "enderecos.apelido": "IFCE" }` e clique em **Find**.

---

### 4.3 Coleção `avaliacoes`: *Referencing (1:Many)*, *Subset Pattern* e *Computed Pattern*

#### Criando a Coleção `avaliacoes` e Consultando as Coleções
1. Clique no botão **`+` (*Create collection*)** ao lado de **`ecommerce_shopgrids`**.
2. Digite `avaliacoes` e clique em **Create Collection**.
3. Clique em **`ecommerce_shopgrids`** para **consultar a lista de coleções** no Compass: verifique que constam `produtos`, `clientes` e `avaliacoes`.

#### Exemplo: Inserindo Manualmente a Primeira Avaliação Referenciada
1. Abra a coleção **`avaliacoes`** e clique em **Add Data $\to$ Insert Document**.
2. Cole o JSON abaixo (referenciando o `_id` do Notebook em `produto_id`) e clique em **Insert**:

```json
{
  "_id": { "$oid": "671ec990a1b2c3d4e5f60999" },
  "produto_id": { "$oid": "671ec880a1b2c3d4e5f60001" },
  "autor": "Lucas",
  "nota": 5,
  "txt": "Otimo!"
}
```

#### Consultando a Lista de Documentos no Compass
* Na aba **Documents** da coleção `avaliacoes`, verifique o documento inserido e o campo `produto_id: ObjectId('671ec880a1b2c3d4e5f60001')`.

---

### 4.4 Coleção `pedidos`: *Extended Reference* e *Snapshot Pattern*

#### Criando a Coleção `pedidos` e Consultando as Coleções
1. Clique no botão **`+` (*Create collection*)** ao lado de **`ecommerce_shopgrids`**.
2. Digite `pedidos` e clique em **Create Collection**.
3. Clique em **`ecommerce_shopgrids`** para **consultar a lista de coleções** no Compass: confirme que as 4 coleções (`produtos`, `clientes`, `avaliacoes` e `pedidos`) estão criadas.

#### Exemplo: Inserindo Manualmente o Primeiro Pedido com Snapshot Fiscal
1. Abra a coleção **`pedidos`** e clique em **Add Data $\to$ Insert Document**.
2. Cole o JSON do pedido `PED-2026-0001` e clique em **Insert**:

```json
{
  "_id": { "$oid": "671eca00a1b2c3d4e5f60777" },
  "codigo_pedido": "PED-2026-0001",
  "cliente": {
    "cliente_id": { "$oid": "671ec880a1b2c3d4e5f60010" },
    "nome": "Ana Costa",
    "cpf": "123.456.789-00"
  },
  "itens": [
    {
      "produto_id": { "$oid": "671ec880a1b2c3d4e5f60001" },
      "sku": "NOTE-ACER-15",
      "nome": "Notebook Gamer Nitro V15",
      "preco_unit": { "$numberDecimal": "4599.90" },
      "quantidade": 1
    }
  ],
  "valor_total": { "$numberDecimal": "4599.90" },
  "status": "PAGO"
}
```

#### Consultando a Lista de Documentos e Testando a Imutabilidade do Snapshot no Compass
1. Na aba **Documents** da coleção `pedidos`, expanda `cliente` (*Extended Reference Pattern*) e `itens` (*Snapshot Pattern*).
2. Vá até a coleção **`produtos`**, clique em **Edit Document** (ícone de lápis) no Notebook (`NOTE-ACER-15`), altere o campo `preco` de `4599.90` para `5299.90` e clique em **Update**.
3. **Consulte a lista de documentos** em `produtos` (novo preço de vitrine: `5299.90`) e volte para consultar a lista de documentos em `pedidos`: o valor pago no pedido `PED-2026-0001` continua congelado em `4599.90`!

---

## Parte 5: Exercício — Povoando o Banco em Lote (Compass e Python `PyMongo`)

Agora que criamos manualmente o primeiro registro de cada coleção e consultamos cada etapa no Compass, vamos povoar o banco com mais documentos usando tanto a importação em lote do **MongoDB Compass** quanto nossos scripts **Python (`PyMongo`)**:

### Opção A: Importando os Lotes JSON Diretamente no MongoDB Compass
1. **Coleção `produtos`:** Clique em **Add Data $\to$ Import JSON or CSV file**, selecione `codigo/produtos_lote.json`, clique em **Import** e **consulte a lista de documentos** na aba *Documents* (5 produtos).
2. **Coleção `clientes`:** Clique em **Add Data $\to$ Import JSON or CSV file**, selecione `codigo/clientes_lote.json`, clique em **Import** e **consulte a lista de documentos** na aba *Documents* (3 clientes).
3. **Coleção `avaliacoes`:** Clique em **Add Data $\to$ Import JSON or CSV file**, selecione `codigo/avaliacoes_lote.json`, clique em **Import** e **consulte a lista de documentos** na aba *Documents* (4 avaliações).
4. **Coleção `pedidos`:** Clique em **Add Data $\to$ Import JSON or CSV file**, selecione `codigo/pedidos_lote.json`, clique em **Import** e **consulte a lista de documentos** na aba *Documents* (2 pedidos).

### Opção B: Povoando e Consultando via Python (`PyMongo`)
No terminal, dentro da pasta `codigo/`, execute os scripts Python:
```bash
cd codigo
# 1. Script de operacoes CRUD passo a passo em Python (mongodb_books.books):
python3 crud_pymongo.py

# 2. Script de modelagem completa do e-commerce (ecommerce_shopgrids):
python3 popular_catalogo_mongodb.py

# 3. Benchmark comparativo Embedding vs. Referencing:
python3 comparativo_embedding_vs_referencing.py
```
Após executar os scripts Python, clique em **Refresh** no **MongoDB Compass** e consulte as coleções e documentos gerados!
