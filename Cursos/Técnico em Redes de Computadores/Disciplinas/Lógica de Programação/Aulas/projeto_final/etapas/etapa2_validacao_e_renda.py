"""
Projeto Final: Planejamento Financeiro
Etapa 2: Entrada Segura de Dados e Previsão de Renda

Novos conceitos trabalhados:
- Funções que recebem parâmetros e devolvem valores (`return`)
- Tratamento de exceções com `try / except ValueError` (evitando falhas por digitação)
- Laço de validação contínua (`while True`) com condições lógicas (`if valor >= 0`)
- Tipos de ponto flutuante (`float`) e formatação monetária com f-strings (`:.2f`)
- Gerenciamento de estado na `main()` (armazenando a renda prevista)
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
            # Atualiza a variável com o retorno da função
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
