# Maratona de Revisão: Lógica e Programação de Computadores
**IFCE Campus Tauá -- Curso Técnico em Redes de Computadores**  
**Docente:** Prof. Reginaldo Fernandes  
**Material de Apoio e Roteiro de Slides**

Este documento acompanha a apresentação em slides (`main.pdf`) e consolida os **25 quesitos práticos de revisão**, cobrindo desde operadores básicos até a criação de funções nos quatro formatos. Cada questão contém o **quesito formal** e uma **ajuda de raciocínio lógico (sem entregar o código final)**.

---

## 📑 Sumário da Distribuição (25 Questões)

1. **Parte 1: Programação Estruturada (Q01 a Q05)**  
   *Operadores aritméticos, divisão inteira, módulo (`%`), operadores relacionais e lógicos.*
2. **Parte 2: Estruturas de Decisão (Q06 a Q10)**  
   *Condicionais simples, compostas e encadeadas (`if-elif-else`), condições múltiplas e menus.*
3. **Parte 3: Estruturas de Repetição e Vetores (Q11 a Q15)**  
   *Laços `for` e `while`, acumuladores, sentinelas, filtragem, busca linear e manipulação de listas.*
4. **Parte 4: Modularização com Funções (Q16 a Q25 -- 10 Questões)**  
   *Funções sem parâmetro e sem retorno, com parâmetro e sem retorno, sem parâmetro e com retorno, com parâmetro e com retorno.*

---

## 📐 Parte 1: Programação Estruturada e Operadores (Q01 a Q05)

### 📌 Questão 01: Operadores Aritméticos Básicos
- **Quesito:** Desenvolva um programa que receba três valores do usuário:
  1. A distância total percorrida em uma viagem em quilômetros (`km`);
  2. O consumo médio do veículo em quilômetros por litro (`km/l`);
  3. O preço unitário do litro de combustível em reais (`R$`).  
  O programa deve calcular e exibir:
  - O total de litros consumidos ($\text{Litros} = \text{Distância} / \text{Consumo}$);
  - O custo financeiro total da viagem formatado com 2 casas decimais.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Converta as entradas de texto do teclado usando `float(input(...))`.
  - Aplique a relação da divisão convencional com o operador `/`.
  - O custo final é obtido pelo produto da quantidade de litros pelo preço por litro (`*`).
  - Para exibir com 2 casas decimais, utilize formatação de string: `f"{custo:.2f}"`.

---

### 📌 Questão 02: Divisão Inteira e Operador Módulo
- **Quesito:** Um sistema de monitoramento de infraestrutura registra o tempo de atividade contínuo (*uptime*) de um servidor em segundos inteiros. Escreva um programa que leia esse valor inteiro e o decomponha no formato tradicional: **Horas**, **Minutos** e **Segundos restantes**.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Lembre-se das equivalências: $1\text{ hora} = 3600\text{ segundos}$ e $1\text{ minuto} = 60\text{ segundos}$.
  - Extraia as horas completas usando a divisão inteira: `horas = total // 3600`.
  - Guarde os segundos que sobraram usando o operador de resto (`%`): `resto = total % 3600`.
  - Em seguida, fatie esse resto para achar os minutos com `// 60` e os segundos finais com `% 60`.

---

### 📌 Questão 03: Operadores Relacionais (Comparação)
- **Quesito:** Um link dedicado de rede opera com capacidade nominal de $1000\text{ Mbps}$. Leia o tráfego atual do link em Mbps e gere três variáveis booleanas (`True` ou `False`), sem utilizar instruções condicionais (`if`):
  1. **Uso Seguro:** O tráfego está estritamente abaixo de $80\%$ da capacidade ($800\text{ Mbps}$)?
  2. **Atenção Crítica:** O tráfego atingiu ou superou $90\%$ da capacidade ($900\text{ Mbps}$)?
  3. **Sobrecarga:** O tráfego é estritamente superior a $100\%$ da capacidade ($1000\text{ Mbps}$)?  
  Exiba o valor booleano resultante de cada uma das três verificações.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Expressões relacionais (`<`, `>=`, `>`) geram diretamente respostas booleanas (`True` ou `False`).
  - Atribua o teste lógico diretamente à variável: `seguro = trafego < 800`.
  - Imprima essas variáveis diretamente com `print()`.

---

### 📌 Questão 04: Operadores Lógicos Comportamentais
- **Quesito:** A catraca eletrônica de acesso a um datacenter deve destravar a porta apenas se:
  - O usuário possui credencial autorizada (`True/False`) **E** o horário atual estiver dentro da janela permitida ($8\text{h}$ às $18\text{h}$);
  - **OU** o protocolo de evacuação por emergência estiver acionado (`True/False`).  
  Construa a expressão lógica em Python que determine se a porta deve destravar.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Identifique as variáveis: `tem_cracha` (bool), `hora` (int) e `modo_emergencia` (bool).
  - A janela horária é descrita por: `(hora >= 8 and hora <= 18)`.
  - Junte o crachá e o horário com o operador `and`.
  - Use parênteses para delimitar a regra normal e una-a à emergência com o operador `or`.

---

### 📌 Questão 05: Expressões Aritmético-Lógicas Combinadas
- **Quesito:** Um ano é bissexto no calendário gregoriano se atender às seguintes condições:
  - É divisível por $4$ **e** não é divisível por $100$; **OU**
  - É divisível por $400$.  
  Receba um ano inteiro e avalie se ele é bissexto utilizando **apenas uma expressão booleana** (sem blocos `if/else`). Imprima apenas o valor booleano resultante.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Um número $A$ é divisível por $B$ quando o resto da divisão é nulo: `A % B == 0`.
  - "Não ser divisível por 100" é escrito como `ano % 100 != 0`.
  - Agrupe a condição do 400 com a do 4 e não 100:  
    `(ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))`.

---

## 🔀 Parte 2: Estruturas de Decisão (Q06 a Q10)

### 📌 Questão 06: Decisão Simples e Composta
- **Quesito:** Leia a velocidade registrada de um veículo em uma via fiscalizada cujo limite é de $60\text{ km/h}$.
  - Se a velocidade for até $60\text{ km/h}$, exiba: `"Velocidade permitida"`.
  - Se ultrapassar $60\text{ km/h}$, alerte `"Multado!"`, calcule e informe o valor da penalidade a $\text{R\$ } 7{,}00$ por cada $\text{km/h}$ excedente.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Utilize um bloco condicional `if-else`.
  - O teste no `if` deve verificar `velocidade > 60`.
  - No corpo verdadeiro, determine o excesso subtraindo o limite da velocidade (`excesso = velocidade - 60`) e multiplique pela taxa unitária da multa.

---

### 📌 Questão 07: Decisão Encadeada (`if-elif-else`)
- **Quesito:** Receba o nível de glicose no sangue de um paciente em jejum ($\text{mg/dL}$) e emita a classificação clínica correspondente:
  - Menor que $70\text{ mg/dL}$: **"Hipoglicemia"**
  - De $70$ a $99\text{ mg/dL}$: **"Normal"**
  - De $100$ a $125\text{ mg/dL}$: **"Pré-diabetes"**
  - $126\text{ mg/dL}$ ou superior: **"Diabetes Estabelecido"**
- **💡 Ajuda de Resolução (Como Pensar):**
  - Utilize uma cadeia `if`, seguidos de `elif` e finalize com `else`.
  - Ordene os testes do menor para o maior.
  - Ao testar `elif glicose <= 99:`, você já tem a garantia de que a glicose é $\ge 70$, pois a primeira condição do `if` resultou falsa.

---

### 📌 Questão 08: Condições Múltiplas e Geometria
- **Quesito:** Receba três lados $A$, $B$ e $C$. O algoritmo deve:
  1. Verificar se formam um triângulo (cada lado deve ser estritamente menor que a soma dos outros dois);
  2. Caso formem, classifique: **Equilátero** (3 lados iguais), **Isósceles** (quaisquer 2 lados iguais) ou **Escaleno** (todos diferentes);
  3. Caso contrário, exiba que as medidas não formam um triângulo.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Condição de existência: `(A < B + C) and (B < A + C) and (C < A + B)`.
  - Aninhe a classificação dentro do bloco do `if` de existência:
    - Teste se `A == B == C` para Equilátero.
    - No `elif`, verifique se ao menos duas medidas coincidem com o operador `or`.
    - O ramo `else` final indicará o triângulo escaleno.

---

### 📌 Questão 09: Tabela Progressiva de Descontos
- **Quesito:** Uma loja virtual aplica descontos escalonados conforme o total bruto da compra:
  - Até $\text{R\$ } 100{,}00$: $0\%$ de desconto;
  - De $\text{R\$ } 100{,}01$ a $\text{R\$ } 300{,}00$: $10\%$ de desconto;
  - De $\text{R\$ } 300{,}01$ a $\text{R\$ } 500{,}00$: $15\%$ de desconto;
  - Acima de $\text{R\$ } 500{,}00$: $20\%$ de desconto.  
  O programa deve ler o valor bruto e exibir: a taxa percentual aplicada, o valor descontado em $\text{R\$}$ e o valor líquido a pagar.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Crie uma variável `taxa = 0.0`.
  - Use o `if-elif-else` exclusivamente para configurar o valor de `taxa` ($0.0$, $0.10$, $0.15$ ou $0.20$).
  - Fora do bloco condicional, realize as operações matemáticas apenas uma vez:  
    $\text{desconto} = \text{valor} \times \text{taxa}$ e $\text{total} = \text{valor} - \text{desconto}$.

---

### 📌 Questão 10: Menu de Operações e Prevenção de Falhas
- **Quesito:** Apresente um menu com opções (`1-Soma`, `2-Subtração`, `3-Multiplicação`, `4-Divisão`), leia a opção desejada e receba dois números reais.
  - Execute a operação matemática correspondente.
  - Na operação de divisão, previna travamentos no programa impedindo a tentativa de divisão por zero.
  - Se for informada uma opção fora do menu, exiba `"Opção Inválida"`.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Estruture as ramificações com `if-elif-else`.
  - Na opção 4, faça uma verificação de segurança: verifique se o segundo operando é diferente de zero (`num2 != 0`) antes de dividir.
  - Deixe o `else` final para tratar valores fora do intervalo válido de opções.

---

## 🔁 Parte 3: Estruturas de Repetição e Vetores (Q11 a Q15)

### 📌 Questão 11: Laço Contado e Vetor Acumulador
- **Quesito:** Leia a temperatura máxima de cada um dos $7$ dias da semana e guarde os dados em uma lista. Ao final, determine e mostre:
  1. A média aritmética simples das temperaturas da semana;
  2. A maior temperatura registrada;
  3. A quantidade de dias em que a temperatura foi estritamente superior à média calculada.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Inicie uma lista vazia e use `for i in range(7):` com `.append()` para coletar os valores.
  - Calcule a média somando a lista (`sum(temperaturas)`) e dividindo por $7$ (ou `len(temperaturas)`).
  - Use um segundo laço `for` para percorrer a lista, contando quantos dias tiveram `temp > media`.

---

### 📌 Questão 12: Repetição com Sentinela (`while`)
- **Quesito:** Crie um programa para fechamento de caixa eletrônico:
  - Leia sucessivos saques até que seja digitado $0$ (sentinela de encerramento).
  - Se o usuário digitar um valor negativo, exiba um alerta e desconsidere essa tentativa.
  - Ao término, exiba a quantidade de saques válidos processados e o montante financeiro total sacado.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Use `while True:` com leitura do valor dentro do laço.
  - Se o valor for $0$, pare o laço com a instrução `break`.
  - Se o valor for negativo, emita o aviso e use `continue` para retornar ao topo do laço sem alterar os acumuladores.
  - Nos demais casos, some o valor em `total_sacado` e incremente o contador de saques.

---

### 📌 Questão 13: Varredura de Vetor e Filtragem
- **Quesito:** Solicite $10$ números inteiros para uma lista inicial. Em seguida, processe os dados para:
  - Separar os números pares em uma segunda lista;
  - Separar os números ímpares em uma terceira lista.  
  Exiba o tamanho e os elementos de cada uma das três listas.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Crie `pares = []` e `impares = []`.
  - Varra a lista principal com `for n in lista_original:`.
  - Teste a paridade com `n % 2 == 0`: adicione em `pares` ou em `impares` via `.append()`.
  - Use a função nativa `len()` para verificar as quantidades.

---

### 📌 Questão 14: Busca Linear em Vetores com Flag
- **Quesito:** Considere uma lista pré-carregada com $8$ matrículas autorizadas. Leia uma matrícula informada pelo usuário e efetue a busca:
  - Se encontrada, exiba: `"Autorizado na posição X"`.
  - Se não constar na lista, exiba: `"Acesso Negado: Matrícula não cadastrada"`.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Inicialize uma flag booleana: `achou = False`.
  - Itere pelos índices usando `for i in range(len(matriculas)):`.
  - Se `matriculas[i] == busca`, marque `achou = True`, mostre o índice `i` e interrompa a busca imediatamente com `break`.
  - Após o laço, verifique se a flag permaneceu `False` (`if not achou:`) para exibir a mensagem de negação.

---

### 📌 Questão 15: Inversão Algorítmica de Vetor
- **Quesito:** Preencha uma lista com $6$ números fornecidos pelo usuário. Crie uma nova lista com os mesmos elementos em **ordem invertida**, sem recorrer a `.reverse()` ou fatiamento `[::-1]`.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Em uma lista de tamanho $N$, o último elemento está no índice $N - 1$.
  - Use `range(len(lista) - 1, -1, -1)` para iterar decrescentemente até o índice $0$.
  - Crie uma nova lista vazia e vá inserindo cada elemento acessado por essa indexação decrescente com `.append()`.

---

## ⚙️ Parte 4: Modularização com Funções (Q16 a Q25 -- 10 Questões)

### 📌 Questão 16: Função Sem Parâmetro e Sem Retorno
- **Quesito:** Crie uma função chamada `exibir_cabecalho()` que imprima na tela um banner com molduras compostas pelo caractere `"="`, contendo o nome da instituição (**IFCE Campus Tauá**) e o curso (**Técnico em Redes de Computadores**). No programa principal, faça a chamada da rotina.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Declare a função com parênteses vazios: `def exibir_cabecalho():`.
  - Utilize apenas comandos `print()` e não coloque a palavra-chave `return`.
  - No código principal, invoque a rotina escrevendo apenas `exibir_cabecalho()`.

---

### 📌 Questão 17: Função Sem Parâmetro e Sem Retorno
- **Quesito:** Implemente uma função chamada `exibir_menu_ajuda()` que apresente na tela as teclas de atalho disponíveis para um operador de sistema (ex: `[S] Salvar`, `[C] Carregar`, `[Q] Sair`). O programa principal deve invocar essa função sempre que o usuário digitar `"ajuda"`.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Escreva a função estruturando visualmente as opções de comando com `print()`.
  - No programa principal, leia uma string do usuário e compare-a dentro de um `if`.
  - Quando a entrada coincidir com `"ajuda"`, faça a chamada da função.

---

### 📌 Questão 18: Função Com Parâmetro e Sem Retorno
- **Quesito:** Crie uma função chamada `notificar_servico(nome, porta, status)` onde `status` é booleano.
  - Se `status` for `True`: imprima `"[OK] Serviço: <nome> | Porta: <porta> -> ATIVO"`.
  - Se `status` for `False`: imprima `"[FALHA] Serviço: <nome> | Porta: <porta> -> PARADO"`.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Declare os 3 parâmetros: `def notificar_servico(nome, porta, status):`.
  - Avalie o booleano com `if status: ... else: ...`.
  - Exiba a saída com f-strings interpolando as variáveis recebidas. Não use `return`.

---

### 📌 Questão 19: Função Com Parâmetro e Sem Retorno
- **Quesito:** Desenvolva uma função chamada `desenhar_separador(simbolo, comprimento)` que receba um caractere textual e a quantidade de repetições horizontais desejada, imprimindo a linha gerada no terminal.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Em Python, multiplicar uma string por um inteiro repete o texto (`simbolo * comprimento`).
  - A função recebe as variáveis e executa o `print()`.
  - Teste passando diferentes símbolos e tamanhos (ex: `"-"`, 40 ou `"="`, 25).

---

### 📌 Questão 20: Função Sem Parâmetro e Com Retorno
- **Quesito:** Implemente a função `ler_inteiro_positivo()` sem parâmetros.
  - Solicite repetidamente que o usuário digite um número inteiro até que seja estritamente maior que zero;
  - Quando o valor for válido, devolva-o com `return`.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Utilize um laço `while True:` interno à função.
  - Faça a leitura com `int(input())`.
  - Se `valor > 0`, execute `return valor`.
  - O comando `return` encerra imediatamente a repetição e a função, entregando o número ao chamador.

---

### 📌 Questão 21: Função Sem Parâmetro e Com Retorno
- **Quesito:** Escreva a função `gerar_token_acesso()` sem parâmetros que sorteie e retorne um número inteiro de $6$ dígitos (no intervalo de $100000$ a $999999$), simulando um token de autenticação de dois fatores.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Importe o módulo nativo com `import random`.
  - Utilize a função `random.randint(100000, 999999)`.
  - Devolva o valor sorteado utilizando `return`.
  - No programa principal, guarde o resultado em uma variável: `token = gerar_token_acesso()`.

---

### 📌 Questão 22: Função Com Parâmetro e Com Retorno
- **Quesito:** Crie uma função chamada `converter_celsius(temp_c, escala)` onde `escala` é a sigla da unidade de destino (`"F"` para Fahrenheit ou `"K"` para Kelvin):
  - Fórmulas: $F = C \times 1.8 + 32$ e $K = C + 273.15$.
  - Calcule e devolva o valor com `return`. Se a sigla for inválida, retorne `None`.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Trate a escala com `.upper()` para aceitar letras minúsculas.
  - Faça a conferência da unidade com `if-elif-else`.
  - Em cada bloco, calcule a conversão correspondente e devolva o número usando `return`.

---

### 📌 Questão 23: Função Com Parâmetro e Com Retorno
- **Quesito:** Crie uma função chamada `eh_primo(numero)` que receba um inteiro positivo e retorne um valor booleano: `True` se o número for primo, ou `False` caso não seja.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Se o número for menor ou igual a 1, retorne `False` imediatamente.
  - Monte um laço de 2 até a raiz quadrada inteira do número (`int(numero**0.5) + 1`).
  - Se encontrar resto zero (`numero % d == 0`), retorne imediatamente `False`.
  - Se o laço terminar sem divisores encontrados, execute `return True` fora do laço.

---

### 📌 Questão 24: Função Com Parâmetro e Retorno Múltiplo
- **Quesito:** Crie uma função chamada `analisar_pico(leituras)` que receba uma lista de números reais. A função deve retornar dois valores simultaneamente: o maior valor encontrado na lista e o índice da primeira ocorrência desse maior valor.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Inicialize variáveis de referência: `maior = leituras[0]` e `posicao = 0`.
  - Percorra a lista com índices usando `for i in range(1, len(leituras)):`.
  - Se `leituras[i] > maior`, atualize ambas as variáveis.
  - Ao término, retorne ambos separados por vírgula: `return maior, posicao`.

---

### 📌 Questão 25: Função Com Parâmetro e Com Retorno de Vetor
- **Quesito:** Desenvolva uma função chamada `filtrar_acima_limiar(valores, limiar)` que receba uma lista de números e um número de corte (`limiar`). A função deve construir e retornar uma **nova lista** contendo apenas os elementos estritamente maiores que o limiar. A lista original não deve ser modificada.
- **💡 Ajuda de Resolução (Como Pensar):**
  - Crie uma lista vazia dentro da função: `resultado = []`.
  - Itere sobre os itens da coleção com `for item in valores:`.
  - Avalie o critério: se `item > limiar:`, adicione o elemento com `resultado.append(item)`.
  - Conclua a função devolvendo a lista populada com `return resultado`.

---

## 📊 Quadro Resumo: Os 4 Tipos de Funções

| Classificação | Recebe Parâmetro? | Possui `return`? | Exemplo Típico |
|---|:---:|:---:|---|
| **Sem Parâmetro e Sem Retorno** | Não | Não | `exibir_cabecalho()` |
| **Com Parâmetro e Sem Retorno** | Sim | Não | `notificar_servico(nome, porta, status)` |
| **Sem Parâmetro e Com Retorno** | Não | Sim | `ler_inteiro_positivo()` |
| **Com Parâmetro e Com Retorno** | Sim | Sim | `converter_celsius(temp, escala)` |

---
*Material elaborado para o Curso Técnico em Redes de Computadores do IFCE Campus Tauá.*
