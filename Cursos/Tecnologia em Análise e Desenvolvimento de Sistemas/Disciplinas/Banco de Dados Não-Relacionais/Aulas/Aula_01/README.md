# Plano de Aula: 01 -- Introdução aos Bancos de Dados Não-Relacionais & O Paradigma Pós-Relacional

**Disciplina:** Bancos de Dados Não-Relacionais (ADS16)  
**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) -- IFCE Campus Tauá  
**Carga Horária do Encontro:** 2 horas (120 minutos)  
**Data Prevista:** 29/09/2026 (Terça-feira)  
**Professor:** Reginaldo Fernandes  

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral:
Compreender as motivações históricas, arquiteturais e de negócio que impulsionaram o surgimento do movimento NoSQL (*Not Only SQL*), identificando as limitações do modelo relacional tradicional frente às demandas contemporâneas de alta escalabilidade, volume massivo e variedade de dados.

### Objetivos Específicos:
1. Conhecer a estrutura, o cronograma semestral e os critérios avaliativos da disciplina (AVT 40%, AVP 40%, Listas 20%).
2. Analisar o fenômeno da Web 2.0, do Big Data e o problema do *Descasamento de Impedância Objeto-Relacional* (*Object-Relational Impedance Mismatch*).
3. Contrastar a escalabilidade vertical (*Scale-Up*) com a escalabilidade horizontal (*Scale-Out*).
4. Compreender a definição do acrônimo NoSQL e classificar os quatro modelos de dados não-relacionais canônicos (Chave-Valor, Documentos, Família de Colunas e Grafos), além da emergência dos Bancos Vetoriais para IA.

---

## 📋 2. Diretrizes e Contrato Pedagógico da Disciplina

### 2.1. Composição da Média Semestral (N1 e N2)
A nota de cada período letivo é calculada pela média ponderada regimental:

$$\text{Nota do Período} = (\text{AVT} \times 0{,}40) + (\text{AVP} \times 0{,}40) + (\text{Listas} \times 0{,}20)$$

*   **AVT (40%):** Avaliação Teórica individual, contemplando fundamentos, Teorema CAP/PACELC, trade-offs de consistência e arquitetura interna.
*   **AVP (40%):** Avaliação Prática.
    *   **AVP1 (N1):** Desafio prático individual em laboratório (Modelagem de Documentos MongoDB + Caching Redis).
    *   **AVP2 (N2):** Projeto prático integrado desenvolvido e apresentado em duplas (aplicação conectada a bancos NoSQL).
*   **Listas (20%):** Conjunto contínuo de listas de exercícios e atividades práticas de laboratório entregues até a data da avaliação teórica de cada período.

### 2.2. Diretriz Estrita dos Sábados Letivos
*   **Dias sem conteúdo novo:** Os sábados letivos previstos no calendário acadêmico (**10/10/2026** e **14/11/2026**) serão utilizados exclusivamente para nivelamento prático (oficina de Docker e Docker Compose), suporte orientado a exercícios e laboratório preparatório para as avaliações de N1.

---

## ⏱️ 3. Cronograma da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades |
| :---: | :---: | :--- |
| **Bloco 1** | 00 -- 25 min | **Acolhimento & Apresentação da Disciplina:** Apresentação docente, objetivos do curso, cronograma das 20 aulas, sistema de avaliação (40% AVT, 40% AVP, 20% Listas), bibliografia e papel do laboratório. |
| **Bloco 2** | 25 -- 50 min | **Contexto Histórico & O Desafio dos Dados:** A hegemonia relacional (Codd, 1970; SQL); a revolução da Web 2.0 (Google, Amazon, Meta); a explosão dos 3 Vs (Volume, Velocidade, Variedade). |
| **Bloco 3** | 50 -- 75 min | **Limitações do Modelo Relacional:** O custo da Escala Vertical vs Escala Horizontal; custos de processamento de `JOIN`s em tabelas gigantescas; garantias rígidas de ACID sob concorrência global distribuída; *Impedance Mismatch*. |
| **Bloco 4** | 75 -- 100 min | **O Movimento NoSQL & Taxonomia:** Definição formal de "Not Only SQL"; Visão geral dos 4 modelos canônicos: Chave-Valor (*Redis*), Documentos (*MongoDB*), Família de Colunas (*Cassandra*) e Grafos (*Neo4j*); Nova fronteira: Bancos Vetoriais (*ChromaDB/Pinecone*) para Inteligência Artificial. |
| **Bloco 5** | 100 -- 120 min | **Demonstração Prática & Conclusão:** Execução do script Python comparativo (Representação tabular normalizada vs Documento JSON nativo); apresentação da Lista de Exercícios 1 e orientações para a Aula 02. |

---

## 🖥️ 4. Roteiro dos Slides (Template Moderno Beamer 16:9)

*   **Slide 01:** Capa da Aula (Identidade IFCE Tauá, Título, Subtítulo, Professor e Semestre 2026.2).
*   **Slide 02:** Agenda / Sumário da Aula.
*   **Slide 03:** Apresentação da Disciplina & Metodologia de Ensino.
*   **Slide 04:** Sistema de Avaliação (Tabela e Cards: AVT 40%, AVP 40%, Listas 20%).
*   **Slide 05:** Cronograma Geral & Política de Sábados Letivos (Sem conteúdo novo).
*   **Slide 06:** O Sucesso do Modelo Relacional (1970–2000) e as Regras de Codd.
*   **Slide 07:** O Ponto de Inflexão: A Web 2.0 e os 3 Vs do Big Data.
*   **Slide 08:** Escala Vertical (*Scale-Up*) vs Escala Horizontal (*Scale-Out*).
*   **Slide 09:** O Custo dos JOINs e o Descasamento de Impedância Objeto-Relacional.
*   **Slide 10:** O que significa NoSQL? (*Not Only SQL* -- Filosofia e História).
*   **Slide 11:** Os 4 Modelos Canônicos de NoSQL (Cards visuais comparativos).
*   **Slide 12:** Modernização: Bancos de Dados Vetoriais e a Era da Inteligência Artificial.
*   **Slide 13:** Quando usar NoSQL? (Trade-offs e Critérios de Decisão).
*   **Slide 14:** Demonstração Prática em Python: Comparando Estrutura Relacional vs Documento.
*   **Slide 15:** Conclusão, Próximos Passos (Aula 02: Teorema CAP/PACELC) e Lista 1.

---

## 🐍 5. Código Prático de Apoio

Arquivo: [`codigo/demonstracao_aula01.py`](file:///home/reginaldo-fernandes/BDNR/Aulas/Aula_01/codigo/demonstracao_aula01.py)  
Objetivo: Demonstrar visualmente o conceito de *Impedance Mismatch* (descasamento objeto-relacional) comparando a complexidade de reconstruir uma entidade de negócio completa via tabelas normalizadas com chave estrangeira versus a leitura direta de um documento aninhado BSON/JSON.

---

## 📝 6. Exercícios de Fixação (Lista 1 -- Bloco 1)

1. Explique por que os bancos de dados relacionais tradicionais (RDBMS) enfrentam dificuldades para escalar horizontalmente mantendo propriedades ACID estritas.
2. Defina com suas palavras o que é o *Descasamento de Impedância Objeto-Relacional* e como o modelo de documentos busca mitigar esse problema.
3. Diferencie escala vertical (*Scale-Up*) de escala horizontal (*Scale-Out*), citando vantagens, desvantagens e custos financeiros de cada abordagem.
4. Cite os quatro modelos canônicos de bancos NoSQL, indicando uma ferramenta representativa e um caso de uso típico para cada um.
