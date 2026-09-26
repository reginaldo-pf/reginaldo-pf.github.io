# Plano de Aula: 14 - Regressão Linear Simples

*   **Módulo:** Análise Exploratória de Dados e Estatística Inferencial
*   **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
*   **Instituição:** IFCE Campus Tauá
*   **Carga Horária:** 2 horas (120 minutos), dividida em dois blocos de 60 minutos
*   **Código de Apoio:** [`codigo_apoio.py`](file:///home/reginaldo-fernandes/CDD/aula14/codigo_apoio.py)

---

## 🎯 Objetivos de Aprendizagem

### Geral
Capacitar os alunos a compreender a regressão linear simples a partir da reta de regressão em unidades padrão e da minimização da função de perda (Raiz do Erro Quadrático Médio - $RMSE$), transicionando para a modelagem nas unidades originais dos dados e habilitando-os a avaliar diagnósticos de resíduos e realizar inferência sobre os parâmetros do modelo.

### Específicos
1.  Compreender a reta de regressão em unidades padrão (Z-scores) e interpretar o Efeito de Regressão (Regressão à Média).
2.  Modelar o problema de ajuste linear como um problema de otimização de uma Função de Perda (Raiz do Erro Quadrático Médio - $RMSE$).
3.  Calcular analiticamente a inclinação (Slope $\beta$) e o intercepto (Intercepto $\alpha$) de mínimos quadrados nas unidades originais dos dados.
4.  Calcular e interpretar o Coeficiente de Determinação ($R^2$) como métrica de qualidade de ajuste.
5.  Diagnosticar visualmente problemas de não-linearidade e heterocedasticidade a partir de Gráficos de Resíduos.
6.  Estimar o Intervalo de Confiança ($IC$) do Slope ($\beta$) via Bootstrap e validar utilizando a biblioteca `statsmodels` do Python.

---

## ⏱️ Cronograma Recomendado

| Horário | Duração | Bloco | Conteúdo / Atividade |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:10** | 10 min | 1 | Introdução: Do problema da média condicional local para a reta global. |
| **00:10 - 00:20** | 10 min | 1 | Reta de Regressão em Unidades Padrão e o Efeito de Regressão. |
| **00:20 - 00:35** | 15 min | 1 | A Função de Perda: Raiz do Erro Quadrático Médio ($RMSE$). |
| **00:35 - 00:45** | 10 min | 1 | O Método dos Mínimos Quadrados Ordinários ($OLS$) e minimização analítica. |
| **00:45 - 01:00** | 15 min | 1 | **Exemplo Pareado 1:** Cálculo do melhor beta normalizado via otimização numérica. |
| **01:00 - 01:15** | 15 min | 2 | Transição para Unidades Originais: Fórmulas de $\beta$ (slope) e $\alpha$ (intercepto). |
| **01:15 - 01:30** | 15 min | 2 | Coeficiente de Determinação ($R^2$) e o Desvio Padrão dos Resíduos ($SD_{res}$). |
| **01:30 - 01:45** | 15 min | 2 | Diagnósticos de Resíduos: Homocedasticidade, Heterocedasticidade e Não-Linearidade. |
| **01:45 - 02:00** | 15 min | 2 | **Exemplo Pareado 2:** Inferência por Intervalo de Confiança ($IC$) via Bootstrap vs. `statsmodels` (Dados de Gambás). |

---

## 🗂️ Slides Sugeridos e Roteiro de Aula

### Bloco 14.1: Predição, Reta em Unidades Padrão e Função de Perda (60 minutos)
*Slides correspondentes ao arquivo:* [`secao1_perda_otimizacao.tex`](file:///home/reginaldo-fernandes/CDD/aula14/secao1_perda_otimizacao.tex)

#### Slide 1: Título e Apresentação
*   **Título:** Introdução à Regressão Linear
*   **Pontos-chave:** Transição da análise de associação (correlação) para modelagem preditiva e funcional.
*   **Nota do Professor:** Situe a regressão linear simples como o ponto de partida clássico tanto da Estatística Inferencial quanto do Aprendizado de Máquina (Machine Learning).

#### Slide 2: Do Local para o Global (Contextualização)
*   **Título:** Como Predizer $Y$ a partir de $X$?
*   **Pontos-chave:**
    *   Podemos segmentar o eixo X em pequenas janelas (vizinhos mais próximos) e tomar a média condicional de $Y$ nessas janelas.
    *   O que fazer se os dados forem esparsos e quisermos uma função contínua para predizer em qualquer ponto?
    *   A solução é ajustar uma linha reta global contínua.
*   **Nota do Professor:** Explique que a reta representa uma média condicional suavizada que resume a tendência de toda a dispersão.
*   **Elemento Visual:** Gráficos intuitivos conectando médias locais a retas globais.

#### Slide 3: Reta em Unidades Padrão
*   **Título:** A Linha de Regressão em Unidades Padrão
*   **Pontos-chave:**
    *   Após a Z-normalização, os dados centram-se em $(0,0)$ com desvio padrão igual a 1.
    *   A reta de mínimos quadrados em unidades padrão possui a equação:
        $$\hat{y}_{su} = r \cdot x_{su}$$
    *   Sempre passa pela origem e possui inclinação igual ao Coeficiente de Correlação de Pearson ($r$).
*   **Nota do Professor:** Discuta o porquê de a inclinação ser exatamente $r$ e não 1 (linha de 45 graus).

#### Slide 4: O Efeito de Regressão
*   **Título:** Efeito de Regressão (Regressão à Média)
*   **Pontos-chave:**
    *   Como $|r| \leq 1$, a inclinação da reta é menor ou igual a 1.
    *   "Se o pai é extremamente alto ($x_{su} = 3.0$), o filho tende a ser alto, mas mais próximo da média do que o pai ($y_{su} = 3.0 \cdot r$)."
*   **Nota do Professor:** Explique a intuição física e histórica da regressão à média descoberta por Sir Francis Galton.
*   **Elemento Visual:** Gráfico [`grafico_linha_45.png`](file:///home/reginaldo-fernandes/CDD/aula14/grafico_linha_45.png).

#### Slide 5: Erro de Estimativa e Função de Perda
*   **Título:** Minimização de Erros de Predição
*   **Pontos-chave:**
    *   Qualquer reta escolhida gerará um erro de estimativa (resíduo) para cada observação:
        $$e_i = y_i - \hat{y}_i$$
    *   Buscamos minimizar o erro global através da Raiz do Erro Quadrático Médio ($RMSE$):
        $$RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$$
*   **Nota do Professor:** Explique que usar o quadrado penaliza erros maiores de forma mais severa e evita que erros positivos e negativos se cancelem na soma.

#### Slide 6: Exemplo Pareado: Otimização Numérica (Python)
*   **Título:** Resolvendo por Otimização Numérica
*   **Pontos-chave:** Definição da função de perda ($RMSE$) e minimização do parâmetro beta utilizando `scipy.optimize.minimize` para dados em unidades padrão.
*   **Nota do Professor:** Demonstre que a otimização numérica chega ao mesmo resultado analítico ($\beta_{su} = r$) de Pearson. O slide deve declarar `[fragile]`.
*   **Elemento Visual:** Bloco de código Python contido no script didático.

---

### Bloco 14.2: Unidades Originais, Diagnósticos e Inferência (60 minutos)
*Slides correspondentes ao arquivo:* [`secao2_regressao_diagnosticos.tex`](file:///home/reginaldo-fernandes/CDD/aula14/secao2_regressao_diagnosticos.tex)

#### Slide 7: A Reta de Regressão nas Unidades dos Dados
*   **Título:** Equação nas Unidades Originais
*   **Pontos-chave:**
    *   Reta real de regressão: $\hat{y} = \beta X + \alpha$
    *   Slope ($\beta$) descreve a taxa de variação de Y por unidade de X:
        $$\beta = r \cdot \frac{s_y}{s_x}$$
    *   Intercepto ($\alpha$) define a previsão para $X = 0$:
        $$\alpha = \bar{Y} - \beta \bar{X}$$
*   **Nota do Professor:** Explicite o significado físico das unidades do Slope (unidades de Y dividido pelas unidades de X) e do Intercepto (unidades de Y).

#### Slide 8: Coeficiente de Determinação ($R^2$)
*   **Título:** Avaliando a Qualidade: O R-Quadrado
*   **Pontos-chave:**
    *   Fração da variabilidade total da variável resposta $Y$ que é explicada pelo modelo:
        $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{Y})^2}$$
    *   Na regressão linear simples, é matematicamente igual a $r^2$.
    *   Varia entre 0 (modelo não explica nada) e 1 (ajuste linear perfeito).
*   **Nota do Professor:** Comente que um $R^2 = 0.65$ significa que 65\% da variação de Y é explicada linearmente por X.

#### Slide 9: Diagnósticos de Resíduos (Teoria e Visão)
*   **Título:** Gráficos de Resíduos (Residual Plots)
*   **Pontos-chave:**
    *   Plotar os resíduos ($e_i$) no eixo Y vs. o preditor ($x_i$) no eixo X.
    *   Modelo ideal (Homocedástico): Dispersão de pontos horizontal, simétrica e sem qualquer tendência ou curvatura em torno da linha $e=0$.
    *   Padrões indesejados a diagnosticar: Não-linearidade (curvas) e Heterocedasticidade (padrão em funil).
*   **Nota do Professor:** O gráfico de resíduos amplifica as imperfeições do ajuste, sendo a ferramenta mais sensível de diagnóstico.

#### Slide 10: Diagnósticos Visuais: Exemplos Gráficos
*   **Título:** Tipos de Gráficos de Resíduos
*   **Pontos-chave:** Apresentação comparativa dos plots homocedásticos, não-lineares e heterocedásticos.
*   **Nota do Professor:** Use os gráficos gerados pelo script didático ([`diagnostico_linear.png`](file:///home/reginaldo-fernandes/CDD/aula14/diagnostico_linear.png), [`diagnostico_nao_linear.png`](file:///home/reginaldo-fernandes/CDD/aula14/diagnostico_nao_linear.png), [`diagnostico_heterocedastico.png`](file:///home/reginaldo-fernandes/CDD/aula14/diagnostico_heterocedastico.png)).
*   **Elemento Visual:** Imagens dos três plots gerados pelo script.

#### Slide 11: Desvio Padrão dos Resíduos
*   **Título:** O Desvio Padrão dos Resíduos ($SD_{res}$)
*   **Pontos-chave:**
    *   Mete o espalhamento vertical dos pontos em torno da reta de regressão.
    *   Se a distribuição for homocedástica e normal, cerca de 95\% dos pontos estarão dentro de $\pm 2 \cdot SD_{res}$ da reta.
    *   Fórmula empírica e analítica:
        $$SD_{res} = \sqrt{\frac{\sum e_i^2}{N - 2}} \approx \sqrt{1 - r^2} \cdot s_y$$
*   **Nota do Professor:** Mostre como $SD_{res}$ diminui à medida que o coeficiente de correlação $r$ aumenta.

#### Slide 12: Inferência Computacional via Bootstrap
*   **Título:** Intervalo de Confiança ($IC$) do Slope via Bootstrap
*   **Pontos-chave:**
    *   Regressões são calculadas sobre amostras. Como saber o erro padrão do Slope na população?
    *   Aproximação computacional (Bootstrap de Pares): Reamostrar as linhas da tabela com reposição, calcular o slope para cada réplica e extrair os percentis 2.5\% e 97.5\% para construir o Intervalo de Confiança ($IC$) de 95\%.
*   **Nota do Professor:** Explique que o Bootstrap dispensa suposições rígidas de normalidade populacional exigidas pela estatística clássica.

#### Slide 13: Exemplo Pareado: Estudo do Caso dos Gambás (Possum)
*   **Título:** Aplicação Real e Inferência
*   **Pontos-chave:** Relação entre comprimento do corpo e tamanho da cabeça de 140 gambás.
    *   $\hat{y} = 0.5743 \cdot X + 42.6419$
    *   $R^2 = 0.65739$
    *   Estatísticas clássicas (`statsmodels`) vs. Bootstrap do slope.
*   **Nota do Professor:** Mostre que os resultados analíticos e computacionais concordam, fortalecendo a credibilidade dos métodos de simulação. O slide deve declarar `[fragile]`.
*   **Elemento Visual:** Tabelas de regressão e códigos de Bootstrap.

---

## 🐍 Código Didático de Demonstração

O professor deve guiar os alunos pela execução do script [`codigo_apoio.py`](file:///home/reginaldo-fernandes/CDD/aula14/codigo_apoio.py) no notebook dos alunos. O script foi validado para rodar no ambiente do curso:

```bash
# Execução no terminal usando o interpretador do curso
/home/reginaldo-fernandes/CDD/aula10/.venv/bin/python3 codigo_apoio.py
```

---

## ✍️ Exercícios Propostos (Atividade Entregável)

1.  **Cálculo e Ajuste Analítico:**
    Considere as variáveis de tempo de estudo em horas ($X$) e a nota final obtida na prova ($Y$) de 5 alunos:
    *   $X = [1, 3, 5, 7, 9]$
    *   $Y = [45, 55, 68, 80, 92]$
    *   *(a)* Calcule as médias e os desvios padrão amostrais de ambas as variáveis.
    *   *(b)* Encontre a inclinação ($\beta$) e o intercepto ($\alpha$) da reta de mínimos quadrados nas unidades originais dos dados.
    *   *(c)* Escreva a equação preditiva final. Qual a previsão de nota para um estudante que estudou 6 horas?

2.  **Qualidade de Ajuste e Resíduos:**
    Ainda com os dados do exercício anterior:
    *   *(a)* Obtenha os valores preditos ($\hat{y}$) e os resíduos ($e$) para cada um dos 5 alunos.
    *   *(b)* Verifique numericamente que a média dos resíduos é zero.
    *   *(c)* Calcule o Coeficiente de Determinação ($R^2$) e o Desvio Padrão dos Resíduos ($SD_{res}$). O que esses valores dizem sobre a adequação do modelo?

3.  **Análise de Diagnóstico Computacional:**
    Escreva um script em Python que:
    *   *(a)* Carregue o dataset [`possum.csv`](file:///home/reginaldo-fernandes/CDD/aula14/possum.csv) (ou baixe via URL do script de apoio).
    *   *(b)* Selecione `totalL` como $X$ e `headL` como $Y$, limpe as observações com nulos.
    *   *(c)* Ajuste um modelo linear simples usando a biblioteca `statsmodels` e imprima o sumário.
    *   *(d)* Plote o Gráfico de Resíduos e avalie visualmente se o modelo linear atende às suposições de linearidade e homocedasticidade.
    *   *(e)* Implemente uma rotina de Bootstrap com 1000 replicações e compare o Intervalo de Confiança ($IC$) do Slope ($\beta$) obtido via Bootstrap com o intervalo clássico da tabela do `statsmodels`.
