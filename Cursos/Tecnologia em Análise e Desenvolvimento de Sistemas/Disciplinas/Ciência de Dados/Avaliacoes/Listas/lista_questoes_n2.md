# IFCE - Instituto Federal do Ceará (Campus Tauá)
## Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
## Disciplina: Ciência de Dados / Análise de Dados
## Professor: Reginaldo Fernandes
## Semestre/Período: N2 — Lista de Exercícios 1 (Aulas 08 a 12)

---

### Apresentação da Atividade
Esta lista de exercícios abrange toda a teoria estatística e computacional ministrada nas **Aulas 08 a 12**. O objetivo é consolidar o aprendizado sobre propriedades da média, variabilidade, Teorema do Limite Central (TLC), Intervalos de Confiança (IC), testes A/B, Testes de Permutação e Causalidade. Além de computar a nota de atividade do período N2, as questões abaixo servem como guia oficial de estudo para a prova teórica.

---

## 📚 Bloco 1: Propriedades da Média, Variabilidade e TLC (Aula 08)

### Questão 1
Demonstre matematicamente que a soma dos desvios de um conjunto de dados $\{x_1, x_2, \dots, x_N\}$ em relação à sua média amostral $\bar{X}$ é igual a zero. Ou seja, prove que:
$$\sum_{i=1}^{N} (x_i - \bar{X}) = 0$$

### Questão 2
Em termos geométricos e analíticos, explique qual a propriedade que diferencia a média da mediana em relação à minimização de erros de previsão. 
*Dica: Compare a minimização da soma dos desvios absolutos ($\sum |x_i - c|$) com a soma dos desvios quadrados ($\sum (x_i - c)^2$).*

### Questão 3
Explique a regra empírica da Curva Normal (Regra 68-95-99.7). Se a distribuição dos salários de uma empresa cearense é aproximadamente normal, com média de R\$ 3.500,00 e desvio padrão de R\$ 400,00, qual é a proporção esperada de funcionários que recebem:
a) Entre R\$ 3.100,00 e R\$ 3.900,00?
b) Entre R\$ 2.700,00 e R\$ 4.300,00?
c) Mais do que R\$ 4.700,00?

### Questão 4
O Teorema do Limite Central (TLC) é considerado o pilar da inferência estatística clássica. 
a) Enuncie o Teorema do Limite Central em termos simples, explicando o que acontece com a distribuição das médias amostrais à medida que o tamanho da amostra ($N$) cresce.
b) Explique a diferença conceitual entre o desvio padrão da população ($\sigma$) e o Erro Padrão da Média ($SE$). Qual a relação matemática entre eles?

### Questão 5
Deseja-se estimar a média de consumo diário de água por habitante em uma cidade do Sertão dos Inhamuns. Sabendo que o desvio padrão histórico é de 30 litros por dia, calcule o tamanho de amostra ($N$) necessário para que o erro da estimativa (margem de erro) não ultrapasse 3 litros, com um nível de confiança de 95\% ($z \approx 1.96$).

---

## 📚 Bloco 2: Intervalos de Confiança: Paramétricos e Bootstrap (Aula 09)

### Questão 6
Explique o significado exato da frase: *"Construímos um Intervalo de Confiança de 95\% para a média populacional $\mu$ que resultou em $[150, 180]$"*.
*   É correto dizer que existe 95\% de probabilidade de o parâmetro populacional $\mu$ estar contido neste intervalo específico? Justifique sua resposta com base na definição teórica frequentista de probabilidade.

### Questão 7
A técnica de Bootstrap é amplamente utilizada quando não conhecemos a distribuição populacional dos dados ou quando trabalhamos com amostras de tamanhos pequenos.
a) Explique a mecânica de amostragem do Bootstrap (reamostragem). Por que é obrigatório que a amostragem seja feita **com reposição**?
b) Qual a diferença fundamental entre a população original, a amostra coletada e as amostras de bootstrap?

### Questão 8
Uma amostra de tamanho $N = 100$ de tempos de entrega de uma transportadora no Ceará apresentou média $\bar{X} = 45$ minutos e desvio padrão amostral $s = 15$ minutos.
a) Construa o Intervalo de Confiança de 95\% para o tempo médio populacional de entrega utilizando o Teorema do Limite Central (TLC).
b) Se construíssemos um Intervalo de Confiança de 99\% utilizando a mesma amostra, o intervalo seria mais largo ou mais estreito do que o de 95\%? Explique a relação entre nível de confiança e precisão do intervalo.

---

## 📚 Bloco 3: Testes de Hipóteses e Testes A/B (Aula 10)

### Questão 9
No contexto de testes de hipóteses, diferencie claramente:
a) Hipótese Nula ($H_0$) vs. Hipótese Alternativa ($H_1$).
b) Erro Tipo I ($\alpha$) vs. Erro Tipo II ($\beta$). Dê um exemplo prático na área médica ou forense sobre as consequências de cometer cada um desses erros.

### Questão 10
Um e-commerce cearense de artesanato testou um novo layout de página de vendas para avaliar o impacto na taxa de conversão (Teste A/B). O grupo de controle (layout antigo) teve taxa de conversão observada de $2.0\%$, enquanto o grupo de tratamento (novo layout) teve taxa de conversão observada de $2.5\%$.
a) Formule as hipóteses nula ($H_0$) e alternativa ($H_1$) para este teste.
b) Explique como você usaria o Bootstrap para simular o comportamento da diferença de taxas sob a hipótese nula $H_0$.

---

## 📚 Bloco 4: Total Variation Distance (TVD) e Teste de Permutação (Aula 11)

### Questão 11
O caso *Robert Swain vs. Alabama (1965)* e o julgamento em *Alameda County* evidenciaram o papel da estatística na avaliação da representatividade racial em júris.
a) Defina matematicamente a estatística de teste Total Variation Distance (TVD). Para que tipo de variáveis essa estatística é ideal?
b) Suponha que a distribuição racial de um município cearense seja: $70\%$ Parda, $20\%$ Branca e $10\%$ Preta. Um júri sorteado de 100 pessoas apresentou a seguinte composição: $50\%$ Parda, $40\%$ Branca e $10\%$ Preta. Calcule o valor do TVD observado para esta amostra.

### Questão 12
Diferencie a lógica de amostragem e finalidade entre os seguintes métodos estatísticos:
a) **Bootstrap**: Reamostragem com reposição.
b) **Permutação**: Embaralhamento sem reposição.
*Em que cenários cada um é preferencialmente aplicado?*

### Questão 13
No exemplo dos salários da NBA analisado na Aula 11 (comparação entre Cleveland e Houston), a estatística de teste utilizada foi a diferença absoluta entre as médias salariais dos dois times. Explique por que, sob desvios padrões (variâncias) muito elevados na amostra, mesmo uma diferença grande entre as médias das duas equipes pode resultar em um $p$-valor alto (falhando em rejeitar $H_0$).

---

## 📚 Bloco 5: Causalidade e Método Científico (Aula 12)

### Questão 14
Diferencie um **Estudo Observacional** de um **Experimento Controlado Aleatório (RCT)**. Por que apenas o segundo permite inferir causalidade direta de um tratamento?

### Questão 15
Explique o conceito de **Fator de Confundimento (Confounding Variable)** e dê um exemplo de como ele pode invalidar as conclusões de um estudo de correlação estatística em saúde pública.

### Questão 16
Explique o modelo de **Resultados Potenciais (Potential Outcomes)** através da metáfora didática do "bilhete de dois lados". 
*   Por que dizemos que o problema fundamental da inferência causal é a impossibilidade de ler as duas faces do bilhete para o mesmo paciente?

### Questão 17
A meta-análise é uma ferramenta fundamental no método científico contemporâneo.
a) O que é uma Meta-Análise e por que ela oferece maior robustez científica do que estudos clínicos individuais com amostras pequenas?
b) Relacione a meta-análise com o conceito de replicação científica.

### Questão 18
Muitas revistas científicas e sociedades de estatística têm criticado o uso excessivo e mecânico de $p$-valores na tomada de decisão (especialmente a barreira arbitrária de $p < 0.05$).
a) Explique dois problemas práticos decorrentes do uso inadequado de $p$-valores (ex: *p-hacking*, viés de publicação).
b) Quais informações adicionais um analista de dados deve sempre reportar ao divulgar o resultado de um teste de hipóteses para garantir o rigor estatístico?

---
---

## 🔑 Gabarito Comentado e Dicas de Resolução

> [!TIP]
> Use as resoluções abaixo para verificar suas respostas e orientar seus estudos para a avaliação teórica da disciplina.

### Resolução 1
A soma dos desvios em relação à média é dada por:
$$\sum_{i=1}^{N} (x_i - \bar{X}) = \sum_{i=1}^{N} x_i - \sum_{i=1}^{N} \bar{X}$$
Como $\bar{X}$ é uma constante para a amostra, somá-la $N$ vezes equivale a multiplicá-la por $N$:
$$\sum_{i=1}^{N} (x_i - \bar{X}) = \sum_{i=1}^{N} x_i - N\bar{X}$$
Sabemos que a definição da média amostral é $\bar{X} = \frac{1}{N} \sum_{i=1}^{N} x_i$, o que implica em $N\bar{X} = \sum_{i=1}^{N} x_i$. Substituindo na equação:
$$\sum_{i=1}^{N} (x_i - \bar{X}) = \sum_{i=1}^{N} x_i - \sum_{i=1}^{N} x_i = 0 \quad \blacksquare$$

### Resolução 2
*   **Média**: Minimiza a soma dos desvios quadráticos ($\sum (x_i - c)^2$). Isso significa que a média é o estimador de mínimos quadrados. Por elevar os desvios ao quadrado, a média é altamente influenciada por valores extremos (*outliers*).
*   **Mediana**: Minimiza a soma dos desvios absolutos ($\sum |x_i - c|$). Em termos geométricos, ela representa o ponto central físico em que metade dos dados está acima e metade está abaixo. É um estimador robusto a *outliers*.

### Resolução 3
A Regra 68-95-99.7 dita que em uma distribuição normal, aproximadamente $68\%$ dos dados estão a $\pm 1$ desvio padrão ($SD$) da média, $95\%$ estão a $\pm 2$ $SD$, e $99.7\%$ estão a $\pm 3$ $SD$.
Dados: $\mu = 3500$, $\sigma = 400$.
*   $\pm 1\sigma = [3100, 3900]$
*   $\pm 2\sigma = [2700, 4300]$
*   $\pm 3\sigma = [2300, 4700]$
a) **Entre R\$ 3.100 e R\$ 3.900**: Corresponde a $\pm 1\sigma \Rightarrow \mathbf{68\%}$ dos funcionários.
b) **Entre R\$ 2.700 e R\$ 4.300**: Corresponde a $\pm 2\sigma \Rightarrow \mathbf{95\%}$ dos funcionários.
c) **Mais do que R\$ 4.700**: R\$ 4.700 é o limite superior de $+3\sigma$. Como a área sob a curva normal é de $100\%$ e ela é simétrica, a área fora de $\pm 3\sigma$ é $100\% - 99.7\% = 0.3\%$. Como queremos apenas a cauda direita (acima de $3\sigma$), dividimos por 2: $0.3\% / 2 = \mathbf{0.15\%}$ (ou proporção de $0.0015$).

### Resolução 4
a) **Enunciado Simplificado**: O TLC garante que se retirarmos infinitas amostras aleatórias de tamanho $N$ de qualquer população (independentemente da sua distribuição original), a distribuição das médias dessas amostras ($\bar{X}$) se aproximará de uma distribuição normal à medida que $N$ cresce (geralmente $N \geq 30$).
b) **Desvio Padrão ($\sigma$) vs. Erro Padrão ($SE$)**:
*   O desvio padrão populacional ($\sigma$) mede a variabilidade ou dispersão dos dados individuais na população original.
*   O Erro Padrão da Média ($SE$) mede a variabilidade ou dispersão das médias amostrais estimadas de amostra para amostra. A relação matemática é:
    $$SE = \frac{\sigma}{\sqrt{N}}$$

### Resolução 5
A fórmula da margem de erro ($E$) para a estimativa da média sob o TLC é:
$$E = z \cdot SE = z \cdot \frac{\sigma}{\sqrt{N}}$$
Desejamos que $E \le 3$, com $z = 1.96$ e $\sigma = 30$. Isolando $N$:
$$3 = 1.96 \cdot \frac{30}{\sqrt{N}} \Rightarrow \sqrt{N} = \frac{1.96 \cdot 30}{3} \Rightarrow \sqrt{N} = 19.6$$
Elevando ambos os lados ao quadrado:
$$N = (19.6)^2 = 384.16$$
Portanto, é necessário selecionar uma amostra de no mínimo \textbf{385 habitantes}.

### Resolução 6
*   **Interpretação exata**: Se repetirmos o procedimento de amostragem e cálculo do intervalo de confiança muitas vezes, $95\%$ dos intervalos construídos conterão a verdadeira média populacional $\mu$. 
*   **Erro de Probabilidade**: Não é correto dizer que existe 95\% de probabilidade de $\mu$ estar contido em $[150, 180]$. Após o intervalo ser calculado, ele se torna fixo (assim como $\mu$ que é um parâmetro constante e fixo). Logo, a média populacional ou está contida no intervalo (probabilidade 1) ou não está (probabilidade 0). O termo "95\% de confiança" refere-se à taxa de acerto do processo/método de estimação, não a uma probabilidade do intervalo fixo.

### Resolução 7
a) **Com reposição**: No Bootstrap, a amostra original (de tamanho $N$) funciona como um modelo da população real. Para gerar uma "amostra de bootstrap", devemos sortear elementos com reposição $N$ vezes. Se sorteássemos *sem reposição*, a amostra gerada seria exatamente idêntica à amostra original (apenas reordenada), resultando em variabilidade zero nas médias calculadas.
b) **Diferenças**:
*   *População*: Entidade completa, imutável e geralmente desconhecida.
*   *Amostra*: Conjunto único obtido por sorteio da população real.
*   *Amostra de Bootstrap*: Sorteios sucessivos feitos computacionalmente a partir dos dados da amostra.

### Resolução 8
a) IC de 95\% via TLC:
$$IC_{95\%} = \bar{X} \pm z \cdot \frac{s}{\sqrt{N}}$$
Dados: $\bar{X} = 45$, $s = 15$, $N = 100$, $z = 1.96$ (para 95\%).
$$SE = \frac{15}{\sqrt{100}} = 1.5$$
$$IC_{95\%} = 45 \pm 1.96 \cdot 1.5 = 45 \pm 2.94 \Rightarrow \mathbf{[42.06; 47.94] \text{ minutos}}$$
b) O intervalo de 99\% será **mais largo**. Para aumentar a confiança no acerto da estimativa, é necessário expandir a amplitude do intervalo (o valor crítico $z$ aumenta de $1.96$ para $2.58$).

### Resolução 9
a) **Hipóteses**:
*   *Hipótese Nula ($H_0$)*: Afirmação de ausência de efeito, igualdade ou manutenção do status quo (ex: o novo layout de e-commerce não muda as conversões).
*   *Hipótese Alternativa ($H_1$)*: Afirmação que contradiz $H_0$, sugerindo a presença de efeito ou diferença (ex: o novo layout aumenta as conversões).
b) **Erros**:
*   *Erro Tipo I ($\alpha$)*: Rejeitar $H_0$ quando $H_0$ é verdadeira (Falso Positivo). Exemplo forense: Condenar um réu inocente.
*   *Erro Tipo II ($\beta$)*: Falhar em rejeitar $H_0$ quando $H_0$ é falsa (Falso Negativo). Exemplo forense: Absolver um réu culpado.

### Resolução 10
a) **Hipóteses**:
*   $H_0$: A taxa de conversão do novo layout é igual à do layout antigo ($p_{\text{tratamento}} = p_{\text{controle}}$).
*   $H_1$: A taxa de conversão do novo layout é diferente da do antigo ($p_{\text{tratamento}} \neq p_{\text{controle}}$).
b) **Bootstrap sob $H_0$**:
1. Una os dados de conversão (0s e 1s) de ambos os grupos em um único vetor.
2. Sorteie reamostras com reposição desse vetor unificado para formar novos grupos simulados de controle e tratamento.
3. Calcule a diferença entre as taxas de conversão simladas.
4. Repita esse processo milhares de vezes para obter a distribuição nula das diferenças sob a premissa de que os grupos vieram da mesma origem.

### Resolução 11
a) O Total Variation Distance (TVD) é a metade da soma das diferenças absolutas entre as proporções observadas e as esperadas de cada categoria:
$$TVD = \frac{1}{2} \sum_{i=1}^{k} |P_i^{\text{observado}} - P_i^{\text{esperado}}|$$
É ideal para variáveis categóricas qualitativas nominais (como raça, cor, gênero ou preferência de marca).
b) Cálculo do TVD:
*   Parda: $|0.50 - 0.70| = 0.20$
*   Branca: $|0.40 - 0.20| = 0.20$
*   Preta: $|0.10 - 0.10| = 0.00$
$$TVD = \frac{1}{2} (0.20 + 0.20 + 0.00) = \frac{1}{2} (0.40) = \mathbf{0.20} \quad (20.0\%)$$

### Resolução 12
*   **Bootstrap**: Amostra com reposição de uma única amostra para estimar a variabilidade de um estimador (ex: erro padrão, intervalos de confiança). É aplicado para inferir propriedades de um estimador sem conhecer a distribuição teórica da população.
*   **Permutação**: Embaralha os rótulos de grupo sem reposição (apenas rearranja as conexões entre tratamento/controle e resultados). É ideal para testar hipóteses de causalidade/independência entre dois grupos amostrais sob a hipótese nula $H_0$ de que o tratamento não tem efeito.

### Resolução 13
O $p$-valor representa a probabilidade de obter uma diferença igual ou mais extrema do que a observada por puro acaso. A variância amostral muito alta significa que os dados individuais são muito dispersos. Sob essa condição, o embaralhamento aleatório (simulação sob $H_0$) gera com frequência grandes oscilações nas médias simuladas. Como oscilações grandes são comuns por puro acaso (variância alta), a diferença observada no estudo não parecerá tão incomum, resultando em um $p$-valor alto e na não-rejeição de $H_0$.

### Resolução 14
*   **Estudo Observacional**: O pesquisador apenas observa as escolhas espontâneas dos participantes (ex: pessoas que escolhem fumar). Isso impossibilita inferir causalidade direta, pois características individuais preexistentes afetam a escolha, confundindo a análise.
*   **Experimento Controlado Aleatório (RCT)**: O pesquisador intervém e determina por sorteio aleatório quem recebe o tratamento ou o placebo. O sorteio equilibra todas as variáveis ocultas nos dois grupos, garantindo que qualquer diferença nos resultados tenha sido causada exclusivamente pelo tratamento.

### Resolução 15
*   **Definição**: Fator de confundimento é uma variável não medida que está associada tanto à exposição (tratamento) quanto ao desfecho (resultado), misturando-se com o efeito real.
*   **Exemplo**: Um estudo observa que pessoas que bebem muito café têm maior incidência de câncer de pulmão. Porém, o hábito de fumar é um fator de confundimento: fumantes tendem a beber mais café, e o tabaco é a real causa do câncer de pulmão, e não o café.

### Resolução 16
*   **Metáfora**: Cada indivíduo tem um bilhete com duas opções de futuro escritas: o resultado se tomasse o remédio (lado esquerdo) e o resultado se tomasse o placebo (lado direito).
*   **Problema Fundamental**: Na realidade, só conseguimos observar uma das opções de tratamento por paciente (um lado do bilhete). O outro lado torna-se contrafactual (desconhecido). Portanto, nunca podemos ver o efeito causal individual real, devendo recorrer à estimativa de médias em grupos randomizados.

### Resolução 17
a) Meta-análise é uma técnica estatística que combina dados de múltiplos estudos independentes sobre o mesmo tema. Ela aumenta o tamanho amostral global ($N$), reduzindo o erro padrão e permitindo detectar efeitos reais que estudos pequenos individuais não teriam poder estatístico para revelar.
b) Ela atesta a replicabilidade: se múltiplos estudos em locais e condições diferentes encontram resultados convergentes, a hipótese ganha alta sustentabilidade científica.

### Resolução 18
a) **Problemas**:
*   *P-hacking*: A prática de realizar múltiplas análises estatísticas, remoções ad-hoc de outliers ou testes sucessivos com diferentes variáveis até que o P-valor caia abaixo de $0.05$.
*   *Viés de Publicação*: Periódicos científicos tendem a publicar apenas artigos que rejeitam a hipótese nula ($p < 0.05$), ocultando da comunidade os estudos que não encontraram efeitos.
b) **Boas Práticas**: Deve-se sempre reportar: (1) O P-valor exato, (2) O tamanho da amostra ($N$), (3) O tamanho do efeito (diferença real das médias ou proporções) e (4) O método estatístico (Bootstrap, permutação ou fórmula paramétrica).
