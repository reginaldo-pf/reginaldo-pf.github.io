# 🐍 Cola de Python: Referência Rápida para Lógica de Programação

Este guia serve como material de apoio rápido para resolver problemas de lógica de programação usando Python. Ele é conciso e foca nas estruturas básicas da linguagem e nas principais funções embutidas.

* **Curso:** Redes de Computadores
* **Instituição:** IFCE Campus Tauá

---

## 1. Entrada, Saída e Conversão de Tipos

Para interagir com o usuário, ler dados do teclado e exibi-los na tela de forma formatada.

```python
# --- ENTRADA DE DADOS ---
texto = input("Digite um texto: ")            # Sempre lê como string (texto)
inteiro = int(input("Digite um inteiro: "))    # Converte o texto digitado para número inteiro
decimal = float(input("Digite um decimal: "))  # Converte o texto digitado para número real

# --- SAÍDA DE DADOS (f-strings) ---
# O 'f' antes do texto permite colocar variáveis dentro de chaves {}
print(f"Texto: {texto} | Inteiro: {inteiro}")

# Formatando casas decimais: usando ':.2f' limitamos para 2 casas decimais
print(f"Decimal formatado: {decimal:.2f}")
```

---

## 2. Operações Matemáticas

Operadores aritméticos básicos no Python para a realização de cálculos.

```python
a = 10
b = 3

soma = a + b        # 13
sub = a - b         # 7
mult = a * b        # 30
div = a / b         # 3.3333... (divisão real)
div_inteira = a // b # 3 (descarta a parte decimal)
resto = a % b       # 1 (resto da divisão, ótimo para verificar se é par/ímpar)
potencia = a ** b   # 1000 (10 elevado a 3)
```

---

## 3. Manipulação de Strings (Textos)

Métodos comuns do Python para realizar alterações e formatações em variáveis de texto.

```python
texto = "  Algoritmos em Python!  "

maiusculo = texto.upper()     # "  ALGORITMOS EM PYTHON!  "
minusculo = texto.lower()     # "  algoritmos em python!  "
limpo = texto.strip()         # "Algoritmos em Python!" (remove espaços no início/fim)
trocado = texto.replace("Python", "C") # "  Algoritmos em C!  "

# Dividir um texto em uma lista com base em um caractere separador
frase = "arroz,feijao,carne"
itens = frase.split(",")       # ['arroz', 'feijao', 'carne']

# Juntar os elementos de uma lista em uma única string
junto = "-".join(itens)        # "arroz-feijao-carne"
```

---

## 4. Decisões e Condições (`if`, `elif`, `else`)

Executa diferentes blocos de código com base em testes lógicos.

```python
# --- OPERADORES DE COMPARAÇÃO ---
# == (igual)   != (diferente)   > (maior)   < (menor)   >= (maior ou igual)   <= (menor ou igual)

# --- OPERADORES LÓGICOS ---
# and (e - ambas verdadeiras)   or (ou - pelo menos uma verdadeira)   not (não - inverte lógica)

# --- IF SIMPLES (Verificação única) ---
nota = 8.5
if nota >= 7.0:
    print("Aprovado!")

# --- IF COMPOSTO (Múltiplos caminhos) ---
idade = 17
tem_autorizacao = True

if idade >= 18:
    print("Acesso liberado (Maior de idade)")
elif idade >= 16 and tem_autorizacao:
    print("Acesso liberado (Com autorização)")
else:
    print("Acesso negado")
```

---

## 5. Repetições (Loops: `for` e `while`)

Repete um bloco de código várias vezes ou enquanto uma condição for verdadeira.

```python
# --- LOOP FOR COM RANGE ---
# range(fim) -> vai de 0 até fim - 1
for i in range(5):
    print(i)  # Imprime: 0, 1, 2, 3, 4

# range(inicio, fim) -> vai de inicio até fim - 1
for i in range(2, 6):
    print(i)  # Imprime: 2, 3, 4, 5

# range(inicio, fim, passo) -> pula de passo em passo
for i in range(10, 21, 2):
    print(i)  # Imprime: 10, 12, 14, 16, 18, 20

# --- LOOP WHILE (Enquanto) ---
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Evita loop infinito!
```

---

## 6. Listas (Vetores de 1 Dimensão)

Estrutura para armazenar múltiplos valores de forma sequencial e ordenada.

```python
numeros = [10, 20, 30, 40]
# Índices:   0   1   2   3  (ou de trás pra frente: -1 é o último elemento)
primeiro = numeros[0]    # 10
ultimo = numeros[-1]     # 40

# --- MODIFICAÇÃO E INSERÇÃO ---
numeros[1] = 25       # Altera o elemento do índice 1: [10, 25, 30, 40]
numeros.append(50)    # Adiciona 50 no fim da lista: [10, 25, 30, 40, 50]
numeros.insert(1, 15) # Insere 15 no índice 1 (empurra os outros): [10, 15, 25, 30, 40, 50]

# --- REMOÇÃO ---
numeros.pop()         # Remove e retorna o último elemento: [10, 15, 25, 30, 40]
numeros.pop(1)        # Remove e retorna o elemento no índice 1: [10, 25, 30, 40]
numeros.remove(30)    # Procura e remove o primeiro valor 30 que encontrar: [10, 25, 40]

# --- ORDENAÇÃO E INVERSÃO ---
valores = [5, 2, 9, 1]
valores.sort()        # Altera a própria lista para crescente: [1, 2, 5, 9]
valores.sort(reverse=True) # Altera para decrescente: [9, 5, 2, 1]
valores.reverse()     # Inverte a ordem atual da lista

# --- PERCORRER COM ÍNDICE ---
for i, num in enumerate(valores):
    print(f"Posição {i} tem o valor {num}")
```

---

## 7. Matrizes (Tabelas/Vetores de 2 Dimensões)

Uma matriz em Python é representada por uma **lista de listas** (uma lista onde cada elemento é uma linha).

```python
# --- CRIAÇÃO E ACESSO ---
matriz = [
    [1, 2, 3],  # Linha 0
    [4, 5, 6],  # Linha 1
    [7, 8, 9]   # Linha 2
]

# Acessando: matriz[linha][coluna]
valor = matriz[1][2]  # Linha 1, Coluna 2 -> valor 6
matriz[0][0] = 99     # Altera valor na Linha 0, Coluna 0

# --- PERCORRER UMA MATRIZ ---
# Método 1: Linha por linha (Ideal para exibir na tela como tabela)
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")  # \t adiciona um espaçamento
    print()  # Pula de linha ao terminar uma linha da matriz

# Método 2: Por índices (Necessário se precisar saber a linha/coluna exata)
linhas = len(matriz)       # Quantidade de linhas
colunas = len(matriz[0])   # Quantidade de colunas (tamanho da primeira linha)

for i in range(linhas):
    for j in range(colunas):
        print(f"Posição [{i}][{j}] contém {matriz[i][j]}")
```

---

## 8. Dicionários (Estruturas de Chave-Valor)

Estruturas ideais para mapear dados rotulados, onde cada elemento possui uma "chave" e um "valor".

```python
# --- CRIAÇÃO E ACESSO ---
aluno = {
    "nome": "João Pedro",
    "idade": 20,
    "curso": "ADS"
}

print(aluno["nome"])  # Acessa o valor da chave "nome" -> "João Pedro"

# --- INSERÇÃO E ALTERAÇÃO ---
aluno["media"] = 8.5  # Cria uma nova chave "media" com o valor 8.5
aluno["idade"] = 21   # Altera o valor da chave existente "idade"

# --- REMOÇÃO ---
del aluno["curso"]           # Remove a chave "curso"
valor_removido = aluno.pop("idade") # Remove a chave e retorna o valor dela

# --- PERCORRER DICIONÁRIOS ---
# Percorrer chaves e valores juntos (Muito comum)
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")
```

---

## 9. Principais Funções Embutidas (`built-in`)

| Função | Descrição | Exemplo de Uso | Resultado |
| :--- | :--- | :--- | :--- |
| `len(c)` | Retorna o tamanho/comprimento de uma coleção | `len([4, 8, 2])` | `3` |
| `sum(c)` | Soma todos os elementos numéricos | `sum([4, 8, 2])` | `14` |
| `min(c)` | Retorna o menor elemento | `min([4, 8, 2])` | `2` |
| `max(c)` | Retorna o maior elemento | `max([4, 8, 2])` | `8` |
| `sorted(c)`| Retorna uma **nova** lista em ordem crescente | `sorted([4, 8, 2])`| `[2, 4, 8]` |
| `abs(n)` | Retorna o valor absoluto (sem sinal) | `abs(-15)` | `15` |
| `round(n, d)`| Arredonda um número decimal para `d` casas | `round(3.14159, 2)`| `3.14` |

---

## 10. Receitas Comuns (Padrões de Algoritmos)

Esses trechos servem de base para resolver mais de 80% das questões básicas de lógica com listas:

### A. Acumulador (Soma acumulada)
Útil para somar valores que dependem de uma condição.
```python
valores = [12, 5, 8, 21, 30, 4]
soma_pares = 0

for v in valores:
    if v % 2 == 0:
        soma_pares += v # Soma apenas os pares
```

### B. Contador
Útil para contar quantas vezes algo acontece.
```python
notas = [6.5, 8.0, 5.5, 9.0, 4.0, 7.0]
aprovados = 0

for nota in notas:
    if nota >= 6.0:
        aprovados += 1 # Incrementa se nota for azul
```

### C. Maior e Menor Elemento (Manualmente)
Como achar o maior ou menor valor de uma lista sem usar as funções `max()` ou `min()`.
```python
idades = [25, 42, 18, 50, 31]

# Começamos assumindo que o primeiro elemento é o maior
maior_idade = idades[0]

for idade in idades:
    if idade > maior_idade:
        maior_idade = idade # Se achou um maior, atualiza
```

### D. Filtragem de Listas
Criar uma nova lista a partir de uma lista existente com base em uma condição.
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []

for n in numeros:
    if n % 2 != 0:
        impares.append(n) # Guarda somente os ímpares
```

---

## 11. List Comprehension

Forma reduzida e otimizada de gerar e filtrar listas em Python.

```python
# --- SINTAXE BÁSICA ---
# [expressao for item in colecao]
quadrados = [x**2 for x in range(5)]            # [0, 1, 4, 9, 16]

# --- SINTAXE COM FILTRAGEM (IF) ---
# [expressao for item in colecao if condicao]
pares = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]

# --- EXEMPLOS TEMÁTICOS (REDES DE COMPUTADORES) ---
# 1. Limpar espaços extras em branco de uma lista de IPs
hosts = [" 192.168.1.1 ", " 10.0.0.1", "172.16.0.254 "]
ips_limpos = [ip.strip() for ip in hosts]
# Resultado: ['192.168.1.1', '10.0.0.1', '172.16.0.254']

# 2. Filtrar apenas IPs que pertencem a subrede local (começam com "192.")
ips = ["192.168.1.5", "10.0.0.3", "192.168.2.10", "8.8.8.8"]
ips_locais = [ip for ip in ips if ip.startswith("192.")]
# Resultado: ['192.168.1.5', '192.168.2.10']
```
