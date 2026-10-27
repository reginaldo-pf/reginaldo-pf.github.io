# Aula 08: Laboratório de Modelagem Conceitual com Ferramentas CASE (brModelo e Draw.io)

* **Curso:** Tecnologia em Telemática  
* **Componente Curricular:** Banco de Dados  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 20 de Outubro de 2026 (Terça-feira)  
* **Carga Horária:** 2 h/a (100 minutos)  
* **Módulo:** Unidade III (N1) — Laboratório Prático de Engenharia de Software Assistida por Computador (CASE) e Construção do DER/EER da AVP1  

---

## 🎯 Competências e Objetivos Consolidados

- [x] Compreender o papel das **Ferramentas CASE (*Computer-Aided Software Engineering*)** no ciclo de vida de bancos de dados: padronização visual, validação sintática/semântica, manutenção do dicionário de dados e rastreabilidade entre os níveis Conceitual e Lógico.
- [x] Dominar a modelagem conceitual na ferramenta nacional **brModelo (Web / Desktop)**, aplicando a notação de **Carlos Alberto Heuser**: entidades fortes, atributos (identificador com bolinha preenchida, simples com bolinha vazia, compostos ramificados e multivalorados $(1, n)$), cardinalidades $(min, max)$ invertidas e triângulo de generalização/especialização (`t`/`p`, `e`/`c`).
- [x] Dominar a construção de diagramas estritamente fiéis à gramática clássica de **Peter Chen (1976)** e **Elmasri & Navathe** utilizando o **Draw.io (diagrams.net)** com a biblioteca nativa *Entity Relation*: retângulos duplos (entidades fracas), losangos duplos (relacionamentos identificadores), elipses duplas (multivalorados), elipses tracejadas (derivados) e círculos EER ($d/o$).
- [x] Aplicar boas práticas de layout, legibilidade, alinhamento em grade (*grid*), minimização de cruzamentos de arestas e nomenclatura padronizada para o entregável da **Etapa 2 do Projeto Prático (AVP1)**.
- [x] Elaborar a **Modelagem Descritiva e Textual Complementar (Dicionário de Dados Conceitual e Matriz de Relacionamentos)**, documentando formalmente domínios semânticos, regras de derivação, restrições de integridade e papéis que complementam o diagrama gráfico.

---

## 📁 Estrutura de Arquivos da Aula

- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico estruturado em 5 blocos temporais, comparativo técnico entre notações (Chen vs. Heuser/brModelo), modelagem descritiva/textual (Dicionário de Dados), checklist de qualidade CASE e exercícios práticos de laboratório.
- [`index.html`](index.html): Portal web didático interativo e responsivo com diagramas visuais SVG, comparativo de formas geométricas, modelo de Dicionário de Dados tabular e visualizador de slides em PDF.
- `assets/img/`: Identidade visual e logotipos institucionais do IFCE Campus Tauá.
- `materiais/`:
  - [`main.tex`](materiais/main.tex): Documento mestre Beamer (Widescreen 16:9, tema visual institucional IFCE Tauá / Scouts).
  - `secao*.tex`: 9 módulos temáticos de slides com figuras geométricas e comparativos gráficos em TikZ entre a notação de Peter Chen (Draw.io) e a notação de Heuser (brModelo), além de tabelas de Dicionário de Dados.
  - [`main.pdf`](materiais/main.pdf): Apresentação em slides compilada em PDF com 24 lâminas de alta qualidade visual.

---

## 📚 Bibliografia Recomendada

- **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulos 2 e 3: Notação de Cardinalidades Mínima/Máxima e Dicionário de Dados).
- **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), New York, v. 1, n. 1, p. 9–36, Mar. 1976.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulos 3 e 4: Modelagem Conceitual, EER e Ferramentas de Projeto).
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020.
- **CANDIDO, Carlos H.** *brModelo: Ferramenta de Modelagem de Banco de Dados Relacional*. Disponível em: https://www.brmodeloweb.com.
