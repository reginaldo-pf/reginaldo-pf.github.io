"""
Projeto Final: Planejamento Financeiro
Etapa 3: Modelando Dados Compostos – Cadastro de Despesas (Listas e Dicionários)

Novos conceitos trabalhados:
- Dicionários em Python (`dict`): pares chave-valor para representar entidades do mundo real
- Listas dinâmicas (`list`): armazenamento de múltiplos registros com `.append()`
- Passagem de parâmetros por referência de objetos mutáveis (a lista é alterada dentro da função)
- Manipulação e validação de strings com `.strip()` e verificação de string vazia (`not descricao`)
- Menus secundários de seleção com laço de validação
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


def main():
    renda_prevista = 0.0
    despesas = []  # Lista que armazenará todos os dicionários de despesas

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            renda_prevista = definir_renda()
        elif opcao == "2":
            adicionar_despesa(despesas)
        elif opcao == "3":
            print(f"\n[EM CONSTRUÇÃO] Total de despesas prontas para listar: {len(despesas)}")
        elif opcao == "4":
            print("\n[EM CONSTRUÇÃO] Funcionalidade de Relatório e Balanço.")
        elif opcao == "0":
            print("\nEncerrando o programa. Até a próxima aula!")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    main()
