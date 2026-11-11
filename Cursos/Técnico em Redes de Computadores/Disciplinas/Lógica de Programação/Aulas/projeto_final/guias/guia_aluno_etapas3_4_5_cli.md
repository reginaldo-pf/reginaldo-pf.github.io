# Roteiro Prático do Aluno – Etapas 3, 4 e 5: Despesas, Tabela e Relatório 50-30-20

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Arquivo de Trabalho:** `etapas/etapa5_projeto_completo.py` (ou `projetinho/main.py`)

---

## 🎯 O que vamos construir nestas etapas?

Nas etapas anteriores, criamos o menu interativo e a funcionalidade de cadastrar a **Receita Prevista** com validação de dados.

Agora, vamos implementar o restante do sistema em modo terminal:

1. **Etapa 3 (Aula 3):** Modelar cada despesa como um **Dicionário (`dict`)** e adicioná-la a uma **Lista Dinâmica (`list`)** com `.append()`.
2. **Etapa 4 (Aula 4):** Exibir todas as despesas em formato de **Tabela Perfeitamente Alinhada** no console usando o laço `for`, `enumerate()` e *f-strings* formatadas.
3. **Etapa 5 (Aula 5):** Construir a inteligência financeira do software: somar os gastos por categoria com **variáveis acumuladoras**, calcular o saldo restante e emitir um **diagnóstico de conformidade com a Regra 50-30-20**.

---

## 🧱 ETAPA 3: Cadastro de Despesas (Dicionários e Listas)

### Passo 3.1: Criar a Lista na `main()`

Na função `main()`, logo abaixo de `renda_prevista = 0.0` (antes do `while True:`), crie a lista vazia:

```python
def main():
    renda_prevista = 0.0
    despesas = []  # Lista que guardará os dicionários de cada gasto
    
    while True:
```

---

### Passo 3.2: Criar a Função `adicionar_despesa(despesas)`

Acima da `main()`, implemente a função que coleta e valida a descrição, o valor e a categoria do gasto:

```python
def adicionar_despesa(despesas):
    """
    Cadastra uma despesa na forma de dicionário e adiciona à lista despesas.
    """
    print("\n--- Nova Despesa ---")

    # 1. Validação da descrição
    descricao = input("Descrição da despesa: ").strip()
    while not descricao:
        print("Erro: A descrição não pode ficar vazia.")
        descricao = input("Descrição da despesa: ").strip()

    # 2. Reutilização da função de validação de valor
    valor = obter_numero_positivo("Valor da despesa (R$): ")

    # 3. Submenu de seleção da categoria
    print("\nSelecione a Categoria:")
    print("1 - Essencial (Moradia, Contas, Alimentação, Saúde)")
    print("2 - Estilo de Vida (Lazer, Restaurantes, Assinaturas)")
    print("3 - Reserva / Metas (Poupança, Quitação de Dívidas)")

    categoria_nome = ""
    while True:
        opcao = input("Opção (1-3): ").strip()
        if opcao == "1":
            categoria_nome = "Essencial"
            break
        elif opcao == "2":
            categoria_nome = "Estilo de Vida"
            break
        elif opcao == "3":
            categoria_nome = "Reserva"
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

    # 4. Criação do registro estruturado (Dicionário)
    item = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria_nome
    }

    # 5. Armazenamento na lista principal
    despesas.append(item)
    print(f"Despesa '{descricao}' registrada com sucesso! (Total cadastradas: {len(despesas)})")
```

---

### Passo 3.3: Ligar a Opção 2 na `main()`

Na `main()`, substitua o print provisório pela chamada da função:

```python
        elif opcao == "2":
            adicionar_despesa(despesas)
```

---

## 📋 ETAPA 4: Listagem Formatada em Tabela

### Passo 4.1: Criar a Função `listar_despesas(despesas)`

Acima da `main()`, implemente a função de exibição tabular com cláusula de guarda e alinhamento de colunas:

```python
def listar_despesas(despesas):
    """
    Exibe todas as despesas cadastradas em uma tabela organizada no console.
    """
    print("\n--- Lista de Despesas Registradas ---")

    # 1. Cláusula de guarda: verifica se a lista está vazia
    if not despesas:
        print("Nenhuma despesa cadastrada até o momento.")
        return

    # 2. Cabeçalho com larguras fixas
    print(f"{'#':<4} {'Descrição':<25} {'Categoria':<15} {'Valor (R$)'}")
    print("-" * 55)

    # 3. Iteração com enumerate para exibir índice e dados
    for indice, item in enumerate(despesas, start=1):
        print(f"{indice:<4} {item['descricao']:<25} {item['categoria']:<15} R$ {item['valor']:>8.2f}")
```

> [!TIP]
> **Entendendo as f-strings alinhadas:**
>
> * `indice:<4`: Alinha o número à esquerda em 4 caracteres.
> * `item['descricao']:<25`: Alinha o texto à esquerda reservando 25 espaços.
> * `item['categoria']:<15`: Alinha a categoria em 15 espaços.
> * `item['valor']:>8.2f`: Alinha o número à direita com 2 casas decimais.

---

### Passo 4.2: Ligar a Opção 3 na `main()`

Na `main()`, conecte a opção `"3"`:

```python
        elif opcao == "3":
            listar_despesas(despesas)
```

---

## 🧠 ETAPA 5: Relatório Analítico e Regra 50-30-20

### Passo 5.1: Criar a Função `exibir_relatorio(renda_prevista, despesas)`

Acima da `main()`, construa a lógica de agregação por categoria e o diagnóstico:

```python
def exibir_relatorio(renda_prevista, despesas):
    """
    Calcula os totais por categoria, o saldo líquido e a conformidade com a regra 50-30-20.
    """
    print("\n--- Balanço e Análise Orçamentária ---")
    if renda_prevista == 0:
        print("Aviso: Defina a previsão de renda na opção 1 para um diagnóstico completo.")

    # 1. Acumuladores condicionais por categoria
    total_essencial = 0.0
    total_estilo_vida = 0.0
    total_reserva = 0.0

    for item in despesas:
        if item["categoria"] == "Essencial":
            total_essencial += item["valor"]
        elif item["categoria"] == "Estilo de Vida":
            total_estilo_vida += item["valor"]
        elif item["categoria"] == "Reserva":
            total_reserva += item["valor"]

    # 2. Cálculos gerais
    total_gasto = total_essencial + total_estilo_vida + total_reserva
    saldo_restante = renda_prevista - total_gasto

    # 3. Resumo financeiro formatado
    print(f"Renda Prevista : R$ {renda_prevista:>10.2f}")
    print(f"Total Despesas : R$ {total_gasto:>10.2f}")
    print(f"Saldo Restante : R$ {saldo_restante:>10.2f}")

    # 4. Diagnóstico de saúde financeira
    if saldo_restante < 0:
        print("ALERTA: O orçamento está deficitário! Os gastos superam as entradas.")
    elif saldo_restante == 0:
        print("Atenção: Saldo zerado. Não sobrou margem de segurança.")
    else:
        print("Situação: Orçamento com superávit.")

    # 5. Avaliação percentual da regra 50-30-20 (com defesa contra divisão por zero)
    if renda_prevista > 0:
        pct_essencial = (total_essencial / renda_prevista) * 100
        pct_estilo = (total_estilo_vida / renda_prevista) * 100
        pct_reserva = (total_reserva / renda_prevista) * 100

        print("\nDiagnóstico de Aderência (Regra 50-30-20):")
        print(f"- Essenciais    : {pct_essencial:5.1f}% (Meta recomendada: até 50%)")
        print(f"- Estilo de Vida: {pct_estilo:5.1f}% (Meta recomendada: até 30%)")
        print(f"- Reserva       : {pct_reserva:5.1f}% (Meta recomendada: no mínimo 20%)")
```

---

### Passo 5.2: Ligar a Opção 4 na `main()`

Na `main()`, conecte a opção `"4"`:

```python
        elif opcao == "4":
            exibir_relatorio(renda_prevista, despesas)
```

---

## 🏁 Código Completo Consolidado (Versão Final da Etapa 5)

```python
"""
Projeto Final: Planejamento Financeiro
Etapa 5: Inteligência de Negócio e Relatório Analítico (Regra 50-30-20)
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
    """Garante que o valor inserido seja um float válido e positivo."""
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


def adicionar_despesa(despesas):
    """Cadastra uma despesa na lista."""
    print("\n--- Nova Despesa ---")
    descricao = input("Descrição da despesa: ").strip()
    while not descricao:
        print("Erro: A descrição não pode ficar vazia.")
        descricao = input("Descrição da despesa: ").strip()

    valor = obter_numero_positivo("Valor da despesa (R$): ")

    print("\nSelecione a Categoria:")
    print("1 - Essencial (Moradia, Contas, Alimentação, Saúde)")
    print("2 - Estilo de Vida (Lazer, Restaurantes, Assinaturas)")
    print("3 - Reserva / Metas (Poupança, Quitação de Dívidas)")

    categoria_nome = ""
    while True:
        opcao = input("Opção (1-3): ").strip()
        if opcao == "1":
            categoria_nome = "Essencial"
            break
        elif opcao == "2":
            categoria_nome = "Estilo de Vida"
            break
        elif opcao == "3":
            categoria_nome = "Reserva"
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

    item = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria_nome
    }
    despesas.append(item)
    print(f"Despesa '{descricao}' registrada com sucesso!")


def listar_despesas(despesas):
    """Exibe todas as despesas cadastradas em uma tabela organizada."""
    print("\n--- Lista de Despesas Registradas ---")
    if not despesas:
        print("Nenhuma despesa cadastrada até o momento.")
        return

    print(f"{'#':<4} {'Descrição':<25} {'Categoria':<15} {'Valor (R$)'}")
    print("-" * 55)
    for indice, item in enumerate(despesas, start=1):
        print(f"{indice:<4} {item['descricao']:<25} {item['categoria']:<15} R$ {item['valor']:>8.2f}")


def exibir_relatorio(renda_prevista, despesas):
    """Calcula os totais e exibe o relatório 50-30-20."""
    print("\n--- Balanço e Análise Orçamentária ---")
    if renda_prevista == 0:
        print("Aviso: Defina a previsão de renda na opção 1 para um diagnóstico completo.")

    total_essencial = 0.0
    total_estilo_vida = 0.0
    total_reserva = 0.0

    for item in despesas:
        if item["categoria"] == "Essencial":
            total_essencial += item["valor"]
        elif item["categoria"] == "Estilo de Vida":
            total_estilo_vida += item["valor"]
        elif item["categoria"] == "Reserva":
            total_reserva += item["valor"]

    total_gasto = total_essencial + total_estilo_vida + total_reserva
    saldo_restante = renda_prevista - total_gasto

    print(f"Renda Prevista : R$ {renda_prevista:>10.2f}")
    print(f"Total Despesas : R$ {total_gasto:>10.2f}")
    print(f"Saldo Restante : R$ {saldo_restante:>10.2f}")

    if saldo_restante < 0:
        print("ALERTA: O orçamento está deficitário! Os gastos superam as entradas.")
    elif saldo_restante == 0:
        print("Atenção: Saldo zerado. Não sobrou margem de segurança.")
    else:
        print("Situação: Orçamento com superávit.")

    if renda_prevista > 0:
        pct_essencial = (total_essencial / renda_prevista) * 100
        pct_estilo = (total_estilo_vida / renda_prevista) * 100
        pct_reserva = (total_reserva / renda_prevista) * 100

        print("\nDiagnóstico de Aderência (Regra 50-30-20):")
        print(f"- Essenciais    : {pct_essencial:5.1f}% (Meta recomendada: até 50%)")
        print(f"- Estilo de Vida: {pct_estilo:5.1f}% (Meta recomendada: até 30%)")
        print(f"- Reserva       : {pct_reserva:5.1f}% (Meta recomendada: no mínimo 20%)")


def main():
    renda_prevista = 0.0
    despesas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            renda_prevista = definir_renda()
        elif opcao == "2":
            adicionar_despesa(despesas)
        elif opcao == "3":
            listar_despesas(despesas)
        elif opcao == "4":
            exibir_relatorio(renda_prevista, despesas)
        elif opcao == "0":
            print("\nEncerrando o programa. Parabéns pela conclusão do projeto!")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    main()
```
