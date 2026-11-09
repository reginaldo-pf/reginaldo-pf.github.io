# Plano de Aula: Aula 24 - Casos de Uso, Diagrama de Classes e Início da Codificação (Sprint 04 - Encontro 1)

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá
*   **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema da Sprint:** Construção de Artefatos de Software: Da Análise de Requisitos e Modelagem Estrutural ao Início da Codificação em Python (Sprint 04: BiblioTauá).
*   **Encontro 1:** Aulas 1 e 2 de 50 minutos (Total: 100 minutos) — Semana 1.
*   **Referências Básicas:**
    *   GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora, **Capítulo 3 (Diagrama de Casos de Uso) e Capítulo 4 (Diagrama de Classes)**.
    *   PRESSMAN, Roger S.; MAXIM, Bruce R. *Engenharia de Software: Uma Abordagem Profissional*. 8ª Ed. Porto Alegre: AMGH, **Capítulos 3, 5, 8 e 9**.

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o estudante a atuar como desenvolvedor de software júnior em uma equipe ágil, dominando a transição completa entre a especificação comportamental (**Diagrama de Casos de Uso e DUC**) e a modelagem estrutural (**Diagrama de Classes UML**), iniciando imediatamente a implementação prática do núcleo de regras de negócio em Python (hierarquia de exceções customizadas e entidade de domínio `Cupom`).

### Objetivos Específicos
*   **Compreender a dinâmica de equipe e ritos da Sprint:** Reconhecer o papel do desenvolvedor na *Sprint Planning*, assumindo a responsabilidade pela `TASK-204: Motor de Validação e Aplicação de Cupons`.
*   **Analisar o Diagrama de Casos de Uso (UML 2):** Identificar fronteiras do sistema, atores do cotidiano (`Cliente / Estudante`), casos de uso associados (`UC02 - Finalizar Pedido`, `UC04 - Aplicar Cupom`, `UC05 - Validar Regras`) e os estereótipos `<<extend>>` e `<<include>>`.
*   **Dissecar a Documentação de Caso de Uso (DUC):** Mapear o caminho feliz, fluxos alternativos (desconto percentual vs. fixo) e os 4 fluxos de exceção (cupom inativo, expirado, esgotado ou subtotal mínimo não atingido).
*   **Modelar o Domínio no Diagrama de Classes (UML 2):** Compreender o ecossistema existente da livraria (`Cliente`, `Livro`, `ItemPedido`, `Pedido`), projetando a nova entidade `Cupom`, a enumeração `TipoDesconto`, seus atributos privados, métodos de negócio e a associação $0..1$ com o pedido.
*   **Iniciar a Implementação Prática (Mão na Massa):**
    *   Codificar a hierarquia de exceções de domínio ricas em `exceptions.py`, herdando de `BiblioTauaException`.
    *   Codificar a entidade de domínio `Cupom` em `models/cupom.py`, implementando validações de inicialização (`__post_init__`), métodos de guarda (`esta_expirado`, `atingiu_limite_usos`, `pode_ser_aplicado_ao_pedido`) e cálculo de desconto (`calcular_desconto`).
*   **Validar a Implementação no `main.py`:** Testar as regras de negócio executando `python3 main.py`, constatando o cálculo correto do desconto e o disparo da exceção de valor mínimo.
*   **Registrar a Daily Standup 1:** Documentar os avanços no diário de bordo do `guia_desenvolvedor.md`.

---

## ⏱️ 2. Cronograma do Encontro (100 Minutos: Aulas 1 e 2)

| Bloco | Duração | Conteúdo Programático e Metodologia | Recursos e Artefatos |
| :--- | :---: | :--- | :--- |
| **Briefing & Casos de Uso** | 00 - 25 min | **Abertura da Sprint 04 & Modelagem de Casos de Uso (UML)**<br>• Fala da Tech Lead Aline Mendes e atribuição da `TASK-204`.<br>• Apresentação do ecossistema da Livraria BiblioTauá.<br>• Diagrama de Casos de Uso: fronteira, ator `Cliente`, `UC02`, `UC04` e `UC05` (`<<extend>>` e `<<include>>`).<br>• Dissecação da DUC: Caminho feliz, FA01, FA02 e fluxos de exceção FE01 a FE04. | Slides 1 a 7<br>Diagrama de UC TikZ<br>Tabela DUC |
| **Diagrama de Classes & Arquitetura** | 25 - 45 min | **Modelagem Estrutural & Arquitetura de Pastas**<br>• Diagrama de Classes UML completo do BiblioTauá (`Cliente`, `Livro`, `ItemPedido`, `Pedido`, `Cupom`).<br>• Assinatura de métodos, tipos e visibilidade.<br>• **Mapa da Arquitetura do Projeto:** Árvore de arquivos e camadas.<br>• **Simulação Real:** Por que o projeto possui arquivos pré-existentes da v0.3.0 e qual o foco novo da `TASK-204`. | Slides 8 a 11<br>Diagrama de Classes TikZ<br>Árvore Arquitetural |
| **Mão na Massa: Exceções** | 45 - 65 min | **Implementação Prática: Exceções de Domínio**<br>• Por que criar exceções customizadas em vez de usar `Exception` genérica?<br>• Codificação de `exceptions.py` a partir do projeto base (`projeto_aluno.zip`):<br>  - `BiblioTauaException`, `CupomInvalidoError`<br>  - `CupomInexistenteError`, `CupomInativoError`, `CupomExpiradoError`<br>  - `CupomEsgotadoError`, `ValorMinimoNaoAtingidoError`.<br>• Rastreabilidade direta com os fluxos FE01 a FE04 da DUC. | Slide 12<br>VS Code / Python<br>`exceptions.py` |
| **Mão na Massa: Entidade Cupom** | 65 - 90 min | **Implementação Prática: Modelo `Cupom` em Python**<br>• Criação de `models/cupom.py` com `@dataclass` e `Enum`.<br>• Validações de integridade no método especial `__post_init__`.<br>• Implementação dos métodos de negócio:<br>  - `esta_expirado()`, `atingiu_limite_usos()`<br>  - `pode_ser_aplicado_ao_pedido()` com disparo das exceções<br>  - `calcular_desconto()` com validação do valor mínimo e teto financeiro.<br>• Criação do script `main.py` e execução dos testes no terminal (`python3 main.py`). | Slides 13 a 16<br>`models/cupom.py`<br>`main.py`<br>Terminal Bash |
| **Daily Standup & Encerramento** | 90 - 100 min | **Registro Ágil & Preparação para o Encontro 2**<br>• Preenchimento da Daily 1 no `guia_desenvolvedor.md`.<br>• Alinhamento para a Aula 25: Diagrama Entidade-Relacionamento e Repositório SQLite (`CupomRepository`). | Slides 17 e 18<br>Template Daily 1 |

---

## 🛠️ 3. Estratégia Metodológica e Papéis

*   **Abordagem Ágil Prática:** A teoria de modelagem UML (Casos de Uso e Classes) é apresentada de forma ágil e focada na primeira metade da aula (45 min), conectando-se imediatamente à codificação orientada a objetos (45 min).
*   **Domínio Cotidiano:** O cenário de compras de livros didáticos e literatura na livraria do campus mantém o estudante concentrado nos princípios de engenharia e na lógica do código.
*   **Rastreabilidade Bidirecional:** Cada exceção em `exceptions.py` e método em `models/cupom.py` tem origem comprovada nos requisitos da DUC e nos atributos do Diagrama de Classes.

---

## 📋 4. Avaliação e Evidências de Aprendizagem

*   **Evidência 1:** Arquivo `exceptions.py` implementado com a hierarquia completa de erros da sprint.
*   **Evidência 2:** Arquivo `models/cupom.py` implementado com enum `TipoDesconto`, validações de inicialização e métodos operacionais.
*   **Evidência 3:** Criação e execução com sucesso do arquivo `main.py` demonstrando a validação do cupom e o tratamento de exceções.
*   **Evidência 4:** Registro formal da Daily 1 no `guia_desenvolvedor.md`.
