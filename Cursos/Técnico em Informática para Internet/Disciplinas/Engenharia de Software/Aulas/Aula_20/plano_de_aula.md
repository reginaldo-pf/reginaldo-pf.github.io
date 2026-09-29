# Plano de Aula: Aula 20 - Introdução à UML, Revisão de OO e Diagrama de Casos de Uso

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá
*   **Professor:** Reginaldo Pereira Fernandes
*   **Tema:** Introdução à UML, Modelagem Visual de Sistemas, Revisão do Paradigma de Orientação a Objetos e Modelagem com o Diagrama de Casos de Uso.
*   **Referência Básica:** GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora, **Capítulos 1, 2 e 3**.
*   **Duração:** 100 minutos (2 horas-aula de 50 minutos).

---

## 🎯 1. Objetivos da Aula

### Objetivo Geral
Capacitar os estudantes a compreenderem o papel da modelagem no ciclo de vida de sistemas para Internet, dominando a elaboração e interpretação de Diagramas de Casos de Uso e suas especificações textuais segundo as diretrizes da UML 2, apoiados na revisão de Orientação a Objetos.

### Objetivos Específicos
*   **Compreender a necessidade da modelagem:** Analisar os impactos da ausência de modelos formais e diferenciar requisitos funcionais de requisitos não funcionais.
*   **Conhecer a taxonomia da UML 2:** Identificar a divisão oficial dos 14 diagramas em Estruturais e Comportamentais (com foco em Interação).
*   **Revisar os alicerces de Orientação a Objetos:** Compreender atributos, métodos, visibilidade (`+`, `-`, `#`, `~`), herança simples/múltipla e polimorfismo através dos exemplos do livro.
*   **Identificar Atores e Casos de Uso:** Reconhecer quem interage com o sistema e quais serviços o sistema disponibiliza.
*   **Dominar relacionamentos de Casos de Uso:** Aplicar associações simples, generalização de atores/casos de uso, inclusão (`<<include>>`) e extensão (`<<extend>>`).
*   **Documentar Casos de Uso:** Escrever especificações textuais estruturadas contendo pré-condições, pós-condições, fluxo principal, fluxos alternativos e fluxos de exceção a partir de requisitos formais.

---

## ⏱️ 2. Cronograma da Aula (100 Minutos)

| Bloco | Conteúdo e Atividades | Recursos / Figuras do Livro |
| :--- | :--- | :--- |
| **00 - 15 min** | **Contextualização e Introdução à UML (Cap. 1)**<br>• Por que modelar software: a analogia da construção civil.<br>• Elicitação de requisitos funcionais e não funcionais.<br>• Prototipação rápida para validação de escopo. | Slides 1 a 4 |
| **15 - 30 min** | **Taxonomia UML e Revisão de OO (Caps. 1 e 2)**<br>• Os *Three Amigos*, histórico e os 14 diagramas da UML 2.<br>• Revisão de OO: Classes, Atributos, Métodos, Visibilidade, Herança e Polimorfismo.<br>• Apresentação do código demonstrativo `exemplo_poo.py`. | Slides 5 a 9<br>**Fig. 1.15, Fig. 2.1 a 2.7**<br>`exemplo_poo.py` |
| **30 - 65 min** | **Diagrama de Casos de Uso (Cap. 3)**<br>• Papel dos Casos de Uso na engenharia de requisitos.<br>• Atores: humanos e sistemas externos.<br>• Casos de uso: sintaxe (verbo + substantivo) e fronteira de sistema.<br>• Associações e Generalização/Especialização.<br>• **Inclusão (`<<include>>`)**: rotinas obrigatórias compartilhadas.<br>• **Extensão (`<<extend>>`)**: fluxos opcionais e pontos de extensão.<br>• Estrutura de Documentação Formal (Fluxo Principal, Alternativo e Exceção).<br>• Estudos de caso: Sistema Bancário, Telefonia Celular e Leilão Web. | Slides 10 a 20<br>**Fig. 3.1 a 3.17**, **Fig. 3.18, Fig. 3.25** |
| **65 - 90 min** | **Atividade Prática: Modelagem de Casos de Uso**<br>• Execução da atividade com base nos requisitos **RF01 a RF13** do sistema *TauáDelivery Web*.<br>• **Parte 1:** Análise conceitual (atores, fronteira, include e extend).<br>• **Parte 2:** Elaboração do Diagrama de Casos de Uso.<br>• **Parte 3:** Especificação textual do caso de uso *UC03 - Finalizar Pedido*. | Guia `atividade_pratica.md` |
| **90 - 100 min**| **Fechamento e Próximos Passos**<br>• Síntese dos tópicos abordados e correção coletiva.<br>• Gancho para a Aula 21: *Diagrama de Classes em Detalhes e Diagrama de Atividades*. | Slides 21 e 22 |

---

## 👨‍🏫 3. Roteiro de Slides (Beamer)

*   **Slide 1: Capa e Identificação**
    *   **Título:** Aula 20: Introdução à UML, Revisão de OO e Casos de Uso.
    *   **Subtítulo:** Engenharia de Software -- Técnico em Informática para Internet.
*   **Slide 2: Sumário da Aula**
    *   **Tópicos:** Introdução à UML; Taxonomia dos 14 Diagramas; Revisão de OO; Diagrama de Casos de Uso; Atores, Inclusão, Extensão e Fronteira; Documentação de Cenários; Atividade Prática.
*   **Slide 3: Por que Modelar Software? (Capítulo 1)**
    *   **Tópicos:** A analogia da construção civil (casinha vs. edifício); O custo do retrabalho tardio; Fatores de mudança contínua.
*   **Slide 4: Elicitação de Requisitos e Prototipação (Capítulo 1)**
    *   **Tópicos:** Requisitos Funcionais vs. Não Funcionais; Ruídos na comunicação com o cliente; Prototipação rápida (RAD).
*   **Slide 5: Histórico e Taxonomia da UML 2 (Capítulo 1)**
    *   **Tópicos:** Os *Three Amigos* (Booch, Rumbaugh, Jacobson); Padronização pela OMG; Organograma dos 14 diagramas da UML 2 (`imagens/Fig1.15.png`).
*   **Slide 6: Revisão de OO: Classes e Compartimentos (Capítulo 2)**
    *   **Tópicos:** As 3 divisões: Nome, Atributos e Métodos (`imagens/Fig2.1.png`, `imagens/Fig2.2.png` e `imagens/Fig2.3.png`).
*   **Slide 7: Visibilidade e Encapsulamento (Capítulo 2)**
    *   **Tópicos:** Notação UML: `+` público, `-` privado, `#` protegido, `~` pacote (`imagens/Fig2.4.png`).
*   **Slide 8: Herança e Polimorfismo (Capítulo 2)**
    *   **Tópicos:** Generalização/Especialização (`imagens/Fig2.5.png`), herança múltipla e polimorfismo bancário (`imagens/Fig2.7.png`).
*   **Slide 9: Mapeamento Conceitual: Do Modelo ao Código (Capítulo 2)**
    *   **Tópicos:** Apresentação do arquivo `exemplo_poo.py` implementando o modelo de classes em Python.
*   **Slide 10: Introdução ao Diagrama de Casos de Uso (Capítulo 3)**
    *   **Tópicos:** Finalidade central, visão de caixa-preta e captura de requisitos funcionais.
*   **Slide 11: Atores no Diagrama de Casos de Uso (Capítulo 3)**
    *   **Tópicos:** Atores humanos vs. sistemas externos; identificação (`imagens/Fig3.1.png`).
*   **Slide 12: Casos de Uso e Associações (Capítulo 3)**
    *   **Tópicos:** Elipse com verbo no infinitivo; conexões por linha contínua (`imagens/Fig3.2.png` e `imagens/Fig3.3.png`).
*   **Slide 13: Generalização/Especialização (Capítulo 3)**
    *   **Tópicos:** Herança entre casos de uso (`imagens/Fig3.4.png`) e herança entre atores (`imagens/Fig3.5.png`).
*   **Slide 14: Relacionamento de Inclusão (`<<include>>`) (Capítulo 3)**
    *   **Tópicos:** Execução obrigatória; reuso de rotinas comuns; seta base $\rightarrow$ incluído (`imagens/Fig3.7.png`).
*   **Slide 15: Relacionamento de Extensão (`<<extend>>`) (Capítulo 3)**
    *   **Tópicos:** Execução opcional/condicional; seta extensor $\rightarrow$ base (`imagens/Fig3.12.png`).
*   **Slide 16: Pontos de Extensão (Capítulo 3)**
    *   **Tópicos:** Localização exata de disparo no caso base; condições de guarda (`imagens/Fig3.14.png`).
*   **Slide 17: Fronteira do Sistema (Capítulo 3)**
    *   **Tópicos:** Delimitação de escopo interno vs. ambiente externo (`imagens/Fig3.17.png`).
*   **Slide 18: Documentação Textual de Casos de Uso (Capítulo 3)**
    *   **Tópicos:** Ficha técnica padronizada: Pré/Pós-condições, Fluxo Principal, Fluxos Alternativos e Fluxos de Exceção.
*   **Slide 19: Estudo de Caso: Sistema de Telefonia Celular (Capítulo 3)**
    *   **Tópicos:** Análise do diagrama do livro com múltiplos atores (`imagens/Fig3.18.png`).
*   **Slide 20: Estudo de Caso: Sistema de Leilão Via Internet (Capítulo 3)**
    *   **Tópicos:** Aplicação direta em sistemas para Internet (`imagens/Fig3.25.png`).
*   **Slide 21: Atividade Prática: Modelagem de Casos de Uso**
    *   **Tópicos:** Apresentação dos requisitos do sistema *TauáDelivery Web* e entregáveis da atividade.
*   **Slide 22: Conclusão e Próximos Passos**
    *   **Tópicos:** Resumo dos conceitos e introdução à Aula 21.

---

## 💻 4. Código de Apoio

O arquivo [`exemplo_poo.py`](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/exemplo_poo.py) contém a implementação em Python dos modelos de classes dos capítulos 1 e 2 (classes `Pessoa`, `Animal`, `Ornitorrinco` e `ContaComum`/`ContaEspecial`), demonstrando encapsulamento, herança múltipla e polimorfismo.

---

## 📝 5. Atividade Prática

A atividade documentada em [`atividade_pratica.md`](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/atividade_pratica.md) fornece os requisitos formais **RF01 a RF13** do sistema *TauáDelivery Web* e guia os estudantes na:
1.  **Análise Conceitual:** Identificação de atores e justificativa dos relacionamentos `<<include>>` e `<<extend>>`.
2.  **Modelagem Visual:** Elaboração do Diagrama de Casos de Uso completo com fronteira de sistema.
3.  **Especificação Textual:** Redação da ficha técnica formal do caso de uso *UC03 - Finalizar Pedido* (fluxos principal, alternativo e de exceção).
