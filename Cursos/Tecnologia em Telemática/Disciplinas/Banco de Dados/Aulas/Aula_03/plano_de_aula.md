# Plano de Aula: 03 - Fases do Projeto de Banco de Dados e Introdução ao Modelo Entidade-Relacionamento (MER)

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 06 de Outubro de 2026 (Terça-feira)  
**Carga Horária:** 100 minutos (2 horas/aula)  
**Regime Didático:** Mentoria e Tutoria Individualizada (1 Aluno)  

---

## 🎯 Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o discente a compreender o ciclo de vida completo do desenvolvimento de bancos de dados relacionais — da análise de requisitos à implementação física —, dominar os princípios ontológicos e conceituais do Modelo Entidade-Relacionamento (MER) proposto por Peter Chen (1976), identificar entidades e conjuntos de entidades em cenários de infraestrutura de telecomunicações e classificar com rigor técnico todos os tipos de atributos e suas respectivas representações no Diagrama Entidade-Relacionamento (DER).

### Objetivos Específicos
1. Identificar as quatro grandes fases do projeto de banco de dados (Análise de Requisitos, Projeto Conceitual, Projeto Lógico e Projeto Físico), compreendendo suas entradas, saídas e independência em relação ao SGBD.
2. Definir formalmente os conceitos de **Entidade**, **Conjunto de Entidades** (*Entity Set*) e **Instância**, aplicando-os a ativos e serviços de redes de computadores e telecomunicações.
3. Compreender e classificar com precisão os tipos de atributos:
   - **Simples (Atômicos)** versus **Compostos**;
   - **Monovalorados** versus **Multivalorados**;
   - **Armazenados** versus **Derivados**;
   - **Nulos (NULL)**: semântica de valor desconhecido versus inaplicável;
   - **Atributos Identificadores (Chaves Conceituais)**: chaves simples e compostas.
4. Dominar a notação gráfica canônica do Diagrama Entidade-Relacionamento (DER) de Peter Chen (retângulos, elipses simples, elipses ramificadas, elipses duplas e elipses tracejadas).
5. Implementar um metamodelo conceitual em Python para validação semântica de esquemas de entidades e simular o impacto do desdobramento de atributos multivalorados e compostos no modelo relacional.

---

## ⏱️ Cronograma da Aula (100 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1** | 00 - 20 min | **Acolhimento & Ponte Conceitual:** Retrospectiva da Aula 02 (da arquitetura ANSI/SPARC de 3 níveis à necessidade de projetar o nível conceitual). Discussão do problema: como transformar as necessidades operacionais de um provedor/NOC em uma estrutura de dados consistente? | Exposição dialogada e diagrama do ciclo de dados. |
| **2** | 20 - 45 min | **Ciclo de Vida do Projeto de Banco de Dados:** Detalhamento formal das 4 fases: (1) Levantamento e Especificação de Requisitos (Minimundo); (2) Projeto Conceitual (MER/DER, independente de SGBD); (3) Projeto Lógico (Esquema Relacional e Normalização); (4) Projeto Físico (Estruturas de arquivos, índices e particionamento). | Slides Beamer (Widescreen 16:9), diagramas de fluxo de engenharia de software e banco de dados. |
| **3** | 45 - 65 min | **O Modelo Entidade-Relacionamento (Peter Chen, 1976):** Conceito ontológico de Entidade vs. Conjunto de Entidades (*Entity Set*). Taxonomia exaustiva de Atributos: simples, compostos, monovalorados, multivalorados, armazenados, derivados, valores nulos e identificadores (chaves). Notação gráfica canônica do DER. | Slides teóricos, quadros comparativos e exemplos no minimundo de Telemática. |
| **4** | 65 - 85 min | **Laboratório Computacional & Estudo de Caso:** Apresentação do minimundo *Datacenter e Gerência de Redes do IFCE Tauá*. Execução do script Python demonstrando a validação de metadados conceituais, cálculo em tempo de execução de atributos derivados e o desdobramento pré-relacional de atributos complexos. | Laboratório prático individual (VS Code / Python / SQLite). |
| **5** | 85 - 100 min | **Síntese, Resolução de Dúvidas & Orientações:** Fechamento dos conceitos, resolução de dúvidas da mentoria individual, apresentação do Bloco 3 da Lista de Exercícios 01 (entregável no sábado letivo - Aula 04) e introdução à Aula 05 (Relacionamentos, Cardinalidades e Participação). | Alinhamento docente-discente e fechamento da aula. |

---

## 💻 Roteiro do Laboratório Prático Computacional

1. **Metamodelo Conceitual em Python:**
   - Construção de classes representativas do modelo conceitual (`AttributeType`, `AttributeDefinition`, `EntitySchema`).
   - Definição do conjunto de entidades `DISPOSITIVO_REDE` com atributos identificadores (`patrimonio_id`), simples (`hostname`, `ip_loopback`, `mtu`), compostos (`localizacao_rack`), multivalorados (`vlan_tags`) e derivados (`dias_operacao` calculado a partir da data de instalação).
2. **Motor de Validação Semântica:**
   - Verificação de unicidade da chave conceitual.
   - Cálculo automático do atributo derivado através de função dinâmica.
   - Validação de atomicidade para rejeição de estruturas anômalas.
3. **Ponte Conceitual $\to$ Relacional (Prévia de Mapeamento):**
   - Demonstração em SQLite de como atributos simples tornam-se colunas diretas.
   - Decomposição das subpartes do atributo composto em colunas atômicas (`rack_datacenter`, `rack_corredor`, `rack_numero`, `rack_posicao_u`).
   - Tratamento de atributo multivalorado através de tabela associativa auxiliar (evitando violação da 1ª Forma Normal).

---

## 📝 Exercícios de Fixação (Lista 1 -- Bloco 3)

1. Descreva as quatro fases fundamentais do projeto de banco de dados, explicitando para cada uma: o objetivo principal, os artefatos de entrada e os artefatos gerados como saída. Por que o Projeto Conceitual deve ser estritamente independente de qualquer SGBD comercial?
2. Em um sistema de gerenciamento de infraestrutura de telecomunicações (NOC), identifique ao menos três conjuntos de entidades do mundo real e forneça a justificativa ontológica para a escolha de cada um.
3. Classifique formalmente cada um dos atributos a seguir relativos a um Roteador de Borda, justificando cada classificação:
   - a) `numero_patrimonio` (número único gravado no chassi metálico).
   - b) `localizacao_datacenter` (composto por: Bloco, Sala do NOC, Número do Rack e Posição em Unidades U).
   - c) `enderecos_ipv6_alocados` (conjunto de prefixos IPv6 configurados nas interfaces do equipamento).
   - d) `tempo_atividade_horas` (quantidade de horas ininterruptas de operação calculada subtraindo o timestamp atual do último boot).
   - e) `observacoes_manutencao` (campo textual que pode estar preenchido ou vazio caso nunca tenha ocorrido intervenção técnica).
4. Desenhe (ou descreva textualmente segundo as regras de notação canônica de Peter Chen) o Diagrama Entidade-Relacionamento (DER) para o conjunto de entidades `SERVIDOR_TELEMATICA`, contemplando obrigatoriamente:
   - 1 atributo identificador simples;
   - 2 atributos simples atômicos;
   - 1 atributo composto contendo no mínimo 3 subatributos;
   - 1 atributo multivalorado;
   - 1 atributo derivado com a respectiva regra de derivação explicitada.
