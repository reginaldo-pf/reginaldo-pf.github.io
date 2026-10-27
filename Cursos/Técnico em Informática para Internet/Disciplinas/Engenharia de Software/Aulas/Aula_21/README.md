# Aula 21: Aprofundamento no Diagrama de Classes e Diagrama de Atividades

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá
*   **Professor:** Reginaldo Pereira Fernandes
*   **Livro-Texto Base:** GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora (**Capítulos 4 e 10**).
*   **Duração da Aula:** 100 minutos (2 horas-aula de 50 minutos).

---

## 🎯 Visão Geral da Aula

Esta aula aprofunda a modelagem estrutural estática e a modelagem comportamental de fluxos e processos na UML 2, integrando os **Capítulos 4 e 10** da obra de Gilleanes Guedes:

1.  **Capítulo 4 (Diagrama de Classes em Detalhes):**
    *   Detalhamento de atributos (`/derivados`, multiplicidade `[0..1]`, valores iniciais, atributos estáticos sublinhados e restrição `{readOnly}`) e assinaturas de operações;
    *   Associações Unária/Reflexiva (com papéis), Binária (multiplicidade, navegabilidade e *class-owned end*) e Ternária ($n$-ária);
    *   Relacionamentos Todo-Parte: **Agregação ($\lozenge$)** vs. **Composição ($\blacklozenge$)** e acoplamento de ciclo de vida;
    *   Generalização/Especialização e Classes Abstratas (nome em *itálico*);
    *   **Classe Associativa** vs. **Classe Intermediária** e Associação Qualificada;
    *   Dependência (`- - ->`), Realização e Interfaces Fornecidas/Requeridas (`<<interface>>`);
    *   Restrições formais em **OCL (*Object Constraint Language*)**;
    *   Estereótipos de Classes: `<<enumeration>>` e arquitetura em camadas MVC/ECB (`<<boundary>>`, `<<control>>`, `<<entity>>`);
    *   Persistência, Mapeamento Objeto-Relacional (`<<Table>>`, `<<PK>>`, `<<FK>>`) e Padrões **Repository** e **DAO**.
2.  **Capítulo 10 (Diagrama de Atividades):**
    *   Modelagem de algoritmos, workflows e fluxos internos de casos de uso;
    *   Atividade, Nó de Ação, Fluxo de Controle, Nó Inicial ($\bullet$) e Nó de Final de Atividade ($\odot$);
    *   Nó de Decisão/Fusão ($\lozenge$) e Condições de Guarda (`[condição]`);
    *   Concorrência e Paralelismo: Barra de Bifurcação/União (*Fork/Join*) e Nó de Final de Fluxo ($\otimes$);
    *   Fluxo de Objetos, Nó de Objeto (`Classe [Estado]`), Alfinetes (*Pins*) e Repositório de Dados (`<<datastore>>`);
    *   Tratamento de Exceções (fluxo em raio), Envio/Aceitação de Sinais e Eventos Temporais (*Timer*);
    *   Ações de Chamada de Comportamento (subatividades) e Chamada de Operação (`Classe::metodo`);
    *   **Partições de Atividade (*Swimlanes* / Raias de Natação)**, Região Interrompível e Nós Estruturados (`<<conditional>>`, `<<loop node>>`).

---

## 📂 Guia de Artefatos Disponíveis

Clique nos links abaixo para acessar os arquivos da aula:

1.  📖 **[Plano de Aula](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/plano_de_aula.md):**
    Planejamento pedagógico completo da aula de 100 minutos contendo objetivos, cronograma em 5 blocos e roteiro detalhado dos 34 slides.
2.  📊 **[Slides da Apresentação em PDF](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/slides_aula.pdf):**
    Apresentação de 34 slides compilada em LaTeX Beamer (`Madrid` / `whale`) ilustrada com as figuras oficiais dos Capítulos 4 e 10 do livro e os diagramas de apoio.
3.  📄 **[Código-Fonte dos Slides em LaTeX](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/slides_aula.tex):**
    Arquivo `.tex` modular compilável sem advertências.
4.  📝 **[Atividade Prática: Classes e Atividades](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/atividade_pratica.md):**
    Estudo prático dando continuidade ao sistema *TauáDelivery Web* com exemplo resolvido de apoio, desafios conceituais, construção do Diagrama de Classes de Domínio e do Diagrama de Atividades com Partições (com rubrica e gabarito comentado).
5.  🐍 **[Código em Python: Classes, Associações e Fluxo de Atividades](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/exemplo_classes_atividades.py):**
    Implementação em Python demonstrando associação reflexiva com papéis, agregação, composição forte, atributos derivados (`/`), restrições OCL, classe associativa, realização de interface (`<<interface>> Pagamento`) e execução passo a passo do Diagrama de Atividade *Emitir Saldo*.
6.  🖼️ **[Diretório de Imagens do Livro e Modelos de Apoio](file:///home/reginaldo/aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_21/imagens):**
    Galeria contendo as 108 figuras oficiais dos Capítulos 4 e 10 extraídas do livro (`Fig4.1.png` a `Fig4.74.png` e `Fig10.1.png` a `Fig10.34.png`) e os diagramas resolvidos de apoio (`modelagem_classes_apoio.png` e `modelagem_atividade_apoio.png`).

---

## ⚡ Comandos para Execução e Compilação

### Execução do Código Python
Para executar a demonstração de relacionamentos de classes e simulação de atividades:

```bash
python3 exemplo_classes_atividades.py
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
| **1. Diagrama de Classes - Parte 1 (Cap. 4)** | 25 min | Atributos (`/derivados`, `{readOnly}`), Associações (Unária, Binária, Ternária), Agregação ($\lozenge$), Composição ($\blacklozenge$) e Herança. |
| **2. Diagrama de Classes - Parte 2 (Cap. 4)** | 20 min | Classe Associativa vs. Intermediária, Interfaces (`<<interface>>`), OCL, Estereótipos MVC/ECB, Mapeamento Relacional (`Repository`/`DAO`) e código `exemplo_classes_atividades.py`. |
| **3. Diagrama de Atividades (Cap. 10)** | 25 min | Ações, Decisões e Guardas, Paralelismo (*Fork/Join*), Final de Fluxo, Fluxo de Objetos, Exceções, Sinais e Partições (*Swimlanes* / Raias). |
| **4. Atividade Prática** | 22 min | Modelagem do Diagrama de Classes de Domínio e do Diagrama de Atividades com Raias (*UC03 - Finalizar Pedido*) do *TauáDelivery Web*. |
| **5. Síntese e Fechamento** | 08 min | Discussão do gabarito e introdução à Aula 22 (Diagramas de Sequência, Comunicação e Máquina de Estados). |
