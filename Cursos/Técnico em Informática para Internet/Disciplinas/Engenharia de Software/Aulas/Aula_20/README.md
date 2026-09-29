# Aula 20: Introdução à UML, Revisão de OO e Diagrama de Casos de Uso

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá
*   **Professor:** Reginaldo Pereira Fernandes
*   **Livro-Texto Base:** GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora (**Capítulos 1, 2 e 3**).
*   **Duração da Aula:** 100 minutos (2 horas-aula de 50 minutos).

---

## 🎯 Visão Geral da Aula

Esta aula estabelece a fundamentação para a modelagem visual de software para a Internet, integrando os **Capítulos 1, 2 e 3** da obra de Gilleanes Guedes:

1.  **Capítulo 1 (Introdução à UML):**
    *   Necessidade da modelagem e o exemplo da construção civil;
    *   Elicitação de requisitos funcionais e não funcionais;
    *   Prototipação rápida para alinhamento com clientes;
    *   Histórico dos autores da UML (Booch, Rumbaugh, Jacobson), padronização pelo OMG e taxonomia oficial dos **14 diagramas da UML 2** (7 estruturais e 7 comportamentais/interação).
2.  **Capítulo 2 (Revisão de Orientação a Objetos):**
    *   Abstração, classificação e instanciação;
    *   Anatomia da classe na UML (3 compartimentos: Nome, Atributos e Métodos);
    *   Modificadores de visibilidade (`+` público, `-` privado, `#` protegido, `~` pacote) e encapsulamento;
    *   Herança simples e múltipla (caso do `Ornitorrinco`);
    *   Polimorfismo e sobrescrita de métodos (caso bancário `ContaComum` vs. `ContaEspecial`);
    *   Mapeamento conceitual para código Python no arquivo `exemplo_poo.py`.
3.  **Capítulo 3 (Diagrama de Casos de Uso):**
    *   Visão externa e captura de requisitos funcionais;
    *   Identificação e representação de Atores (humanos e sistemas externos);
    *   Casos de Uso (sintaxe de verbo no infinitivo + substantivo);
    *   Associações diretas e Generalização entre Atores e entre Casos de Uso;
    *   Relacionamentos essenciais:
        *   **Inclusão (`<<include>>`):** execução obrigatória de rotinas comuns (`CasoBase ---> <<include>> ---> CasoIncluido`);
        *   **Extensão (`<<extend>>`):** execução condicional ou opcional (`CasoExtensor ---> <<extend>> ---> CasoBase`);
        *   Pontos de extensão (*Extension Points*) e condições de guarda;
    *   Fronteira do Sistema (*System Boundary*);
    *   Documentação formal de Casos de Uso (Pré/Pós-condições, Fluxo Principal, Fluxos Alternativos e Fluxos de Exceção);
    *   Estudos de caso reais do livro: Sistema de Controle Bancário, Telefonia Celular e Leilão Via Internet.

---

## 📂 Guia de Artefatos Disponíveis

Clique nos links abaixo para acessar os arquivos da aula:

1.  📖 **[Plano de Aula](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/plano_de_aula.md):**
    Documento completo de planejamento da aula de 100 minutos contendo objetivos, cronograma por blocos e roteiro de slides Beamer.
2.  📊 **[Slides da Apresentação em PDF](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/slides_aula.pdf):**
    Apresentação completa de 22 slides compilada em LaTeX Beamer (`Madrid` / `whale`) contendo todas as figuras oficiais dos capítulos 1, 2 e 3 do livro.
3.  📄 **[Código-Fonte dos Slides em LaTeX](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/slides_aula.tex):**
    Arquivo `.tex` estruturado, modular e compilável sem advertências.
4.  📝 **[Atividade Prática: Modelagem de Casos de Uso](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/atividade_pratica.md):**
    Guia contendo a lista formal de requisitos **RF01 a RF13** do sistema *TauáDelivery Web* para elaboração do Diagrama de Casos de Uso e especificação técnica textual de cenários (com rubrica de avaliação e gabarito).
5.  🐍 **[Código em Python: Mapeamento POO e UML](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/exemplo_poo.py):**
    Implementação em Python das classes conceituais apresentadas nos capítulos 1 e 2 do livro (`Pessoa`, `Animal`, `Ornitorrinco` e `ContaComum`/`ContaEspecial`), demonstrando encapsulamento, herança múltipla e polimorfismo.
6.  🖼️ **[Diretório de Imagens do Livro](file:///home/reginaldo-fernandes/Aulas/Cursos/T%C3%A9cnico%20em%20Inform%C3%A1tica%20para%20Internet/Disciplinas/Engenharia%20de%20Software/Aulas/Aula_20/imagens):**
    Conjunto com as imagens oficiais dos capítulos 1, 2 e 3 extraídas do arquivo EPUB.

---

## ⚡ Comandos para Execução e Compilação

### Execução do Código Python
Para executar o exemplo de POO demonstrando o comportamento em tempo de execução:

```bash
python3 exemplo_poo.py
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
| **1. Contextualização (Cap. 1)** | 15 min | O paradoxo da construção civil, elicitação de requisitos e prototipação. |
| **2. Taxonomia & Revisão de OO (Caps. 1 e 2)** | 15 min | Histórico, 14 diagramas da UML 2 e revisão de OO com o exemplo `exemplo_poo.py`. |
| **3. Diagrama de Casos de Uso (Cap. 3)** | 35 min | Atores, Casos de Uso, Associações, Inclusão (`<<include>>`), Extensão (`<<extend>>`), Fronteira e Especificação Textual. |
| **4. Atividade Prática** | 25 min | Modelagem visual do *TauáDelivery Web* a partir dos requisitos RF01 a RF13 e documentação do caso de uso *UC03*. |
| **5. Síntese e Fechamento** | 10 min | Discussão coletiva, alinhamento dos erros comuns e introdução à Aula 21. |
