# Plano de Aula: 06 - Do CRUD Básico e Python (`PyMongo`) à Modelagem de Documentos BSON no MongoDB

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Data da Aula:** 27 de Outubro de 2026 (Terça-feira)  
* **Módulo:** Unidade I (N1) — O Modelo Orientado a Documentos (MongoDB)  

---

## 🧭 1. Princípios e Diretrizes Pedagógicas da Aula

1. **Aprendizado Gradual do Zero:**
   Para que os discentes aprendam a utilizar o banco de dados desde os primeiros passos sem saltos bruscos, a aula inicia pelos conceitos fundamentais do modelo de documentos e do formato BSON, avança devagar pelas operações CRUD básicas (`insertOne`, `find`, *dot notation* em subdocumentos, `updateOne` com `$set`, `deleteOne` e `bulkWrite`) na interface gráfica **MongoDB Compass** e no **`mongosh`**, e em seguida reproduz cada operação passo a passo em **Python (`PyMongo`)**.
2. **Conexão Sólida entre Teoria e Prática:**
   Estudo das anomalias de atualização do modelo relacional (1NF–5NF) frente às três estratégias de modelagem do MongoDB (**Embedded Data**, **References** e **Denormalization**), analisando a métrica de **Read-Write Ratio** (proporção leitura vs. escrita), os **3 pilares do BSON (*Lightweight, Traversable, Efficient*)** e os padrões de projeto (*Polymorphic*, *Subset*, *Computed*, *Extended Reference* e *Snapshot*).
3. **Dinâmica Interativa no MongoDB Compass:**
   Ao criar cada coleção (`books`, `produtos`, `clientes`, `avaliacoes`, `pedidos`), os alunos consultam a lista de coleções no Compass; ao inserir manualmente o primeiro documento de cada coleção (usando *Extended JSON* estrito), consultam imediatamente a lista de documentos nas visões *List*, *JSON* e *Table* do Compass; e apenas ao final realizam o povoamento em lote.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar os discentes a operar o MongoDB do zero — realizando operações CRUD no **MongoDB Compass**, no **`mongosh`** e com o driver oficial **Python (`PyMongo`)** — e a fundamentar decisões de modelagem de esquemas BSON (*Embedding*, *Referencing* e Padrões de Projeto).

### Objetivos Específicos
1. **Do RDBMS ao BSON:** Contrastar as Formas Normais relacionais com documentos BSON (até 100 níveis e 16 MB), explicando os 3 pilares do BSON (*Lightweight, Traversable, Efficient*), os 12 bytes do `ObjectId` e o tipo financeiro exato `Decimal128`.
2. **CRUD do Zero no Compass e no `mongosh`:** Criar bancos e coleções, consultar a lista de coleções, inserir documentos simples e com subdocumentos (`meta`), filtrar com *dot notation* (`"meta.version"`), operadores de comparação (`$gt`) e expressões regulares (`$regex`), atualizar com `$set` (compreendendo `matchedCount` e `modifiedCount`) e remover com `deleteOne`.
3. **CRUD com Python (`PyMongo`):** Conectar ao servidor via `MongoClient`, testar a conexão com `ping` e executar `insert_one`, `insert_many`, `find`, `find_one`, consultas com `$gt`, `AND` e `$or`, `update_one`, `delete_one` e `bulk_write`.
4. **Modelagem e Padrões de Projeto:** Aplicar *Embedded Data* (`1:1` e `1:Few`), *References* (`1:Many`), *Polymorphic Pattern*, *Subset Pattern*, *Computed Pattern* e *Extended Reference + Snapshot Pattern* nas coleções `produtos`, `clientes`, `avaliacoes` e `pedidos`.

---

## ⏱️ 3. Cronograma da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1. Teoria & BSON** | 00 – 25 min | **RDBMS vs. Modelo de Documentos e BSON:** Anomalias relacionais (1NF–5NF) vs. documentos BSON (16 MB / 100 níveis); os 3 pilares do BSON (*Lightweight, Traversable, Efficient*); `ObjectId` (12 bytes) e `Decimal128`. | Exposição dialogada com slides Beamer. |
| **2. CRUD do Zero** | 25 – 55 min | **CRUD Passo a Passo no Compass e `mongosh`:** Criação do banco `mongodb_books` e coleção `books`; consulta de coleções; inserção manual do 1.º livro; subdocumento `meta` e busca com *dot notation*, `$gt` e `$regex`; `updateOne` (`$set`) e `deleteOne`. | Prática guiada no MongoDB Compass e `mongosh`. |
| **3. CRUD Python** | 55 – 80 min | **Programando com o Driver `PyMongo`:** Conexão com `MongoClient` e `ping`; execução passo a passo de `insert_one`, `insert_many`, `find` (*dot notation*, `$regex`, `$gt`, `$or`), `update_one` e `delete_one` sincronizados com o Compass. | Execução ao vivo de `crud_pymongo.py`. |
| **4. Schema Design** | 80 – 120 min | **Modelagem no E-Commerce ShopGrids:** *Embedded Data* vs. *References* vs. *Denormalization*; *Read-Write Ratio*; construção manual do 1.º registro de `produtos`, `clientes`, `avaliacoes` e `pedidos` no Compass e povoamento final em lote. | Prática guiada no Compass e scripts Python. |

---

## 📊 4. Slides da Apresentação Oficial (Beamer 16:9 — 26 Páginas)

* **Slides 1–2:** Capa Institucional e Agenda do Encontro.
* **Slides 3–7 (Seção 1 — Fundamentos Teóricos e BSON):** Do RDBMS (anomalias e 1NF–5NF) ao Modelo de Documentos; Terminologia SQL vs. MongoDB e Ferramentas Oficiais; Os 3 Pilares do BSON (*Lightweight, Traversable, Efficient*) e Tipos BSON; Anatomia do `ObjectId` (12 bytes) e Extended JSON no Compass.
* **Slides 8–12 (Seção 2 — CRUD do Zero no Compass e `mongosh`):** Passo 1: Criando `mongodb_books` e consultando coleções; Passo 2: `insertOne` e `find` no Compass e `mongosh`; Passo 3: Subdocumento `meta`, *Dot Notation*, `$gt` e `$regex`; Passo 4: `updateOne` (`$set`), `deleteOne` e `bulkWrite`.
* **Slides 13–16 (Seção 3 — CRUD com Python `PyMongo`):** Conectando com `MongoClient` (`ping`) e inserindo com `insert_one`/`insert_many`; Consultando no Python com `find`, *Dot Notation*, `$regex`, `$gt`, `AND` e `$or`; Atualizando com `update_one` e removendo com `delete_one`.
* **Slides 17–20 (Seção 4 — Teoria de Schema Design):** As 3 estratégias (*Embedded Data*, *References*, *Denormalization*) e *Read-Write Ratio*; Diagrama visual *Embedding* vs. *Referencing*; Anti-padrão *Unbounded Arrays* e Catálogo de Padrões (*Polymorphic*, *Subset*, *Extended Reference*, *Computed*).
* **Slides 21–26 (Seção 5 — Prática no ShopGrids):** Coleção `produtos` (*Polymorphic Pattern* + validação); Coleções `avaliacoes` e `pedidos` (*Subset*, *Computed*, *Extended Reference* + *Snapshot*); Arquitetura completa das 4 coleções; Checklist de decisão e roteiro passo a passo.

---

## 📝 5. Exercícios de Fixação da Aula 06

1. **RDBMS vs. Modelo de Documentos e os 3 Pilares do BSON:**
   Explique por que os bancos relacionais precisam normalizar tabelas (1NF–5NF) para evitar anomalias de atualização e como o MongoDB resolve esse problema por meio de documentos BSON. Descreva as três características de projeto do BSON (*Lightweight*, *Traversable* e *Efficient*).
2. **Operações CRUD e *Dot Notation*:**
   Considere um documento na coleção `books` com a estrutura `{"isbn": "301", "name": "Python and MongoDB", "meta": {"version": "MongoDB 7.0"}, "price": 60}`. Escreva:
   a) A consulta para buscar livros cuja versão dentro de `meta` seja `"MongoDB 7.0"` usando *dot notation*.
   b) O comando `updateOne` (ou `update_one` no Python) para alterar o preço do livro de ISBN `"301"` para `75` usando `$set`, explicando a diferença entre `matchedCount` e `modifiedCount`.
3. **Consultas com `PyMongo`:**
   Escreva um trecho em Python utilizando `PyMongo` que busque na coleção `books` todos os documentos que tenham `"price"` maior que `50` (`$gt`) **OU** (`$or`) cujo `"isbn"` seja `"101"`.
4. ***Read-Write Ratio*, *Unbounded Arrays* e *Subset Pattern*:**
   Explique como a métrica *Read-Write Ratio* influencia a escolha entre *Embedding* e *Referencing*, por que embutir 50.000 avaliações dentro de um produto viola o limite de 16 MB do BSON, e como o *Subset Pattern* aliado ao *Computed Pattern* resolve esse problema.
5. ***Extended Reference* e *Snapshot Pattern* em Pedidos:**
   Justifique por que armazenar apenas o `produto_id` dentro de um pedido em `pedidos` corrompe o histórico fiscal quando o produto sofre reajuste de preço, e mostre como o *Snapshot Pattern* congela os dados da compra.
