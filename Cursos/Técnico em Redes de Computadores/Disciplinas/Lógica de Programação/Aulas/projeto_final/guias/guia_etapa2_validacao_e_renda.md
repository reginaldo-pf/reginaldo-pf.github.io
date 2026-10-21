# Guia de Aula Interativo Linha a Linha: Etapa 2 – Entrada Segura e Previsão de Renda

* **Curso:** Técnico em Redes de Computadores
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Instituição:** Instituto Federal do Ceará (IFCE) – Campus Tauá
* **Metodologia:** *Live Coding Dialogado* (Construção alternada entre a função `main()`, a função especialista `definir_renda()` e a função guardiã `obter_numero_positivo()`).
* **Código de Apoio:** [etapas/etapa2_validacao_e_renda.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa2_validacao_e_renda.py)

---

## 🧭 Como Usar Este Guia em Sala de Aula

> [!IMPORTANT]
> **Ponto de Partida:** Comece abrindo o arquivo finalizado na Aula 1 ([etapa1_menu_e_fluxo.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa1_menu_e_fluxo.py)).
> Hoje vamos transformar a **Opção 1** (que apenas exibia `[EM CONSTRUÇÃO]`) em uma funcionalidade real, segura e à prova de falhas humanas.

---

## 🎬 Ato 0: O Desafio do Dia e a Criação do Estado na `main()`

Abra o código da Aula 1 e localize a função `main()`:

```python
def main():
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Definir Renda.")
```

### Passo 0.1: Onde Guardar a Renda Mensal?
Faça a seguinte pergunta para a turma:
> *"Quando o usuário digitar a renda dele (ex: R$ 3.000,00), onde esse número precisa ficar armazenado para que possamos usá-lo mais tarde no relatório final?"*

Explique: *"Ele precisa ficar em uma variável dentro da função `main()`. Mas atenção: **onde** dentro da `main()`?"*

Digite na primeira linha da `main()`, **antes** do `while True:`:

```python
def main():
    renda_prevista = 0.0  # Estado persistente na memória da aplicação
    
    while True:
```

💬 **O que explicar para a turma (Conceito Crítico de Escopo e Laço):**
* *"Se colocássemos `renda_prevista = 0.0` dentro do `while True:`, a cada vez que o menu reaparecesse na tela, a variável seria resetada para zero e esqueceria o que o usuário cadastrou!"*
* *"Variáveis declaradas **antes** do laço continuam existindo e mantêm seus valores durante todas as voltas do menu."*

---

## 🔌 Ato 1: Conectando a Chamada na `main()` (Top-Down Design)

### Passo 1.1: Substituir o Print de Construção
Na `main()`, dentro do `if opcao == "1":`, remova o print provisório e digite:

```python
        if opcao == "1":
            renda_prevista = definir_renda()
```

💬 **O que explicar para a turma:**
* *"Estamos dizendo para o Python: 'Quando o usuário escolher 1, execute a função `definir_renda()`. Quando ela terminar de trabalhar, ela nos entregará um valor que será guardado na nossa variável `renda_prevista`'."*

🧪 **Teste com a Turma (Executar agora de propósito):**
Rode o script no terminal e escolha a opção `1`.
* O terminal exibirá um erro vermelho:
  ```text
  NameError: name 'definir_renda' is not defined
  ```
* Comente com os alunos: *"Perfeito! O Python nos avisou: 'Você mandou executar `definir_renda()`, mas essa função ainda não existe!'. É exatamente isso que nos guia para o próximo passo."*

---

## 🏗️ Ato 2: Criando a Função `definir_renda()` no Topo

Suba o cursor para cima da função `main()` (abaixo de `exibir_menu()`) e crie o esqueleto:

```python
def definir_renda():
    """Solicita e confirma a previsão de renda mensal."""
    print("\n--- Previsão de Renda Mensal ---")
    renda = float(input("Informe a receita líquida esperada (R$): "))
    print(f"Renda prevista atualizada para: R$ {renda:.2f}")
    return renda
```

💬 **O que explicar linha a linha:**
1. `print("\n--- Previsão de Renda Mensal ---")`: Cabeçalho que dá contexto ao usuário.
2. `renda = float(input(...))`: Lê o texto digitado e tenta converter para número de ponto flutuante (`float`).
3. `f"Renda prevista atualizada para: R$ {renda:.2f}"`: O modificador `:.2f` formata o número com 2 casas decimais. Se o usuário digitar `2000`, a tela mostrará `2000.00`.
4. `return renda`: **A esteira de entrega.** Devolve o valor calculado para a linha `renda_prevista = definir_renda()` na `main()`.

🧪 **Teste 1 com a Turma (Cenário Feliz):**
* Execute o programa. Escolha `1`. Digite `2500.50`.
* A tela confirma: `Renda prevista atualizada para: R$ 2500.50` e volta ao menu. Funcionou!

🧪 **Teste 2 com a Turma (O Crash):**
* Peça para um aluno testar digitando: `dois mil` ou teclar apenas `ENTER`.
* O programa trava completamente:
  ```text
  ValueError: could not convert string to float: 'dois mil'
  ```
* Teste também digitando: `-500`.
* O programa aceita um salário negativo de -R$ 500,00!

Pergunta à turma:
> *"Em um sistema de finanças ou em uma configuração de rede, podemos deixar o programa fechar com erro fatal na cara do usuário porque ele digitou uma letra? E podemos aceitar uma renda negativa?"*

---

## 🛡️ Ato 3: A Função Guardiã (`obter_numero_positivo`)

Comente com a turma:
*"Poderíamos colocar um monte de `while` e `try/except` dentro de `definir_renda()`? Sim. Mas na Aula 3 teremos que ler o **Valor da Despesa**, que também precisa ser um número positivo e seguro. Vamos reescrever o mesmo código duas vezes? Não! Vamos criar uma **função especialista em obter números positivos**!"*

Suba o cursor para cima da função `definir_renda()` e digite a assinatura da função:

```python
def obter_numero_positivo(mensagem):
    """Garante que o valor inserido seja um float válido e positivo."""
    while True:
```

💬 **O que explicar sobre a linha `while True:`:**
* *"O laço infinito aqui significa: 'Enquanto o usuário não me der um número aceitável, eu não saio daqui e não deixo o sistema prosseguir'."*

---

### Passo 3.1: O Bloco Monitorado (`try`)
Dentro do `while True:` de `obter_numero_positivo`, digite:

```python
    while True:
        try:
            valor = float(input(mensagem))
```

💬 **O que explicar para a turma:**
* *"O bloco `try:` diz ao Python: 'Tente executar o que está aqui dentro. Se ocorrer algum problema de conversão, não quebre o programa; deixe que eu mesmo assumo o controle!'."*
* *"O parâmetro `mensagem` permite que a função receba qualquer texto como pergunta, tornando-a 100% reutilizável."*

---

### Passo 3.2: A Validação da Regra de Negócio (`if valor >= 0`)
Abaixo da leitura do float, ainda dentro do `try`:

```python
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            print("Erro: O valor não pode ser negativo.")
```

💬 **O que explicar para a turma (Superpoder do `return`):**
* *"Se o valor for zero ou positivo, executamos `return valor`."*
* *"Atenção para este detalhe fundamental: **o `return` encerra a função e quebra o `while True` imediatamente!** Não precisamos nem escrever `break`. Ele pega o dado válido e devolve para quem chamou."*
* *"Se o valor for negativo (ex: `-100`), a condição falha, ele cai no `print` avisando que não pode ser negativo, e o `while` repete a pergunta!"*

---

### Passo 3.3: A Rede de Proteção (`except ValueError`)
Agora feche o bloco com a captura da exceção:

```python
        except ValueError:
            print("Erro: Digite um número válido (ex: 1500.50).")
```

💬 **O que explicar para a turma:**
* *"Se o usuário digitar `'abc'` ou apertar ENTER vazio, a linha `float()` falha. O Python pula instantaneamente para dentro do `except ValueError:`."*
* *"Em vez de fechar o programa em tela vermelha, ele exibe um aviso educado ao usuário e o `while` recomeça!"*

---

## 🔄 Ato 4: Refatorando `definir_renda()` para Consumir a Guardiã

Agora vamos colher os frutos do nosso trabalho.
Desça o cursor para a função `definir_renda()` e altere a linha do input bruto:

### Antes:
```python
renda = float(input("Informe a receita líquida esperada (R$): "))
```

### Agora (Refatorado):
```python
def definir_renda():
    """Solicita e confirma a previsão de renda mensal."""
    print("\n--- Previsão de Renda Mensal ---")
    renda = obter_numero_positivo("Informe a receita líquida esperada (R$): ")
    print(f"Renda prevista atualizada para: R$ {renda:.2f}")
    return renda
```

💬 **O que explicar para a turma:**
* *"Vejam como a função `definir_renda()` ficou limpa e elegante! Ela delegou o trabalho duro de validação para a função `obter_numero_positivo()`. Isso se chama separação de responsabilidades."*

---

## 👁️ Ato 5: Provando que a Memória Guardou o Valor (Opção 4 na `main`)

Desça o cursor até a função `main()`.
Na opção `"4"`, nós tínhamos um stub genérico. Vamos ajustá-lo para que o aluno veja a prova real de que o valor está guardado na variável `renda_prevista`:

```python
        elif opcao == "4":
            print(f"\n[EM CONSTRUÇÃO] Renda atual cadastrada: R$ {renda_prevista:.2f}")
```

🧪 **Bateria Final de Testes com a Turma:**
1. Rode o programa.
2. Digite `4` ➔ Exibe `R$ 0.00` (valor inicial).
3. Digite `1` (Definir Renda).
   - Digite `dez reais` ➔ O sistema avisa: *"Digite um número válido"*.
   - Digite `-800` ➔ O sistema avisa: *"O valor não pode ser negativo"*.
   - Digite `3250.75` ➔ O sistema aceita e confirma!
4. Voltou ao menu principal.
5. Digite `4` novamente ➔ Exibe: `Renda atual cadastrada: R$ 3250.75`!
6. Digite `0` ➔ Programa encerra suavemente.

Parabéns à turma: o valor foi capturado, validado, blindado e mantido na memória da aplicação!

---

## 🏁 Ato 6: Código Completo Consolidado da Etapa 2

```python
"""
Projeto Final: Planejamento Financeiro
Etapa 2: Entrada Segura de Dados e Previsão de Renda
"""

def exibir_menu():
    """Exibe o menu principal de opções para o usuário."""
    print("\n" + "=" * 40)
    print("      PLANEJAMENTO FINANCEIRO")
    print("=" * 40)
    print("1 - Definir Previsão de Renda")
    print("2 - Adicionar Despesa")
    print("3 - Listar Todas as Despesas")
    print("4 - Exibir Balanço e Relatório 50-30-20")
    print("0 - Sair")
    print("=" * 40)


def obter_numero_positivo(mensagem):
    """
    Função reutilizável: solicita um número ao usuário e garante
    que seja um valor numérico válido (float) e não negativo.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            print("Erro: O valor não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um número válido (ex: 1500.50).")


def definir_renda():
    """Solicita e confirma a previsão de renda mensal."""
    print("\n--- Previsão de Renda Mensal ---")
    renda = obter_numero_positivo("Informe a receita líquida esperada (R$): ")
    print(f"Renda prevista atualizada para: R$ {renda:.2f}")
    return renda


def main():
    renda_prevista = 0.0

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            renda_prevista = definir_renda()
        elif opcao == "2":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Adicionar Despesa.")
        elif opcao == "3":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Listar Despesas.")
        elif opcao == "4":
            print(f"\n[EM CONSTRUÇÃO] Renda atual cadastrada: R$ {renda_prevista:.2f}")
        elif opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    main()
```

---

## 🎯 Síntese Pedagógica da Etapa 2

| Linha / Comando no Código | Relação Causa-Efeito | Por que foi escrita dessa forma? |
| :--- | :--- | :--- |
| `renda_prevista = 0.0` antes do `while` | Preservação de Estado. | Se ficasse dentro do `while`, seria reinicializada para zero a cada exibição do menu. |
| `renda_prevista = definir_renda()` na opção 1 | Atribuição de Retorno. | Captura o dado que a função devolveu através do seu `return`. |
| `mensagem` como parâmetro | Reutilização de Código. | Permite que a mesma função valide tanto a renda mensal quanto as despesas da próxima aula. |
| `try / except ValueError` | Blindagem Defensiva. | Impede o fechamento abrupto (*crash*) quando o usuário digita letras ou deixa vazio. |
| `if valor >= 0: return valor` | Regra de Negócio + Saída. | Garante finanças com números positivos e encerra a função dispensando o comando `break`. |
