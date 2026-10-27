# Aula 06: Do CRUD Básico e Python (`PyMongo`) à Modelagem de Documentos BSON no MongoDB

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 27 de Outubro de 2026 (Terça-feira)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Módulo:** Unidade I (N1) — O Modelo Orientado a Documentos (MongoDB)  

---

## 🎯 Competências e Objetivos

- [x] Compreender os fundamentos teóricos que separam os SGBDs Relacionais (anomalias de atualização e Formas Normais 1NF–5NF) do **Modelo Orientado a Documentos** do MongoDB (documentos de até **16 MB** e **100 níveis** de aninhamento).
- [x] Dominar os **3 pilares do BSON (*Lightweight, Traversable, Efficient*)** e seus tipos de dados nativos (`ObjectId` de 12 bytes, `Decimal128`, `ISODate`, `Int32`, `Int64`, `Object`, `Array`).
- [x] Aprender a usar o MongoDB **do zero, passo a passo**, criando o banco `mongodb_books` e a coleção `books` no **MongoDB Compass (GUI)** e no `mongosh`, consultando a lista de coleções, inserindo o 1.º documento manualmente, consultando a lista de documentos, filtrando subdocumentos com *dot notation* (`"meta.version"`), `$gt` e `$regex`, atualizando com `updateOne`/`$set` e removendo com `deleteOne`.
- [x] Programar operações CRUD passo a passo usando o driver oficial **Python (`PyMongo`)** (`MongoClient`, `ping`, `insert_one`, `insert_many`, `find`, *dot notation*, `$gt`, `$or`, `update_one`, `delete_one` e `bulk_write`).
- [x] Aplicar **Schema Design e Padrões de Projeto** (*Embedded Data*, *References*, *Denormalization*, *Read-Write Ratio*, *Polymorphic Pattern*, *Subset Pattern*, *Computed Pattern* e *Extended Reference + Snapshot Pattern*) construindo passo a passo o banco `ecommerce_shopgrids` no **MongoDB Compass** e no **Python**.

---

## 📁 Estrutura de Arquivos da Aula 06

- [`tutorial_construcao_passo_a_passo.md`](tutorial_construcao_passo_a_passo.md): **Guia Passo a Passo Completo** — dividido em 5 partes:
  1. Fundamentos Teóricos (RDBMS vs. Documentos, 3 pilares do BSON e tipos de dados).
  2. CRUD do Zero passo a passo no **MongoDB Compass** e no `mongosh` (`mongodb_books.books`).
  3. CRUD passo a passo com o driver **Python (`PyMongo`)**.
  4. Modelagem das 4 coleções de `ecommerce_shopgrids` (`produtos`, `clientes`, `avaliacoes`, `pedidos`) com inserção manual do 1.º registro de cada coleção e consulta visual no Compass.
  5. Exercício de povoamento em lote (via Compass Import JSON e via Python).
- [`index.html`](index.html): Portal web da Aula 06 com o conteúdo teórico e prático, guia passo a passo, slides em PDF e scripts.
- `codigo/`:
  - [`crud_pymongo.py`](codigo/crud_pymongo.py): Script Python (`PyMongo`) implementando passo a passo o CRUD (`mongodb_books.books`) e exemplos de modelagem (`users`, `professors`, `courses`).
  - [`popular_catalogo_mongodb.py`](codigo/popular_catalogo_mongodb.py): Script Python (`PyMongo`) de raio-X do BSON (`ObjectId`, `Decimal128`) e modelagem das 4 coleções do `ecommerce_shopgrids`.
  - [`comparativo_embedding_vs_referencing.py`](codigo/comparativo_embedding_vs_referencing.py): Benchmark em Python comparando *Embedding* vs. *Referencing* e teste de integridade do *Snapshot Pattern*.
  - [`mongosh_guia_pratico.js`](codigo/mongosh_guia_pratico.js): Script completo para o `mongosh`.
  - [`produtos_lote.json`](codigo/produtos_lote.json), [`clientes_lote.json`](codigo/clientes_lote.json), [`avaliacoes_lote.json`](codigo/avaliacoes_lote.json), [`pedidos_lote.json`](codigo/pedidos_lote.json): Arquivos JSON para povoamento em lote no exercício final via **MongoDB Compass**.
  - [`docker-compose.yml`](codigo/docker-compose.yml): Configuração para subir o servidor MongoDB na porta `27017`.
- `materiais/`:
  - [`main.pdf`](materiais/main.pdf) e arquivos `.tex` da apresentação em slides Beamer Widescreen (26 páginas).
