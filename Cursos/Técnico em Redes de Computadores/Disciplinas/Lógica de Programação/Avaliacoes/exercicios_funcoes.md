# Exercícios de Fixação: Funções com Parâmetro e Retorno em Python

Esta lista contém 4 exercícios práticos para exercitar a criação de funções em Python que recebem parâmetros de entrada e retornam valores processados.

---

## 📋 Exercício 1: Conversor de Temperatura (Fahrenheit para Celsius)

### 📌 Enunciado
Escreva uma função chamada `fahrenheit_para_celsius` que recebe uma temperatura em graus Fahrenheit ($F$) como parâmetro, calcula e retorna a temperatura correspondente em graus Celsius ($C$).

A fórmula de conversão é:
$$C = (F - 32) \times \frac{5}{9}$$

No programa principal, solicite que o usuário digite a temperatura em Fahrenheit, chame a função passando esse valor e exiba o resultado retornado com 2 casas decimais.

### 📥 Entrada e Saída (Exemplo)
```text
Digite a temperatura em Fahrenheit: 77
A temperatura em Celsius é: 25.00°C
```

---

## 📋 Exercício 2: Verificador de Senha Segura

### 📌 Enunciado
Crie uma função chamada `verificar_senha_segura` que recebe uma string `senha` como parâmetro. A função deve retornar um valor booleano (`True` se a senha for segura ou `False` caso contrário). 

Para ser considerada segura, a senha deve atender a **ambos** os critérios:
1. Conter no mínimo 8 caracteres.
2. Conter pelo menos um número (caractere entre `'0'` e `'9'`).

No programa principal, leia uma senha do teclado, passe-a para a função e imprima se a senha foi aceita ou rejeitada.

### 📥 Entrada e Saída (Exemplo 1)
```text
Digite a senha para cadastro: teste123
Resultado: Senha aceita e segura!
```

### 📥 Entrada e Saída (Exemplo 2)
```text
Digite a senha para cadastro: python
Resultado: Senha fraca. Deve conter pelo menos 8 caracteres e um número.
```

---

## 📋 Exercício 3: Média Ponderada e Situação Acadêmica

### 📌 Enunciado
Implemente uma função chamada `avaliar_aluno` que recebe três notas ($N_1$, $N_2$, $N_3$) e seus respectivos pesos ($P_1$, $P_2$, $P_3$). A função deve calcular a média ponderada do aluno e retornar uma **tupla** contendo a média calculada (arredondada para 2 casas decimais) e uma string com a situação acadêmica baseada nas regras:
- **"Aprovado"**: Média maior ou igual a 7.0
- **"Recuperação"**: Média entre 5.0 e 6.9 (inclusive)
- **"Reprovado"**: Média menor que 5.0

No programa principal, receba as notas e chame a função. Exiba a média final e o status retornado pela função.

A fórmula da média ponderada é:
$$\text{Média Ponderada} = \frac{(N_1 \times P_1) + (N_2 \times P_2) + (N_3 \times P_3)}{P_1 + P_2 + P_3}$$

### 📥 Entrada e Saída (Exemplo)
```text
Nota 1: 6.0 | Peso 1: 2
Nota 2: 7.5 | Peso 2: 3
Nota 3: 5.0 | Peso 3: 5
Média Final: 6.00 - Situação: Recuperação
```

---

## 📋 Exercício 4: Estatísticas de Preços de Produtos

### 📌 Enunciado
Crie uma função chamada `analisar_precos` que recebe uma lista de preços de produtos (lista de números reais). A função deve retornar um **dicionário** contendo as seguintes estatísticas sobre os preços:
1. O preço mais caro.
2. O preço mais barato.
3. A média aritmética simples dos preços.

No programa principal, peça para o usuário digitar os preços de 5 produtos, armazene-os em uma lista, passe a lista para a função e depois exiba as estatísticas retornadas na tela de forma legível.

*(Dica: Se a lista estiver vazia, trate o caso retornando valores nulos ou padrão)*

### 📥 Entrada e Saída (Exemplo)
```text
Digite o preço do produto 1: 15.50
Digite o preço do produto 2: 45.00
Digite o preço do produto 3: 10.00
Digite o preço do produto 4: 25.00
Digite o preço do produto 5: 30.00

--- Estatísticas das Compras ---
Maior Preço: R$ 45.00
Menor Preço: R$ 10.00
Preço Médio: R$ 25.10
```

---

# 💡 Gabarito de Soluções (Códigos de Exemplo)

Abaixo está a implementação sugerida em Python para cada um dos exercícios descritos.

### Solução do Exercício 1
```python
def fahrenheit_para_celsius(f):
    c = (f - 32) * 5 / 9
    return c

# Programa Principal
temp_f = float(input("Digite a temperatura em Fahrenheit: "))
temp_c = fahrenheit_para_celsius(temp_f)
print(f"A temperatura em Celsius é: {temp_c:.2f}°C")
```

### Solução do Exercício 2
```python
def verificar_senha_segura(senha):
    # Critério 1: Comprimento
    if len(senha) < 8:
        return False
    
    # Critério 2: Conter pelo menos um número
    tem_numero = False
    for char in senha:
        if char.isdigit():  # Verifica se o caractere é um dígito de 0 a 9
            tem_numero = True
            break
            
    return tem_numero

# Programa Principal
senha_usuario = input("Digite a senha para cadastro: ")
if verificar_senha_segura(senha_usuario):
    print("Resultado: Senha aceita e segura!")
else:
    print("Resultado: Senha fraca. Deve conter pelo menos 8 caracteres e um número.")
```

### Solução do Exercício 3
```python
def avaliar_aluno(n1, n2, n3, p1, p2, p3):
    soma_pesos = p1 + p2 + p3
    media = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / soma_pesos
    media_arredondada = round(media, 2)
    
    if media_arredondada >= 7.0:
        situacao = "Aprovado"
    elif media_arredondada >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    return media_arredondada, situacao

# Programa Principal
n1 = float(input("Digite a nota 1: "))
p1 = int(input("Digite o peso da nota 1: "))
n2 = float(input("Digite a nota 2: "))
p2 = int(input("Digite o peso da nota 2: "))
n3 = float(input("Digite a nota 3: "))
p3 = int(input("Digite o peso da nota 3: "))

media, status = avaliar_aluno(n1, n2, n3, p1, p2, p3)
print(f"Média Final: {media:.2f} - Situação: {status}")
```

### Solução do Exercício 4
```python
def analisar_precos(lista_precos):
    if not lista_precos:
        return {"maior": 0.0, "menor": 0.0, "media": 0.0}
    
    maior = max(lista_precos)
    menor = min(lista_precos)
    media = sum(lista_precos) / len(lista_precos)
    
    return {
        "maior": maior,
        "menor": menor,
        "media": round(media, 2)
    }

# Programa Principal
precos = []
for i in range(5):
    preco = float(input(f"Digite o preço do produto {i + 1}: "))
    precos.append(preco)

estatisticas = analisar_precos(precos)

print("\n--- Estatísticas das Compras ---")
print(f"Maior Preço: R$ {estatisticas['maior']:.2f}")
print(f"Menor Preço: R$ {estatisticas['menor']:.2f}")
print(f"Preço Médio: R$ {estatisticas['media']:.2f}")
```
