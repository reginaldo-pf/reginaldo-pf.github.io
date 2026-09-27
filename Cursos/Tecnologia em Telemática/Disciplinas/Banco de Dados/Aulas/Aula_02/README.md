# Aula 02 - Arquitetura ANSI/SPARC, Independência de Dados, Catálogo do Sistema e Sublinguagens SQL

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 30 de Setembro de 2026 (Quarta-feira)  
**Carga Horária:** 100 minutos (2 horas/aula)  

---

## 🎯 Objetivos de Aprendizagem

- [x] Compreender a evolução e os objetivos da arquitetura ANSI/SPARC de três níveis (Externo, Conceitual e Interno).
- [x] Identificar e diferenciar a Independência Lógica de Dados da Independência Física de Dados, avaliando seu impacto na manutenção de sistemas de telecomunicações e redes.
- [x] Explorar o Catálogo do Sistema (Dicionário de Dados) e compreender como os SGBDs modernos armazenam e consultam metadados.
- [x] Dominar a taxonomia formal das sublinguagens SQL: DDL (*Data Definition Language*), DML (*Data Manipulation Language*), DQL (*Data Query Language*), DCL (*Data Control Language*) e TCL (*Transaction Control Language*).
- [x] Executar operações práticas em Python e SQLite inspecionando o catálogo (`sqlite_master`), manipulando estruturas com DDL, manipulando dados e aplicando pontos de salvamento com TCL.

---

## 📁 Estrutura de Arquivos da Aula

- `plano_de_aula.md`: Roteiro pedagógico detalhado com cronograma em 5 blocos de aula e diretrizes docentes.
- `index.html`: Portal web interativo com abas didáticas, visualizador de slides PDF integrado, código executável e central de arquivos.
- `codigo/`:
  - `script_apoio.py`: Script Python com demonstração completa de inspeção do catálogo, DDL, DML, DQL e controle transacional TCL.
  - `script_apoio.ipynb`: Notebook Jupyter interativo para execução local ou via Google Colab.
- `materiais/`:
  - `main.tex`: Documento mestre da apresentação em LaTeX Beamer (Widescreen 16:9, Tema Scouts IFCE).
  - `main.pdf`: Apresentação compilada com fundamentação teórica aprofundada e bibliografia ABNT.

---

## 📚 Bibliografia Recomendada

- **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Campus, 2004.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 6. ed. São Paulo: Pearson Education do Brasil, 2011.
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 6. ed. Rio de Janeiro: Elsevier, 2012.
- **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009.
