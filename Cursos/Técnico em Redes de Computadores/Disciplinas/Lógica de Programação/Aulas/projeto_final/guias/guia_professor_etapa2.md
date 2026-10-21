# Guia do Professor – Etapa 2: Entrada Segura de Dados e Previsão de Renda

* **Curso:** Técnico em Redes de Computadores
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Instituição:** Instituto Federal do Ceará (IFCE) – Campus Tauá
* **Metodologia:** *Live Coding Dialogado* (Partindo do código real de `projetinho/main.py` construído na Aula 1, alternando entre `main()`, `definir_renda()` e `obter_numero_positivo()`).
* **Arquivos de Referência:**
  * Ponto de partida da turma: [projetinho/main.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/projetinho/main.py)
  * Gabarito da etapa: [etapas/etapa2_validacao_e_renda.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa2_validacao_e_renda.py)

---

## 🧭 Visão Geral e Estratégia da Aula

> [!IMPORTANT]
> **Ponto de Partida Real:** Na aula anterior, construímos o esqueleto em [projetinho/main.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/projetinho/main.py). Hoje vamos transformar a **Opção 1 ("1 - Cadastrar Receita")** de um simples `print` provisório (*stub*) em uma rotina completa, segura e com persistência de estado em memória.

### Objetivos Pedagógicos desta Aula:
1. **Gerenciamento de Estado:** Entender por que variáveis que guardam dados do sistema (`renda_prevista`) devem morar **antes** do `while True`.
2. **Comunicação entre Funções:** Compreender a diferença entre apenas `printar` um valor na tela e **devolver** o valor com `return` para quem chamou.
3. **Programação Defensiva (`try / except`):** Blindar o software contra erros de digitação (`ValueError`) e regras de negócio inválidas (números negativos).
4. **Reaproveitamento de Código:** Criar uma função especialista (`obter_numero_positivo`) que servirá tanto para a Receita hoje quanto para as Despesas na próxima aula.

---

## 🎬 Ato 0: Revisão Rápida e Refino do Código da Aula 1 (10 min)

Abra o arquivo [projetinho/main.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/projetinho/main.py) no projetor:

```python
def main():
    print("Sistema iniciado com sucesso.")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
```

### 💡 Dica de Mediação 0.1: O pequeno bug do espaço em branco (`.strip()`)
Antes de iniciar a Etapa 2, faça um teste rápido no código atual da turma:
1. Rode o `main.py` e digite `" 1 "` (com um espaço antes ou depois do número 1).
2. O programa cairá no `else: Opção inválida!`.
3. **Pergunte à turma:** *"Eu digitei o número 1! Por que o Python disse que a opção é inválida?"*
4. **Explicação Técnica:** Para o computador, `"1"` é diferente de `" 1"`. Apresente o método `.strip()`, que funciona como uma "tesoura" cortando espaços invisíveis nas pontas do texto:

```python
        opcao = input("Escolha uma opção: ").strip()
```

---

## 🧠 Ato 1: Onde Guardar o Dinheiro? (Escopo e Estado na `main`) (15 min)

### Passo 1.1: Criando a variável de estado
Pergunte aos alunos:
> *"Quando o usuário escolher a opção 1 e digitar que ganha R$ 2.500,00, precisamos guardar esse número na memória para calcular o Balanço na opção 4. Onde criamos essa variável?"*

Adicione na `main()`, **logo acima** do `while True:`:

```python
def main():
    print("Sistema iniciado com sucesso.")
    renda_prevista = 0.0  # Estado inicial da receita na memória

    while True:
```

> [!WARNING]
> **Armadilha Clássica dos Alunos (O Efeito Amnésia):**
> Muitos alunos vão declarar `renda_prevista = 0.0` **dentro** do `while True:` (logo abaixo de `exibir_menu()`).
> * **Como demonstrar:** Explique que tudo dentro do `while True` roda repetidamente a cada volta do menu. Se `renda_prevista = 0.0` estiver lá dentro, toda vez que o menu aparecer na tela, o programa sofre "amnésia" e zera o salário do usuário!
> * **Analogia de Redes:** É como configurar o IP de um roteador na memória RAM volátil e reiniciar a interface a cada comando sem salvar no estado ativo da sessão.

---

## 🔌 Ato 2: Chamando a Função e o Conceito de `return` (20 min)

### Passo 2.1: Substituindo o Stub da Opção 1
Localize o bloco da opção `"1"` na `main()`:

```python
        elif opcao == "1":
            renda_prevista = definir_renda()
```

💬 **O que explicar para a turma:**
* *"Reparem no sinal de igual (`=`). Em programação, o lado direito executa primeiro: o Python pausa a `main()`, viaja até a função `definir_renda()`, coleta o valor que ela devolver e guarda dentro da gaveta `renda_prevista`."*

### Passo 2.2: Construindo a Primeira Versão de `definir_renda()` (Versão Ingênua)
Suba o cursor acima da `main()` e crie a função:

```python
def definir_renda():
    """Solicita e registra a receita líquida esperada no mês."""
    print("\n--- Previsão de Renda Mensal ---")
    renda = float(input("Informe a receita líquida esperada (R$): "))
    print(f"Renda prevista atualizada para: R$ {renda:.2f}")
    return renda
```

### 🔍 Informações Extras sobre Funcionalidades (Para explicar no quadro/projetor):
1. **Por que `float()` e não `int()`?**
   * No mundo financeiro existem centavos (`1500.50`). O `int()` rejeitaria casas decimais ou truncaria valores.
2. **O que faz a f-string `f"... R$ {renda:.2f}"`?**
   * O `f` antes das aspas ativa a interpolação de variáveis entre chaves `{}`.
   * O sufixo `:.2f` significa *Floating point com 2 casas decimais fixas*. Mesmo que o usuário digite `1500`, o Python exibirá `1500.00` como em um extrato bancário real.
3. **O papel vital do `return renda`:**
   * **Demonstração prática recomendada:** Comente temporariamente a linha `# return renda` e mostre que toda função em Python sem `return` devolve `None` (vazio). Sem o `return`, a variável `renda_prevista` na `main()` vira `None` e o dinheiro desaparece quando a função termina!

---

## 💥 Ato 3: Provocando o Crash ao Vivo (A Necessidade de Validação) (15 min)

Execute o programa no projetor e faça dois testes com a participação dos alunos:

1. **Teste de Tipo Inválido:**
   * Escolha a opção `1` e digite `dois mil`, ou apenas aperte `ENTER` sem digitar nada, ou digite `1500,50` (com vírgula).
   * **Resultado:** O programa morre com um erro vermelho assustador:
     `ValueError: could not convert string to float: ...`
2. **Teste de Regra de Negócio Absurda:**
   * Rode novamente, escolha a opção `1` e digite `-5000`.
   * **Resultado:** O programa aceita alegremente: `Renda prevista atualizada para: R$ -5000.00`.

💬 **Pergunta Disparadora para a Turma:**
> *"Um sistema profissional pode quebrar e fechar na cara do cliente porque ele esbarrou em uma letra ou apertou Enter sem querer? E faz sentido alguém planejar o mês com salário negativo de -R$ 5.000?"*

---

## 🛡️ Ato 4: A Função Guardiã (`obter_numero_positivo`) (20 min)

Explique para a turma:
*"Em vez de colocar uma barragem de proteção só dentro de `definir_renda()`, vamos pensar como engenheiros: na próxima aula teremos que pedir o **Valor da Despesa**, que também não pode ter letras nem ser negativo. Então vamos criar uma função especialista que serve para qualquer número positivo do sistema!"*

### Passo 4.1: Escrevendo `obter_numero_positivo(mensagem)`
Suba o cursor acima de `definir_renda()` e construa passo a passo:

```python
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
```

### 🧠 Detalhamento Técnico e Dicas para o Professor:
* **Analogia da Catraca Eletrônica:** O `while True` é uma catraca trancada. O único jeito de passar pela catraca é chegando na linha `return valor`.
* **Por que não precisamos de `break` depois do `return`?**
  * Muitos alunos perguntam: *"Professor, não tem `break` nesse `while True`, não vai ficar infinito?"*.
  * **Explicação:** O comando `return` é mais poderoso que o `break`: enquanto o `break` sai apenas do laço `while`, o `return` **encerra a função inteira imediatamente** e já leva o valor na mão para entregar a quem chamou!
* **Como funciona o par `try / except ValueError`?**
  * O Python tenta executar as linhas dentro do `try`.
  * Se a função `float()` falhar na linha `valor = float(input(mensagem))`, o Python **não executa** o `if valor >= 0` abaixo dele; ele salta imediatamente para o bloco `except ValueError:`, imprime a mensagem amigável e dá uma nova volta no `while True`.

### Passo 4.2: Conectando a Guardiã dentro de `definir_renda()`
Agora atualize a função `definir_renda()` trocando o `float(input(...))` pela chamada da nossa nova função guardiã:

```python
def definir_renda():
    """Solicita e confirma a previsão de renda mensal."""
    print("\n--- Previsão de Renda Mensal ---")
    renda = obter_numero_positivo("Informe a receita líquida esperada (R$): ")
    print(f"Renda prevista atualizada para: R$ {renda:.2f}")
    return renda
```

---

## 👁️ Ato 5: Verificando o Estado na Opção 4 (10 min)

Para provar aos alunos que a variável `renda_prevista` na `main()` realmente guardou o valor após várias voltas do menu, atualize o `print` provisório da **Opção 4** na `main()`:

```python
        elif opcao == "4":
            print(f"\n[EM CONSTRUÇÃO] Funcionalidade de Exibir Balanço 50-30-20 (Receita atual: R$ {renda_prevista:.2f})")
```

🧪 **Roteiro de Teste Final no Projetor:**
1. Inicie o programa e escolha a opção `4` ➔ Mostra `Receita atual: R$ 0.00`.
2. Escolha a opção `1`:
   * Digite `abc` ➔ Barra com `Erro: Digite um número válido`.
   * Digite `-200` ➔ Barra com `Erro: O valor não pode ser negativo`.
   * Digite `3500.5` ➔ Aceita e exibe `R$ 3500.50`.
3. Escolha a opção `4` novamente ➔ Mostra `Receita atual: R$ 3500.50`.

---

## 🌟 Funcionalidades Extras e Dicas Avançadas (Carta na Manga do Professor)

Caso a turma avance rápido ou surjam dúvidas/curiosidades durante a aula, você pode apresentar estas melhorias práticas:

### Extra 1: Aceitar tanto Vírgula quanto Ponto nos Centavos (`.replace(",", ".")`)
* **Contexto:** No Brasil, o teclado numérico usa vírgula (`1500,50`), mas o padrão americano do `float()` exige ponto (`1500.50`). Quando o aluno digita vírgula, o Python lança `ValueError`.
* **Como implementar em 1 linha:**
  ```python
  entrada = input(mensagem).strip().replace(",", ".")
  valor = float(entrada)
  ```
* **Dica Didática:** Mostrar o encadeamento de métodos de string (`.strip().replace(",", ".")`) encanta os alunos porque resolve um incômodo real que eles mesmos sentem ao testar no laboratório!

### Extra 2: Exibir a Receita Atual no Topo do Menu Dinamicamente
* **Contexto:** E se o próprio menu principal já mostrasse quanto de receita está cadastrado no momento?
* **Como fazer:** Passar `renda_prevista` como parâmetro para `exibir_menu(renda_prevista)`:
  ```python
  def exibir_menu(renda_atual):
      print("\n" + "=" * 40)
      print("        Planejamento Financeiro")
      print(f"      [Receita Atual: R$ {renda_atual:.2f}]")
      print("=" * 40)
  ```
* **Valor Pedagógico:** Excelente para reforçar passagem de parâmetro para funções caso algum aluno termine o exercício antes dos colegas.

### Extra 3: Confirmação antes de Sobrescrever uma Receita já Cadastrada
* **Contexto:** Se o usuário já cadastrou `R$ 3000.00` e entra na Opção 1 de novo, podemos avisar qual era o valor anterior antes de alterar.
* **Como fazer:** Passar `renda_prevista` para `definir_renda(renda_atual)` e exibir `if renda_atual > 0: print(f"Valor atual: R$ {renda_atual:.2f}")`.

---

## 🛠️ Guia Rápido de Troubleshooting no Laboratório (Erros mais comuns na tela dos alunos)

| Sintoma na máquina do aluno | Causa Provável | Como orientar sem dar a resposta pronta |
| :--- | :--- | :--- |
| Mostra `R$ None` ou dá `TypeError` ao formatar `:.2f` na Opção 4 | Esqueceu de colocar `return renda` no final de `definir_renda()` ou `return valor` em `obter_numero_positivo()`. | *"Sua função calculou o número, mas entregou de volta na esteira? Olhe a última linha da função."* |
| O usuário digita a renda, mas na Opção 4 continua aparecendo `R$ 0.00` | Na opção `"1"` da `main()`, o aluno chamou `definir_renda()` solto, sem atribuir: `renda_prevista = definir_renda()`. Ou declarou `renda_prevista = 0.0` dentro do `while True`. | *"A função arremessou o valor de volta, mas quem estava lá na `main()` esperando com a luva aberta para guardar na variável?"* |
| Fica preso pedindo número infinitamente mesmo digitando um valor positivo | Esqueceu a indentação do `return valor` dentro do `if valor >= 0:` ou colocou `valor < 0`. | *"Verifique os 4 espaços de recuo abaixo do `if valor >= 0:`."* |
| Erro `NameError: name 'obter_numero_positivo' is not defined` | Errou a grafia do nome da função (ex: `obter_numero_positivos`) ou definiu depois de chamar o `main()` no final do arquivo. | *"Compare letra por letra o nome no `def` com o nome onde você chamou a função."* |
