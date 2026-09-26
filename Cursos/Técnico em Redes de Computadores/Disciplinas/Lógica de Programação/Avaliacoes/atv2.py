'''
Posição| Qtd | Preço
1      | 15  | 10,00
2      |  8  | 25,00
3      | 20  | 05,00
      
      ...

10     |  8  | 80,00
'''
qtd = []
preco = []

for i in range(10):
    quantidade = int(input(f"Digite a quantidade do {i + 1}º produto: "))
    qtd.append(quantidade)
    valor = float(input(f"Digite o preço do {i + 1}º produto: "))
    preco.append(valor)

print("Posição | Quantidade | Preço | Total")
for i in range(10):
    total = qtd[i] * preco[i]
    print(f"{i + 1}       | {qtd[i]}         | {preco[i]:.2f} | {total:.2f}")