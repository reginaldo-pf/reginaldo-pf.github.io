nomes = []
notas = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    
    nomes.append(nome)
    notas.append(nota)

soma_notas = sum(notas)
media = soma_notas / len(notas)

print(f"Média Geral da Turma: {media:.2f}")

print("Alunos com nota acima da média:")
for i in range(len(notas)):
    if notas[i] > media:
        print(f"{nomes[i]}: {notas[i]:.2f}")
