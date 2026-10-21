"""
Projeto Final: Planejamento Financeiro
Etapa 4: Visualização e Iteração – Listagem Formatada em Tabela

Novos conceitos trabalhados:
- Laço de repetição `for .. in ..` percorrendo listas de dicionários
- Função embutida `enumerate(colecao, start=1)` para numeração amigável
- Cláusula de guarda para lista vazia (`if not despesas: return`)
- Formatação de strings profissional (f-strings com alinhamento `<` à esquerda e `>` à direita)
- Design de interface em modo console (tabelas e alinhamento de colunas)
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
    """
    Exibe todas as despesas cadastradas em uma tabela organizada no console.
    """
    print("\n--- Lista de Despesas Registradas ---")
    
    # 1. Verificação de lista vazia
    if not despesas:
        print("Nenhuma despesa cadastrada até o momento.")
        return

    # 2. Cabeçalho da tabela com larguras fixas
    print(f"{'#':<4} {'Descrição':<25} {'Categoria':<15} {'Valor (R$)'}")
    print("-" * 55)

    # 3. Iteração com enumerate para exibir índice e dados de cada item
    for indice, item in enumerate(despesas, start=1):
        print(f"{indice:<4} {item['descricao']:<25} {item['categoria']:<15} R$ {item['valor']:>8.2f}")


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
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Relatório e Balanço.")
        elif opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    main()
