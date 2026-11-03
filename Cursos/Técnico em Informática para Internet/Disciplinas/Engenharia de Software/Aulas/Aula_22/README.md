# Aula 22: Diagramas de Interação (Sequência e Comunicação) e Diagrama de Máquina de Estados

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá
*   **Professor:** Reginaldo Pereira Fernandes
*   **Livro-Texto Base:** GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora (**Capítulos 7, 8 e 9**).
*   **Duração da Aula:** 100 minutos (2 horas-aula de 50 minutos).

---

## 🎯 Visão Geral da Aula

Esta aula cobre a modelagem dinâmica comportamental de troca de mensagens e o ciclo de vida reativo de objetos na UML 2, integrando os **Capítulos 7, 8 e 9** da obra de Gilleanes Guedes:

1.  **Capítulo 7 (Diagrama de Sequência):**
    *   Linhas de vida (*Lifelines*), cabeçalho (`objeto:Classe`), linha tracejada vertical e barra de ativação (*foco de controle*);
    *   Atores e tipos de mensagens: **Síncrona ($\blacktriangleright$)**, **Assíncrona ($\rightarrow$)**, **Resposta/Retorno ($\dashrightarrow$)** e **Autochamada (*self-call*)**;
    *   Mensagens Construtoras (`<<create>>` / `new()`) e Destrutoras com marcador de encerramento ($\times$);
    *   **Fragmentos Combinados (*Combined Fragments*):**
        *   `alt` (*Alternatives*): desvios mutuamente exclusivos (\texttt{if-then-else});
        *   `opt` (*Option*): execução condicional simples (\texttt{if});
        *   `loop`: repetições e laços com guardas e contadores;
        *   `par`: processamento concorrente/paralelo;
        *   `break`: tratamento de exceções e quebra de fluxo.
    *   Invariante de Estado (*StateInvariant*), Usos de Interação (`ref`) e Portões (*Gates*);
    *   Integração com persistência em camadas: Padrões **Repository** e **DAO**.
2.  **Capítulo 8 (Diagrama de Comunicação):**
    *   Equivalência semântica com o Diagrama de Sequência sob uma visão topológica e espacial;
    *   Objetos, Vínculos Estruturais (*Links*) e Direção dos Estímulos;
    *   **Numeração Sequencial Hierárquica e Aninhada:** `1`, `1.1`, `1.2`, `1.2.1`, `1.2.1.1` expressando aninhamento de chamadas;
    *   Condições de guarda `[condição]` e expressões de iteração com asterisco (`* [i:=1..n]`);
    *   Análise comparativa detalhada: quando escolher Sequência ou Comunicação.
3.  **Capítulo 9 (Diagrama de Máquina de Estados):**
    *   Conceito de Estado e modelagem do ciclo de vida (*lifecycle*) de entidades reativas;
    *   Estado Inicial ($\bullet$), Estado Simples (retângulo arredondado) e Estado Final ($\odot$);
    *   Sintaxe Canônica da Transição: `gatilho/evento [condição de guarda] / ação de efeito`;
    *   **Atividades Internas do Estado:** compartimento com `entry /` (ao entrar), `do /` (execução contínua) e `exit /` (ao sair);
    *   Transições Internas (sem disparo de `entry`/`exit`) vs. Autotransições (com saída e reentrada);
    *   **Pseudoestados:** Escolha (*Choice* $\lozenge$ com avaliação dinâmica em runtime), Junção (*Junction* $\bullet$ com pré-avaliação estática), Barra de Bifurcação/União (*Fork/Join*), Histórico Raso ($H$) e Profundo ($H^*$), Pontos de Entrada/Saída e Término ($\bigotimes$);
    *   Estados Compostos e Regiões Ortogonais (concorrência).

---

## 📂 Guia de Artefatos Disponíveis

Clique nos links abaixo para acessar os arquivos da aula:

1.  📖 **[Plano de Aula](plano_de_aula.md):**
    Planejamento pedagógico completo da aula de 100 minutos contendo objetivos, cronograma em 5 blocos e roteiro detalhado dos 35 slides.
2.  📊 **[Slides da Apresentação em PDF](slides_aula.pdf):**
    Apresentação de 35 slides compilada em LaTeX Beamer (`Madrid` / `whale`) ilustrada com as figuras oficiais dos Capítulos 7, 8 e 9 do livro e diagramas de apoio.
3.  📄 **[Código-Fonte dos Slides em LaTeX](slides_aula.tex):**
    Arquivo `.tex` modular compilável sem erros (`pdflatex`).
4.  📝 **[Atividade Prática: Interação e Estados](atividade_pratica.md):**
    Estudo prático dando continuidade ao sistema *TauáDelivery Web* com questionário conceitual, Diagrama de Sequência, Diagrama de Comunicação e Diagrama de Máquina de Estados (com gabarito comentado e rubrica de avaliação).
5.  🐍 **[Código em Python: Interação, Despacho e Máquina de Estados](exemplo_interacao_estados.py):**
    Implementação em Python simulando linhas de vida, numeração aninhada hierárquica, máquina de estados finita reativa com atividades `entry`/`exit`, avaliação de guardas e histórico de auditoria.
6.  🖼️ **[Diretório de Imagens do Livro e Modelos de Apoio](imagens/):**
    Galeria contendo as 79 figuras oficiais dos Capítulos 7, 8 e 9 extraídas do livro (`Fig7.*`, `Fig8.*` e `Fig9.*`) e os 3 diagramas resolvidos de apoio (`modelagem_sequencia_apoio.png`, `modelagem_comunicacao_apoio.png` e `modelagem_estados_apoio.png`).
7.  🌐 **[Portal Web da Aula 22](index.html):**
    Página interativa com abas de conteúdo, galeria de slides, visualizador de código com syntax highlighting e atalhos rápidos.

---

## ⚡ Comandos para Execução e Compilação

### Execução da Simulação em Python
Para executar a simulação da troca de mensagens e transições de estado do pedido no terminal:

```bash
python3 exemplo_interacao_estados.py
```

### Compilação dos Slides em LaTeX
Para recompilar o arquivo Beamer gerando o PDF:

```bash
pdflatex -interaction=nonstopmode slides_aula.tex
```

---

## ⏱️ Cronograma da Aula (100 Minutos)

| Bloco | Duração | Descrição do Conteúdo |
| :--- | :---: | :--- |
| **1. Diagrama de Sequência (Cap. 7)** | 25 min | Lifelines, foco de controle, mensagens (síncrona, assíncrona, retorno, construtora, destrutora), Fragmentos Combinados (`alt`, `opt`, `loop`, `par`, `break`), Invariante de Estado, Uso de Interação (`ref`) e Persistência com Repository/DAO. |
| **2. Diagrama de Comunicação (Cap. 8)** | 15 min | Vínculos estruturais (*links*), numeração sequencial aninhada (`1`, `1.1`, `1.2.1`), guardas, iterações, autochamada e comparativo analítico: Sequência vs. Comunicação. |
| **3. Diagrama de Máquina de Estados (Cap. 9)** | 25 min | Estados simples, sintaxe canônica `evento [guarda] / acao`, atividades internas (`entry`, `do`, `exit`), transições internas vs. autotransições, pseudoestados (Escolha vs. Junção, Fork/Join, Histórico $H/H^*$, Término) e demonstração em Python (`exemplo_interacao_estados.py`). |
| **4. Atividade Prática Orientada** | 23 min | Modelagem do *TauáDelivery Web*: Diagrama de Sequência, Diagrama de Comunicação e Ciclo de Vida da entidade `Pedido` com máquina de estados. |
| **5. Síntese e Fechamento** | 12 min | Discussão coletiva das soluções, boas práticas e gancho para a Aula 23 (Diagramas Arquiteturais: Pacotes, Componentes e Implantação). |
