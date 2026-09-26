def somar(num1, num2):
    s = 0
    for i in range(num1, num2 + 1):
        s = s + i
    return s

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = somar(numero1, numero2)
print(f"A soma dos números entre {numero1} e {numero2} é: {resultado}")