# Aula 07 - Sábado Letivo: Estudo Dirigido do Projeto Prático (AVP1) — Definição do Escopo do Minimundo

**Disciplina:** [Banco de Dados](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/README.md)  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 17 de Outubro de 2026 (Sábado Letivo)  
**Carga Horária:** 100 minutos (2 horas/aula assíncronas)  
**Regime Didático:** Mentoria e Tutoria Individualizada (1 Aluno)  

---

## 🎯 Objetivos e Competências Consolidadas

A Aula 07 é um **Sábado Letivo Assíncrono (sem conteúdo novo)** dedicado à concepção e especificação formal da **Etapa 1 do Projeto Prático de Banco de Dados (AVP1)**, que responde por **40% da nota do Período N1**.

O projeto consiste na aplicação dos construtos do Modelo Entidade-Relacionamento (Peter Chen, 1976) e do Modelo EER sobre um sistema de informação (como **Clínica Médica**, **Gestão Acadêmica Universitária**, **Sistema de Biblioteca** ou **E-Commerce / Pedidos**).

O caderno oficial do Estudo Dirigido ([`estudo_dirigido_avp1.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/materiais/estudo_dirigido_avp1.pdf)) está estruturado em duas partes:

- [x] **Parte A — Exemplo Modelo Completo Resolvido ("Clínica Médica VidaPlena"):**
  - Narrativa de requisitos de dados, quadro resumo de extração gramatical e **Diagrama EER Completo**.
  - Catálogo de **3 Opções de Minimundos** sugeridos (`SGA-Universidade`, `BiblioTech` e `MercadoFácil`).
- [x] **Parte B — Formulário Oficial de Especificação do Escopo do Aluno (5 Etapas — 10,0 pts):**
  - *Etapa 1 (2,0 pts):* Identificação do Tema e Narrativa Completa das Regras de Negócio (15 a 20 linhas).
  - *Etapa 2 (2,0 pts):* Catálogo de Entidades Regulares ($\ge 5$ entidades fortes) e Taxonomia de Atributos de Peter Chen (PK, simples, composto, multivalorado e derivado).
  - *Etapa 3 (2,0 pts):* Matriz de Relacionamentos ($1:1$, $1:N$, $N:M$ com atributo descritivo próprio e Auto-relacionamento recursivo com papéis e restrições $(min, max)$).
  - *Etapa 4 (2,0 pts):* Especificação de Entidade Fraca (proprietário, relacionamento identificador e discriminador) e Hierarquia EER (superclasse, subclasses, disjunção $d/o$ e integralidade Total/Parcial).
  - *Etapa 5 (2,0 pts):* Esboço Integrado do Diagrama Conceitual (DER/EER na notação canônica de Peter Chen), que servirá como base direta para a **Aula 08** (*Laboratório CASE com brModelo/Draw.io*).

---

## 📁 Estrutura de Arquivos da Aula

- [`plano_de_aula.md`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/plano_de_aula.md): Plano de aula detalhado com metodologia de engenharia de requisitos, caso modelo resolvido, catálogo de temas e barema.
- [`index.html`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/index.html): Portal web interativo da Aula 07 com guia da AVP1, visualizador de PDFs e laboratório Python.
- [`estudo_dirigido_avp1.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/estudo_dirigido_avp1.pdf): Caderno oficial impresso em A4 (5 páginas) para especificação do escopo do projeto.
- [`codigo/`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/codigo/):
  - [`script_apoio.py`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/codigo/script_apoio.py): Validador automático de conformidade do escopo da AVP1 em Python orientado a objetos.
  - [`script_apoio.ipynb`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/codigo/script_apoio.ipynb): Notebook interativo para auditoria do minimundo escolhido pelo aluno.
- [`materiais/`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/materiais/):
  - [`estudo_dirigido_avp1.tex`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/materiais/estudo_dirigido_avp1.tex) e [`estudo_dirigido_avp1.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/materiais/estudo_dirigido_avp1.pdf): Código-fonte e PDF oficial do caderno de especificação.
  - [`main.tex`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/materiais/main.tex) e [`main.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/materiais/main.pdf): Apresentação em slides Beamer (Widescreen 16:9, 25 slides) com o guia completo do estudo dirigido.
- [`../../Avaliacoes/Estudo_Dirigido_AVP1.md`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Avaliacoes/Estudo_Dirigido_AVP1.md) e [`../../Avaliacoes/estudo_dirigido_avp1.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Avaliacoes/estudo_dirigido_avp1.pdf): Cópias sincronizadas na pasta geral de avaliações.

---

## 📚 Bibliografia Recomendada

- **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), v. 1, n. 1, p. 9–36, 1976.
- **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson, 2018.
- **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009.
- **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020.
