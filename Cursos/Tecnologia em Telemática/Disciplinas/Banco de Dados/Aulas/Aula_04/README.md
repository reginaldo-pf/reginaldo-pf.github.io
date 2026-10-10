# Aula 04 - Aplicação da Lista de Exercícios 01 (N1): Atividade Avaliativa Assíncrona

**Disciplina:** [Banco de Dados](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/README.md)  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 10 de Outubro de 2026 (Sábado Letivo)  
**Carga Horária:** 100 minutos (2 horas/aula assíncronas)  
**Regime Didático:** Mentoria e Tutoria Individualizada (1 Aluno)  

---

## 🎯 Objetivos e Competências Avaliadas

A Aula 04 é um **Sábado Letivo Assíncrono (sem conteúdo novo)** dedicado à resolução, consolidação e aplicação da **Lista de Exercícios 01 (N1)**, correspondendo a **20% da avaliação do Período N1**. Como o aprendizado prático de sintaxe e dialetos SQL ocorrerá a partir do Período N2 (Aula 22), **esta avaliação é estritamente conceitual e arquitetural, não exigindo codificação em SQL**.

A avaliação é estruturada em **8 questões aprofundadas** (totalizando 10,0 pontos) implementadas em **LaTeX com diagramas vetoriais em TikZ**:

- [x] **Parte I: Fundamentos de SGBD & Arquitetura ANSI/SPARC (3,0 pts)**
  - *Questão 1 (1,0 pt):* Comparativo técnico SGBD vs. Arquivos Planos (Redundância, Concorrência, ACID e WAL).
  - *Questão 2 (1,0 pt):* Níveis de Abstração ANSI/SPARC e Independência de Dados (Física vs. Lógica em redes e NOC).
  - *Questão 3 (1,0 pt - DIAGRAMA TIKZ):* Diagrama Esquemático da Arquitetura ANSI/SPARC de 3 Níveis com visões de Telemática, mapeamentos e catálogo central de metadados.
- [x] **Parte II: Ciclo de Vida do Projeto & Ontologia de Atributos (2,5 pts)**
  - *Questão 4 (1,0 pt):* As 4 Fases Canônicas de Projeto e a justificativa da independência tecnológica do MER frente a SGBDs e SQL.
  - *Questão 5 (1,5 pt):* Ontologia de Entidades/Instâncias e Taxonomia de Atributos em `ROTEADOR_BORDA_BGP` (identificador, composto, multivalorado, derivado e nulo).
- [x] **Parte III: Produção de Diagramas Conceituais (DER Peter Chen) em LaTeX/TikZ (4,5 pts)**
  - *Questão 6 (1,5 pt - DIAGRAMA DER TIKZ):* Modelagem em TikZ da entidade `SERVIDOR_VIRTUALIZADO` do Data Center IFCE.
  - *Questão 7 (2,0 pts - DIAGRAMA DER TIKZ):* Modelagem em TikZ do Minimundo do Backbone Óptico Regional do IFCE (`PONTO_DE_PRESENCA`, `ENLACE_OPTICO` e `EQUIPAMENTO_TRANSMISSAO`).
  - *Questão 8 (1,0 pt - DIAGRAMA DER & ANÁLISE):* Normalização e DER Chen de planilha de `ROTEADOR_CLIENTE` e análise comparativa Peter Chen vs. Pé de Galinha (*Crow's Foot*).

---

## 📁 Estrutura de Arquivos da Aula

- [`plano_de_aula.md`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/plano_de_aula.md): Plano de aula detalhado com objetivos, metodologia assíncrona, caderno completo das 8 questões e barema oficial.
- [`lista_01.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/lista_01.pdf): Caderno oficial da avaliação em PDF para impressão e resolução por escrito.
- [`codigo/`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/codigo/):
  - [`script_apoio.py`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/codigo/script_apoio.py): Script didático em Python com metamodelo do DER Peter Chen e gerador de código Mermaid/TikZ.
  - [`script_apoio.ipynb`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/codigo/script_apoio.ipynb): Notebook interativo para visualização de diagramas e testes conceituais.
- [`materiais/`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/materiais/):
  - [`lista_01.tex`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/materiais/lista_01.tex): Documento fonte em LaTeX da avaliação oficial com estilos TikZ e diagramas.
  - [`lista_01.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/materiais/lista_01.pdf): Caderno oficial da avaliação compilado em PDF de alta qualidade vetorial (6 páginas).
  - [`main.tex`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/materiais/main.tex): Documento mestre Beamer (16:9, padrão institucional IFCE Tauá).
  - [`main.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/materiais/main.pdf): Apresentação compilada com as orientações, diretrizes e barema (28 slides).
- [`../../Avaliacoes/Lista_01_N1.md`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Avaliacoes/Lista_01_N1.md): Caderno da avaliação em Markdown sincronizado.
- [`../../Avaliacoes/lista_01.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Avaliacoes/lista_01.pdf): Cópia oficial do PDF da Lista 01 na pasta geral de avaliações.

---

## 📬 Instruções e Prazo de Entrega

* **Data Limite Improrrogável:** **12 de Outubro de 2026** (Segunda-feira).
* **Forma de Entrega:** Entrega obrigatoriamente **por escrito (manuscrita)** ao professor, utilizando o caderno impresso [`lista_01.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/materiais/lista_01.pdf) ou folhas anexas com respostas à caneta azul ou preta.
* **Diagramas Conceituais:** Desenhados à mão com régua/gabarito, respeitando rigorosamente a notação canônica de Peter Chen (1976).

---

## 📚 Bibliografia Recomendada

- **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), v. 1, n. 1, p. 9–36, 1976.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson, 2018.
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020.
- **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Campus, 2004.
- **TANTAN, Till et al.** *The TikZ and PGF Packages: Manual for Version 3.1.10*. CTAN, 2023.
