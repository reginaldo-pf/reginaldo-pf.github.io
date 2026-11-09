# Plano de Aula: Aula 27 - Testes Automatizados (Pytest), Demonstração CLI e Fechamento da Sprint (Sprint 04 - Encontro 4)

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá
*   **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema da Sprint:** Construção de Artefatos de Software: Da Garantia de Qualidade (QA) e Testes Automatizados ao Fechamento Ágil da Sprint (Sprint 04: BiblioTauá).
*   **Encontro 4:** Aulas 7 e 8 de 50 minutos (Total: 100 minutos) — Semana 2.
*   **Referências Básicas:**
    *   PRESSMAN, Roger S.; MAXIM, Bruce R. *Engenharia de Software: Uma Abordagem Profissional*. 8ª Ed. Porto Alegre: AMGH, **Capítulos 17 e 18 (Estratégias e Técnicas de Teste de Software)**.
    *   GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora, **Capítulo 3 (Rastreabilidade de Requisitos)**.

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o estudante a validar rigorosamente a conformidade das regras de negócio através de **testes automatizados com Pytest**, demonstrar a solução funcionando no terminal interativo (**CLI**) da livraria universitária, consolidar os commits semânticos no Git e formalizar a entrega através do **Pull Request** e do **Relatório da Sprint Quinzenal** (Sprint Review e Retrospectiva) para a liderança técnica.

### Objetivos Específicos
*   **Compreender a Pirâmide de Testes de Software:** Diferenciar testes unitários isolados, testes de integração com banco de dados em memória e testes de ponta a ponta.
*   **Projetar a Matriz de Rastreabilidade:** Mapear cada especificação da DUC (Caminho Feliz, FA01, FA02 e FE01 a FE04) para seu método de teste correspondente no Pytest.
*   **Construir Fixtures Isoladas no Pytest:** Utilizar *fixtures* com banco SQLite em memória (`:memory:`) para garantir repetibilidade sem efeitos colaterais no disco.
*   **Implementar Casos de Teste com `pytest.raises`:** Validar o lançamento preciso das exceções `CupomInvalidoError`, `CupomExpiradoError`, `CupomEsgotadoError`, `ValorMinimoNaoAtingidoError` e `CupomInexistenteError`.
*   **Executar e Homologar no CLI Interativo (`main.py`):** Realizar compras simuladas de livros no acervo da livraria, aplicando cupons válidos e inválidos com feedback visual.
*   **Consolidar o Ciclo Ágil com Git:** Elaborar o Pull Request (PR) com template formal e consolidar a Sprint Review e Retrospectiva no `guia_desenvolvedor.md`.

---

## ⏱️ 2. Cronograma do Encontro (100 Minutos: Aulas 7 e 8)

| Bloco | Duração | Conteúdo Programático e Metodologia | Recursos e Artefatos |
| :--- | :---: | :--- | :--- |
| **Abertura & Pirâmide de Testes** | 00 - 25 min | **Garantia de Qualidade (QA) e Rastreabilidade**<br>• Por que testes manuais não são suficientes na engenharia de software?<br>• Diagrama da Pirâmide de Testes e Matriz de Rastreabilidade DUC $\leftrightarrow$ Testes.<br>• Estrutura do Pytest: fixtures, asserções e `pytest.raises`. | Slides 1 a 7<br>Diagrama Pirâmide TikZ |
| **Git Flow & Ciclo de Entrega** | 25 - 45 min | **Git Flow e Commits Semânticos**<br>• Diagrama de Git Flow: Da branch `feature/` ao Pull Request e tag de release `v0.4.0`.<br>• O padrão Conventional Commits (`feat:`, `test:`, `fix:`, `docs:`).<br>• Critérios de Aceite formais para homologação da Tech Lead Aline Mendes. | Slides 8 a 12<br>Diagrama Git Flow TikZ |
| **Mão na Massa: Pytest Automatizado** | 45 - 70 min | **Construção e Execução da Suíte de Testes (`test_cupons.py`)**<br>• Implementação de fixtures com SQLite em memória.<br>• Codificação de testes para caminho feliz e os 4 fluxos de exceção.<br>• Teste de integração com decremento de estoque e baixa atômica de cupons.<br>• Execução no terminal: `pytest bibliotaua/tests` (100% verde). | Slides 13 a 18<br>`test_cupons.py`<br>Terminal Pytest |
| **Mão na Massa: Demonstração no CLI** | 70 - 85 min | **Homologação Interativa via Terminal (`main.py`)**<br>• Execução do sistema interativo da Livraria BiblioTauá.<br>• Simulação de compra de livros e aplicação de cupom com feedback visual discriminado (Subtotal, Desconto, Total Líquido). | Slides 19 a 22<br>`main.py`<br>Terminal Bash |
| **Pull Request & Fechamento da Sprint** | 85 - 100 min | **Fechamento Ágil: Pull Request e Relatório da Sprint**<br>• Redação formal do Pull Request para o Tech Lead.<br>• Preenchimento da Sprint Review e Sprint Retrospective no `guia_desenvolvedor.md`.<br>• Celebração da entrega da Sprint 04! | Slides 23 a 25<br>Template de PR<br>Relatório da Sprint |

---

## 🛠️ 3. Estratégia Metodológica e Avaliação

*   **Evidências de Aprendizagem:**
    *   Suíte de 10 testes no Pytest executando com 100% de sucesso.
    *   Demonstração prática no CLI interativo (`main.py`).
    *   Documento do Pull Request e Relatório da Sprint no `guia_desenvolvedor.md`.
    *   Histórico consolidado de Commits Semânticos.
