'''
 0   1   2  3  4    5  6  7   8
[7, 10, 13, 4, 17, 20, 9, 2, 15]

Número primo: 7  Posição: 1
Número primo: 13 Posição: 3
Número primo: 17 Posição: 5
Número primo: 2  Posição: 8
'''
num = []

for i in range(9):
    valor = int(input(f"Digite o {i + 1}º número: "))
    num.append(valor)
print(num)

for i in range(9):
    cont = 0
    for j in range(1, num[i] + 1):
        if num[i] % j == 0:
            cont += 1
    if cont == 2:
        print(f"Número primo: {num[i]}  Posição: {i}")