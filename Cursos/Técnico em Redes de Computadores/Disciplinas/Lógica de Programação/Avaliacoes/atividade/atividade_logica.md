# Atividade Prática: Lógica de Programação com Python

Esta atividade foi projetada para uma aula prática de 1 hora, abordando os conceitos de **estruturas condicionais**, **laços de repetição** e **listas (vetores)** em Python.

---

## Questão 1: O Sistema de Apoio ao Professor (Média e Destaques)

### Contexto
O professor Carlos leciona a disciplina de Introdução à Programação. Ao final do semestre, ele precisa fechar as notas de sua turma de 5 alunos. Para facilitar seu trabalho, ele deseja um programa em Python que:
1. Permita digitar o nome e a nota final de cada um dos 5 alunos e armazene essas informações em listas.
2. Calcule e exiba a média geral da turma.
3. Exiba uma lista contendo os nomes dos alunos que obtiveram nota igual ou superior à média da turma.
4. Identifique e exiba qual aluno obteve a maior nota da turma e qual foi essa nota.

### Dicas de Resolução
* **Estrutura de Dados:** Crie duas listas vazias no início do programa: uma para armazenar os nomes (`nomes = []`) e outra para armazenar as notas (`notas = []`).
* **Laço de Entrada:** Use um laço `for` que execute 5 vezes (dica: utilize `range(5)`). A cada repetição, solicite o nome e a nota e adicione-os às listas usando o método `.append()`.
* **Cálculo da Média:** Some todas as notas usando a função `sum(notas)` e divida pela quantidade total de notas, obtida com `len(notas)`.
* **Filtragem dos Alunos:** Use um novo laço `for` para percorrer a lista de notas (usando índices, como `for i in range(len(notas))`). Use uma estrutura condicional `if` para verificar se a nota do aluno na posição `i` é maior ou igual à média da turma. Se for, imprima o nome correspondente da lista de nomes na mesma posição `i`.
* **Maior Nota:** Encontre a maior nota utilizando a função `max(notas)`. Para descobrir quem tirou essa nota, descubra o índice dela na lista usando `notas.index(maior_nota)` e acesse a lista de nomes nessa mesma posição.

---

## Questão 2: Alerta de Estoque Mínimo no Supermercado

### Contexto
Um mercadinho de bairro deseja automatizar seu controle de estoque. Eles possuem 6 produtos principais nas prateleiras. O gerente do mercado precisa de um sistema que:
1. Cadastre os nomes de 6 produtos e suas respectivas quantidades atuais em estoque.
2. Defina um limite mínimo de segurança (estoque crítico), que é de **10 unidades**.
3. Verifique o estoque de cada produto e exiba um relatório de alertas listando quais produtos estão abaixo do estoque crítico e quantas unidades faltam para atingir o estoque mínimo de segurança (10 unidades).
4. Ao final do relatório, exiba a quantidade total de produtos que precisam de reposição imediata.

### Dicas de Resolução
* **Estruturas de Repetição e Listas:** Assim como no exercício anterior, use duas listas: uma para os nomes dos produtos e outra para as quantidades em estoque. Popule as listas usando um laço `for` com `range(6)`.
* **Contador de Alertas:** Crie uma variável acumuladora inicializada em zero (ex: `total_alertas = 0`) para contar quantos produtos precisam de reposição.
* **Relatório de Crise:** Percorra as listas usando um laço `for i in range(6)`. Dentro do laço, use uma estrutura condicional `if` para testar se a quantidade do produto na posição `i` é menor que 10.
* **Cálculo da Diferença:** Se a quantidade for menor que 10, calcule a quantidade de reposição necessária (`10 - quantidade[i]`), exiba o nome do produto com o alerta e a quantidade a ser comprada, e incremente a variável `total_alertas` em 1.
* **Resultado Final:** Fora do laço de verificação, exiba o valor armazenado em `total_alertas`.
