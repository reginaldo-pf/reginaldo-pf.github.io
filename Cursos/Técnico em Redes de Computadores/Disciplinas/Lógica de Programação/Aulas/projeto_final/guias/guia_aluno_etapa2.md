# Roteiro Prático do Aluno – Etapa 2: Entrada Segura e Previsão de Renda

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Arquivo de Trabalho:** `projetinho/main.py`

---

## 🎯 O que vamos construir hoje?

Na **Etapa 1**, criamos o menu interativo e o loop principal do nosso **Sistema de Planejamento Financeiro**. Porém, ao escolher a opção `1`, o sistema apenas exibia uma mensagem dizendo que a funcionalidade estava em construção.

Hoje vamos dar vida à **Opção 1 (Cadastrar Receita)**! Ao final desta aula, seu programa será capaz de:
1. Ler e armazenar a receita mensal do usuário na memória do programa.
2. Bloquear valores negativos (afinal, não existe salário negativo!).
3. Proteger o sistema para **não travar com erro vermelho** caso alguém digite letras ou símbolos por engano.

---

## 🔍 Antes de Começar: Revise seu Código da Etapa 1

Abra o seu arquivo `main.py`. Ele deve estar parecido com este:

```python
def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n" + "=" * 40)
    print("        Planejamento Financeiro")
    print("=" * 40)
    print("1 - Cadastrar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar todas as despesas")
    print("4 - Exibir Balanço 50-30-20")
    print("0 - Sair")
    print("=" * 40)


def main():
    print("Sistema iniciado com sucesso.")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "4":
            print("\n Funcionalidade de Exibir Balanço 50-30-20")
        elif opcao == "3":
            print("\n Funcionalidade de Listar Despesas")
        elif opcao == "2":
            print("\n Funcionalidade de Adicionar Despesa")
        elif opcao == "1":
            print("\n Funcionalidade de Definir receita")
        elif opcao == "0":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    main()
```

> [!TIP]
> **Dica Importante:** Veja se a linha do `input` possui o `.strip()` no final: `opcao = input("Escolha uma opção: ").strip()`. Ele remove espaços vazios acidentais caso o usuário digite `" 1 "` com espaço!

---

## 🛠️ Passo a Passo de Construção

### Passo 1: Criar a variável para guardar a Receita na `main()`

Precisamos de uma variável para guardar o valor da receita durante toda a execução do programa.

1. Localize a função `def main():`.
2. **Antes** do `while True:`, crie a variável `renda_prevista = 0.0`:

```python
def main():
    print("Sistema iniciado com sucesso.")
    renda_prevista = 0.0
    
    while True:
```

> [!WARNING]
> **Cuidado com a armadilha!** A linha `renda_prevista = 0.0` **DEVE** ficar fora (acima) do `while True:`. Se você colocá-la dentro do `while`, o seu programa vai zerar a receita toda vez que o menu aparecer na tela!

---

### Passo 2: Criar a Função Guardiã (`obter_numero_positivo`)

Se usarmos apenas `float(input())` e o usuário digitar uma letra (como `"abc"`), o Python fecha o programa com um erro chamado `ValueError`. Além disso, o usuário poderia digitar um número negativo como `-500`.

Vamos criar uma função especialista que funciona como uma **catraca de segurança**: ela só deixa passar números válidos e positivos!

Acima da função `main()`, adicione a função abaixo:

```python
def obter_numero_positivo(mensagem):
    """
    Solicita um número ao usuário e garante que seja
    um valor numérico válido (float) e não negativo.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            print("Erro: O valor não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um número válido (ex: 1500.50).")
```

#### 🧠 Entendendo como essa função trabalha:
* **`try:` (Tente):** O Python tenta converter o texto digitado para número decimal (`float`).
* **`if valor >= 0: return valor`:** Se deu certo e o número não é negativo, o comando `return` devolve o número imediatamente e encerra a função!
* **`except ValueError:`:** Se o usuário digitou letras ou símbolos inválidos, em vez de o programa quebrar, ele pula para cá, exibe a mensagem de erro amigável e o `while True` repete a pergunta.

---

### Passo 3: Criar a Função `definir_renda()`

Agora vamos criar a função responsável pela **Opção 1** do nosso menu. Ela vai usar a nossa função guardiã do Passo 2!

Logo abaixo de `obter_numero_positivo`, digite:

```python
def definir_renda():
    """Solicita e confirma a previsão de renda mensal."""
    print("\n--- Previsão de Renda Mensal ---")
    renda = obter_numero_positivo("Informe a receita líquida esperada (R$): ")
    print(f"Renda prevista atualizada para: R$ {renda:.2f}")
    return renda
```

> [!NOTE]
> **O que significa `:.2f`?**
> Dentro de uma *f-string* (`f"..."`), colocar `{renda:.2f}` formata o número sempre com **2 casas decimais** (centavos). Exemplo: se você digitar `2000`, ele mostrará `R$ 2000.00`.

---

### Passo 4: Conectar a Função na `main()`

Agora precisamos ligar os fios! Na função `main()`, localize o `elif opcao == "1":` e substitua o `print` antigo pela chamada da nossa nova função.

Aproveite também para atualizar o `print` da **opção `"4"`** para conseguirmos ver se a receita ficou realmente salva na memória:

```python
        if opcao == "4":
            print(f"\n[EM CONSTRUÇÃO] Receita atual cadastrada: R$ {renda_prevista:.2f}")
        elif opcao == "3":
            print("\n Funcionalidade de Listar Despesas")
        elif opcao == "2":
            print("\n Funcionalidade de Adicionar Despesa")
        elif opcao == "1":
            renda_prevista = definir_renda()
```

---

## 🧪 Hora de Testar! (Checklist de Validação)

Execute o seu programa no terminal (`python main.py`) e faça os testes abaixo marcando cada etapa:

- [ ] **Teste 1 (Valor Inicial):** Assim que abrir o programa, escolha a opção `4`. Ele deve mostrar `Receita atual cadastrada: R$ 0.00`.
- [ ] **Teste 2 (Proteção contra Letras):** Escolha a opção `1` e digite `mil reais` ou `abc`. O programa **não pode fechar com erro**; ele deve exibir `Erro: Digite um número válido (ex: 1500.50).` e pedir o valor novamente.
- [ ] **Teste 3 (Proteção contra Negativos):** Ainda na opção `1`, digite `-300`. Ele deve exibir `Erro: O valor não pode ser negativo.` e pedir o valor novamente.
- [ ] **Teste 4 (Cadastro Correto):** Digite `2850.5` e aperte Enter. Ele deve confirmar `Renda prevista atualizada para: R$ 2850.50` e voltar ao menu.
- [ ] **Teste 5 (Memória Persistente):** No menu principal, escolha a opção `4` novamente. Agora ele deve mostrar `Receita atual cadastrada: R$ 2850.50`!

---

## 🆘 Problemas Comuns (Deu erro? Confira aqui!)

1. **Apareceu `R$ None` ou erro ao escolher a opção 4:**
   * Verifique se você não esqueceu de escrever `return renda` na última linha de `definir_renda()` ou `return valor` dentro de `obter_numero_positivo()`.
2. **Cadastrei a renda na opção 1, mas na opção 4 continua mostrando `R$ 0.00`:**
   * Verifique se na opção `"1"` da `main()` você escreveu `renda_prevista = definir_renda()` (com o sinal de `=`).
   * Verifique se `renda_prevista = 0.0` está realmente **acima** do `while True:`.

---

## 🚀 Desafios Extras (Para quem terminar antes!)

Terminou todos os testes acima e funcionou perfeitamente? Tente implementar estas melhorias no seu código:

### 🌟 Desafio 1: Aceitar Vírgula nos Centavos
No Brasil, costumamos digitar `1500,50` com vírgula em vez de ponto (`1500.50`). Mas o `float()` do Python só entende ponto!
* **Missão:** Dentro de `obter_numero_positivo`, use o método `.replace(",", ".")` logo após o `input(mensagem)` para trocar automaticamente qualquer vírgula por ponto antes de converter para `float`!

### 🌟 Desafio 2: Mostrar a Receita no Cabeçalho do Menu
Que tal exibir o valor da receita atual diretamente no topo do menu principal toda vez que ele aparece na tela?
* **Missão:** Modifique a função `exibir_menu(renda_atual)` para receber a variável `renda_prevista` como parâmetro e mostrar uma linha `[Receita Atual: R$ 0.00]` no cabeçalho do menu!
