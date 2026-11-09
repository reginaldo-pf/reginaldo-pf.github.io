# Roteiro de Produção de Videoaula: Aula 26 (Encontro 3)
## Diagrama de Sequência e Orquestração do Negócio (100 Minutos)

---

## 🎬 Metadados e Diretrizes Audiovisuais

*   **Curso:** Técnico em Informática para Internet — IFCE Campus Tauá
*   **Disciplina:** Engenharia de Software | **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema:** Sprint 04: Diagrama de Sequência e Orquestração do Negócio (BiblioTauá)
*   **Duração Total:** 100 minutos (Bloco 1: 50 min — Sequência & Atividades; Bloco 2: 50 min — Serviços & Checkout)
*   **Padrão de Câmeras:**
    *   **[CÂMERA 1 - PRINCIPAL]:** Plano Médio do Professor.
    *   **[TELA CHEIA]:** Slides Beamer com Diagrama de Sequência TikZ.
    *   **[SPLIT-SCREEN]:** Professor no canto com VS Code demonstrando a transação.

---

## ⏱️ BLOCO 1 (00:00 - 50:00): A Visão Temporal da Interação

### Cena 1: Abertura e a Necessidade da Visão Dinâmica (00:00 - 15:00)
*   **Visual:** [CÂMERA 1] Abertura institucional IFCE Tauá -> Corte para o Professor. Em seguida, [SPLIT-SCREEN] mostrando as classes da livraria.
*   **Áudio / Professor:**
    > *"Olá a todos! Sejam muito bem-vindos ao Encontro 3 da nossa Sprint 04! Já temos entidades em Python e tabelas no SQLite. Mas como esses elementos interagem no tempo durante uma compra? Hoje responderemos a essa pergunta com o poderoso **Diagrama de Sequência da UML 2**!"*

### Cena 2: Diagrama de Sequência na Prática (15:00 - 35:00)
*   **Visual:** [TELA CHEIA] Slide Beamer com o Diagrama de Sequência TikZ. Destaque para as 7 etapas cronológicas de troca de mensagens.
*   **Áudio / Professor:**
    > *"Vejam a precisão do Diagrama de Sequência: o cliente aciona o serviço; o serviço primeiro consulta o repositório; se válido, aplica o desconto no pedido; debita o estoque do livro físico e, por fim, grava a transação. Se qualquer etapa falhar, o pedido é abortado!"*

### Cena 3: Diagrama de Atividades e Regras de Transação (35:00 - 50:00)
*   **Visual:** [TELA CHEIA] Diagrama de Atividades em TikZ.
*   **Áudio / Professor:**
    > *"Analisem as bifurcações de decisão: se o cliente não informou cupom, o fluxo segue sem desconto. Se informou cupom inválido, a exceção é disparada imediatamente. Isso garante integridade total ao negócio da livraria."*

---

## ⏱️ BLOCO 2 (50:00 - 100:00): Live Coding — Serviços e Checkout

### Cena 4: Implementando a Calculadora de Desconto (50:00 - 65:00)
*   **Visual:** [SPLIT-SCREEN] Professor no canto; VS Code editando `bibliotaua/services/calculadora_desconto.py`.
*   **Áudio / Professor:**
    > *"Desacoplamos o cálculo matemático em uma classe de serviço pura com métodos estáticos. Isso facilita enormemente a escrita de testes unitários rápidos."*

### Cena 5: Integrando o Cupom ao Pedido e Criando o `CheckoutService` (65:00 - 90:00)
*   **Visual:** [TELA CHEIA] VS Code com `models/pedido.py` e `services/checkout_service.py`.
*   **Áudio / Professor:**
    > *"No `CheckoutService`, unimos todas as peças: repositório de cupons, baixa no estoque de livros e persistência do pedido. É a orquestração completa da nossa arquitetura em camadas!"*

### Cena 6: Simulação no Terminal e Fechamento da Daily 3 (90:00 - 100:00)
*   **Visual:** [SPLIT-SCREEN] Terminal executando simulação de checkout e exibindo resumo formatado da compra com cupom de desconto.
*   **Áudio / Professor:**
    > *"Sensacional! Nosso motor está 100% integrado. No Encontro 4, fecharemos com chave de ouro: criaremos a suíte de testes com Pytest, rodaremos a interface CLI e submeteremos o Pull Request formal da nossa Sprint 04!"*
