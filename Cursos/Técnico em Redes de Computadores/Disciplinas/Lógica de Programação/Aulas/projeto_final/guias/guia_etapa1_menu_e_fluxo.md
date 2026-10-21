# Guia de Aula Interativo Linha a Linha: Etapa 1 – Menu e Controle de Fluxo

* **Curso:** Técnico em Redes de Computadores
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Instituição:** Instituto Federal do Ceará (IFCE) – Campus Tauá
* **Metodologia:** *Live Coding Dialogado* (Construção alternada entre funções, iniciando pelo ponto de entrada `main`).
* **Código de Apoio:** [etapas/etapa1_menu_e_fluxo.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa1_menu_e_fluxo.py)

---

## 🧭 Como Usar Este Guia em Sala de Aula

> [!IMPORTANT]
> **Regra de Ouro da Aula:** Não copie e cole blocos prontos. Este roteiro foi desenhado para ser digitado na frente dos alunos, linha por linha, alternando intencionalmente entre a função `main()` e a função `exibir_menu()`. A cada linha adicionada, faça uma pergunta à turma, mostre o erro ou o comportamento no terminal, e justifique a necessidade daquela linha específica na aplicação.

---

## 🎬 Ato 0: O Ponto de Partida e o Padrão de Execução (`if __name__`)

Abra o VS Code ou editor no projetor com um arquivo novo em branco: `etapa1_menu_e_fluxo.py`.

### Passo 0.1: O Bloco de Execução Principal
Pergunte aos alunos: *"Por onde o interpretador Python começa a ler nosso script quando o executamos pelo terminal?"*.
Digite no final do arquivo:

```python
if __name__ == "__main__":
    main()
```

💬 **O que explicar para a turma:**
* *"O interpretador do Python define automaticamente variáveis internas especiais com dois sublinhados (chamadas de dunder). Uma delas é a `__name__`."*
* *"Quando você clica em Play ou digita `python etapa1.py`, o próprio interpretador atribui o valor `'__main__'` a essa variável."*
* *"Essa linha diz: 'Se este arquivo está sendo executado diretamente pelo usuário, comece chamando a função principal `main()`'."*

---

### Passo 0.2: A Função `main()`
Suba o cursor para cima do `if` e digite:

```python
def main():
    print("Sistema iniciado com sucesso!")
```

💬 **O que explicar para a turma:**
* *"A palavra-chave `def` ensina uma nova rotina ao Python. Estamos criando a função `main()`, que será o maestro de todo o nosso sistema."*

🧪 **Teste com a Turma (Executar agora):**
Execute no terminal: `python etapa1_menu_e_fluxo.py`.
* Saída esperada:
  ```text
  Sistema iniciado com sucesso!
  ```
* Mostre que o script executou uma única linha e **morreu**.
* Pergunta disparadora: *"Um sistema de console como o Cisco IOS ou o terminal do Linux morre após exibir a primeira mensagem? Não! Ele fica esperando. Como manter nosso programa vivo?"*

---

## 🔄 Ato 1: O Ciclo de Vida da Aplicação (`while True`)

### Passo 1.1: O Loop Contínuo
Na função `main()`, substitua o print pelo laço de repetição:

```python
def main():
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")
    
    while True:
        pass  # comando temporario para o Python nao reclamar de bloco vazio
```

💬 **O que explicar para a turma:**
* *"O `while True:` cria uma repetição cuja condição é sempre verdadeira. Isso significa que tudo o que estiver identado dentro deste bloco rodará em loop contínuo, mantendo a aplicação viva."*
* *"O comando `pass` é apenas um marcador de posição temporário para evitar erro de sintaxe enquanto não escrevemos a lógica."*

---

## 🖥️ Ato 2: A Primeira Necessidade – O Menu Visual (`exibir_menu`)

### Passo 2.1: Por que Criar uma Função Externa?
Na `main()`, comente: *"Dentro do `while`, precisamos mostrar as opções para o usuário. Poderíamos colocar 10 prints aqui dentro? Poderíamos, mas a função `main()` ficaria enorme e poluída. Vamos separar a responsabilidade visual em uma função especialista!"*

Suba o cursor para o topo do arquivo (acima da `main`) e digite:

```python
def exibir_menu():
    """Exibe o menu textual com as opções disponíveis do sistema."""
    print("\n" + "=" * 40)
    print("      PLANEJAMENTO FINANCEIRO")
    print("=" * 40)
```

💬 **O que explicar para a turma:**
* *"O `\n` pula uma linha no início para não colar no texto anterior do terminal."*
* *"A expressão `"=" * 40` multiplica a string por 40, desenhando uma linha divisória perfeita sem precisarmos digitar 40 sinais de igual manualmente."*

---

### Passo 2.2: Conectando o Menu dentro da `main()`
Agora desça o cursor de volta para a função `main()` e substitua o `pass` pela chamada da função:

```python
def main():
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")
    
    while True:
        exibir_menu()
        break  # colocamos break apenas para testar sem travar a tela agora!
```

🧪 **Teste com a Turma (Executar agora):**
* Execute o script.
* O cabeçalho formatado deve aparecer na tela e o programa sai por causa do `break`.
* Explique: *"Agora que a moldura visual funciona, precisamos de opções reais para o usuário escolher!"*

---

## 🚪 Ato 3: A Opção de Saída ("0 - Sair") – Alternando Entre Funções

> [!TIP]
> **Princípio Pedagógico:** Antes de ensinar o usuário a entrar nas opções, ensine o sistema a sair com segurança!

### Passo 3.1: Adicionar a Opção 0 no Menu
Suba o cursor para a função `exibir_menu()` e adicione a opção de saída:

```python
def exibir_menu():
    """Exibe o menu textual com as opções disponíveis do sistema."""
    print("\n" + "=" * 40)
    print("      PLANEJAMENTO FINANCEIRO")
    print("=" * 40)
    print("0 - Sair")
    print("=" * 40)
```

---

### Passo 3.2: Capturar a Escolha na `main()`
Desça o cursor imediatamente para a `main()`. Remova aquele `break` provisório e capture o input:

```python
def main():
    print("Bem-vindo ao Sistema de Planejamento Financeiro!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
```

💬 **O que explicar para a turma sobre o `.strip()`:**
* *"O método `.strip()` elimina espaços em branco antes e depois do texto. Se o usuário digitar `' 0 '` por engano, ele é limpo para `'0'`, evitando rejeição indevida."*

---

### Passo 3.3: Reagir à Opção "0" na `main()`
Logo abaixo da captura da opção na `main()`, crie a condicional de encerramento:

```python
        if opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
```

💬 **O que explicar para a turma:**
* *"Notem a relação direta: a linha `print('0 - Sair')` no menu gerou a linha `if opcao == '0':` na `main()`."*
* *"O comando `break` interrompe imediatamente o laço `while True`. É a nossa alavanca de emergência para desligar o motor do sistema!"*

🧪 **Teste com a Turma (Executar agora):**
1. Rode o programa.
2. Digite `0` ➔ O programa despede-se e fecha suavemente.
3. Rode de novo e digite `qualquer coisa` ➔ O menu reaparece em loop!

---

## 🛡️ Ato 4: A Proteção Contra Entradas Inválidas (`else`)

Pergunte aos alunos: *"Se o usuário digitar `'9'`, o que nosso código faz agora? Ele simplesmente repete o menu sem dizer nada. O usuário fica sem saber se o sistema travou ou se ele digitou errado!"*.

### Passo 4.1: Adicionar o `else` na `main()`
Na `main()`, adicione o desvio padrão logo após o `if`:

```python
        if opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 4.")
```

🧪 **Teste com a Turma (Executar agora):**
* Digite `8`, tecle `ENTER` vazio ou digite `teste`.
* O sistema alerta educadamente: *"Opção inválida!"* e reapresenta o menu.
* Destaque: *"Nosso sistema já é tolerante a falhas básicas!"*

---

## ➕ Ato 5: A Opção 1 – Definir Previsão de Renda

Agora faremos a alternância guiada para a primeira funcionalidade de negócio.

### Passo 5.1: Escrever a Opção no Menu
Suba o cursor para `exibir_menu()` e insira a Opção 1 antes da opção 0:

```python
def exibir_menu():
    """Exibe o menu textual com as opções disponíveis do sistema."""
    print("\n" + "=" * 40)
    print("      PLANEJAMENTO FINANCEIRO")
    print("=" * 40)
    print("1 - Definir Previsão de Renda")
    print("0 - Sair")
    print("=" * 40)
```

---

### Passo 5.2: Adicionar a Resposta na `main()`
Desça imediatamente para a `main()`.
* Mostre aos alunos: a opção `"0"` era um `if`. Agora que temos a opção `"1"`, ela assume o `if`, e a opção `"0"` vira `elif`!

```python
        if opcao == "1":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Definir Renda.")
        elif opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 4.")
```

💬 **O que explicar para a turma sobre Stubs:**
* *"Um 'Stub' é um código de reserva. Nós ainda não construímos a lógica matemática da renda, mas o esqueleto do sistema já reconhece a opção sem travar. Isso é desenvolvimento incremental!"*

🧪 **Teste com a Turma:**
* Digite `1` ➔ Surge: `[EM CONSTRUÇÃO] Funcionalidade de Definir Renda.` e o menu volta.

---

## 🚀 Ato 6: Completando o Menu (Opções 2, 3 e 4)

Peça para os alunos ditarem para você o que deve ser escrito no menu e como isso se reflete na `main()`.

### Passo 6.1: Expandir o Menu
Suba para `exibir_menu()` e complete todas as opções:

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

---

### Passo 6.2: Expandir os Ramos `elif` na `main()`
Desça para a `main()` e mapeie cada linha nova com seu respectivo `elif`:

```python
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

## 🏁 Ato 7: Código Final da Etapa 1 e Validação Geral

Projete o código completo consolidado na tela para os alunos conferirem a identação:

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

## 🎯 Síntese Pedagógica da Etapa 1

| Linha / Comando no Código | Por que foi escrita? | O que acontece se removermos? |
| :--- | :--- | :--- |
| `if __name__ == "__main__":` | Garante execução direta e padronizada. | O script ainda roda sem ela se chamarmos `main()`, mas perde boas práticas profissionais de modularização. |
| `while True:` | Mantém a aplicação viva aguardando comandos. | O programa executa uma opção e fecha imediatamente. |
| `.strip()` no input | Remove espaços acidentais antes e depois. | Se o usuário digitar `" 1 "`, o sistema diz que a opção é inválida. |
| `break` na opção `"0"` | Interrompe o loop infinito da aplicação. | O programa nunca fecha e fica preso no terminal. |
| `else:` na árvore de opções | Trata entradas não previstas. | O programa repete o menu em silêncio quando o usuário erra a tecla. |
