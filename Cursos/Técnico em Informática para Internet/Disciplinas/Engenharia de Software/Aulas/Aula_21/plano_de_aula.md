# Plano de Aula: Aula 21 - Aprofundamento no Diagrama de Classes e Diagrama de Atividades

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá
*   **Professor:** Reginaldo Pereira Fernandes
*   **Tema:** Aprofundamento Estrutural no Diagrama de Classes (Associações Complexas, Interfaces, Estereótipos e Mapeamento Objeto-Relacional) e Modelagem Comportamental de Fluxos com o Diagrama de Atividades.
*   **Referência Básica:** GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora, **Capítulos 4 e 10**.
*   **Duração:** 100 minutos (2 horas-aula de 50 minutos).

---

## 🎯 1. Objetivos da Aula

### Objetivo Geral
Capacitar os estudantes a modelarem a estrutura estática de domínio de aplicações para a Internet utilizando recursos avançados do **Diagrama de Classes** (Capítulo 4) e a representarem fluxos procedurais, regras de decisão, paralelismo e responsabilidades entre atores/camadas com o **Diagrama de Atividades** (Capítulo 10) da UML 2.

### Objetivos Específicos
*   **Especificar atributos e assinaturas de operações:** Utilizar atributos derivados (`/`), valores iniciais, multiplicidade em atributos, atributos estáticos (sublinhados) e restrições (`{readOnly}`, OCL).
*   **Dominar os relacionamentos do Diagrama de Classes:** Aplicar associações unárias (reflexivas), binárias, ternárias ($n$-árias), multiplicidades, papéis e navegabilidade.
*   **Diferenciar Agregação e Composição:** Distinguir relações Todo-Parte fracas (losango vazio $\lozenge$) de relações Todo-Parte fortes com acoplamento de ciclo de vida (losango preenchido $\blacklozenge$).
*   **Aplicar Classes Associativas, Interfaces e Estereótipos Arquiteturais:** Modelar atributos próprios de ligações `N:N` (`Classe Associativa` vs. `Classe Intermediária`), contratos (`<<interface>>`, Dependência e Realização), enumerações (`<<enumeration>>`) e estereótipos MVC/ECB (`<<boundary>>`, `<<control>>`, `<<entity>>`), além de compreender noções de mapeamento objeto-relacional (`<<Table>>`, `Repository` e `DAO`).
*   **Modelar fluxos de controle e de objetos no Diagrama de Atividades:** Utilizar Nó Inicial, Nós de Ação, Fluxos de Controle, Nós de Decisão/Fusão com condições de guarda, Nós de Bifurcação/União (*Fork/Join*), Final de Atividade vs. Final de Fluxo, Nós de Objeto, Alfinetes (*Pins*), Exceções e Partições (*Swimlanes* / Raias).

---

## ⏱️ 2. Cronograma da Aula (100 Minutos)

| Bloco | Conteúdo e Atividades | Recursos / Figuras do Livro |
| :--- | :--- | :--- |
| **00 - 25 min** | **Aprofundamento no Diagrama de Classes - Parte 1 (Cap. 4)**<br>• Detalhamento de Atributos (`/derivados`, estáticos, `{readOnly}`) e Assinaturas de Operações.<br>• Associações Unária/Reflexiva (com papéis), Binária (multiplicidade, navegabilidade e *class-owned end*) e Ternária.<br>• Relacionamentos Todo-Parte: **Agregação ($\lozenge$)** vs. **Composição ($\blacklozenge$)**.<br>• Generalização/Especialização e Classes Abstratas. | Slides 1 a 10<br>**Fig. 4.1 a 4.12** |
| **25 - 45 min** | **Aprofundamento no Diagrama de Classes - Parte 2 (Cap. 4)**<br>• Classe Associativa vs. Classe Intermediária e Associação Qualificada.<br>• Dependência, Realização e Interfaces Fornecidas/Requeridas (`<<interface>>`).<br>• Restrições e OCL (*Object Constraint Language*).<br>• Estereótipos (`<<enumeration>>`, `<<boundary>>`, `<<control>>`, `<<entity>>`).<br>• Modelo Conceitual vs. Modelo de Domínio, Mapeamento Relacional (`<<Table>>`) e Padrões `Repository` e `DAO`.<br>• Demonstração prática com `exemplo_classes_atividades.py`. | Slides 11 a 19<br>**Fig. 4.13 a 4.18, 4.22, 4.25, 4.38, 4.44, 4.51, 4.60, 4.66, 4.68, 4.72**<br>`exemplo_classes_atividades.py` |
| **45 - 70 min** | **Diagrama de Atividades (Cap. 10)**<br>• Finalidade: modelagem de algoritmos, workflows e processos de casos de uso.<br>• Elementos básicos: Atividade, Nó de Ação, Fluxo de Controle, Nó Inicial e Nó de Final de Atividade.<br>• Nó de Decisão e Condições de Guarda (`[condição]`).<br>• Concorrência e Paralelismo: Nó de Bifurcação/União (*Fork/Join*) e Final de Fluxo ($\otimes$).<br>• Fluxo de Objetos, Nó de Objeto, Alfinetes (*Pins*), Repositório (`<<datastore>>`), Exceções e Sinais/Eventos.<br>• **Partições de Atividade (*Swimlanes* / Raias)** e Região Interrompível.<br>• Estudos de caso: Sistema Bancário e Sistema de Leilão Via Internet. | Slides 20 a 29<br>**Fig. 10.1 a 10.11, 10.13 a 10.16, 10.19, 10.20, 10.28, 10.32** |
| **70 - 92 min** | **Atividade Prática: Modelagem Estrutural e de Fluxo**<br>• Continuidade do projeto *TauáDelivery Web* iniciado na Aula 20.<br>• **Parte 1:** Análise conceitual (Agregação vs. Composição, Classe Associativa e Fork/Join vs. Decisão).<br>• **Parte 2:** Elaboração do Diagrama de Classes do Domínio de Pedidos e Pagamentos.<br>• **Parte 3:** Elaboração do Diagrama de Atividades com Partições (*Raias*) do caso de uso *UC03 - Finalizar Pedido*. | Slides 30 a 33<br>Guia `atividade_pratica.md` |
| **92 - 100 min**| **Fechamento e Próximos Passos**<br>• Revisão coletiva das soluções e discussão de boas práticas.<br>• Gancho para a Aula 22: *Diagramas de Interação (Sequência e Comunicação) e Diagrama de Máquina de Estados (Caps. 7, 8 e 9)*. | Slide 34 |

---

## 👨‍🏫 3. Roteiro de Slides (Beamer)

*   **Slide 1:** Capa e Identificação da Aula 21.
*   **Slide 2:** Sumário da Aula.
*   **Slide 3:** Do Caso de Uso à Estrutura Interna (Visão Geral do Cap. 4).
*   **Slide 4:** Detalhamento de Atributos e Assinaturas de Operações (`Fig4.1.png`, `Fig4.2.png`, `Fig4.3.png`).
*   **Slide 5:** Associação Unária (Reflexiva) e Uso de Papéis (`Fig4.4.png`, `Fig4.5.png`).
*   **Slide 6:** Associação Binária, Multiplicidade e Navegabilidade (`Fig4.6.png`, `Fig4.7.png`, `Fig4.8.png`).
*   **Slide 7:** Associação Ternária ou N-ária (`Fig4.9.png`).
*   **Slide 8:** Relacionamento Todo-Parte: Agregação (`Fig4.10.png`).
*   **Slide 9:** Relacionamento Todo-Parte Forte: Composição (`Fig4.11.png`).
*   **Slide 10:** Generalização, Especialização e Classes Abstratas (`Fig4.12.png`).
*   **Slide 11:** Classe Associativa vs. Classe Intermediária (`Fig4.13.png`, `Fig4.14.png`).
*   **Slide 12:** Associação Qualificada e Dependência (`Fig4.15.png`, `Fig4.16.png`).
*   **Slide 13:** Realização e Interfaces Fornecidas/Requeridas (`Fig4.18.png`, `Fig4.22.png`).
*   **Slide 14:** Restrições, Atributos Estáticos e OCL (`Fig4.25.png`, `Fig4.28.png`, `Fig4.29.png`).
*   **Slide 15:** Estereótipos: Enumeração e Arquitetura MVC/ECB (`Fig4.38.png`, `Fig4.44.png`, `Fig4.47.png`).
*   **Slide 16:** Estudo de Caso Bancário: Modelo de Domínio Completo (`Fig4.51.png`).
*   **Slide 17:** Estudo de Caso Web: Sistema de Leilão Via Internet (`Fig4.72.png`).
*   **Slide 18:** Persistência, Mapeamento Relacional (`<<Table>>`) e Padrões Repository/DAO (`Fig4.60.png`, `Fig4.66.png`, `Fig4.68.png`).
*   **Slide 19:** Do Modelo ao Código Python (`exemplo_classes_atividades.py`).
*   **Slide 20:** Introdução ao Diagrama de Atividades e Elementos Básicos (`Fig10.1.png` a `Fig10.5.png`).
*   **Slide 21:** Nó de Decisão, Condições de Guarda e Processo Emitir Saldo (`Fig10.6.png`, `Fig10.7.png`).
*   **Slide 22:** Paralelismo (Bifurcação/União - *Fork/Join*) e Final de Fluxo (`Fig10.8.png`, `Fig10.9.png`).
*   **Slide 23:** Fluxo de Objetos, Nó de Objeto, Alfinetes e Repositório de Dados (`Fig10.10.png`, `Fig10.11.png`, `Fig10.13.png`).
*   **Slide 24:** Tratamento de Exceções, Envio de Sinais e Eventos Temporais (`Fig10.14.png`, `Fig10.15.png`, `Fig10.16.png`).
*   **Slide 25:** Chamada de Comportamento e Chamada de Operação (`Fig10.17.png`, `Fig10.18.png`).
*   **Slide 26:** Partições de Atividade (*Swimlanes* / Raias de Natação) (`Fig10.19.png`).
*   **Slide 27:** Região de Atividade Interrompível e Nós Estruturados (`Fig10.20.png`, `Fig10.22.png`, `Fig10.23.png`).
*   **Slide 28:** Estudo de Caso Bancário: Atividade Realizar Saque (`Fig10.28.png`).
*   **Slide 29:** Estudo de Caso Web: Atividade Realizar Leilão Via Internet (`Fig10.32.png`).
*   **Slide 30:** Atividade Prática: Proposta Estrutural e Comportamental (*TauáDelivery Web*).
*   **Slide 31:** Exemplo Resolvido de Apoio 1: Modelo de Classes do Subsistema de Cardápio (`modelagem_classes_apoio.png`).
*   **Slide 32:** Exemplo Resolvido de Apoio 2: Diagrama de Atividades com Raias do Carrinho (`modelagem_atividade_apoio.png`).
*   **Slide 33:** Orientações para Entrega das Partes 1, 2 e 3.
*   **Slide 34:** Conclusão e Próximos Passos (Aula 22).

---

## 💻 4. Código de Apoio

O arquivo [`exemplo_classes_atividades.py`](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/exemplo_classes_atividades.py) implementa em Python os modelos dos Capítulos 4 e 10 (`Funcionario` com associação reflexiva, `Pessoa`/`PessoaFisica` e `ContaComum` com agregação e atributo derivado `/saldoConta`, `RevistaCientifica`/`Edicao`/`Artigo` com composição forte, `Ator`/`Filme`/`Atua` com classe associativa, interface `Pagamento` com realização polimórfica e simulação passo a passo do Diagrama de Atividade `Emitir Saldo`).

---

## 📝 5. Atividade Prática

A atividade documentada em [`atividade_pratica.md`](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/atividade_pratica.md) dá continuidade ao projeto *TauáDelivery Web*, guiando os alunos na construção do **Diagrama de Classes de Domínio** e do **Diagrama de Atividades com Partições (Raias)** para o processo de fechamento e pagamento de pedidos.
