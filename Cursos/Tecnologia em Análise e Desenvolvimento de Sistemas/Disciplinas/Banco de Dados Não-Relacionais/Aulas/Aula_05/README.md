# Aula 05: Redis na Prática: Estratégias de Cache (TTL), Controle de Sessão e Filas

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 20 de Outubro de 2026 (Terça-feira)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Módulo:** Unidade II (N1) — O Modelo Chave-Valor e Arquiteturas In-Memory  

---

## 🎯 Competências e Objetivos Consolidados

- [x] Projetar esquemas de chaves semânticas no padrão `namespace:entidade:id` no Redis.
- [x] Implementar o padrão **Cache-Aside (Lazy Loading)** com expiração automática (TTL) e mensuração direta da aceleração de leitura ($> 250\times$).
- [x] Estruturar tokens de autenticação e sessões de usuário em memória com renovação deslizante (*Sliding Expiration* com `EXPIRE`).
- [x] Manipular carrinhos de compras em tempo real utilizando **Hashes do Redis** (`HINCRBY`, `HGETALL`, `HDEL`), eliminando condições de corrida sem lock de banco.
- [x] Desacoplar o checkout de pedidos através do padrão **Produtor-Consumidor (Queue)** com Listas do Redis (`LPUSH`) e workers com bloqueio inteligente (`BRPOP`).
- [x] Operar uma aplicação web real de comércio eletrônico (**FastCommerce NoSQL**) conectada ao Redis.
- [x] Estabelecer a ponte de **Persistência Poliglota** rumo à Aula 06, onde o catálogo e os pedidos consumidos da fila se transformarão em documentos BSON persistentes no MongoDB.

---

## 📁 Estrutura de Arquivos da Aula 05

- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico estruturado em 4 etapas (*Projeto $\to$ Implementação $\to$ Uso $\to$ Síntese*), objetivos detalhados, slides e 5 exercícios de fixação.
- [`index.html`](index.html): Portal web didático interativo e responsivo com Tailwind CSS, Prism.js, visualizador de slides em PDF e abas integradas.
- `codigo/`:
  - [`app.py`](codigo/app.py): Aplicação web / API em Python com Flask e `redis-py`, implementando sessões, cache-aside, carrinho em hash e checkout enfileirado.
  - [`worker_pedidos.py`](codigo/worker_pedidos.py): Script de worker em background consumindo pedidos da fila via `BRPOP` e simulando aprovação de pagamento.
  - [`templates/index.html`](codigo/templates/index.html): Interface web moderna e reativa do FastCommerce com monitor de telemetria, vitrine e carrinho drawer.
  - [`demonstracao_aula05.ipynb`](codigo/demonstracao_aula05.ipynb): Jupyter Notebook interativo com células de execução passo a passo dos 4 pilares do Redis.
  - [`docker-compose.yml`](codigo/docker-compose.yml): Configuração para subir o Redis via container Docker em uma única linha.
  - [`requirements.txt`](codigo/requirements.txt): Dependências Python do projeto.
- `materiais/`:
  - [`main.tex`](materiais/main.tex): Documento mestre Beamer (Widescreen 16:9, tema institucional IFCE Tauá / Scouts).
  - `secao*.tex`: 5 módulos temáticos de slides com fundamentação formal e diagramas canônicos.
  - [`main.pdf`](materiais/main.pdf): Apresentação em slides compilada em PDF com 18 páginas e zero avisos de overfull.

---

## 🚀 Como Executar a Aplicação em Sala de Aula

1. **Suba o Redis:**
   ```bash
   redis-server
   # ou: docker compose -f codigo/docker-compose.yml up -d
   ```
2. **Execute o Servidor Web:**
   ```bash
   cd codigo
   python app.py
   ```
3. **Acesse no Navegador:**
   Abra `http://localhost:5000` para experimentar a vitrine, o carrinho de compras e a telemetria ao vivo.
4. **Execute o Worker de Processamento:**
   ```bash
   python worker_pedidos.py
   ```
