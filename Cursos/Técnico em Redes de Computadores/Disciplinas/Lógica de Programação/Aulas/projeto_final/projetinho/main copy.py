def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n" + "=" * 40)
    print("        Planejamento Financeiro")
    print("\n" + "=" * 40)
    print("1 - Cadastrar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar todas as despesas")
    print("4 - Exibir Balanço 50-30-20")
    print("0 - Sair")
    print("\n" + "=" * 40)


def main():
    print("Sistema iniciado com sucesso.")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
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