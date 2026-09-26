numeros = []

for i in range(9):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = [n for n in numeros if eh_primo(n)]

print("\nNúmeros digitados:", numeros)
print("Números primos:", primos)