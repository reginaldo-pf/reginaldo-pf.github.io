# Plano de Aula: Aula 22 - Diagramas de Interação (Sequência e Comunicação) e Diagrama de Máquina de Estados

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá
*   **Professor:** Reginaldo Pereira Fernandes
*   **Tema:** Modelagem Dinâmica Comportamental de Troca de Mensagens (Diagramas de Sequência e Comunicação) e Ciclo de Vida Reativo de Entidades (Diagrama de Máquina de Estados).
*   **Referência Básica:** GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora, **Capítulos 7, 8 e 9**.
*   **Duração:** 100 minutos (2 horas-aula de 50 minutos).

---

## 🎯 1. Objetivos da Aula

### Objetivo Geral
Capacitar os estudantes a projetarem e documentarem a colaboração temporal e topológica entre objetos de software através dos **Diagramas de Interação** (Sequência - Capítulo 7 e Comunicação - Capítulo 8), bem como a modelarem o ciclo de vida reativo e as mudanças de estado de entidades de domínio com o **Diagrama de Máquina de Estados** (Capítulo 9) da UML 2.

### Objetivos Específicos
*   **Compreender a dinâmica temporal no Diagrama de Sequência (Cap. 7):** Identificar linhas de vida (*lifelines*), barras de ativação (*foco de controle*), atores e a semântica dos tipos de mensagens (síncrona, assíncrona, resposta/retorno, construtora, destrutora e autochamada).
*   **Dominar os Fragmentos Combinados na UML 2:** Aplicar operadores de interação (`alt`, `opt`, `loop`, `par`, `break`) e guardas booleanas para representar desvios condicionais, loops e fluxos concorrentes.
*   **Integrar Camadas Arquiteturais e Persistência:** Representar as chamadas entre objetos de fronteira (`<<boundary>>`), controle (`<<control>>`), entidade (`<<entity>>`) e persistência (*Repository* / *DAO*).
*   **Construir Diagramas de Comunicação (Cap. 8):** Mapear interações sobre vínculos estruturais (*links*), utilizando numeração sequencial hierárquica e aninhada (ex.: `1`, `1.1`, `1.2`, `1.2.1`), condições de guarda e iterações.
*   **Comparar Diagrama de Sequência vs. Diagrama de Comunicação:** Avaliar quando priorizar a visão de ordem temporal (Sequência) ou a visão de organização estrutural/topológica de vínculos (Comunicação).
*   **Modelar o Ciclo de Vida no Diagrama de Máquina de Estados (Cap. 9):** Identificar estados simples, transições dirigidas por eventos (`evento [guarda] / acao`), atividades internas (`entry /`, `do /`, `exit /`), transições internas e autotransições.
*   **Aplicar Pseudoestados e Estados Compostos:** Utilizar pseudoestados de escolha (*choice*), junção (*junction*), bifurcação/união (*fork/join*), histórico (*shallow* $H$ e *deep* $H^*$), ponto de entrada/saída e término.
*   **Implementar e Simular em Código:** Mapear a máquina de estados e a troca de mensagens para classes e padrões de projeto em Python (`exemplo_interacao_estados.py`).

---

## ⏱️ 2. Cronograma da Aula (100 Minutos)

| Bloco | Conteúdo e Metodologia | Recursos e Figuras do Livro |
| :--- | :--- | :--- |
| **00 - 25 min** | **Diagrama de Sequência em Detalhes (Cap. 7)**<br>• Transição da estrutura para o comportamento temporal dos Casos de Uso.<br>• Linhas de vida (*Lifelines*), cabeçalho (`objeto:Classe`), linha tracejada e barra de ativação (*foco de controle*).<br>• Tipos de mensagens: Síncrona ($\blacktriangleright$), Assíncrona ($\rightarrow$), Resposta ($\dashrightarrow$), Construtora (`<<create>>` / `new`), Destrutora (`<<destroy>>` / $\times$) e Autochamada (*self-call*).<br>• Fragmentos Combinados: Operadores `alt` (desvio exclusivo), `opt` (opcional), `loop` (iteração), `par` (paralelismo) e `break` (exceção).<br>• Invariante de Estado, Uso de Interação (`ref`), Portões (*Gates*) e persistência com *Repository/DAO*.<br>• Exemplos do Sistema Bancário: Emissão de Saldo, Saque e Depósito. | Slides 1 a 11<br>**Fig. 7.1 a 7.13, 7.15 a 7.22, 7.23, 7.26, 7.28** |
| **25 - 40 min** | **Diagrama de Comunicação (Cap. 8)**<br>• Mudança de perspectiva: foco na arquitetura de vínculos vs. foco na linha de tempo.<br>• Objetos, Vínculos (*Links*) e Direção das Mensagens.<br>• Numeração Sequencial Hierárquica e Aninhada (`1`, `1.1`, `1.1.1`, `1.2`, `2`).<br>• Guardas booleanas e iterações (`* [i:=1..n]`).<br>• Autochamada em Diagramas de Comunicação.<br>• Comparativo analítico: Sequência vs. Comunicação (equivalência semântica e casos de uso recomendados).<br>• Exemplo do Sistema Bancário: Emissão de Saldo. | Slides 12 a 17<br>**Fig. 8.1 a 8.5, 8.7, 8.8, 8.9** |
| **40 - 65 min** | **Diagrama de Máquina de Estados (Cap. 9)**<br>• Conceito de Estado e Ciclo de Vida (*Lifecycle*) de entidades reativas.<br>• Notação: Estado Inicial ($\bullet$), Estados Simples (retângulo arredondado) e Estado Final ($\odot$).<br>• Sintaxe das Transições: `evento [guarda] / ação de efeito`.<br>• Atividades Internas do Estado: `entry /` (entrada), `do /` (execução contínua), `exit /` (saída).<br>• Transições Internas vs. Autotransições (impacto sobre `entry` e `exit`).<br>• Pseudoestados: Escolha (*Choice* - losango dinâmico), Junção (*Junction* - estático), *Fork/Join*, Histórico ($H, H^*$) e Término ($\bigotimes$).<br>• Estados Compostos e Estados Compostos Ortogonais (concorrência).<br>• Exemplos do Sistema Bancário: Ciclo de vida da Conta, Emissão de Saldo e Saque.<br>• Demonstração prática do código `exemplo_interacao_estados.py`. | Slides 18 a 28<br>**Fig. 9.1 a 9.12, 9.14 a 9.17, 9.20, 9.21, 9.28**<br>`exemplo_interacao_estados.py` |
| **65 - 88 min** | **Atividade Prática Orientada: TauáDelivery Web**<br>• Continuidade da aplicação dos requisitos do *TauáDelivery Web*.<br>• **Parte 1:** Desafios conceituais (Sequência vs. Comunicação, Fragmentos `alt`/`opt`/`loop`, Choice vs. Junction).<br>• **Parte 2:** Elaboração do Diagrama de Sequência para o caso de uso *UC03 - Finalizar Pedido e Processar Pagamento* (incluindo persistência via Repository e gateway externo).<br>• **Parte 3:** Construção do Diagrama de Comunicação correspondente com numeração aninhada.<br>• **Parte 4:** Modelagem da Máquina de Estados da entidade `Pedido` (`CRIADO`, `AGUARDANDO_PAGAMENTO`, `EM_PREPARO`, `PRONTO_COLETA`, `EM_ROTA`, `ENTREGUE`, `CANCELADO`). | Slides 29 a 33<br>Guia `atividade_pratica.md`<br>Diagramas de apoio |
| **88 - 100 min**| **Síntese, Gabarito e Próximos Passos**<br>• Apresentação dos diagramas de apoio resolvidos e discussão de erros comuns de modelagem.<br>• Feedback coletivo e esclarecimento de dúvidas.<br>• Gancho para a Aula 23: *Diagramas Arquiteturais da UML 2 (Objetos, Pacotes, Componentes e Implantação - Caps. 5, 6, 12 e 13)*. | Slides 34 e 35 |

---

## 👨‍🏫 3. Roteiro Detalhado de Slides (Beamer)

*   **Slide 1: Capa da Aula** — Identificação institucional (IFCE Campus Tauá), curso, disciplina, professor e tema da Aula 22.
*   **Slide 2: Sumário Integrado** — Linha condutora da aula: Sequência (ordem temporal), Comunicação (vínculos) e Máquina de Estados (ciclo de vida).
*   **Slide 3: Do Diagrama de Classes aos Diagramas de Interação** — Como a estrutura estática (classes/associações) ganha vida na execução dos Casos de Uso.
*   **Slide 4: Anatomia do Diagrama de Sequência (Cap. 7)** — Linhas de vida (*Lifelines*), representação do ator, linha pontilhada vertical e barra de ativação (*foco de controle*) (`Fig7.1.png`, `Fig7.2.png`).
*   **Slide 5: Tipos de Mensagens e Estímulos** — Mensagem Síncrona ($\blacktriangleright$), Assíncrona ($\rightarrow$), Resposta/Retorno ($\dashrightarrow$) e Autochamada (*self-call*) (`Fig7.3.png`, `Fig7.4.png`).
*   **Slide 6: Criação e Destruição de Instâncias** — Mensagens construtoras (`<<create>>` / `new`), instanciação de linhas de vida e mensagens destrutoras com marcador de encerramento ($\times$) (`Fig7.5.png`, `Fig7.6.png`, `Fig7.7.png`).
*   **Slide 7: Fragmentos Combinados: Operadores `alt` e `opt`** — Desvio condicional alternativo (`alt` / if-else) e bloco opcional (`opt` / if) com condições de guarda (`Fig7.8.png`, `Fig7.9.png`).
*   **Slide 8: Fragmentos Combinados: Operadores `loop`, `par` e `break`** — Iteração sobre coleções (`loop [i:=1..n]`), execução concorrente (`par`) e tratamento de exceção/abandono de fluxo (`break`) (`Fig7.10.png`, `Fig7.11.png`, `Fig7.12.png`).
*   **Slide 9: Recursos Avançados de Sequência** — Invariante de Estado (*StateInvariant*), Usos de Interação (`ref`) e Portões (*Gates*) (`Fig7.13.png`, `Fig7.15.png`).
*   **Slide 10: Integração com Arquitetura e Persistência (Repository / DAO)** — Modelagem de camadas MVC/ECB com banco de dados no Diagrama de Sequência (`Fig7.22.png`, `Fig7.23.png`).
*   **Slide 11: Estudo de Caso Bancário: Sequência de Emissão de Saldo e Saque** — Análise dos diagramas completos do livro de Guedes (`Fig7.16.png`, `Fig7.18.png`).
*   **Slide 12: Introdução ao Diagrama de Comunicação (Cap. 8)** — Mudança de paradigma: a ênfase na rede de relacionamentos e vínculos estruturais (`Fig8.1.png`, `Fig8.2.png`).
*   **Slide 13: Mensagens e Numeração Sequencial Hierárquica** — A notação `1`, `1.1`, `1.2`, `1.2.1` e a propagação de mensagens sobre vínculos (`Fig8.3.png`, `Fig8.4.png`).
*   **Slide 14: Autochamada, Condições de Guarda e Iterações** — Notação de autoenvio, guardas booleanas `[condição]` e laços `* [i:=1..n]` em comunicação (`Fig8.5.png`, `Fig8.8.png`).
*   **Slide 15: Estudo de Caso Bancário: Comunicação no Processo Emitir Saldo** — Análise do diagrama oficial do livro de Guedes (`Fig8.7.png`).
*   **Slide 16: Análise Comparativa: Sequência vs. Comunicação** — Quadro comparativo de vantagens, limitações, legibilidade e cenários de escolha.
*   **Slide 17: Regras de Equivalência Semântica e Conversão** — Como converter sistematicamente uma linha do tempo de Sequência em um grafo de Comunicação.
*   **Slide 18: Introdução ao Diagrama de Máquina de Estados (Cap. 9)** — Conceito de estado, entidades reativas, estado inicial ($\bullet$) e estado final ($\odot$) (`Fig9.1.png`, `Fig9.2.png`, `Fig9.3.png`).
*   **Slide 19: Transições Dirigidas por Eventos e Guardas** — A fórmula canônica da UML 2: `gatilho/evento [condição de guarda] / ação de efeito` (`Fig9.4.png`, `Fig9.5.png`).
*   **Slide 20: Atividades Internas do Estado (`entry`, `do`, `exit`)** — Comportamentos na entrada, permanência e saída do estado (`Fig9.6.png`).
*   **Slide 21: Transições Internas vs. Autotransições** — Diferença crucial: preservação ou reinicialização das atividades `entry`/`exit` (`Fig9.7.png`, `Fig9.8.png`).
*   **Slide 22: Pseudoestados de Decisão: Escolha (*Choice*) vs. Junção (*Junction*)** — Avaliação dinâmica em tempo de execução ($\lozenge$) vs. pré-avaliação estática ($\bullet$) (`Fig9.9.png`, `Fig9.16.png`).
*   **Slide 23: Pseudoestados de Concorrência e Histórico** — Barra de Bifurcação/União (*Fork/Join*), Pseudoestado de Histórico Raso ($H$) e Profundo ($H^*$) (`Fig9.10.png`, `Fig9.12.png`).
*   **Slide 24: Estados Compostos e Ortogonais** — Subestados sequenciais e subestados concorrentes em regiões ortogonais separadas por linha pontilhada (`Fig9.11.png`, `Fig9.14.png`).
*   **Slide 25: Pseudoestados Especiais e Pontos de Conexão** — Estado de Submáquina, Ponto de Entrada/Saída e Pseudoestado de Término ($\bigotimes$) (`Fig9.15.png`, `Fig9.17.png`, `Fig9.18.png`).
*   **Slide 26: Estudo de Caso Bancário: Máquina de Estados da ContaComum** — Ciclo de vida completo: Cadastrada, Ativa, Bloqueada e Encerrada (`Fig9.20.png`, `Fig9.21.png`, `Fig9.28.png`).
*   **Slide 27: Da Máquina de Estados ao Código Python** — Apresentação do script `exemplo_interacao_estados.py` implementando o State Pattern e despacho de mensagens.
*   **Slide 28: Execução Prática e Rastreamento de Estados em Python** — Visualização das transições no terminal e validação de guardas booleanas.
*   **Slide 29: Atividade Prática: Proposta Comportamental (*TauáDelivery Web*)** — Contextualização dos requisitos para o Subsistema de Pedidos e Pagamentos.
*   **Slide 30: Exemplo Resolvido de Apoio 1: Diagrama de Sequência do Carrinho** — Projeção da figura `modelagem_sequencia_apoio.png`.
*   **Slide 31: Exemplo Resolvido de Apoio 2: Diagrama de Comunicação do Carrinho** — Projeção da figura `modelagem_comunicacao_apoio.png`.
*   **Slide 32: Exemplo Resolvido de Apoio 3: Ciclo de Vida do Pedido em Estados** — Projeção da figura `modelagem_estados_apoio.png`.
*   **Slide 33: Orientações de Entrega das Partes 1, 2, 3 e 4** — Critérios de modelagem, rubrica de avaliação e uso do Mermaid.js / PlantUML.
*   **Slide 34: Síntese da Aula e Boas Práticas** — Recapitulação das diretrizes de modelagem dinâmica e armadilhas a evitar.
*   **Slide 35: Conclusão e Próximos Passos (Aula 23)** — Fechamento da Unidade de Comportamento e introdução aos Diagramas Arquiteturais (Pacotes, Componentes e Implantação).

---

## 💻 4. Código de Apoio Didático

O arquivo [`exemplo_interacao_estados.py`](exemplo_interacao_estados.py) implementa em Python estruturado e legível os conceitos dos Capítulos 7, 8 e 9:
1. **Padrão de Interação (Simulação de Sequência):** Linhas de vida implementadas como instâncias desacopladas (`Cliente`, `TelaCheckoutBoundary`, `PedidoController`, `GatewayPagamentoService`, `PedidoRepository`) com registro de chamadas síncronas, assíncronas e respostas.
2. **Rastreamento de Comunicação Hierárquica:** Impressão em console do fluxo com numeração decimal aninhada (`1`, `1.1`, `1.2`, `1.2.1`, etc.).
3. **Máquina de Estados Finita Completa (`PedidoStateMachine`):**
   - Estados: `CRIADO`, `AGUARDANDO_PAGAMENTO`, `EM_PREPARO`, `PRONTO_PARA_COLETA`, `EM_ROTA_DE_ENTREGA`, `ENTREGUE` e `CANCELADO`.
   - Execução de atividades `entry /` e `exit /` associadas a cada estado.
   - Avaliação de condições de guarda (ex.: `[valor_pago >= total]`, `[tempo_expirado]`, `[codigo_otp_valido]`).
   - Prevenção de transições inválidas com lançamento de exceções semânticas.
   - Histórico completo de transições de estado para auditoria.

---

## 📝 5. Atividade Prática

A atividade documentada em [`atividade_pratica.md`](atividade_pratica.md) conduz os estudantes na modelagem dinâmica do *TauáDelivery Web*:
*   **Parte 1: Questões Conceituais:** Diferenciação semântica entre Sequência e Comunicação, uso de operadores `alt` vs. `opt`, e distinção entre Pseudoestados de Escolha e de Junção.
*   **Parte 2: Diagrama de Sequência:** Modelagem completa da interação do caso de uso *UC03: Finalizar Pedido e Processar Pagamento*, abrangendo o ator `Cliente`, controller, gateway Pix externo e gravação via repositório.
*   **Parte 3: Diagrama de Comunicação:** Conversão estrutural do fluxo da Parte 2 para vínculos topológicos com numeração de mensagens aninhada.
*   **Parte 4: Diagrama de Máquina de Estados:** Mapeamento de todos os estados do `Pedido`, identificando gatilhos, guardas, efeitos e atividades internas `entry`/`exit`.
*   **Gabarito Comentado e Rubrica:** Modelos resolvidos em sintaxe Mermaid e critérios claros de avaliação.
