# Roteiro de Produção de Videoaula: Aula 27 (Encontro 4)
## Testes Automatizados (Pytest), CLI e Fechamento da Sprint (100 Minutos)

---

## 🎬 Metadados e Diretrizes Audiovisuais

*   **Curso:** Técnico em Informática para Internet — IFCE Campus Tauá
*   **Disciplina:** Engenharia de Software | **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema:** Sprint 04: Testes Automatizados (Pytest), CLI e Fechamento da Sprint (BiblioTauá)
*   **Duração Total:** 100 minutos (Bloco 1: 50 min — QA & Pytest; Bloco 2: 50 min — CLI & Pull Request)
*   **Padrão de Câmeras:**
    *   **[CÂMERA 1 - PRINCIPAL]:** Plano Médio do Professor.
    *   **[TELA CHEIA]:** Slides Beamer com a Pirâmide de Testes TikZ e terminal Pytest.
    *   **[SPLIT-SCREEN]:** Professor no canto inferior com o relatório do Pull Request.

---

## ⏱️ BLOCO 1 (00:00 - 50:00): Garantia de Qualidade e Suíte Pytest

### Cena 1: Abertura e a Filosofia de QA (00:00 - 15:00)
*   **Visual:** [CÂMERA 1] Abertura institucional do IFCE Tauá -> Corte para o Professor em plano médio. Em seguida, [SPLIT-SCREEN] com a fala da Tech Lead Aline Mendes sobre homologação.
*   **Áudio / Professor:**
    > *"Olá a todos! Sejam muito bem-vindos ao Encontro 4, o grande desfecho da nossa Sprint 04! Construímos modelos, banco SQLite e orquestração de serviços. Mas um bom engenheiro de software nunca diz que terminou sem antes provar que seu código funciona através de testes automatizados!"*

### Cena 2: A Pirâmide de Testes e Rastreabilidade da DUC (15:00 - 30:00)
*   **Visual:** [TELA CHEIA] Slide Beamer com o Diagrama da Pirâmide de Testes em TikZ.
*   **Áudio / Professor:**
    > *"Vejam a base da nossa pirâmide: cada fluxo de exceção que lemos lá na Aula 24 na especificação DUC virou agora uma função de teste automatizada com Pytest. Usamos fixtures em memória (`:memory:`) para que os testes rodem em milissegundos sem sujar o banco de dados de produção."*

### Cena 3: Execução e Análise do Pytest (30:00 - 50:00)
*   **Visual:** [SPLIT-SCREEN] Terminal executando `PYTHONPATH=. pytest bibliotaua/tests/test_cupons.py -v`. Destaque para os 10 testes verdes.
*   **Áudio / Professor:**
    > *"Observem: 10 cenários testados em 0.03 segundos! Cobrimos desconto percentual, valor fixo, cupom inativo, expirado, esgotado, subtotal mínimo e baixa de estoque de livros. Essa é a verdadeira garantia de qualidade na engenharia!"*

---

## ⏱️ BLOCO 2 (50:00 - 100:00): Demonstração CLI e Fechamento da Sprint

### Cena 4: Demonstração Interativa no Terminal (`main.py`) (50:00 - 70:00)
*   **Visual:** [TELA CHEIA] Execução interativa de `python3 -m bibliotaua.main`. Simulação de compra do livro 'Introdução ao Python' com aplicação do cupom 'VOLTAAULAS10'.
*   **Áudio / Professor:**
    > *"Vejam o fluxo no terminal: o cliente escolhe o livro, insere o cupom, o sistema discrimina subtotal, desconto e o total a pagar no PIX, além de debitar o exemplar do estoque. O ciclo está completo!"*

### Cena 5: Consolidação dos Commits Semânticos e Pull Request (70:00 - 90:00)
*   **Visual:** [TELA CHEIA] Diagrama de Git Flow TikZ e template de Pull Request preenchido.
*   **Áudio / Professor:**
    > *"Escrevemos mensagens atômicas no padrão Conventional Commits e abrimos nosso Pull Request formal para a Tech Lead Aline Mendes e para a QA Beatriz. É assim que desenvolvedores maduros entregam software no mercado!"*

### Cena 6: Retrospectiva da Sprint e Celebração Final (90:00 - 100:00)
*   **Visual:** [CÂMERA 1] Professor em plano médio; [GC / Lettering] destacando as conquistas dos 4 encontros.
*   **Áudio / Professor:**
    > *"Parabéns a cada um de vocês! Em quatro encontros intensivos, vivenciamos uma sprint completa: de requisitos e classes até persistência relacional, serviços e testes automatizados. O BiblioTauá v0.4.0 está homologado com louvor! Nos vemos na próxima sprint quinzenal!"*
