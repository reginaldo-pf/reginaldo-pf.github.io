# Plano de Aula: 05 - Redis na Prática: Estratégias de Cache (TTL), Controle de Sessão e Filas

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Data da Aula:** 20 de Outubro de 2026 (Terça-feira)  
* **Módulo:** Unidade II (N1) — O Modelo Chave-Valor e Arquiteturas In-Memory  

---

## 🧭 1. Princípios e Diretrizes Pedagógicas da Aula

1. **Abordagem de Engenharia Real (*Projeto $\to$ Implementação $\to$ Uso*):**
   A aula abandona comandos descontextualizados no terminal para construir uma aplicação web de comércio eletrônico real (**FastCommerce NoSQL**). Os alunos compreendem *por que* cada estrutura de dados do Redis existe antes de digitar a sintaxe.
2. **Padrão de Persistência Poliglota (*Polyglot Persistence*):**
   Demonstração do modelo híbrido de banco de dados moderno: a memória RAM rápida (Redis) atua como camada de aceleração de altíssima frequência (microssegundos), enquanto a base persistente orientada a documentos (MongoDB) gerenciará o ciclo de vida permanente a partir da Aula 06.
3. **Comprovação Empírica da Física de Acesso:**
   Mensuração e visualização direta no navegador da diferença entre *Cache Hit* (RAM em $\approx 0.4\text{ ms}$) versus *Cache Miss* (simulação de leitura em disco $\approx 120\text{ ms}$), comprovando o ganho de aceleração (*Speedup* $> 250\times$).
4. **Desacoplamento Assíncrono com Filas:**
   Demonstração prática do padrão Produtor-Consumidor para evitar o travamento de requisições de checkout HTTP síncronas através de Listas (`LPUSH`) e workers com bloqueio inteligente (`BRPOP`).

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar os discentes a projetar, implementar e operar arquiteturas de alta performance utilizando o Redis como gerenciador de sessões de usuário, provedor de cache com invalidação e expiração automática (TTL), manipulador atômico de carrinhos de compras em hashes e intermediário de filas assíncronas de mensagens em uma aplicação web real.

### Objetivos Específicos
1. **Modelagem de Chaves e Namespaces:** Projetar esquemas de chaves semânticas no padrão `namespace:entidade:id` (`session:*`, `cart:*`, `cache:*`, `fila:*`).
2. **Implementação do Padrão Cache-Aside:** Construir o fluxo de leitura sob demanda com expiração programada (`SETEX`) e invalidação pró-ativa (`DEL`).
3. **Gestão de Sessão Centralizada:** Estruturar tokens de autenticação em memória com renovação de tempo de vida deslizante (*Sliding Expiration* com `EXPIRE`).
4. **Manipulação Atômica de Hashes:** Empregar o comando `HINCRBY` no carrinho de compras, eliminando condições de corrida (*Race Conditions*) sem lock explícito.
5. **Arquitetura Produtor-Consumidor (Queue):** Desacoplar o fechamento de pedidos via lista do Redis (`LPUSH`) e consumo por worker em background com `BRPOP`.
6. **Integração Web em Python:** Conectar a biblioteca `redis-py` a uma aplicação web com rotas REST e interface reativa em JavaScript.
7. **Ponte Conceitual com o MongoDB:** Identificar os limites de retenção da memória volátil e justificar a necessidade da camada de documentos BSON (Aulas 06 a 08).

---

## ⏱️ 3. Cronograma da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1. Projeto** | 00 – 25 min | **Modelagem de Chaves e Persistência Poliglota:** Apresentação da dor de arquitetura do e-commerce (lentidão de catálogo e gargalo de checkout). Desenho no quadro das estruturas do Redis: Hashes vs. Strings vs. Listas. | Exposição dialogada e diagrama arquitetural. |
| **2. Implementação** | 25 – 70 min | **Construção Guiada da API FastCommerce:** Codificação dos 4 pilares no back-end Python: (1) Gerenciador de Sessão com TTL, (2) Cache-Aside de Produtos, (3) Carrinho Atômico em Hash e (4) Fila de Checkout com `LPUSH`. | Live coding em laboratório com `redis-py` e Flask. |
| **3. Uso Prático** | 70 – 105 min | **Experimentação na Interface Web e Terminal:** Os alunos abrem o navegador: adicionam produtos ao carrinho, testam o botão de invalidação de cache (Hit vs Miss), finalizam pedidos e disparam o `worker_pedidos.py` com `BRPOP`. | Prática hands-on no navegador e console `redis-cli`. |
| **4. Síntese** | 105 – 120 min | **Fechamento e Preparação para o MongoDB:** Discussão sobre o ciclo de vida dos dados: *"O Redis finalizou a compra, mas onde guardamos o histórico de 10 anos da nota fiscal?"* $\to$ Conexão com o MongoDB na Aula 06. | Mentoria docente e direcionamento para a AVP1. |

---

## 📊 4. Slides da Apresentação Oficial (Beamer 16:9)

* **Slide 1:** Capa Institucional (Banco de Dados Não-Relacionais -- Aula 05: Redis na Prática).
* **Slide 2:** Agenda Temática do Encontro (5 seções modulares).
* **Slide 3:** O Fim do Monolito de Dados e a Persistência Poliglota (*Martin Fowler*).
* **Slide 4:** O Projeto Transversal FastCommerce NoSQL: Do Redis ao MongoDB.
* **Slide 5:** Diagrama Arquitetural: Front Web $\to$ API REST $\to$ Redis In-Memory $\to$ Worker.
* **Slide 6:** O Padrão Cache-Aside (*Lazy Loading*): Mecânica de Leitura e Gravação.
* **Slide 7:** A Finitude da Memória RAM: Por que todo cache DEVE ter TTL programado?
* **Slide 8:** Código Python: Implementação da Vitrine com Medição de Latência (Hit vs Miss).
* **Slide 9:** Gestão de Sessão Distribuída e Expiração Deslizante (*Sliding Expiration*).
* **Slide 10:** Hashes vs. Strings no Carrinho de Compras: Evitando *Race Conditions* com `HINCRBY`.
* **Slide 11:** Código Python: Manipulação Atômica de Itens do Carrinho e Expiração de Carrinhos Abandonados.
* **Slide 12:** O Gargalo do Checkout Síncrono e a Necessidade de Filas Assíncronas.
* **Slide 13:** O Padrão Produtor-Consumidor FIFO: `LPUSH` na Esquerda e `BRPOP` na Direita.
* **Slide 14:** Código Python: Rota de Checkout Produtora e Worker Consumidor Desacoplado.
* **Slide 15:** Checklist de Competências Práticas Consolidadas na Aula 05.
* **Slide 16:** Onde o Redis Termina? A Transição para o MongoDB na Aula 06.
* **Slide 17:** Linha do Tempo do Projeto FastCommerce rumo à AVP1 (Aula 10).
* **Slide 18:** Encerramento e Atividades de Laboratório.

---

## 💻 5. Roteiro do Laboratório Prático Computacional

1. **Subindo o Ecossistema:**
   ```bash
   # Terminal 1: Iniciar servidor Redis (ou docker compose up -d)
   redis-server
   
   # Terminal 2: Iniciar a aplicação web FastCommerce
   python app.py
   ```
2. **Acesso à Aplicação Web:**
   * Abrir `http://localhost:5000` no navegador.
   * Observar no banner de telemetria a latência da 1ª consulta (**Cache Miss: ~120 ms**) e recarregar para ver a 2ª consulta (**Cache Hit: < 1 ms**).
3. **Experimentação com o Carrinho de Compras:**
   * Clicar em "Adicionar ao Carrinho" em múltiplos produtos.
   * Abrir o `redis-cli` no terminal e auditar a chave:
     ```bash
     redis-cli
     KEYS cart:*
     HGETALL cart:<sua_sessao>
     TTL cart:<sua_sessao>
     ```
4. **Fechamento de Pedido e Fila Assíncrona:**
   * Clicar em "Finalizar Pedido" na gaveta lateral do carrinho.
   * Notar que a lista `fila:pedidos` agora possui 1 item pendente.
   * No terminal, executar o worker:
     ```bash
     python worker_pedidos.py
     ```
   * Observar o consumo imediato via `BRPOP` e a mensagem de gancho para o MongoDB!

---

## 📝 6. Exercícios de Fixação da Aula 05

1. **Padrão Cache-Aside e Invalidação:**
   Explique por que a estratégia recomendada ao alterar o preço de um produto em um banco de dados é executar `DEL cache:produto` em vez de `SET cache:produto <novo_preco>`.
2. **Atomicidade e Hashes:**
   Durante uma promoção de Black Friday com milhares de compras por segundo, por que o comando `HINCRBY cart:usr_1 prod_1 1` é muito mais seguro e performático do que ler um JSON, alterar o campo no Python e salvar de volta com `SET`?
3. **Políticas de Expiração (TTL):**
   Diferencie **Absolute Expiration** (expiração rígida) de **Sliding Expiration** (expiração deslizante), citando em qual situação cada uma foi aplicada no FastCommerce (catálogo vs. sessão).
4. **Consumo Bloqueante de Filas:**
   Por que a implementação de workers com `BRPOP chave timeout` é superior à implementação com loop infinito usando `RPOP` intercalado com `time.sleep(1)`?
5. **Persistência Poliglota:**
   Discuta as razões técnicas pelas quais uma loja virtual moderna utiliza o Redis para carrinhos e sessões, mas migra os pedidos finalizados para o MongoDB na camada de persistência definitiva.

---

## 📚 7. Referências Bibliográficas

* **SANFILIPPO, Salvatore (antirez).** *Redis: The Definitive Guide to In-Memory Data Structures and Real-Time Computing.* Redis Documentation, 2024. Disponível em: <https://redis.io/docs/>.
* **SADALAGE, Pramod J.; FOWLER, Martin.** *NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota.* São Paulo: Novatec Editora, 2014. (Capítulo 2: Persistência Poliglota e Capítulo 5: Bancos de Chave-Valor).
* **KLEPPMANN, Martin.** *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems.* Sebastopol, CA: O'Reilly Media, 2017. (Capítulo 3: Storage and Retrieval e Capítulo 11: Stream Processing).
* **FROZZA, Angelo A.; SCHREINER, Paulo; MELLO, Ronaldo dos Santos.** *Projeto de Bancos de Dados NoSQL: Modelagem e Arquiteturas Chave-Valor e Documentos.* Livro Colaborativo de Bancos Não-Relacionais, 2022.
