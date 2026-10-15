# Aula 06: Entidades Fracas e Modelo Entidade-Relacionamento Estendido (EER)

* **Curso:** Tecnologia em Telemática  
* **Componente Curricular:** Banco de Dados  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 14 de Outubro de 2026 (Quarta-feira)  
* **Carga Horária:** 2 h/a (100 minutos)  
* **Módulo:** Unidade III (N1) — Modelagem Conceitual Avançada no MER/EER  

---

## 🎯 Competências e Objetivos Consolidados

- [x] Identificar e formalizar o conceito de **Entidade Fraca (*Weak Entity*)**, diferenciando **dependência existencial** de **dependência de identificação**.
- [x] Definir a **Chave Parcial (Discriminador)** e derivar a chave primária composta global em conjunto com a entidade proprietária.
- [x] Aplicar a gramática gráfica canônica de Peter Chen: **Retângulo Duplo** (entidade fraca), **Losango Duplo** (relacionamento identificador), **Linha Dupla** (participação total) e **Sublinhado Tracejado** (discriminador).
- [x] Compreender os fundamentos do **Modelo EER** (*Enhanced Entity-Relationship*), suas motivações e o mecanismo universal de **Herança de Atributos e de Relacionamentos**.
- [x] Projetar taxonomias conceituais aplicando restrições de **Disjunção** ($d$ para disjunta e $o$ para sobreposta) e **Integralidade** (Total vs. Parcial).
- [x] Executar e explorar o script Python didático com metamodelo orientado a objetos para validação dinâmica de integridade composta e travas de disjunção em memória.

---

## 📁 Estrutura de Arquivos da Aula

- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico estruturado em 5 blocos temporais, objetivos detalhados, slides e lista de exercícios de fixação.
- [`index.html`](index.html): Portal web didático interativo e responsivo com Tailwind CSS, Prism.js, visualizador de slides em PDF e abas integradas.
- `assets/img/`: Identidade visual e logotipos institucionais do IFCE Campus Tauá.
- `codigo/`:
  - [`script_apoio.py`](codigo/script_apoio.py): Implementação em Python de metamodelo orientado a objetos para validação de entidades fracas, discriminadores e restrições EER em memória.
  - [`script_apoio.ipynb`](codigo/script_apoio.ipynb): Jupyter Notebook interativo com explicações conceituais, diagramas e células de execução imediata.
- `materiais/`:
  - [`main.tex`](materiais/main.tex): Documento mestre Beamer (Widescreen 16:9, tema visual institucional IFCE Tauá / Scouts).
  - `secao*.tex`: 9 módulos temáticos de slides com fundamentação teórica formal e DERs canônicos de Peter Chen / EER com TikZ.
  - [`main.pdf`](materiais/main.pdf): Apresentação em slides compilada em PDF com alta qualidade visual.

---

## 📚 Bibliografia Recomendada

- **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), New York, v. 1, n. 1, p. 9–36, Mar. 1976.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 3: Modelagem Conceitual e Capítulo 4: O Modelo Entidade-Relacionamento Estendido - EER).
- **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 2: O Modelo Entidade-Relacionamento e Capítulo 3: Generalização e Especialização).
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020. (Capítulo 6: O Modelo E-R Estendido).
- **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier / Campus, 2004.
