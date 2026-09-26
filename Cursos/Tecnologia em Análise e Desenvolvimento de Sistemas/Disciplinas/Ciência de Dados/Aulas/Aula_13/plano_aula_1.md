# Plano de Aula: 13 - Correlação Linear e Associação

*   **Módulo:** Análise Exploratória de Dados e Estatística Inferencial
*   **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
*   **Instituição:** IFCE Campus Tauá
*   **Carga Horária:** 2 horas (120 minutos), dividida em dois blocos de 60 minutos
*   **Código de Apoio:** [`codigo_apoio_aula_1.py`](file:///home/reginaldo-fernandes/CDD/aula13/codigo_apoio_aula_1.py)

---

## 🎯 Objetivos de Aprendizagem

### Geral
Capacitar os alunos a compreender a covariância e a correlação linear como medidas de associação entre duas variáveis quantitativas, habilitando-os a implementar os cálculos em Python, interpretar gráficos de dispersão e diagnosticar armadilhas estatísticas como outliers e o Paradoxo de Simpson.

### Específicos
1. Diferenciar associação linear de associação não-linear a partir de representações visuais.
2. Calcular analiticamente (passo a passo) e computacionalmente a Covariância Amostral ($cov(X, Y)$) e o Coeficiente de Correlação de Pearson ($r$).
3. Compreender a escala e as propriedades matemáticas do Coeficiente de Correlação de Pearson ($r$).
4. Identificar e mitigar a influência de outliers e correlações espúrias.
5. Aplicar o Coeficiente de Correlação de Postos de Spearman ($r_s$) em relações não-lineares monótonas.
6. Identificar e contornar o Paradoxo de Simpson em dados estratificados na tomada de decisão.

---

## ⏱️ Cronograma Recomendado

| Horário | Duração | Bloco | Conteúdo / Atividade |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:05** | 5 min | 1 | Introdução: Problema do mundo real (potência de motor vs consumo). |
| **00:05 - 00:15** | 10 min | 1 | Revisão conceitual de Variância Amostral ($s^2$). |
| **00:15 - 00:30** | 15 min | 1 | Covariância Amostral ($cov(X, Y)$): Definição nos quadrantes geométricos. |
| **00:30 - 00:45** | 15 min | 1 | Coeficiente de Correlação de Pearson ($r$): normalização e limites. |
| **00:45 - 01:00** | 15 min | 1 | **Exemplo Pareado 1:** Cálculo manual de $r$ vs. código Python equivalente. |
| **01:00 - 01:15** | 15 min | 2 | Propriedades de $r$, sensibilidade a outliers e correlação ecológica. |
| **01:15 - 01:30** | 15 min | 2 | Correlação de Postos de Spearman ($r_s$): quando aplicar. |
| **01:30 - 01:50** | 20 min | 2 | O Paradoxo de Simpson: análise de casos reais (COVID-19 e Colesterol). |
| **01:50 - 02:00** | 10 min | 2 | Fechamento: Correlação não é Causalidade e apresentação de Exercícios. |

---

## 🗂️ Slides Sugeridos e Roteiro de Aula

### Bloco 1.1: Fundamentos de Covariância e Pearson (60 minutos)
*Slides correspondentes ao arquivo:* [`aula1_bloco1.tex`](file:///home/reginaldo-fernandes/CDD/aula13/aula1_bloco1.tex)

#### Slide 1: Título e Apresentação
*   **Título:** Associação Linear e Correlação
*   **Pontos-chave:** Introdução do tema no curso de Análise e Desenvolvimento de Sistemas (ADS).
*   **Nota do Professor:** Dê as boas-vindas aos alunos e situe o tema como o passo inicial para a regressão linear e modelagem preditiva em ciência de dados.

#### Slide 2: Problema do Mundo Real (Contextualização)
*   **Título:** Como Mensurar a Relação Entre Duas Variáveis?
*   **Pontos-chave:** Como a aceleração de um veículo varia com o consumo de combustível (milhas por galão)? Como descrever essa relação estatisticamente de forma quantitativa e visual?
*   **Nota do Professor:** Mostre que gráficos nos dão uma intuição visual, mas precisamos de uma métrica formal que nos diga a força e a direção dessa relação.
*   **Elemento Visual:** Gráfico de dispersão clássico com eixos rotulados.

#### Slide 3: Revisão Estatística
*   **Título:** Lembrando da Variância Amostral
*   **Pontos-chave:** A Variância Amostral ($s^2$) sumariza a dispersão de apenas uma variável quantitativa.
    $$s^2 = \frac{\sum_{i=1}^N (x_i - \bar{X})^2}{N - 1}$$
    Como expandir esse conceito para dados bidimensionais ($X$ e $Y$)?
*   **Nota do Professor:** Lembre os alunos que o denominador $N-1$ representa os graus de liberdade na estimativa amostral.

#### Slide 4: Definição Geométrica de Associação
*   **Título:** Quadrantes de Dispersão
*   **Pontos-chave:** Ao traçar linhas na Média Amostral de X ($\bar{X}$) e na Média Amostral de Y ($\bar{Y}$), dividimos o espaço em 4 quadrantes.
    *   Quadrante 1 (Superior Direito): $x_i > \bar{X}$ e $y_i > \bar{Y} \implies$ produto dos desvios é positivo.
    *   Quadrante 3 (Inferior Esquerdo): $x_i < \bar{X}$ e $y_i < \bar{Y} \implies$ produto dos desvios é positivo.
*   **Nota do Professor:** Explique que o sinal do produto das diferenças em relação às médias serve como indicador da direção da associação.
*   **Elemento Visual:** Gráfico com os 4 quadrantes identificados e pontos dispersos.

#### Slide 5: A Covariância Amostral
*   **Título:** Formalizando a Covariância
*   **Pontos-chave:** Medida de dispersão conjunta de duas variáveis quantitativas:
    $$cov(X, Y) = \frac{\sum_{i=1}^N (x_i - \bar{X})(y_i - \bar{Y})}{N - 1}$$
    Se $cov(X, Y) > 0$, a associação é positiva. Se $cov(X, Y) < 0$, a associação é negativa.
*   **Nota do Professor:** Aponte o principal problema da covariância: a unidade de medida final é o produto das unidades das duas variáveis (ex: $kg \cdot m$), o que inviabiliza a interpretação de intensidade.

#### Slide 6: O Coeficiente de Correlação de Pearson ($r$)
*   **Título:** Coeficiente de Correlação de Pearson
*   **Pontos-chave:** Normalização da covariância dividindo pelo Desvio Padrão Amostral ($s_x$, $s_y$) de ambas as variáveis.
    $$r = \frac{cov(X, Y)}{s_x \cdot s_y} = \frac{\sum (x_i - \bar{X})(y_i - \bar{Y})}{\sqrt{\sum (x_i - \bar{X})^2 \sum (y_i - \bar{Y})^2}}$$
    Adimensional, variando estritamente entre $-1$ e $+1$.
*   **Nota do Professor:** Destaque que a divisão cancela as unidades originais, tornando $r$ uma escala universal.

#### Slide 7: Exemplo Pareado (Teórico)
*   **Título:** Exemplo Numérico Passo a Passo
*   **Pontos-chave:** Dado o conjunto de pontos: $(1, 2), (2, 4), (3, 5), (4, 4), (5, 5)$.
    *   $\bar{X} = 3.0$, $\bar{Y} = 4.0$
    *   $cov(X, Y) = 1.5$
    *   $s_x \approx 1.581$, $s_y \approx 1.225$
    *   $r = \frac{1.5}{1.581 \times 1.225} \approx 0.7746$ (Forte associação positiva).
*   **Nota do Professor:** Calcule no quadro cada etapa dessa tabela para fixar a mecânica da equação.

#### Slide 8: Exemplo Pareado (Computacional)
*   **Título:** Implementação do Exemplo em Python
*   **Pontos-chave:** Apresentação do script em Python usando as bibliotecas standard (`numpy` e `scipy.stats`) para calcular $r$.
*   **Nota do Professor:** Comente as funções utilizadas (`np.cov` e `stats.pearsonr`). Garanta que o slide declare `[fragile]`.
*   **Elemento Visual:** Bloco de código Python formatado e limpo.

---

### Bloco 1.2: Propriedades, Outliers, Spearman e Simpson (60 minutos)
*Slides correspondentes ao arquivo:* [`aula1_bloco2.tex`](file:///home/reginaldo-fernandes/CDD/aula13/aula1_bloco2.tex)

#### Slide 9: Propriedades Matemáticas de $r$
*   **Título:** Propriedades do Coeficiente $r$
*   **Pontos-chave:**
    *   Invariante à escala e à translação: somar ou multiplicar constantes aos dados não altera $r$.
    *   Simetria: $r_{XY} = r_{YX}$.
    *   Interpretação geométrica: cosseno do ângulo entre os vetores de desvios padronizados.
*   **Nota do Professor:** Reforce o significado geométrico: vetores ortogonais $\implies r = 0$; vetores colineares de mesma direção $\implies r = 1$.

#### Slide 10: Armadilhas da Correlação Linear
*   **Título:** Limitações de Pearson
*   **Pontos-chave:**
    *   Mede apenas relações lineares.
    *   Apresentação de uma curva quadrática perfecta com $r \approx 0$.
    *   Sensibilidade extrema a outliers (um único ponto distante pode inflar ou destruir $r$).
*   **Nota do Professor:** Diga a frase clássica: "Sempre plote seus dados antes de calcular qualquer estatística de resumo!".

#### Slide 11: Correlação de Postos de Spearman ($r_s$)
*   **Título:** Correlação de Postos de Spearman
*   **Pontos-chave:**
    *   Utiliza os postos (ordenações) das variáveis no lugar dos valores reais.
    *   Ideal para relações não-lineares, mas monótonas.
    *   Muito mais robusto a outliers que Pearson.
*   **Nota do Professor:** Explique que a correlação de Spearman converte os dados em posições rankeadas ($1^{\circ}, 2^{\circ}, \dots, N^{\circ}$) antes de calcular o coeficiente de correlação tradicional de Pearson.

#### Slide 12: Exemplo Pareado: Pearson vs. Spearman
*   **Título:** Comparação Prática: Pearson vs. Spearman
*   **Pontos-chave:** Demonstração visual e em código do ajuste em uma relação exponencial. Pearson subestima a relação ($r = 0.86$) por não ser linear, enquanto Spearman identifica a perfeita monotonicidade ($r_s = 0.99$).
*   **Nota do Professor:** Utilize o gráfico previamente gerado pelo script (`grafico_pearson_vs_spearman.png`).
*   **Elemento Visual:** Imagem `grafico_pearson_vs_spearman.png` ao lado do código Python de execução.

#### Slide 13: O Paradoxo de Simpson (Conceito)
*   **Título:** O Paradoxo de Simpson
*   **Pontos-chave:**
    *   Fenômeno estatístico em que uma associação observada em vários grupos se inverte ou desaparece quando os grupos são agregados.
    *   Causa: Variáveis de confusão omitidas (confounders).
*   **Nota do Professor:** Destaque o perigo de tomar decisões de negócio observando apenas dados agregados sem controle demográfico ou de contexto.

#### Slide 14: Simpson: Caso do Nível de Colesterol vs. Exercício
*   **Título:** Colesterol vs. Exercício Físico
*   **Pontos-chave:**
    *   Agregado: Maior prática de exercício físico parece correlacionada a maiores níveis de colesterol.
    *   Estratificado por Idade: Em cada faixa etária (Jovens, Adultos, Idosos), o exercício reduz o colesterol.
*   **Nota do Professor:** Explique que a idade é a variável de confusão: pessoas mais velhas exercitam-se menos e têm colesterol mais alto naturalmente.
*   **Elemento Visual:** Gráficos `simpson_agregado.png` e `simpson_estratificado.png`.

#### Slide 15: Simpson: Caso COVID-19 (Itália vs. China)
*   **Título:** Taxa de Letalidade de COVID-19
*   **Pontos-chave:**
    *   No agregado, a taxa de letalidade da Itália era superior à da China.
    *   Quando analisada por faixas etárias específicas, a taxa de letalidade da China era maior em quase todas as faixas.
    *   Explicação: A Itália tinha uma população muito mais envelhecida (maior proporção de casos em grupos de risco).
*   **Nota do Professor:** Reforce a importância da estratificação de dados na epidemiologia e na tomada de decisão de políticas públicas.

#### Slide 16: Associação não é Causalidade
*   **Título:** Correlação não implica Causalidade
*   **Pontos-chave:** Duas variáveis podem ter $r$ muito forte sem qualquer relação de causa e efeito (variáveis ocultas, tendências temporais comuns ou coincidência puramente estatística).
*   **Nota do Professor:** Finalize estimulando o espírito crítico do cientista de dados de ADS.

---

## 🐍 Código Didático de Demonstração

O professor deve guiar os alunos pela execução do script [`codigo_apoio_aula_1.py`](file:///home/reginaldo-fernandes/CDD/aula13/codigo_apoio_aula_1.py) no notebook dos alunos. O script foi validado para rodar no ambiente virtual do curso:

```bash
# Execução no terminal usando o interpretador do curso
/home/reginaldo-fernandes/CDD/aula10/.venv/bin/python3 codigo_apoio_aula_1.py
```

---

## ✍️ Exercícios Propostos

1.  **Cálculo Manual e Validação:**
    Dados os seguintes dados amostrais de Horas de Estudo ($X$) e Nota da Prova ($Y$):
    *   $X = [2, 4, 6, 8]$
    *   $Y = [50, 60, 75, 85]$
    *   *(a)* Calcule manualmente o Coeficiente de Correlação de Pearson ($r$). Mostre todos os passos (médias, desvios e covariância).
    *   *(b)* Escreva um script Python usando Pandas e verifique o resultado obtido no item (a).

2.  **Sensibilidade a Outliers:**
    Utilizando o dataset do exercício anterior:
    *   *(a)* Adicione um outlier extremo: $X_{novo} = 15$, $Y_{novo} = 20$.
    *   *(b)* Calcule o novo $r$ de Pearson e o novo $r_s$ de Spearman. Explique a diferença de sensibilidade entre os dois coeficientes.

3.  **Análise de Dados Reais:**
    Carregue o dataset [`hybrid.csv`](file:///home/reginaldo-fernandes/CDD/aula13/data/hybrid.csv) e:
    *   *(a)* Calcule a matriz de correlação de Pearson para as variáveis numéricas.
    *   *(b)* Crie um scatter plot da variável `msrp` (preço sugerido) vs. `mpg` (milhas por galão). O que o gráfico revela sobre a linearidade dessa relação?
    *   *(c)* Compare a correlação de Pearson e Spearman para essa relação e discuta qual é a métrica mais apropriada.
