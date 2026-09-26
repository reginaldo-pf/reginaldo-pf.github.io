# Plano de Aula: 14 (Parte 2) - Introdução à Função de Verossimilhança e Máxima Verossimilhança

*   **Módulo:** Modelagem Estatística e Ciência de Dados
*   **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
*   **Instituição:** IFCE Campus Tauá
*   **Carga Horária:** 2 horas (120 minutos)
*   **Código de Apoio:** [`codigo_apoio.py`](file:///home/reginaldo-fernandes/CDD/aula14/parte%202/codigo_apoio.py)

---

## 🎯 Objetivos de Aprendizagem

### Geral
Apresentar o conceito da Função de Verossimilhança ($L$) e o método de Estimativa de Máxima Verossimilhança ($MLE$ - Maximum Likelihood Estimation) como princípios fundamentais para estimar parâmetros populacionais a partir de dados amostrais observados, diferenciando probabilidade de verossimilhança e estendendo o conceito do caso discreto para o contínuo.

### Específicos
1.  **Diferenciar** conceitualmente Probabilidade de Verossimilhança a partir de cenários práticos de amostragem.
2.  **Formular matematicamente** a Função de Verossimilhança ($L$) para o modelo discreto de Bernoulli (ensaios de moedas) e obter o seu ponto de máximo graficamente e analiticamente.
3.  **Compreender e aplicar** a transformação de Log-Verossimilhança ($\ln L$) para simplificar operações de produtos em somatórios e evitar subfluxo numérico (*underflow*).
4.  **Formular a Verossimilhança** para dados contínuos assumindo uma distribuição Normal (Gaussiana) e derivar analiticamente os estimadores de máxima verossimilhança da Média Populacional ($\mu$) e Variância Populacional ($\sigma^2$).
5.  **Explicar a conexão** entre a minimização do Erro Quadrático Médio ($MSE$) na regressão linear e a maximização da Log-Verossimilhança de um ruído Gaussiano.
6.  **Implementar computacionalmente** em Python a avaliação de funções de verossimilhança para diferentes valores de parâmetros.

---

## ⏱️ Cronograma Recomendado

| Horário | Duração | Bloco | Conteúdo / Atividade |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:15** | 15 min | 1 | **Conceito Fundamental:** O que é verossimilhança? Diferença entre probabilidade e plausibilidade dos parâmetros. |
| **00:15 - 00:35** | 20 min | 1 | **O Caso Discreto (Bernoulli):** Ensaios independentes de Bernoulli (cara ou coroa), definição de $L(\theta)$ e gráfico da curva de verossimilhança. |
| **00:35 - 00:50** | 15 min | 1 | **A Log-Verossimilhança ($\ln L$):** Justificativa matemática e computacional para a mudança de escala. |
| **00:50 - 01:00** | 10 min | 1 | **Exemplo Pareado 1:** Derivação analítica do estimador da proporção $\theta$ vs. código Python. |
| **01:00 - 01:25** | 25 min | 2 | **O Caso Contínuo (Normal):** Densidade de probabilidade para dados contínuos. A Função de Verossimilhança Gaussiana para a média ($\mu$) e variância ($\sigma^2$). |
| **01:25 - 01:40** | 15 min | 2 | **Exemplo Pareado 2:** Cálculo manual da log-verossimilhança normal vs. código Python equivalente. |
| **01:40 - 02:00** | 20 min | 2 | **Atividade Prática:** Implementação do cálculo da log-verossimilhança e estimação de parâmetros de uma amostra normal em Python. |

---

## 🗂️ Slides Sugeridos e Roteiro de Aula

### Bloco 14.2.1: Conceito de Verossimilhança e o Caso Bernoulli (60 minutos)
*Slides correspondentes ao arquivo:* [`secao1_bernoulli.tex`](file:///home/reginaldo-fernandes/CDD/aula14/parte%202/secao1_bernoulli.tex)

#### Slide 1: Título e Apresentação
*   **Título:** Introdução à Função de Verossimilhança e Máxima Verossimilhança
*   **Pontos-chave:** O pilar da inferência estatística moderna em Ciência de Dados.
*   **Nota do Professor:** Introduza o tema explicando que até agora sabíamos como medir erros geométricos, mas agora aprenderemos a quantificar a plausibilidade estatística de parâmetros em modelos populacionais.

#### Slide 2: Probabilidade vs. Verossimilhança
*   **Título:** O Sentido Oposto da Inferência
*   **Pontos-chave:**
    *   **Probabilidade:** Parâmetro populacional $\theta$ é conhecido. Queremos saber a chance de obter certos dados $X$ (Dedutivo: Geral $\rightarrow$ Particular).
    *   **Verossimilhança:** Os dados $X$ já foram observados. Queremos avaliar quais parâmetros $\theta$ tornam esses dados mais plausíveis (Indutivo: Particular $\rightarrow$ Geral).
*   **Nota do Professor:** Use a metáfora de uma moeda: se eu sei que a moeda é justa ($\theta=0.5$), posso prever a chance de tirar 3 caras. Se eu joguei a moeda 10 vezes e saíram 8 caras, quero saber se a moeda é viciada e qual o valor mais provável de $\theta$.

#### Slide 3: O Experimento de Lançamento de Moedas (Bernoulli)
*   **Título:** Função de Verossimilhança de Bernoulli
*   **Pontos-chave:**
    *   Modelo Bernoulli: $X_i \in \{0, 1\}$ com $P(X_i = 1) = \theta$ e $P(X_i = 0) = 1-\theta$.
    *   Função de Massa de Probabilidade ($PMF$): $P(X_i = x_i) = \theta^{x_i}(1-\theta)^{1-x_i}$.
    *   Para uma amostra de tamanho $N$ independente:
        $$L(\theta) = \prod_{i=1}^N \theta^{x_i}(1-\theta)^{1-x_i} = \theta^{\sum x_i}(1-\theta)^{N-\sum x_i}$$
*   **Nota do Professor:** Aponte que a verossimilhança é o produto das probabilidades de cada observação individual porque assumimos que os lançamentos são independentes.

#### Slide 4: Gráfico de Verossimilhança de Bernoulli
*   **Título:** Curva de Plausibilidade
*   **Pontos-chave:**
    *   Dado um experimento real: lançamos a moeda $N=13$ vezes e obtivemos 4 caras (sucessos) e 9 coroas (fracassos).
    *   A função assume a forma: $L(\theta) = \theta^4(1-\theta)^9$.
    *   O ponto de máximo ocorre exatamente no valor $\theta \approx 0.3077$.
*   **Nota do Professor:** Chame a atenção para o fato de que a escala de $L(\theta)$ é muito pequena (valores da ordem de $10^{-4}$), o que introduz problemas numéricos.
*   **Elemento Visual:** Gráfico [`verossimilhanca_bernoulli.png`](file:///home/reginaldo-fernandes/CDD/aula14/parte%202/verossimilhanca_bernoulli.png).

#### Slide 5: A Log-Verossimilhança ($\ln L$)
*   **Título:** O Poder do Logaritmo
*   **Pontos-chave:**
    *   Multiplicações de probabilidades menores que 1 decaem rapidamente para zero em computadores (*underflow*).
    *   A aplicação do logaritmo natural ($\ln$) transforma produtos em somas:
        $$\ln L(\theta) = \ln \left( \prod P(X_i) \right) = \sum_{i=1}^N \ln P(X_i)$$
    *   Como a função logaritmo é estritamente crescente, o valor de $\theta$ que maximiza $L(\theta)$ também maximiza $\ln L(\theta)$.
*   **Nota do Professor:** Explique que trabalhar com somas facilita a derivação no cálculo diferencial.

#### Slide 6: Exemplo Pareado 1: Derivação de Moeda Passo a Passo
*   **Título:** Máxima Verossimilhança Analítica
*   **Pontos-chave:**
    *   Para o caso de moedas: $\ln L(\theta) = (\sum x_i) \ln \theta + (N - \sum x_i) \ln(1-\theta)$.
    *   Derivando com relação a $\theta$ e igualando a zero:
        $$\frac{d\ln L(\theta)}{d\theta} = \frac{\sum x_i}{\theta} - \frac{N - \sum x_i}{1 - \theta} = 0 \implies \hat{\theta}_{MLE} = \frac{\sum x_i}{N}$$
    *   Para a nossa amostra: $\hat{\theta}_{MLE} = 4 / 13 \approx 0.3077$.
*   **Nota do Professor:** Mostre que a matemática concorda com a nossa intuição de usar a frequência relativa da amostra como o melhor estimador.

#### Slide 7: Exemplo Pareado 1: Código Equivalente em Python
*   **Título:** Implementação em Python
*   **Pontos-chave:** Definição da PMF de Bernoulli e avaliação da verossimilhança e log-verossimilhança de forma vetorizada com NumPy.
*   **Elemento Visual:** Bloco de código em Python contido no script didático (declarar frame `[fragile]`).

---

### Bloco 14.2.2: O Caso Contínuo (Normal) e Atividade (60 minutos)
*Slides correspondentes ao arquivo:* [`secao2_normal.tex`](file:///home/reginaldo-fernandes/CDD/aula14/parte%202/secao2_normal.tex)

#### Slide 8: Verossimilhança de Dados Contínuos
*   **Título:** Modelando Dados Contínuos
*   **Pontos-chave:**
    *   Para variáveis contínuas, usamos a Função de Densidade de Probabilidade ($PDF$) em vez da $PMF$.
    *   Assumimos que nossos dados seguem uma distribuição Normal $N(\mu, \sigma^2)$:
        $$f(x_i | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right)$$
    *   A Função de Verossimilhança de uma amostra independente de tamanho $N$ é:
        $$L(\mu, \sigma^2) = \prod_{i=1}^N f(x_i | \mu, \sigma^2)$$

#### Slide 9: A Log-Verossimilhança Gaussiana
*   **Título:** Simplificação do Modelo Normal
*   **Pontos-chave:**
    *   Aplicando o logaritmo natural ($\ln$) na verossimilhança Gaussiana:
        $$\ln L(\mu, \sigma^2) = -\frac{N}{2} \ln(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^N (x_i - \mu)^2$$
    *   Note que, para maximizar com relação a $\mu$, o primeiro termo é constante e a segunda parcela deve ser maximizada (o que equivale a minimizar a soma dos quadrados $(x_i - \mu)^2$).
*   **Nota do Professor:** Destaque a conexão de ouro: a minimização dos quadrados (como em Mínimos Quadrados de Regressão) surge naturalmente da maximização da verossimilhança sob a hipótese de ruído Gaussiano!

#### Slide 10: Derivação dos Estimadores Gaussianos
*   **Título:** Estimadores de Máxima Verossimilhança (Normal)
*   **Pontos-chave:**
    *   Para a Média populacional ($\mu$):
        $$\frac{\partial \ln L}{\partial \mu} = \frac{1}{\sigma^2} \sum_{i=1}^N (x_i - \mu) = 0 \implies \hat{\mu}_{MLE} = \bar{X}$$
    *   Para a Variância populacional ($\sigma^2$):
        $$\frac{\partial \ln L}{\partial (\sigma^2)} = 0 \implies \hat{\sigma}^2_{MLE} = \frac{1}{N} \sum_{i=1}^N (x_i - \bar{X})^2$$
*   **Nota do Professor:** Explique que o estimador $MLE$ da variância divide por $N$ e não por $N-1$, o que o torna ligeiramente tendencioso (viesado) para pequenas amostras.

#### Slide 11: Exemplo Pareado 2: Cálculo da Verossimilhança Gaussiana
*   **Título:** Cálculo Computacional da Plausibilidade Gaussiana
*   **Pontos-chave:**
    *   Carregar uma amostra contínua de comprimento de peças ou dados simulados.
    *   Calcular a média e desvio padrão amostrais.
    *   Escrever a função de log-verossimilhança Gaussiana em Python e testar diferentes valores de $\mu$ para encontrar o ponto de máximo.
*   **Elemento Visual:** Código Python e gráficos de log-verossimilhança da média.

#### Slide 12: Apresentação da Atividade Prática
*   **Título:** Atividade de Laboratório (Estimando Parâmetros via MLE)
*   **Pontos-chave:** Diretrizes para os alunos implementarem as funções de verossimilhança em Python a partir de dados reais de gambás ou moedas e extraírem o melhor modelo.

---

## 🐍 Código Didático de Demonstração

O professor deve guiar os alunos pelo arquivo [`codigo_apoio.py`](file:///home/reginaldo-fernandes/CDD/aula14/parte%202/codigo_apoio.py). Ele contém a implementação vetorizada da função de verossimilhança de Bernoulli e Gaussiana, além das rotinas que geram os gráficos a serem exibidos nos slides da aula.

---

## ✍️ Atividade Prática Final (Entregável)

Os alunos deverão criar e executar um Jupyter Notebook para realizar as seguintes tarefas:

### Questão 1: Simulação e Máxima Verossimilhança Discreta
1.  Considere um experimento de lançar uma moeda onde a probabilidade verdadeira de obter cara é $\theta = 0.65$. Simule 100 lançamentos dessa moeda utilizando `np.random.choice` ou `np.random.binomial`.
2.  Implemente a função `log_verossimilhanca_bernoulli(dados, theta)` que recebe a série de dados e um valor candidato de $\theta$.
3.  Avalie a função para um grid de valores candidatos de $\theta \in [0.01, 0.99]$.
4.  Gere um gráfico da curva de log-verossimilhança em função dos valores Candidatos.
5.  Determine numericamente qual valor de $\theta$ no grid maximiza a log-verossimilhança e compare com o estimador de proporção empírica ($\frac{\text{sucessos}}{N}$).

### Questão 2: MLE para Distribuição Normal
1.  Utilizando uma amostra simulada de idades de usuários em um sistema, com parâmetros verdadeiros de $\mu = 30$ e $\sigma = 5$ (tamanho $N=50$):
    ```python
    np.random.seed(42)
    dados = np.random.normal(loc=30, scale=5, size=50)
    ```
2.  Implemente a função da Log-Verossimilhança Gaussiana em Python:
    `log_verossimilhanca_normal(dados, mu, sigma)`
3.  Mantenha o valor do desvio padrão fixo em $\sigma = 5.0$ e calcule a log-verossimilhança para um grid de médias candidatas $\mu \in [20, 40]$.
4.  Plote a curva e encontre o valor de $\mu$ que atinge o máximo de plausibilidade. Esse valor coincide com `np.mean(dados)`? Explique o porquê.
