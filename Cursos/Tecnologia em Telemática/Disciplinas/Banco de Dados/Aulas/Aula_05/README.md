# Aula 05 - Relacionamentos no Modelo Entidade-Relacionamento (MER): Grau, Papéis, Cardinalidades e Participação

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 13 de Outubro de 2026 (Terça-feira)  
**Carga Horária:** 100 minutos (2 horas/aula presenciais)  
**Regime Didático:** Mentoria / Tutoria Individual (1 Aluno)  

---

## 🎯 Objetivos de Aprendizagem

- [x] Definir formalmente **Tipo de Relacionamento**, **Conjunto de Relacionamentos** (*Relationship Set*) e **Instância de Relacionamento** no modelo ontológico de Peter Chen (1976).
- [x] Classificar e dominar os diferentes **Graus de Relacionamento**: Unário (Auto-relacionamento/Recursivo), Binário, Ternário e N-ário.
- [x] Aplicar a semântica de **Papéis (*Roles*)** para desambiguar arestas em relacionamentos e topologias de rede.
- [x] Determinar com rigor as **Razões de Cardinalidade**: $1:1$ (Um para Um), $1:N$ (Um para Muitos) e $N:M$ (Muitos para Muitos).
- [x] Diferenciar e aplicar as **Restrições de Participação**: Total (Existência dependente / Linha dupla) vs. Parcial (Opcional / Linha simples) e a notação estrutural $(min, max)$.
- [x] Executar e explorar o script Python didático com metamodelo orientado a objetos para validação dinâmica das regras de cardinalidade (1:1, 1:N, N:M), papéis em auto-relacionamento e auditoria de participação total.

---

## 📁 Estrutura de Arquivos da Aula

- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico estruturado em 5 blocos temporais, objetivos detalhados, slides e lista de exercícios de fixação.
- [`index.html`](index.html): Portal web didático interativo e responsivo com Tailwind CSS, Prism.js, visualizador de slides em PDF e abas integradas.
- `assets/img/`: Identidade visual e logotipos institucionais do IFCE Campus Tauá.
- `codigo/`:
  - [`script_apoio.py`](codigo/script_apoio.py): Implementação em Python de metamodelo orientado a objetos para validação de relacionamentos, cardinalidades, atributos descritivos e participação no MER.
  - [`script_apoio.ipynb`](codigo/script_apoio.ipynb): Jupyter Notebook interativo com explicações conceituais, diagramas e células de execução imediata.
- `materiais/`:
  - [`main.tex`](materiais/main.tex): Documento mestre Beamer (Widescreen 16:9, tema visual institucional IFCE Tauá / Scouts).
  - `secao*.tex`: 9 módulos temáticos de slides com fundamentação teórica formal e DERs canônicos de Peter Chen com TikZ.
  - [`main.pdf`](materiais/main.pdf): Apresentação em slides compilada em PDF com alta qualidade visual.

---

## 📚 Bibliografia Recomendada

- **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), New York, v. 1, n. 1, p. 9–36, Mar. 1976.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 3: Modelagem de Dados Usando o Modelo Entidade-Relacionamento).
- **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 2: O Modelo Entidade-Relacionamento e Capítulo 3: Projeto Conceitual).
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020. (Capítulo 6: Projeto de Bancos de Dados e o Modelo E-R).
- **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier / Campus, 2004.
