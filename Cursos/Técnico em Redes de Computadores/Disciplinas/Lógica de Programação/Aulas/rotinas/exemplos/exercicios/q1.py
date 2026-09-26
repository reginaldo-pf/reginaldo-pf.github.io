def verifica(num):
    if num >= 0:
        return 1
    else:
        return 0

numero = int(input("Digite um número: "))

resultado = verifica(numero)

if resultado >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")