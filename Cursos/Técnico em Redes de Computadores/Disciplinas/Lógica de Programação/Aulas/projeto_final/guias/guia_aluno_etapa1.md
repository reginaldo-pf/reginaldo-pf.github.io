# Roteiro Prático do Aluno – Etapa 1: Menu Interativo e Controle de Fluxo

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Arquivo de Trabalho:** `projetinho/main.py` (ou `etapas/etapa1_menu_e_fluxo.py`)

---

## 🎯 O que vamos construir hoje?

Hoje daremos o pontapé inicial no desenvolvimento do nosso **Sistema de Planejamento Financeiro Pessoal**!

Nesta primeira etapa, vamos construir a espinha dorsal de um software em modo texto (terminal):

1. **Estrutura Profissional:** Organizar o código em funções modulares usando o ponto de entrada seguro `if __name__ == "__main__":`.
2. **Ciclo de Vida Contínuo:** Manter o programa vivo e aguardando comandos do usuário através do laço `while True`.
3. **Menu Interativo:** Exibir uma moldura visual limpa e reagir a cada opção digitada pelo teclado.
4. **Encerramento Suave:** Garantir que o sistema só feche quando o usuário solicitar explicitamente (opção `0 - Sair`).
5. **Tolerância a Falhas:** Avisar educadamente quando o usuário teclar uma opção inválida, sem fechar nem travar o programa.

---

## 🛠️ Passo a Passo de Construção

### Passo 1: O Ponto de Partida e a Função `main()`

Abra o seu editor (VS Code) com um arquivo novo ou abra o seu arquivo `main.py`.

Vamos começar ensinando ao Python onde o programa deve iniciar. Digite no seu arquivo:

```python
def main():
    """Função principal: controla o ciclo de vida da aplicação."""
    print("Sistema iniciado com sucesso!")


if __name__ == "__main__":
    main()
```

> [!NOTE]
> **Por que usar `if __name__ == "__main__":`?**
>
> O Python cria automaticamente variáveis internas chamadas de *dunder* (com dois sublinhados). Quando você executa o arquivo diretamente no terminal, o interpretador atribui o texto `'__main__'` à variável `__name__`. Esse padrão garante que o script só execute a função `main()` quando você o rodar diretamente, evitando execuções acidentais caso ele seja importado por outro módulo no futuro.

---

### Passo 2: Mantendo o Software Vivo (`while True`)

Se você rodar o script agora (`python main.py`), ele exibe a mensagem e **encerra imediatamente**. Um sistema interativo precisa continuar rodando até que o usuário decida sair!

Atualize a sua função `main()` adicionando o laço de repetição:

```python
def main():
    """Função principal: controla o ciclo de vida da aplicação."""
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")

    while True:
        pass  # comando temporário para não quebrar a sintaxe enquanto preparamos a tela
```

> [!TIP]
> **O que é o `pass`?**
>
> Em Python, blocos de código (como `while`, `if` ou `def`) não podem ficar vazios. O comando `pass` é apenas uma instrução nula que serve de "marcador de posição" temporário.

---

### Passo 3: Criando a Função Especialista do Menu (`exibir_menu`)

Para não poluir a função `main()` com vários comandos de impressão, vamos separar a responsabilidade visual em uma função exclusiva.

Acima da função `main()`, adicione a função `exibir_menu()`:

```python
def exibir_menu():
    """Exibe o menu textual com as opções disponíveis do sistema."""
    print("\n" + "=" * 40)
    print("      PLANEJAMENTO FINANCEIRO")
    print("=" * 40)
    print("0 - Sair")
    print("=" * 40)
```

> [!NOTE]
> **Dica de Formatação:**
>
> A expressão `"=" * 40` multiplica o caractere por 40, desenhando uma linha divisória perfeita no console sem precisarmos digitar 40 sinais de igual manualmente. O `\n` pula uma linha no início para afastar o menu do comando anterior.

---

### Passo 4: Conectando o Menu e a Opção de Saída Segura

Agora voltamos para a função `main()` para chamar o menu, ler a escolha do usuário e implementar a alavanca de parada (`break`):

```python
def main():
    """Função principal: controla o ciclo de vida da aplicação."""
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
```

> [!IMPORTANT]
> **O poder do `.strip()`:**
>
> A função `.strip()` corta espaços em branco acidentais antes e depois do texto digitado. Se você teclar `" 0 "` com espaço antes ou depois, o Python limpa para `"0"`, evitando que a opção seja rejeitada injustamente.
>
> O comando `break` interrompe imediatamente o laço `while True` e finaliza a execução.

---

### Passo 5: Protegendo Contra Opções Inválidas (`else`)

E se o usuário teclar `9`, `teste` ou apertar Enter vazio? O sistema deve alertar educadamente em vez de ficar mudo.

Adicione o desvio `else:` logo após o `if opcao == "0":`:

```python
        if opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 4.")
```

---

### Passo 6: Expandindo o Menu com Stubs (Desenvolvimento Incremental)

Agora que o esqueleto do programa está protegido, vamos adicionar as opções de negócio do nosso sistema.

#### 6.1 Atualizar o Menu

No topo do arquivo, atualize a função `exibir_menu()`:

```python
def exibir_menu():
    """Exibe o menu textual com as opções disponíveis do sistema."""
    print("\n" + "=" * 40)
    print("      PLANEJAMENTO FINANCEIRO")
    print("=" * 40)
    print("1 - Definir Previsão de Renda")
    print("2 - Adicionar Despesa")
    print("3 - Listar Todas as Despesas")
    print("4 - Exibir Balanço e Relatório 50-30-20")
    print("0 - Sair")
    print("=" * 40)
```

#### 6.2 Espelhar as Opções na `main()`

Na função `main()`, espelhe cada opção usando ramos `elif` com mensagens de reserva (*stubs*):

```python
def main():
    """Função principal: controla o ciclo de vida da aplicação."""
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Definir Renda.")
        elif opcao == "2":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Adicionar Despesa.")
        elif opcao == "3":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Listar Despesas.")
        elif opcao == "4":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Relatório e Balanço.")
        elif opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 4.")
```

---

## 🧪 Hora de Testar! (Checklist de Validação)

Execute o seu script no terminal (`python main.py`) e teste os comportamentos abaixo:

* [ ] **Teste 1 (Layout do Menu):** O cabeçalho com linhas divisórias aparece limpo na tela.
* [ ] **Teste 2 (Tratamento de Entradas Inválidas):** Digite `8`, tecle Enter vazio ou digite `abc`. O programa deve exibir `Opção inválida! Digite um número de 0 a 4.` e reapresentar o menu.
* [ ] **Teste 3 (Stubs das Opções 1 a 4):** Ao escolher `1`, `2`, `3` ou `4`, o sistema confirma que a funcionalidade está em construção e não fecha.
* [ ] **Teste 4 (Encerramento Suave):** Ao digitar `0`, o sistema despede-se e fecha limpo, retornando o controle ao terminal.

---

## 🆘 Problemas Comuns (Deu erro? Confira aqui!)

1. **O menu fica se repetindo infinitamente na tela sem esperar eu digitar:**
   * Verifique se você não esqueceu a linha `opcao = input(...)` dentro do bloco `while True:`.
2. **O programa fecha logo após a primeira opção que eu escolho:**
   * Verifique se você não deixou um comando `break` solto dentro do `while` fora da opção `0`.
3. **Digitei 0 mas o programa não encerra:**
   * Certifique-se de que a comparação é com texto entre aspas (`if opcao == "0":`) e que dentro do bloco há o comando `break`.

---

## 🏁 Código Consolidado da Etapa 1

```python
"""
Projeto Final: Planejamento Financeiro
Etapa 1: Estrutura do Programa, Loop Principal e Menu de Opções
"""

def exibir_menu():
    """Exibe o menu textual com as opções disponíveis do sistema."""
    print("\n" + "=" * 40)
    print("      PLANEJAMENTO FINANCEIRO")
    print("=" * 40)
    print("1 - Definir Previsão de Renda")
    print("2 - Adicionar Despesa")
    print("3 - Listar Todas as Despesas")
    print("4 - Exibir Balanço e Relatório 50-30-20")
    print("0 - Sair")
    print("=" * 40)


def main():
    """Função principal: controla o ciclo de vida da aplicação."""
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Definir Renda.")
        elif opcao == "2":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Adicionar Despesa.")
        elif opcao == "3":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Listar Despesas.")
        elif opcao == "4":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Relatório e Balanço.")
        elif opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    main()
```

---

## 🚀 Desafios Extras (Para quem terminar antes!)

* **Desafio 1 (Personalização):** Solicite o nome do usuário antes do `while True` e exiba uma saudação personalizada acima do menu: `print(f"Olá, {nome}! Bem-vindo ao seu Planejador Financeiro.")`.
* **Desafio 2 (Opção Limpar Tela):** Descubra como usar o comando `os.system("clear")` (Linux) ou `os.system("cls")` (Windows) para limpar a tela do terminal a cada nova exibição do menu!
