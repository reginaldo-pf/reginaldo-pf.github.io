# Aula 09: Fundamentos Formais do Modelo Relacional e Restrições de Integridade

* **Curso:** Tecnologia em Telemática  
* **Componente Curricular:** Banco de Dados  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 21 de Outubro de 2026 (Quarta-feira)  
* **Carga Horária:** 2 h/a (100 minutos)  
* **Módulo:** Unidade II (N1) — O Modelo Relacional de Dados (Edgar F. Codd, 1970)  

---

## 🎯 Competências e Objetivos Consolidados

- [x] Compreender a revolução científica de **Edgar Frank Codd (1970)** na IBM e a independência entre a representação lógica matemática dos dados e o armazenamento físico em disco.
- [x] Dominar a terminologia formal do Modelo Relacional e sua correspondência com a linguagem de mercado: **Domínio ($D_i$)**, **Atributo ($A_i$)**, **Esquema de Relação ($R(A_1, A_2, \dots, A_n)$)**, **Tupla ($t$)**, **Estado/Instância da Relação ($r(R) \subseteq D_1 \times D_2 \times \dots \times D_n$)**, **Grau (Aridade)** e **Cardinalidade**.
- [x] Aplicar as propriedades matemáticas das relações como conjuntos: **ausência de ordem entre tuplas**, **ausência de tuplas duplicadas**, **ausência de ordem posicional estrita nos atributos nomeados** e **atomicidade dos valores (1FN)**.
- [x] Diferenciar com rigor matemático **Superchave ($SK$)**, **Chave Candidata ($CK$ — minimalidade/irredutibilidade)**, **Chave Primária ($PK$)**, **Chave Alternativa ($AK$)** e **Chave Estrangeira ($FK$)**.
- [x] Auditar as quatro categorias de restrições do Modelo Relacional: **Integridade de Domínio**, **Integridade de Chave (Unicidade)**, **Integridade de Entidade** ($\text{PK} \neq \text{NULL}$) e **Integridade Referencial** ($\text{FK} \in \text{PK}_{\text{origem}} \lor \text{FK} = \text{NULL}$), incluindo o comportamento formal diante de operações de Inserção, Exclusão e Atualização (Rejeição/Restrição, Cascata e Anulação).
- [x] Representar esquemas relacionais completos nas formas **Textual/Intensional**, **Diagrama de Esquema com Arcos Direcionados** e **Auditoria Tabular de Instâncias**.

---

## 📁 Estrutura de Arquivos da Aula

- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico estruturado em 5 blocos temporais, formalismo matemático de Codd, estudo das restrições de integridade, modelagem de esquemas e instâncias relacionais e lista de 5 exercícios analíticos.
- [`index.html`](index.html): Portal web didático interativo e responsivo com diagramas de esquema relacional em SVG, tabelas de instâncias e auditoria formal de tuplas e visualizador de slides em PDF.
- `assets/img/`: Identidade visual e logotipos institucionais do IFCE Campus Tauá.
- `materiais/`:
  - [`main.tex`](materiais/main.tex): Documento mestre Beamer (Widescreen 16:9, tema visual institucional IFCE Tauá / Scouts).
  - `secao*.tex`: 9 módulos temáticos de slides com diagramas de esquemas relacionais, anatomia tabular e arcos de integridade referencial em TikZ.
  - [`main.pdf`](materiais/main.pdf): Apresentação em slides compilada em PDF com 22 lâminas de alta qualidade visual.

---

## 📚 Bibliografia Recomendada

- **CODD, Edgar Frank.** *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM (CACM), New York, v. 13, n. 6, p. 377–387, June 1970.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 5: O Modelo de Dados Relacional e as Restrições de Banco de Dados Relacional).
- **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 4: Projeto Lógico — O Modelo Relacional).
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020. (Capítulo 2: Introdução ao Modelo Relacional).
- **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier / Campus, 2004.
