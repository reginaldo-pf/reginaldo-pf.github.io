def divisores(a, b, c):
    s = 0

    for i in range(b, c + 1):
        if i % a == 0:
            s = s + i
    return s

a = int(input("Digite o número a: "))
b = int(input("Digite o número b: "))
c = int(input("Digite o número c: "))
resultado = divisores(a, b, c)
print(f"A soma dos números entre {b} e {c} que são divisíveis por {a} é: {resultado}")