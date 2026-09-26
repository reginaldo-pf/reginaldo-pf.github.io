# Solução Comentada: Lógica de Programação com Python

Este documento apresenta a solução detalhada para as duas questões propostas, explicando o papel de cada estrutura e comando utilizado, sem o uso de *list comprehension*, visando o aprendizado de lógica estruturada.

---

## Solução da Questão 1: O Sistema de Apoio ao Professor

### Código Python Completo

```python
# 1. Inicializando as listas vazias
nomes = []
notas = []

# 2. Entrada de dados com laço de repetição
for i in range(5):
    # Solicitamos o nome (texto/string)
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    # Solicitamos a nota (número decimal/float)
    nota = float(input(f"Digite a nota de {nome}: "))
    
    # Adicionamos as informações nas respectivas listas
    nomes.append(nome)
    notas.append(nota)

# 3. Cálculo da média geral
soma_notas = sum(notas)
total_alunos = len(notas)
media = soma_notas / total_alunos

print(f"\nMédia geral da turma: {media:.2f}")

# 4. Filtragem de alunos acima ou igual à média
print("\nAlunos com nota igual ou superior à média:")
for i in range(len(notas)):
    if notas[i] >= media:
        print(f"- {nomes[i]} (Nota: {notas[i]})")

# 5. Identificação da maior nota e do aluno correspondente
maior_nota = max(notas)
indice_maior = notas.index(maior_nota)
aluno_maior = nomes[indice_maior]

print(f"\nA maior nota foi {maior_nota}, obtida pelo aluno {aluno_maior}.")
```

### Explicação Detalhada do Código

1. **Criação das Listas (`nomes` e `notas`)**:
   * Começamos declarando `nomes = []` e `notas = []`. Elas começam vazias para que possamos armazenar múltiplos valores digitados pelo usuário durante a execução.
2. **O Laço de Entrada (`for i in range(5)`)**:
   * O `range(5)` gera uma sequência de 0 a 4. O laço executa 5 vezes.
   * `i+1` é usado na mensagem de digitação apenas para ficar mais amigável para o usuário (mostrando "1º aluno", "2º aluno", etc., em vez de "0º aluno").
   * A função `.append()` adiciona o valor lido ao final de cada lista correspondente.
3. **Cálculo da Média**:
   * `sum(notas)` percorre toda a lista de notas e faz a soma total dos valores.
   * `len(notas)` retorna o tamanho da lista (nesse caso, 5).
   * Dividimos a soma pelo tamanho para obter a média da turma.
4. **O Laço de Filtragem**:
   * Usamos `for i in range(len(notas))` para percorrer os índices da lista (0, 1, 2, 3 e 4).
   * A estrutura condicional `if notas[i] >= media` verifica se a nota guardada na posição `i` é maior ou igual à média.
   * Se for verdade, usamos o mesmo índice `i` para buscar o nome do aluno na lista de nomes (`nomes[i]`). Isso é possível porque as duas listas são paralelas (o aluno da posição `i` na lista `nomes` possui a nota na posição `i` da lista `notas`).
5. **Encontrando a Maior Nota**:
   * `max(notas)` analisa a lista e retorna o maior valor numérico contido nela.
   * `notas.index(maior_nota)` encontra em qual posição (índice) a maior nota está guardada.
   * Por fim, usamos essa mesma posição para recuperar o nome do aluno em `nomes[indice_maior]`.

---

## Solução da Questão 2: Alerta de Estoque Mínimo no Supermercado

### Código Python Completo

```python
# 1. Inicializando as listas vazias
produtos = []
quantidades = []

# 2. Entrada de dados com laço de repetição
for i in range(6):
    produto = input(f"Digite o nome do {i+1}º produto: ")
    quantidade = int(input(f"Digite a quantidade atual de '{produto}' em estoque: "))
    
    produtos.append(produto)
    quantidades.append(quantidade)

# Definindo as variáveis de controle
limite_seguranca = 10
total_alertas = 0

print("\n=== RELATÓRIO DE ALERTAS DE ESTOQUE CRÍTICO ===")

# 3. Processamento de dados e verificação
for i in range(6):
    if quantidades[i] < limite_seguranca:
        # Calcula quantas unidades faltam para atingir o estoque mínimo
        diferenca = limite_seguranca - quantidades[i]
        
        # Exibe o alerta
        print(f"Alerta: O produto '{produtos[i]}' está com estoque baixo ({quantidades[i]} un.).")
        print(f"        -> Comprar mais {diferenca} unidades para atingir o limite.")
        
        # Incrementa o contador de alertas
        total_alertas = total_alertas + 1

print("==============================================")
# 4. Exibindo o resultado final
print(f"Total de produtos que precisam de reposição: {total_alertas}")
```

### Explicação Detalhada do Código

1. **Listas Paralelas**:
   * Usamos `produtos` e `quantidades` como listas paralelas. Cada produto cadastrado no índice `i` terá sua quantidade de estoque armazenada exatamente no mesmo índice `i` da outra lista.
2. **Entrada de Dados (`for i in range(6)`)**:
   * O programa executa o cadastro 6 vezes. Convertemos a entrada da quantidade para inteiro (`int`), pois contagem física de estoque de produtos do mercado neste contexto usa números inteiros.
3. **Contador de Alertas (`total_alertas`)**:
   * Declaramos a variável `total_alertas = 0` antes de iniciar a verificação. Ela funcionará como um acumulador que soma 1 toda vez que encontrarmos um estoque crítico.
4. **Verificação com Condicional (`if quantidades[i] < limite_seguranca`)**:
   * Lemos a quantidade de cada produto em `quantidades[i]`. Se o valor for estritamente menor que 10:
     * Calculamos a diferença necessária para atingir o estoque de segurança (`limite_seguranca - quantidades[i]`).
     * Exibimos uma mensagem formatada alertando o gerente.
     * Somamos 1 ao contador (`total_alertas = total_alertas + 1`).
5. **Resultado do Acumulador**:
   * Após terminar o laço `for`, o programa sai da estrutura de repetição e imprime a quantidade total de alertas acumulados, fornecendo o panorama geral solicitado pelo gerente.
