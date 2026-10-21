"""
Projeto Final: Planejamento Financeiro
Etapa 1: Estrutura do Programa, Loop Principal e Menu de Opções

Conceitos trabalhados:
- Definição de funções sem parâmetros e sem retorno (`def exibir_menu()`, `def main()`)
- Laço de repetição infinito controlado por sentinela (`while True` com `break`)
- Entrada de dados com `input()` e limpeza com `.strip()`
- Estruturas condicionais (`if / elif / else`)
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
