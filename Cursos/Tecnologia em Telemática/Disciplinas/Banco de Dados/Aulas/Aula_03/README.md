# Aula 03 - Fases do Projeto de Banco de Dados e Introdução ao Modelo Entidade-Relacionamento (MER)

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 06 de Outubro de 2026 (Terça-feira)  
**Carga Horária:** 100 minutos (2 horas/aula)  

---

## 🎯 Objetivos de Aprendizagem

- [x] Dominar o ciclo de vida e as 4 fases canônicas do projeto de banco de dados: Análise de Requisitos (Minimundo), Projeto Conceitual, Projeto Lógico e Projeto Físico.
- [x] Compreender a fundamentação ontológica e teórica do Modelo Entidade-Relacionamento (MER) estabelecido por Peter Chen em 1976.
- [x] Definir formalmente e distinguir os conceitos de **Entidade**, **Conjunto de Entidades** (*Entity Set*) e **Instância**, aplicando-os a sistemas de telecomunicações e redes.
- [x] Classificar e dominar a taxonomia completa de atributos: **Simples vs. Compostos**, **Monovalorados vs. Multivalorados**, **Armazenados vs. Derivados**, **Valores Nulos (NULL)** e **Atributos Identificadores (Chaves)**.
- [x] Compreender e aplicar a notação gráfica clássica do Diagrama Entidade-Relacionamento (DER) de Peter Chen (retângulos, elipses simples, duplas, tracejadas e ramificadas).
- [x] Executar e explorar o script Python didático para simulação de metamodelo conceitual, validação semântica e mapeamento pré-relacional de atributos.

---

## 📁 Estrutura de Arquivos da Aula

- `plano_de_aula.md`: Roteiro pedagógico estruturado em 5 blocos temporais, objetivos e exercícios de fixação.
- `index.html`: Portal web didático completo e responsivo (Tailwind CSS, Prism.js, visualizador de slides PDF integrado e abas temáticas).
- `codigo/`:
  - `script_apoio.py`: Implementação em Python de metamodelo MER, validação de regras de atributos e demonstração de mapeamento para SQLite.
  - `script_apoio.ipynb`: Jupyter Notebook interativo para execução local ou execução direta no Google Colab.
- `materiais/`:
  - `main.tex`: Documento mestre Beamer (Widescreen 16:9, padrão visual IFCE Tauá).
  - `secao*.tex`: Módulos de slides com fundamentação teórica formal, DERs conceituais e exemplos práticos.
  - `main.pdf`: Apresentação compilada com rigor gráfico e bibliografia ABNT.

---

## 📚 Bibliografia Recomendada

- **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), v. 1, n. 1, p. 9–36, 1976.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 6. ed. São Paulo: Pearson Education do Brasil, 2011. (Capítulo 7: Modelagem de Dados Usando o Modelo Entidade-Relacionamento).
- **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 2: Modelo Conceitual e Modelo Entidade-Relacionamento).
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 6. ed. Rio de Janeiro: Elsevier, 2012. (Capítulo 7: Modelo Entidade-Relacionamento).
- **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Campus, 2004.
