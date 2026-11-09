"""
BiblioTauá - Sistema de Livraria e Biblioteca Universitária (IFCE Campus Tauá)
Interface de Linha de Comando (CLI) para Demonstração da Sprint 04
"""
import os
import sys
from bibliotaua.database import inicializar_banco, popular_dados_iniciais, obter_conexao
from bibliotaua.models.cliente import Cliente
from bibliotaua.repositories.livro_repository import LivroRepository
from bibliotaua.repositories.cupom_repository import CupomRepository
from bibliotaua.services.checkout_service import CheckoutService
from bibliotaua.exceptions import BiblioTauaException

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("=" * 70)
    print("  📚  BIBLIOTAUÁ - LIVRARIA E BIBLIOTECA UNIVERSITÁRIA DO IFCE  📚")
    print("       Sprint 04: Motor de Validação e Aplicação de Cupons")
    print("=" * 70)

def main():
    # Inicializa e popula o banco de dados se necessário
    inicializar_banco()
    popular_dados_iniciais()

    conn = obter_conexao()
    livro_repo = LivroRepository(conn)
    cupom_repo = CupomRepository(conn)
    checkout_service = CheckoutService(conn)

    # Cliente padrão da demonstração
    cliente = Cliente(id=1, nome="Carlos Eduardo Santos", email="carlos.edu@aluno.ifce.edu.br", matricula="2024101TII001")

    while True:
        banner()
        print(f"\n👤 Cliente Ativo: {cliente.nome} (Matrícula: {cliente.matricula})")
        print("\nEscolha uma opção:")
        print("  [1] Listar Livros Disponíveis no Acervo")
        print("  [2] Consultar Cupons Promocionais Cadastrados")
        print("  [3] Simular Compra de Livro e Testar Cupom de Desconto")
        print("  [4] Cadastrar Novo Cupom Promocional")
        print("  [0] Sair do Sistema")
        opcao = input("\n👉 Opção: ").strip()

        if opcao == "1":
            livros = livro_repo.listar_todos()
            print("\n📖 LIVROS NO CATÁLOGO:")
            print("-" * 75)
            print(f"{'ID':<4} | {'Título':<40} | {'Preço':<10} | {'Estoque':<7}")
            print("-" * 75)
            for l in livros:
                print(f"{l.id:<4} | {l.titulo[:38]:<40} | R$ {l.preco:>7.2f} | {l.estoque:<7}")
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            cupons = cupom_repo.listar_todos()
            print("\n🏷️  CUPONS REGISTRADOS NO SISTEMA:")
            print("-" * 80)
            print(f"{'Código':<14} | {'Tipo':<12} | {'Valor':<8} | {'Mínimo':<10} | {'Usos':<10} | {'Validade':<11} | {'Status':<6}")
            print("-" * 80)
            for c in cupons:
                tipo_str = "%" if c.tipo_desconto.value == "PERCENTUAL" else "R$"
                valor_str = f"{c.valor_desconto}{tipo_str}"
                minimo_str = f"R$ {c.valor_minimo_pedido:.2f}"
                usos_str = f"{c.usos_realizados}/{c.limite_usos}"
                status_str = "Ativo" if c.ativo else "Inativo"
                print(f"{c.codigo:<14} | {c.tipo_desconto.value:<12} | {valor_str:<8} | {minimo_str:<10} | {usos_str:<10} | {str(c.validade_ate):<11} | {status_str:<6}")
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            livros = livro_repo.listar_todos()
            print("\nSelecione um livro para compra:")
            for l in livros:
                print(f"  [{l.id}] {l.titulo} - R$ {l.preco:.2f} (Estoque: {l.estoque})")
            
            try:
                livro_id = int(input("\nID do Livro: ").strip())
                qtd = int(input("Quantidade desejada: ").strip())
                codigo_cupom = input("Código do Cupom de Desconto (ou ENTER para nenhum): ").strip().upper()
                if not codigo_cupom:
                    codigo_cupom = None

                print("\n⚙️  Processando checkout e aplicando regras de negócio...")
                pedido = checkout_service.realizar_checkout(
                    cliente=cliente,
                    itens_solicitados=[(livro_id, qtd)],
                    codigo_cupom=codigo_cupom
                )

                print("\n✅ PEDIDO PROCESSADO COM SUCESSO!")
                print(f"   Pedido ID: #{pedido.id}")
                print(f"   Subtotal:  R$ {pedido.subtotal:.2f}")
                if pedido.cupom_aplicado:
                    print(f"   Cupom:     {pedido.cupom_aplicado.codigo} ({pedido.cupom_aplicado.tipo_desconto.value})")
                    print(f"   Desconto: -R$ {pedido.desconto_aplicado:.2f}")
                print(f"   TOTAL:     R$ {pedido.total:.2f}")
                print("   Status:    PAGO (Gravado no SQLite bibliotaua.db)")

            except BiblioTauaException as err:
                print(f"\n❌ ERRO DE REGRA DE NEGÓCIO: {err}")
            except Exception as e:
                print(f"\n⚠️  ERRO INESPERADO: {e}")
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            print("\n➕ CADASTRAR NOVO CUPOM:")
            codigo = input("Código (ex: NATAL15): ").strip().upper()
            tipo = input("Tipo ([1] Percentual, [2] Valor Fixo): ").strip()
            tipo_enum = "PERCENTUAL" if tipo == "1" else "VALOR_FIXO"
            valor = float(input("Valor do desconto (ex: 15 para 15% ou 20 para R$20): ").strip())
            minimo = float(input("Valor mínimo do pedido em R$ (ex: 50): ").strip())
            limite = int(input("Limite de utilizações (ex: 100): ").strip())
            validade = input("Data de validade (AAAA-MM-DD): ").strip()

            from bibliotaua.models.cupom import Cupom, TipoDesconto
            novo_cupom = Cupom(
                codigo=codigo,
                tipo_desconto=TipoDesconto(tipo_enum),
                valor_desconto=valor,
                valor_minimo_pedido=minimo,
                limite_usos=limite,
                validade_ate=validade
            )
            cupom_repo.salvar(novo_cupom)
            print(f"\n🎉 Cupom '{codigo}' cadastrado com sucesso no banco de dados!")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            print("\nEncerrando o sistema BiblioTauá. Bom trabalho na Sprint!")
            break
        else:
            print("\nOpção inválida.")
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
