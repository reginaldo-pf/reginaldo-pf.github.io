def exibir_menu(renda_atual):
    """Exibe o menu principal do sistema."""
    print("        Planejamento Financeiro")
    print(f"      [Receita Atual: R$ {renda_atual:.2f}]")
    print("\n" + "=" * 40)
    print("1 - Cadastrar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar todas as despesas")
    print("4 - Exibir Balanço 50-30-20")
    print("0 - Sair")
    print("\n" + "=" * 40)

def obter_numero_positivo(mensagem):
    """
    Função reutilizável: solicita um número ao usuário e garante
    que seja um valor numérico válido (float) e não negativo.
    """
    while True:
        try:
            entrada = input(mensagem).strip().replace(",", ".")
            valor = float(entrada)

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
    print("Sistema iniciado com sucesso.")

    renda_prevista = 0.0  # Estado inicial da receita na memória

    while True:
        exibir_menu(renda_prevista)
        opcao = input("Escolha uma opção: ").strip().replace(",", ".")
        if opcao == "4":
            print(f"\n Funcionalidade de Exibir Balanço 50-30-20 (Receita atual: R$ {renda_prevista:.2f})")
        elif opcao == "3":
            print("\n Funcionalidade de Listar Despesas")
        elif opcao == "2":
            print("\n Funcionalidade de Adicionar Despesa")
        elif opcao == "1":
            renda_prevista = definir_renda()
            print("\n Funcionalidade de Definir receita")
        elif opcao == "0":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    main()