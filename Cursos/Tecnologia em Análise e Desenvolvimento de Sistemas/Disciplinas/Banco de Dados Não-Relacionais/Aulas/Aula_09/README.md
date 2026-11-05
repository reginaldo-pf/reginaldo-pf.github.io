# Aula 09: Laboratório de Fixação Intensiva e Revisão Prática Integrada (Redis + MongoDB) — Sábado Letivo

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 14 de Novembro de 2026 (Sábado Letivo)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Módulo:** Laboratório (N1) — Preparatório para Avaliação Prática 1 (AVP1) e Avaliação Teórica 1 (AVT1)  

---

## 🎯 Competências e Objetivos

- [x] Consolidar os conceitos basilares de arquitetura distribuída: **Teorema CAP** (Brewer), **Teorema PACELC** (Abadi) e o contraste rigoroso entre **ACID** (transações relacionais) e **BASE** (consistência eventual).
- [x] Operar com fluência as estruturas nativas do **Redis** (Strings, Hashes, Lists, Sets e Sorted Sets) no terminal `redis-cli`, na interface gráfica Redis Insight e em scripts Python (`redis-py`).
- [x] Implementar o padrão arquitetural **Cache-Aside (Lazy Loading)** em Python integrando Redis e MongoDB, garantindo o ciclo correto de *Cache Hit*, *Cache Miss* e *Invalidação Imediata* em mutações de dados.
- [x] Executar operações de CRUD atômico no **MongoDB** utilizando operadores seletivos (`$set`, `$inc`, `$push`, `$addToSet`) e buscas seguras em arrays com `$elemMatch`.
- [x] Projetar e justificar a **Regra de Ouro ESR** (*Equality, Sort, Range*) na criação de índices compostos $B\text{-Tree}$, eliminando varreduras lineares (`COLLSCAN`) e ordenações estouradas em memória (`SORT`).
- [x] Construir pipelines analíticos com o **MongoDB Aggregation Framework** (`$match`, `$unwind`, `$group`, `$sort`), calculando métricas de faturamento e estoque.
- [x] Resolver a suíte completa de testes automatizados do **Simulado Integrado N1**, preparando-se para as avaliações oficiais AVP1 e AVT1.

---

## 📁 Estrutura de Arquivos da Aula 09

- [`tutorial_construcao_passo_a_passo.md`](tutorial_construcao_passo_a_passo.md): **Guia Passo a Passo Completo** — dividido em 5 partes:
  1. Revisão Conceitual e Teoremas Distribuídos (CAP, PACELC e ACID vs BASE).
  2. Revisão Prática do Redis (Terminal CLI e Python).
  3. Revisão Prática do MongoDB (Operadores Atômicos e Regra ESR).
  4. Implementação Integrada do Padrão Cache-Aside em Python.
  5. Guia de Execução e Gabarito Analítico do Simulado N1.
- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico estruturado para 120 minutos de oficina prática, objetivos, cronograma e caderno de desafios.
- [`roteiro_privado_professor_videoaula.md`](roteiro_privado_professor_videoaula.md): Roteiro exclusivo do docente com diretrizes didáticas, armadilhas comuns dos discentes e critérios de correção.
- [`index.html`](index.html): Portal web interativo da Aula 09, reunindo a fundamentação teórica, código interativo, comparativo de latência poliglota e links para download.
- `codigo/`:
  - [`docker-compose.yml`](codigo/docker-compose.yml): Stack integrada com Redis 7.4, Redis Insight, MongoDB 8.0 e Mongo Express.
  - [`requirements.txt`](codigo/requirements.txt): Dependências Python (`pymongo`, `redis`, `matplotlib`, `numpy`, `pandas`).
  - [`simulado_n1_desafios.py`](codigo/simulado_n1_desafios.py): Caderno prático com os 5 grandes desafios do simulado e suíte de validação automatizada.
  - [`solucao_simulado_n1.py`](codigo/solucao_simulado_n1.py): Gabarito comentado de referência para todas as questões práticas.
  - [`benchmark_latencia_revisao.py`](codigo/benchmark_latencia_revisao.py): Medição empírica de latência entre Redis (RAM), MongoDB indexado e MongoDB COLLSCAN gerando o gráfico `benchmark_latencia_revisao.png`.
  - [`revisao_comandos_mongosh_redis.sh`](codigo/revisao_comandos_mongosh_redis.sh): Folha de cola (*cheat sheet*) com os comandos essenciais para terminal.
  - [`demonstracao_aula09.ipynb`](codigo/demonstracao_aula09.ipynb): Caderno Jupyter com exercícios guiados do simulado.
- `materiais/`:
  - [`main.pdf`](materiais/main.pdf) e módulos LaTeX Beamer 16:9 (`secao1_*.tex` a `secao5_*.tex`) para apoio à revisão.
  - [`benchmark_latencia_revisao.png`](materiais/benchmark_latencia_revisao.png): Gráfico comparativo de latência em escala linear e logarítmica.

---

## 🚀 Como Executar o Simulado Localmente

1. **Subir a Infraestrutura Unificada:**
   ```bash
   cd codigo
   docker compose up -d
   ```
2. **Instalar Dependências no Ambiente Virtual:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Executar a Medição de Latência:**
   ```bash
   python3 benchmark_latencia_revisao.py
   ```
4. **Executar e Validar os Desafios do Simulado:**
   ```bash
   python3 simulado_n1_desafios.py
   ```
5. **Acessar os Ambientes Visuais e Linha de Comando:**
   * **Redis Insight:** `http://localhost:5540`
   * **Mongo Express:** `http://localhost:8081`
   * **CLI do Redis:** `docker exec -it shopgrids-redis-aula09 redis-cli`
   * **CLI do Mongo:** `docker exec -it shopgrids-mongodb-aula09 mongosh`
