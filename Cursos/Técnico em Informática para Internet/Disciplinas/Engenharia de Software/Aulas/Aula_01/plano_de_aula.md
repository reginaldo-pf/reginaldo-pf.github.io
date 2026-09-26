# Plano de Aula: Aula 1 - Simulação de Primeira Reunião Pós-Backlog e Planejamento da Sprint 1

*   **Disciplina:** Engenharia de Software
*   **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
*   **Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá
*   **Tema:** Estimativa de Esforço com Planning Poker, Planejamento da Sprint 1 e Distribuição de Tarefas para uma Equipe de 5 Alunos com Simulação de Monte Carlo.

---

## 💡 1. Filosofia Pedagógica e Metodologia

Esta aula adota a metodologia de Aprendizagem Baseada em Projetos (ABP) combinada com a simulação do cotidiano profissional de uma equipe Scrum. O conteúdo se desenvolve em quatro pilares metodológicos:

1.  **Contextualização Prática (Problema de Negócio):** O desafio de uma equipe de 5 desenvolvedores recém-formada que precisa estimar o esforço de um novo produto (Sistema de Finanças Familiares com IA) e definir quais tarefas cabem na primeira sprint de 2 semanas, sem histórico prévio de velocidade do grupo.
2.  **Método Teórico Clássico:** Aplicação da sequência de Fibonacci para estimativa de esforço relativo, cálculo da Média Amostral ($\bar{X}$) dos Story Points (Pontos de História), cálculo do Desvio Padrão Amostral ($s$) e do Erro Padrão ($SE$) para medir a incerteza das estimativas da equipe.
3.  **Abordagem Computacional (Simulação):** Uso de um script Python para realizar uma Simulação de Monte Carlo (10.000 iterações) que projeta o cronograma de sprints com base na oscilação da velocidade amostral da equipe.
4.  **Tomada de Decisão Visual:** Análise de um gráfico de Função de Distribuição Acumulada Empírica (ECDF) gerado pela simulação para determinar prazos de entrega com níveis de confiança de 50%, 80% e 90%, ensinando os alunos a gerenciarem riscos de escopo e cronograma.

---

## 🎯 2. Objetivos de Aprendizagem

### Geral
Capacitar os alunos a simularem uma reunião de planejamento de sprint (Sprint Planning), aplicando técnicas estatísticas e computacionais de estimativa de esforço para organizar o backlog, estimar tarefas e distribuir o trabalho de forma equilibrada em uma equipe de 5 desenvolvedores utilizando Next.js 16.

### Específicos
*   Compreender e aplicar o concept de estimativa de esforço relativo (Story Points) usando a sequência de Fibonacci.
*   Calcular de forma analítica e manual a incerteza estatística (Média Amostral, Desvio Padrão Amostral e Erro Padrão) sobre as estimativas.
*   Executar e interpretar uma simulação Monte Carlo em Python para projetar o prazo total do projeto (número de sprints) com base na variabilidade da velocidade.
*   Distribuir o backlog da primeira sprint de forma equilibrada e orientada por perfis arquiteturais em Next.js 16.
*   Definir metas individuais de gerenciamento de objetivos para cada membro da equipe.

---

## ⏱️ 3. Cronograma Recomendado (100 Minutos)

| Tempo | Atividade | Descrição |
| :--- | :--- | :--- |
| **00 - 15 min** | **Apresentação do Problema** | Contextualização do projeto *FamilyFinance.AI* e apresentação do Documento de Requisitos e Backlog Inicial. |
| **15 - 35 min** | **Teoria Clássica e Estimativa** | Explicação de Story Points, Planning Poker e cálculo estatístico manual de capacidade e incerteza ($s$ e $SE$). |
| **35 - 55 min** | **Abordagem Computacional** | Apresentação e execução do script Python de simulação Monte Carlo para prazo e velocidade. |
| **55 - 75 min** | **Planejamento da Sprint 1** | Divisão de tarefas práticas entre os 5 alunos (perfis), justificando pelo esforço estimado em pontos. |
| **75 - 90 min** | **Guia de Gestão e OKRs** | Como cada aluno usará o guia individual para controlar seu progresso técnico. |
| **90 - 100 min**| **Encerramento e Exercícios** | Discussão sobre tomada de decisão visual (ECDF) e orientações sobre a entrega prática. |

---

## 👨‍🏫 4. Roteiro de Slides Sugeridos (Beamer)

*   **Slide 1: Título da Aula**
    *   **Título:** Planejamento e Estimativa de Projetos Ágeis com Simulação Monte Carlo.
    *   **Tópicos:** Apresentação do Projeto *FamilyFinance.AI*, Métodos Ágeis no IFCE Campus Tauá.
    *   **Nota do Professor:** Acolher a turma e explicar que a aula simulará uma reunião real de Sprint Planning.
*   **Slide 2: O Problema de Negócio**
    *   **Título:** Contexto e Requisitos do FamilyFinance.AI.
    *   **Tópicos:** Registro diário de gastos; Relatórios mensais estruturados; Vínculo familiar de contas (multi-tenant); Planejamento financeiro preditivo via Inteligência Artificial (Gemini API).
    *   **Elemento Visual:** Diagrama simples de blocos mostrando o Usuário, o Vínculo Familiar, as transações e o módulo de IA.
*   **Slide 3: Fundamentação Teórica - Esforço Relativo**
    *   **Título:** Por que Story Points e não Horas?
    *   **Tópicos:** Complexidade, incerteza e esforço. Sequência de Fibonacci ($1, 2, 3, 5, 8, 13$). Planning Poker para obter consenso.
    *   **Nota do Professor:** Enfatizar que horas geram falsa precisão. Pontos comparam o tamanho das tarefas de forma relativa.
*   **Slide 4: Exemplo Teórico Analítico (Cálculo Passo a Passo)**
    *   **Título:** Estatística Aplicada às Estimativas.
    *   **Tópicos:** Cálculo da Média Amostral ($\bar{X}$), Desvio Padrão Amostral ($s$) e Erro Padrão ($SE$).
    *   **Fórmulas:**
        $$\bar{X} = \frac{\sum X_i}{N}$$
        $$s = \sqrt{\frac{\sum (X_i - \bar{X})^2}{N - 1}}$$
        $$SE = \frac{s}{\sqrt{N}}$$
    *   **Nota do Professor:** Resolver no quadro o exemplo clássico de 5 desenvolvedores estimando uma mesma tarefa com as notas: $3, 5, 5, 8, 5$.
*   **Slide 5: Demonstração Computacional Equivalente (Código Python)**
    *   **Título:** Verificação Computacional das Estimativas.
    *   **Tópicos:** Script simples em Python para calcular média, desvio padrão e erro padrão amostral a partir de uma lista de palpites.
    *   **Elemento Visual:** Código Python em slide Beamer usando a macro `\textbf` para destaque (sem acentos nos comentários do script).
*   **Slide 6: Simulação de Monte Carlo para Prazo**
    *   **Título:** Projeção de Cronograma com Incerteza.
    *   **Tópicos:** O que é Monte Carlo? Simulação de $10.000$ cenários de velocidade. Como prever a data de entrega de $80$ Story Points do backlog total.
    *   **Nota do Professor:** Mostrar que a velocidade flutua a cada sprint. A simulação ajuda a entender a variação agregada.
*   **Slide 7: Tomada de Decisão Visual (ECDF)**
    *   **Título:** Interpretando a ECDF para Prazos.
    *   **Tópicos:** Nível de Confiança de 50% (cenário provável); Nível de Confiança de 80% (cenário recomendado para compromissos); Nível de Confiança de 90% (cenário pessimista/conservador).
    *   **Elemento Visual:** Gráfico de Função de Distribuição Acumulada Empírica (ECDF) com linhas indicadoras de percentil.
*   **Slide 8: O Backlog da Sprint 1**
    *   **Título:** Divisão de Trabalho para 5 Alunos.
    *   **Tópicos:** Aluno A (Infraestrutura/Next.js 16); Aluno B (Autenticação/Família); Aluno C (CRUD Transações); Aluno D (Dashboard/Relatórios); Aluno E (Integração IA/Gemini).
    *   **Nota do Professor:** Discutir a carga de trabalho de cada aluno baseada no peso das tarefas em Story Points (Equilíbrio de Carga).
*   **Slide 9: Arquitetura Next.js 16**
    *   **Título:** Padrões Arquiteturais Propostos.
    *   **Tópicos:** Next.js 16 (App Router), React 19 Server Components, ORM Prisma para PostgreSQL, Vercel AI SDK.
    *   **Elemento Visual:** Fluxo de dados entre componentes de servidor (RSC), cliente (RCC) e banco de dados.
*   **Slide 10: Conclusão e Diretrizes da Sprint**
    *   **Título:** OKRs e Monitoramento Pessoal.
    *   **Tópicos:** Como o aluno acompanha o seu próprio progresso diário. Uso do Daily Check-in e métricas de autoavaliação.

---

## 🐍 5. Exemplo Teórico-Computacional Pareado (Para Sala de Aula)

### Exemplo Teórico Manual (Passo a Passo)
Imagine que, para a tarefa **"Integrar API do Gemini para gerar relatórios preditivos"**, a equipe de 5 alunos deu as seguintes estimativas em Story Points:
*   Aluno A: $5$ SP
*   Aluno B: $8$ SP
*   Aluno C: $5$ SP
*   Aluno D: $8$ SP
*   Aluno E: $8$ SP

**Passo 1: Calcular a Média Amostral ($\bar{X}$):**
$$\bar{X} = \frac{5 + 8 + 5 + 8 + 8}{5} = \frac{34}{5} = 6.8 \text{ Story Points}$$

**Passo 2: Calcular o Desvio Padrão Amostral ($s$):**
$$s = \sqrt{\frac{(5-6.8)^2 + (8-6.8)^2 + (5-6.8)^2 + (8-6.8)^2 + (8-6.8)^2}{5-1}}$$
$$s = \sqrt{\frac{(-1.8)^2 + (1.2)^2 + (-1.8)^2 + (1.2)^2 + (1.2)^2}{4}}$$
$$s = \sqrt{\frac{3.24 + 1.44 + 3.24 + 1.44 + 1.44}{4}} = \sqrt{\frac{10.8}{4}} = \sqrt{2.7} \approx 1.643 \text{ Story Points}$$

**Passo 3: Calcular o Erro Padrão ($SE$):**
$$SE = \frac{s}{\sqrt{N}} = \frac{1.643}{\sqrt{5}} = \frac{1.643}{2.236} \approx 0.735 \text{ Story Points}$$

O Erro Padrão ($SE$) de $0.735$ mostra a oscilação esperada para a estimativa média da equipe.

---

### Código Python de Demonstração Equivalente
```python
import numpy as np

# Estimativas dos 5 alunos
estimativas = np.array([5, 8, 5, 8, 8])
n = len(estimativas)

# Calculos Estatisticos
media = np.mean(estimativas)
desvio_padrao = np.std(estimativas, ddof=1) # ddof=1 garante o desvio padrao amostral (N-1)
erro_padrao = desvio_padrao / np.sqrt(n)

print(f"Media Amostral: {media:.2f} SP")
print(f"Desvio Padrao Amostral: {desvio_padrao:.2f} SP")
print(f"Erro Padrao: {erro_padrao:.2f} SP")
```

---

## 📝 6. Exercícios Propostos para os Alunos

1.  **Exercício 1 (Estatística Manual):** Durante a reunião, a tarefa "Criar Relatórios Mensais com Gráficos" recebeu as seguintes estimativas da equipe de 5 alunos: $3, 5, 3, 5, 8$ Story Points. Calcule a Média Amostral ($\bar{X}$), o Desvio Padrão Amostral ($s$) e o Erro Padrão ($SE$) do esforço desta tarefa.
2.  **Exercício 2 (Análise de Gráficos e Decisão):** Conforme a simulação Monte Carlo (`simulador_sprint.py`), se a equipe de 5 alunos se comprometer com um prazo de conclusão de 6 sprints para entregar o backlog de 80 SP, qual é o nível de confiança (probabilidade) estatístico obtido? Qual seria o prazo necessário se precisássemos de 90% de confiança?
3.  **Exercício 3 (Modificação de Parâmetros):** Modifique o script `simulador_sprint.py` para simular uma velocidade média reduzida ($\bar{X} = 12$ SP e $s = 4.5$ SP), simulando um membro a menos ou gargalo técnico. Qual o impacto visual e estatístico na curva ECDF para o prazo do projeto?
