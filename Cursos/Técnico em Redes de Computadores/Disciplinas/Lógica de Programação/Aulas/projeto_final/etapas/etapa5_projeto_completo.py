"""
Projeto Final: Planejamento Financeiro
Etapa 5: Inteligência de Negócio e Relatório Analítico (Regra 50-30-20)

Novos conceitos trabalhados:
- Variáveis acumuladoras (somatórios condicionais por categoria)
- Operações aritméticas e cálculos percentuais sobre a receita
- Tomada de decisão em regras de negócio com múltiplas ramificações (`if / elif / else`)
- Alertas e diagnósticos automatizados ao usuário (déficit, superávit, meta 50-30-20)
- Fechamento da aplicação e boas práticas (`if __name__ == "__main__":`)
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

    # 5. Avaliação percentual da regra 50-30-20
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
