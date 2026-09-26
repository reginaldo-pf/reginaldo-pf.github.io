# Plano de Aula: 12 - Causalidade e Método Científico

## Metadados
*   **Módulo:** Inferência Estatística e Testes de Hipóteses
*   **Disciplina:** Ciência de Dados / Análise de Dados
*   **Professor:** Reginaldo Fernandes (IFCE Campus Tauá)
*   **Carga Horária:** 2 horas (120 minutos)
*   **Contexto Local:** Hospital Universitário Walter Cantídio (HUWC - UFC), Fortaleza, Ceará.

---

## 🎯 Objetivos de Aprendizagem
*   **Geral:** Compreender a diferença fundamental entre associação e causalidade através de experimentos controlados aleatórios, utilizando a lógica de testes de permutação.
*   **Específicos:**
    1.  Diferenciar estudos observacionais de experimentos controlados aleatórios ($RCT$).
    2.  Compreender o conceito de *resultados potenciais* (potential outcomes) usando a metáfora didática do "bilhete de dois lados".
    3.  Formular hipóteses estatísticas clara de nulidade ($H_0$) e alternativa ($H_1$) para experimentos clínicos.
    4.  Implementar testes de permutação em Python para avaliar a significância estatística de tratamentos médicos.
    5.  Interpretar criticamente o $p$-valor empírico e tomar decisões baseadas em dados no contexto de saúde pública.

---

## ⏰ Cronograma Recomendado
1.  **Abertura e Contextualização (20 min):** A história de pacientes cearenses com dor lombar crônica no HUWC. O problema de correlação vs. causalidade.
2.  **O Modelo de Resultados Potenciais (20 min):** Explicação da metáfora do bilhete de dois lados. Por que só vemos metade de cada bilhete?
3.  **Definição das Hipóteses e Estatística de Teste (25 min):** Formulação matemática da diferença absoluta de proporções de recuperação.
4.  **Simulação Computacional e Permutação (30 min):** Passo a passo do embaralhamento de rótulos e cálculo do $p$-valor empírico.
5.  **Tomada de Decisão e Meta-Análise (15 min):** Análise do histograma de distribuição nula, interpretação do poder do teste e encerramento.
6.  **Atividade Prática/Exercício (10 min):** Breve discussão de casos observacionais.

---

## 🖥️ Roteiro de Slides Sugeridos

#### Slide 1: Título e Apresentação
*   **Título:** Causalidade e Método Científico: Testes Clínicos Randomizados
*   **Subtítulo:** Estabelecendo causa e efeito com dados experimentais do Ceará
*   **Nota do Professor:** Dê as boas-vindas. Destaque que hoje responderemos à pergunta definitiva: "Como provar que uma ação causa um resultado, em vez de ser mera organização?".

#### Slide 2: O Desafio da Causalidade
*   **Título:** Associação vs. Causalidade
*   **Tópicos:**
    *   Correlação não implica causalidade.
    *   **Fator de Confundimento (Confounding Variable):** Variáveis ocultas que afetam tanto o tratamento quanto o resultado (ex: hábitos de saúde, gravidade da dor).
    *   **Estudos Observacionais:** Os sujeitos escolhem seu tratamento (alto risco de confundimento).
    *   **Experimentos Controlados Aleatórios ($RCT$):** A atribuição aleatória elimina vieses de confundimento.
*   **Nota do Professor:** Explique a ideia de que, se os próprios pacientes escolhem tomar o remédio, os mais graves podem escolher mais, confundindo a análise. A aleatorização quebra essa barreira!

#### Slide 3: Estudo de Caso: Dor Lombar Crônica no Ceará
*   **Título:** Um Teste Clínico no HUWC
*   **Tópicos:**
    *   Pacientes cearenses no Hospital Universitário Walter Cantídio com dor lombar crônica persistente.
    *   Tratamento inovador avaliado: Toxina Botulínica Tipo A ($BTA$).
    *   Grupo de Controle: Recebeu solução salina (placebo).
    *   Experimento **Duplo-Cego**: Nem médicos nem pacientes sabem quem recebeu o quê.
    *   Tamanho da Amostra ($N$): $31$ participantes.
        *   Grupo de Tratamento ($N_A = 15$ pacientes).
        *   Grupo de Controle ($N_B = 16$ pacientes).
*   **Elemento Visual:** Ilustração simplificada da divisão aleatória dos 31 pacientes em dois grupos.

#### Slide 4: Os Resultados do Estudo
*   **Título:** Proporção de Recuperação (Alívio da Dor)
*   **Tópicos:**
    *   Após 8 semanas, avaliou-se o alívio clínico da dor:
        *   **Grupo de Controle (Solução Salina):** Apenas $2$ dos $16$ pacientes apresentaram melhoras.
        *   **Grupo de Tratamento ($BTA$):** $9$ dos $15$ pacientes apresentaram melhoras significativas.
    *   Proporções amostrais obtidas:
        *   Proporção de Controle ($p_{\text{controle}}$) = $2/16 = 0.125$ ($12.5\%$)
        *   Proporção de Tratamento ($p_{\text{tratamento}}$) = $9/15 = 0.600$ ($60.0\%$)
*   **Elemento Visual:** Gráfico de barras comparando as taxas de recuperação ($60\%$ vs. $12.5\%$).

#### Slide 5: Resultados Potenciais (A Teoria dos Bilhetes)
*   **Título:** O Modelo de Resultados Potenciais
*   **Tópicos:**
    *   Para cada paciente, existem dois resultados potenciais:
        1.  O resultado se ele receber o tratamento.
        2.  O resultado se ele receber o controle.
    *   **A Metáfora do Bilhete:** Cada paciente tem um bilhete de dois lados. Mas nós só conseguimos ler um dos lados!
        *   Ao atribuir o paciente ao grupo de Tratamento, revelamos o lado esquerdo e o direito permanece "Desconhecido".
        *   Ao atribuir ao grupo de Controle, revelamos o lado direito e o esquerdo fica "Desconhecido".
*   **Elemento Visual:** Diagrama com bilhetes fictícios mostrando uma face revelada e a outra oculta ("Unknown").

#### Slide 6: As Hipóteses Estatísticas
*   **Título:** O que estamos testando?
*   **Tópicos:**
    *   **Hipótese Nula ($H_0$):** A Toxina Botulínica Tipo A ($BTA$) tem o mesmo efeito da solução salina. Para cada paciente, o resultado final seria o mesmo nos dois lados do bilhete. As diferenças observadas são puro acaso da divisão dos grupos.
    *   **Hipótese Alternativa ($H_1$):** A Toxina Botulínica Tipo A ($BTA$) tem um efeito sistematicamente diferente da solução salina.
*   **Nota do Professor:** Enfatize que sob $H_0$, as etiquetas "Tratamento" e "Controle" são irrelevantes; poderiam ser reordenadas sem alterar as respostas dos pacientes.

#### Slide 7: A Estatística de Teste
*   **Título:** Medindo a Distância entre os Grupos
*   **Tópicos:**
    *   Como a variável de resultado é binária ($1$ para alívio da dor, $0$ para sem melhora), a média de cada grupo representa a proporção de melhora.
    *   **Estatística de Teste:** Distância absoluta entre as proporções dos grupos:
        $$\text{Estatística de Teste} = |p_{\text{tratamento}} - p_{\text{controle}}|$$
    *   **Valor Observado na Amostra:**
        $$\text{Diferença Observada} = |0.600 - 0.125| = 0.475 \quad (47.5\%)$$
*   **Nota do Professor:** Explique que valores grandes da estatística de teste favorecem a hipótese alternativa ($H_1$).

#### Slide 8: Implementando o Teste de Permutação
*   **Título:** Simulação sob a Hipótese Nula ($H_0$)
*   **Tópicos:**
    *   Se $H_0$ é verdadeira, os $11$ pacientes que melhoraram teriam melhorado de qualquer forma.
    *   Podemos simular o acaso embaralhando os rótulos de grupo ("Tratamento" e "Controle") $10.000$ vezes.
    *   Em cada simulação, dividimos os 31 resultados embaralhados em grupos de 15 e 16, e recalculamos a estatística de teste.
*   **Nota do Professor:** Esse processo computacional gera a distribuição empírica da estatística sob a suposição de que o remédio não funciona.

#### Slide 9: Código em Python: Teste de Permutação
*   **Título:** Algoritmo de Permutação para Causalidade
*   **Nota do Professor:** Apresente a listagem de código Python limpa. Destaque que a amostragem sem reposição (`np.random.permutation`) simula o embaralhamento físico das etiquetas de grupo.

#### Slide 10: Resultados da Simulação
*   **Título:** Tomada de Decisão Visual
*   **Tópicos:**
    *   O histograma exibe a distribuição de diferenças absolutas que esperaríamos obter puramente por acaso.
    *   O valor observado de $0.475$ é extremamente raro sob o modelo nulo.
    *   **P-valor Empírico:** Proporção de simulações em que a diferença simulada $\geq 0.475$.
    *   Resultado obtido: $P\text{-valor} \approx 0.009$ ($0.9\%$).
*   **Elemento Visual:** Histograma de distribuição nula gerado pelo script com a linha vermelha do valor observado na cauda extrema.

#### Slide 11: A Decisão Científica
*   **Título:** Conclusão do Estudo no Ceará
*   **Tópicos:**
    *   Como o $P\text{-valor}$ ($0.9\%$) $<$ Limiar de Significância ($\alpha = 5\%$), **rejeitamos a hipótese nula $H_0$**.
    *   A diferença de $47.5\%$ na taxa de recuperação é estatisticamente significante.
    *   **Conclusão de Causalidade:** Como a alocação foi aleatória, podemos afirmar que a Toxina Botulínica Tipo A ($BTA$) **causou** o alívio da dor lombar nos pacientes tratados.
*   **Nota do Professor:** Discuta a importância desse resultado para a medicina baseada em evidências no sistema de saúde local.

#### Slide 12: Meta-Análise: Uma Visão Cética
*   **Título:** O Método Científico e o Tamanho Amostral
*   **Tópicos:**
    *   Um estudo com apenas $31$ pacientes é suficiente para aprovar um remédio no SUS?
    *   **Meta-Análise (2011):** Resumo de todos os testes clínicos controlados de $BTA$ para dor lombar.
        *   $19$ estudos foram descartados por falta de aleatorização ou dados incompletos.
        *   Apenas $3$ estudos controlados aleatórios eram confiáveis (incluindo o que analisamos).
    *   **Conclusão da Meta-Análise:** Embora haja evidência positiva de eficácia, a qualidade global das evidências ainda é baixa. São necessários estudos com amostras maiores ($N > 500$) para consolidar a recomendação clínica.

#### Slide 13: O Trabalho do Cientista de Dados
*   **Título:** O Rigor da Ciência de Dados
*   **Tópicos:**
    *   Qualquer ciência (inclusive a nova "ciência de dados") é complexa e exige rigor e ética na interpretação.
    *   Aprendemos apenas uma ferramenta básica: testes de hipóteses via permutação e bootstrap.
    *   **Próximos Passos:** Expandiremos nosso repertório com modelos preditivos (Regressão e Classificação).
*   **Nota do Professor:** Destaque que testes de hipóteses nos ajudam a lidar com incerteza na descrição dos dados, mas na segunda parte do curso seremos capazes de prever novos dados.

#### Slide 14: O Caso da Cloroquina: Falta de Randomização
*   **Título:** Cloroquina: O Perigo da Falta de Rigor
*   **Tópicos:**
    *   Estudos frágeis em 2020 causaram pressões no mundo inteiro para a adoção da cloroquina.
    *   Os próprios autores do estudo de base admitiram que o estudo **não foi randomizado**.
    *   A escolha do paciente sobre tomar ou não o remédio gerou fortes fatores de confundimento e viés de seleção.
    *   Estudos clínicos robustos e meta-análises posteriores provaram que o medicamento não tem efeito.
*   **Elemento Visual:** Recorte do cabeçalho do artigo científico de Gautret et al. evidenciando o termo "non-randomized clinical trial" no lado direito do slide.

#### Slide 15: Método Científico
*   **Título:** Método Científico
*   **Tópicos:**
    *   O arcabouço de testes de hipóteses é uma ótima ferramenta para a ciência no geral (testar hipóteses é o grande objetivo da ciência!).
    *   Nem toda ciência usa Estatística ou Ciência de Dados.
    *   **Formas de fazer experimentos:**
        *   **Experimentos Físicos:** Equações para explicar nosso mundo comprovadas via experimentos.
        *   **Qualitativos:** Estudos onde não necessariamente usamos dados/médias, mas que ainda assim são feitos com método.
        *   **Tentativas de Provas para os Teóricos:** Cada tentativa de prova matemática é uma hipótese.

#### Slide 16: Ciência de Dados no mundo da Ciência
*   **Título:** Ciência de Dados no mundo da Ciência
*   **Tópicos:**
    *   **A Incerteza nos Dados:** "All datasets involve uncertainty. There may be uncertainty about how they were collected, how they were measured, or the process that created them."
    *   A Ciência de Dados **não é toda a ciência**! Ela apenas ajuda no método científico ao quantificar incertezas e analisar dados.

#### Slide 17: O Ciclo do Método Científico
*   **Título:** O Ciclo da Descoberta Científica
*   **Tópicos:**
    *   1. Pergunta -> 2. Revisão da Literatura -> 3. Hipótese -> 4. Experimento -> 5. Análise do Resultado -> 6. Comunicação.
    *   Ciência de dados ajuda principalmente na formulação de hipóteses com dados, na criação de experimentos (como testes A/B) e na análise empírica dos resultados.

#### Slide 18: A Replicação como Regra de Ouro
*   **Título:** Se não é replicável, não é ciência!
*   **Tópicos:**
    *   Um único experimento positivo não é definitivo (exemplo do BTA com $N=31$).
    *   Sempre existe chance de erros e vieses amostrais locais.
    *   A replicação por outros cientistas independentes é a chave para o progresso do conhecimento.

#### Slide 19: Críticas aos Testes de Hipóteses
*   **Título:** Críticas aos Testes de Hipóteses e P-valores
*   **Tópicos:**
    *   Estatísticos criticam o uso cego do limiar de significância de $5\%$ ($p < 0.05$).
    *   Problemas de "P-hacking" e viés de publicação (apenas resultados significativos são publicados).
    *   **Boas Práticas:** Sempre relatar o P-valor exato, o tamanho da amostra ($N$), o tamanho do efeito (effect size) e as premissas de teste (ex: Bootstrap vs. Permutação).

#### Slide 20: Resumo e Principais Aprendizados
*   **Título:** Resumo da Aula
*   **Tópicos:**
    *   **Causalidade vs. Associação:** RCTs eliminam viés de confundimento por meio da aleatorização.
    *   **Resultados Potenciais:** Metáfora do bilhete de dois lados (um observado, um desconhecido).
    *   **Permutação:** Embaralhamento para simular o modelo nulo sob $H_0$.
    *   **Rigor Científico:** Importância da replicabilidade, meta-análise e ceticismo saudável com P-valores.

#### Slide 21: Referências Bibliográficas
*   **Título:** Referências e Leituras Recomendadas
*   **Tópicos:**
    *   Lau, S., Gonzalez, J., & Nolan, D. *Learning Data Science*, Capítulo 17: Inference, Prediction, and Generalization.
    *   Adhikari, A., & DeNero, J. *Computational and Inferential Thinking*, Capítulo 11: Testing Hypotheses (Seção 11.1).
    *   Foster et al. (2001). *Botulinum Toxin A in the Treatment of Chronic Low Back Pain: A Randomized Double-Blind Study*.

---

## 🐍 Código Prático de Apoio
O script de simulação computacional encontra-se no arquivo [aula12_pratica.py](file:///home/reginaldo-fernandes/CDD/aula12/aula12_pratica.py). Ele gera os gráficos de suporte e realiza a simulação do teste de permutação de forma vetorizada via NumPy.

---

## 📝 Exercícios Didáticos recomendados
1.  **Análise Crítica:** Por que a alocação aleatória (randomização) permite estabelecer uma relação de causalidade, enquanto uma associação observada em um hospital privado (sem sorteio) não permite? Justifique usando o conceito de variáveis de confundimento.
2.  **Modificação do Teste:** O teste bicaudal que realizamos avalia apenas se o tratamento "é diferente" do controle. Altere a estatística de teste no script Python para avaliar se o tratamento é sistematicamente **melhor** do que o controle (teste unilateral da cauda direita: $p_{\text{tratamento}} - p_{\text{controle}}$). Recalcule o $p$-valor e compare com o bicaudal.
3.  **Bootstrap vs. Permutação:** Qual a diferença conceitual entre usar Bootstrap (reamostragem com reposição) para construir um intervalo de confiança e usar Permutação (embaralhamento sem reposição) para testar uma hipótese de causalidade?
