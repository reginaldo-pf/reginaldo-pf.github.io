# 🔒 Roteiro do Professor: Aula 09 — Laboratório de Fixação Intensiva e Simulado Integrado N1 (Sábado Letivo)

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Data Prevista:** 14 de Novembro de 2026 (Sábado Letivo)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Materiais de Apoio:** `materiais/main.pdf` (apresentação Beamer 16:9), `tutorial_construcao_passo_a_passo.md`, pasta `codigo/`.

---

## 🧭 Visão Geral e Estratégia da Oficina

Este encontro de sábado letivo cumpre a diretriz estrita do planejamento semestral: **não introduzir matéria nova**, atuando como um laboratório intensivo de consolidação e revisão preparatória para as duas avaliações do primeiro período:
1. **AVP1 (Aula 10 - Terça-feira seguinte):** Prova prática individual/dupla em laboratório sobre integração Redis + MongoDB em Python.
2. **AVT1 (Aula 11):** Prova teórica individual abrangendo Teorema CAP/PACELC, ACID vs BASE e modelos NoSQL, acompanhada do fechamento da Lista 1.

O papel do docente neste encontro é atuar como facilitador, conduzindo uma síntese teórica nos primeiros 45 minutos e deixando a maior parte do tempo dedicada à resolução ativa do simulado prático pelos próprios estudantes.

---

## ⏱️ Bloco a Bloco: Condução da Aula (120 Minutos)

### Bloco 1: Revisão Teórica e Teoremas (00 a 25 min)
* **Revisão Relâmpago do Teorema CAP (10 min):**
  - Chamar um estudante e pedir para explicar por que não existe banco "CA" em redes distribuídas reais.
  - Reforçar: partições de rede ($P$) ocorrem na infraestrutura física; logo, a decisão reside entre consistência forte (CP) ou disponibilidade contínua (AP).
* **O Teorema PACELC e ACID vs BASE (15 min):**
  - Explicar o que significa a sigla PACELC e qual a relevância da cláusula *Else* (operação normal em regime estável).
  - Destacar que o Redis é tipicamente PA/EL (latência mínima em RAM) e o MongoDB atua como PC/EC.

---

### Bloco 2: Revisão Operacional do Redis (25 a 45 min)
* **Revisão de Comandos Chave (10 min):**
  - Relembrar o uso de `SET ... EX <seg>` e `TTL`.
  - Revisar Hashes (`HSET`, `HINCRBY`, `HGETALL`) e por que são superiores a Strings puras para carrinhos de compras (permitem mutação atômica de campos individuais sem reescrever o JSON inteiro).
* **Filas FIFO com Listas (10 min):**
  - Demonstrar o par `LPUSH` / `RPOP` e o consumo bloqueante com `BRPOP`.

---

### Bloco 3: Revisão Operacional do MongoDB (45 a 70 min)
* **CRUD Atômico e Array Filters (10 min):**
  - Relembrar o uso obrigatório do operador `$elemMatch` para evitar falsos positivos ao buscar múltiplos atributos dentro de um mesmo subdocumento de array.
* **A Regra de Ouro ESR e o explain() (15 min):**
  - Escrever no quadro a sequência:
    $$\text{1. Igualdade (Equality)} \implies \text{2. Ordenação (Sort)} \implies \text{3. Faixa (Range)}$$
  - Mostrar como o índice ESR evita o estouro do buffer de ordenação em RAM (`SORT memory limit`).

---

### Bloco 4: Simulado Prático Assistido (70 a 105 min)
* **Orientação para o Laboratório (5 min):**
  - Pedir aos discentes para abrirem o terminal e iniciarem os containers: `docker compose up -d`.
  - Explicar a estrutura do arquivo `simulado_n1_desafios.py`.
* **Resolução Ativa (30 min):**
  - Circular pelas bancadas dos discentes, observando as dificuldades de sintaxe e raciocínio na implementação dos 5 desafios.
  - Orientar os alunos a executarem o script de teste para receberem o feedback automático do console.

---

### Bloco 5: Plantão de Dúvidas e Gabarito Comentado (105 a 120 min)
* **Projeção da Solução de Referência (10 min):**
  - Projetar o arquivo `solucao_simulado_n1.py`.
  - Comentar ponto a ponto como o Cache-Aside deve tratar a serialização do `_id` (converter de `ObjectId` para string) antes de gravar no Redis.
* **Orientações para o Dia da Prova (5 min):**
  - Relembrar o formato da AVP1 (sem consulta à internet livre, permitida apenas consulta à documentação oficial local e aos scripts desenvolvidos em aula).

---

## ⚠️ Armadilhas Comuns dos Estudantes no Simulado

1. **Erro de Serialização do ObjectId:**
   - *Sintoma:* `TypeError: Object of type ObjectId is not JSON serializable`.
   - *Intervenção:* Lembrar que o método `json.dumps()` não reconhece o tipo nativo BSON `ObjectId`; é necessário converter o campo para string antes (`doc["_id"] = str(doc["_id"])`).
2. **Esquecer de Definir TTL no Redis:**
   - *Sintoma:* O cache cresce indefinidamente até esgotar a memória do host.
   - *Intervenção:* Exigir sempre o uso de `setex(chave, tempo, valor)` ou `expire(chave, tempo)`.
3. **Inversão da Ordem na Regra ESR:**
   - *Sintoma:* Colocar o campo de faixa (*Range*) antes do campo de ordenação (*Sort*) no índice composto, forçando o motor a realizar o estágio custoso `SORT` em memória RAM.
