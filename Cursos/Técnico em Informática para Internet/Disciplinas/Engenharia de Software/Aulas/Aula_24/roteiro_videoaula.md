# Roteiro de Produção de Videoaula: Aula 24 (Encontro 1)
## Casos de Uso, Diagrama de Classes e Início da Codificação em Python (100 Minutos)

---

## 🎬 Metadados e Diretrizes de Produção Audiovisual

*   **Curso:** Técnico em Informática para Internet — IFCE Campus Tauá
*   **Disciplina:** Engenharia de Software | **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema:** Sprint 04: Casos de Uso, Diagrama de Classes e Início da Codificação (BiblioTauá)
*   **Duração Total:** 100 minutos (Bloco 1: 50 min — Modelagem UML; Bloco 2: 50 min — Codificação Prática)
*   **Padrão de Câmeras:**
    *   **[CÂMERA 1 - PRINCIPAL]:** Plano Médio do Professor.
    *   **[TELA CHEIA]:** Slides Beamer com Diagramas TikZ de alta resolução e terminal Python.
    *   **[SPLIT-SCREEN]:** Professor no canto inferior com diagrama/código ao centro.

---

## ⏱️ BLOCO 1 (00:00 - 50:00): Do Briefing aos Diagramas de UC e Classes

### Cena 1: Abertura da Sprint 04 e Ticket TASK-204 (00:00 - 15:00)
*   **Visual:** [CÂMERA 1] Abertura institucional do IFCE Tauá -> Corte para o Professor. Em seguida, [SPLIT-SCREEN] com o ticket da `TASK-204` e a fala da Tech Lead Aline Mendes.
*   **Áudio / Professor:**
    > *"Olá a todos! Sejam muito bem-vindos à nossa Sprint 04 no BiblioTauá! Hoje vamos acelerar o nosso ritmo de engenharia: entenderemos os requisitos no Diagrama de Casos de Uso, mapearemos a estrutura no Diagrama de Classes e já começaremos a programar em Python ainda nesta primeira aula! Nada de esperar duas aulas para colocar a mão na massa!"*

### Cena 2: Diagrama de Casos de Uso e Dissecação da DUC (15:00 - 30:00)
*   **Visual:** [TELA CHEIA] Exibição do Diagrama de Casos de Uso em TikZ (Slide 6). Foco nas relações `<<extend>>` e `<<include>>`.
*   **Áudio / Professor:**
    > *"Vejam como o caso de uso UC04 (Aplicar Cupom) estende opcionalmente a finalização do pedido e inclui a validação de regras. Na tabela da DUC, cada fluxo de exceção (FE01 a FE04) previne um risco real de negócio na livraria."*

### Cena 3: Diagrama de Classes e Arquitetura do Projeto (30:00 - 50:00)
*   **Visual:** [TELA CHEIA] Diagrama de Classes TikZ (Slides 8 e 9) e Árvore Arquitetural (Slides 10 e 11).
*   **Áudio / Professor:**
    > *"Aqui está a transição da engenharia: os conceitos da DUC viram classes, atributos e métodos. E prestem muita atenção nos Slides 10 e 11: nosso projeto já possui os arquivos de Cliente, Livro e Pedido porque estamos simulando uma equipe profissional ágil! O sistema BiblioTauá já tem uma base v0.3.0 das sprints anteriores. Hoje nosso foco cirúrgico de codificação é a TASK-204: criar exceptions.py e models/cupom.py. Vamos abrir o VS Code e programar!"*

---

## ⏱️ BLOCO 2 (50:00 - 100:00): Live Coding — Exceções e Modelo Cupom

### Cena 4: Implementação das Exceções de Domínio (50:00 - 70:00)
*   **Visual:** [SPLIT-SCREEN] Professor no canto inferior; VS Code em tela principal editando `bibliotaua/exceptions.py`.
*   **Áudio / Professor:**
    > *"Vamos codificar nossa hierarquia de erros herdando de `BiblioTauaException`. Se tentarem aplicar um cupom esgotado ou abaixo do valor mínimo, nosso sistema lançará erros semanticamente expressivos!"*

### Cena 5: Implementação da Entidade `Cupom` (70:00 - 90:00)
*   **Visual:** [TELA CHEIA] VS Code com `bibliotaua/models/cupom.py`.
*   **Áudio / Professor:**
    > *"Utilizaremos `@dataclass` e `Enum`. No `__post_init__`, protegemos o domínio contra valores negativos ou percentuais acima de 100%. Nos métodos `pode_ser_aplicado_ao_pedido` e `calcular_desconto`, garantimos que o total da compra nunca fique negativo."*

### Cena 6: Testando a Implementação no `main.py` e Daily 1 (90:00 - 100:00)
*   **Visual:** [SPLIT-SCREEN] Professor demonstrando a criação do script `main.py` no VS Code e executando `python3 main.py` no terminal integrado, mostrando o cálculo do desconto e o bloqueio da exceção de valor mínimo.
*   **Áudio / Professor:**
    > *"Agora vem o teste da nossa entrega: criamos um script simples `main.py` na raiz do projeto para instanciar o cupom e executar nossos métodos. Vejam o resultado no terminal: para um pedido de R$ 100.00, o desconto de 10% calcula exatamente R$ 10.00. E quando tentamos aplicar em um carrinho de R$ 30.00, o sistema dispara nossa exceção ValorMinimoNaoAtingidoError com a mensagem formatada! Missão cumprida na primeira aula. Registrem a Daily 1 e nos vemos na Aula 25 para criar a persistência no SQLite!"*
