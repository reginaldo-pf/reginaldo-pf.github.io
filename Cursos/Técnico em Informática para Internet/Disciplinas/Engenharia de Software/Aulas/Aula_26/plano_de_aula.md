# Plano de Aula: Aula 26 - Orquestração do Negócio: Diagrama de Sequência e Integração do Pedido (Sprint 04 - Encontro 3)

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá
*   **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema da Sprint:** Construção de Artefatos de Software: Da Modelagem Dinâmica (Diagrama de Sequência) aos Serviços de Aplicação e Integração de Domínio (Sprint 04: BiblioTauá).
*   **Encontro 3:** Aulas 5 e 6 de 50 minutos (Total: 100 minutos) — Semana 2.
*   **Referências Básicas:**
    *   GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora, **Capítulo 5 (Diagrama de Sequência)**.
    *   PRESSMAN, Roger S.; MAXIM, Bruce R. *Engenharia de Software: Uma Abordagem Profissional*. 8ª Ed. Porto Alegre: AMGH, **Capítulos 11 e 12 (Projeto de Componentes e Serviços)**.

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o estudante a compreender e projetar o comportamento temporal de sistemas de software através do **Diagrama de Sequência UML**, implementando os serviços de aplicação (`CalculadoraDescontoService` e `CheckoutService`) e integrando a entidade `Cupom` ao agregado `Pedido`, garantindo transacionalidade e coerência entre regras de negócio, estoque e faturamento.

### Objetivos Específicos
*   **Interpretar o Diagrama de Sequência (UML 2):** Compreender linhas de vida (*lifelines*), mensagens síncronas com argumentos, mensagens de resposta (*returns*), caixas de ativação e fluxo temporal ordenado entre componentes.
*   **Modelar o Fluxo Dinâmico do Checkout:** Mapear a sequência de chamadas entre a interface do cliente, o serviço orquestrador `CheckoutService`, os repositórios (`CupomRepository`, `LivroRepository`, `PedidoRepository`) e as entidades de negócio.
*   **Implementar a `CalculadoraDescontoService` (`services/calculadora_desconto.py`):** Desacoplar os cálculos matemáticos específicos das entidades de banco.
*   **Integrar o Cupom ao Agregado `Pedido` (`models/pedido.py`):**
    *   Adicionar os atributos `cupom: Optional[Cupom]` e `desconto_aplicado: float`.
    *   Implementar o método `aplicar_cupom(cupom)`.
    *   Atualizar o cálculo da propriedade dinâmica `total`: $\text{total} = \max(\text{subtotal} - \text{desconto\_aplicado}, 0.0)$.
*   **Implementar o Serviço Orquestrador `CheckoutService` (`services/checkout_service.py`):** Coordenar em uma única operação a validação do cupom, abatimento no pedido, débito no estoque do acervo e persistência transacional.
*   **Registrar a Daily Standup 3:** Documentar os avanços de integração no diário de bordo do `guia_desenvolvedor.md`.

---

## ⏱️ 2. Cronograma do Encontro (100 Minutos: Aulas 5 e 6)

| Bloco | Duração | Conteúdo Programático e Metodologia | Recursos e Artefatos |
| :--- | :---: | :--- | :--- |
| **Abertura & Sequência UML** | 00 - 25 min | **Modelagem Dinâmica: Diagrama de Sequência UML 2**<br>• Por que o Diagrama de Classes não é suficiente para entender o tempo?<br>• Anatomia do Diagrama de Sequência: Lifelines, Mensagens, Ativações.<br>• O fluxo dinâmico da `TASK-204`: quem chama quem durante a compra de um livro com cupom? | Slides 1 a 7<br>Diagrama Sequência TikZ |
| **Serviços & Atividades** | 25 - 45 min | **Arquitetura de Serviços e Fluxo de Decisão**<br>• O papel dos Domain Services vs Application Services.<br>• Diagrama de Atividades: tomada de decisão no checkout com cupom.<br>• Como coordenar baixa de estoque de livros com abatimento financeiro. | Slides 8 a 12<br>Diagrama Atividades TikZ |
| **Mão na Massa: Calculadora & Pedido** | 45 - 65 min | **Implementação Prática: `CalculadoraDesconto` & `Pedido`**<br>• Criação de `services/calculadora_desconto.py`.<br>• Refatoração de `models/pedido.py`: método `aplicar_cupom(cupom)` e propriedade `total`.<br>• Teste unitário manual da composição do pedido com cupom. | Slides 13 a 17<br>`pedido.py`<br>`calculadora_desconto.py` |
| **Mão na Massa: CheckoutService** | 65 - 90 min | **Implementação Prática: Orquestrador `CheckoutService`**<br>• Codificação de `services/checkout_service.py`.<br>• Fluxo transacional ponta a ponta: busca cupom $\rightarrow$ valida $\rightarrow$ aplica $\rightarrow$ debita estoque $\rightarrow$ registra uso.<br>• Execução de simulação com dados reais da livraria. | Slides 18 a 22<br>`checkout_service.py`<br>Terminal Python |
| **Daily Standup & Encerramento** | 90 - 100 min | **Registro Ágil & Preparação para a Aula 27**<br>• Registro formal da Daily 3 no `guia_desenvolvedor.md`.<br>• Alinhamento para a Aula 27: Pirâmide de Testes (Pytest), CLI interativo e Pull Request formal. | Slides 23 a 25<br>Template Daily 3 |

---

## 🛠️ 3. Estratégia Metodológica e Avaliação

*   **Ponte Dinâmica-Código:** O estudante visualiza cada seta do Diagrama de Sequência virando uma linha de invocação de método em Python.
*   **Transacionalidade e Consistência:** Enfatiza a importância de atomicidade: um pedido não pode ser faturado se o livro estiver sem estoque ou se o cupom tiver esgotado sua cota.
*   **Evidências de Aprendizagem:**
    *   Arquivos `services/calculadora_desconto.py`, `models/pedido.py` e `services/checkout_service.py` integrados e funcionais.
    *   Simulação transacional executada no terminal.
    *   Registro da Daily 3 no diário de bordo.
