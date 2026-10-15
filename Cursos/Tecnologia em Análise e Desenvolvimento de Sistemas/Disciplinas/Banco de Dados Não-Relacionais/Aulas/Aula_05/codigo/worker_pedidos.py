"""
FastCommerce NoSQL - Worker Assíncrono de Processamento de Pedidos (Redis Queue)
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 05 (20/10/2026)
Prof. Me. Reginaldo Fernandes

Demonstração do Padrão Produtor-Consumidor (Queue) com Redis:
1. O Front-end/API atua como PRODUTOR inserindo pedidos via LPUSH na lista 'fila:pedidos'.
2. Este Worker atua como CONSUMIDOR executando BRPOP 'fila:pedidos' (espera bloqueante de baixo consumo de CPU).
3. Simula validação de pagamento e emissão de nota fiscal.
4. GANCHO COM AULA 06: Na próxima aula, este mesmo worker gravará o documento BSON definitivo no MongoDB!
"""

import json
import time
import sys
import redis

# Cores ANSI para o terminal
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
VERMELHO = "\033[91m"
CIANO = "\033[96m"
NEGRITO = "\033[1m"
RESET = "\033[0m"


def iniciar_worker():
    print("=" * 80)
    print(f"{CIANO}{NEGRITO}FASTCOMMERCE - WORKER DE PROCESSAMENTO DE PEDIDOS (REDIS QUEUE){RESET}")
    print(f"Disciplina: Banco de Dados Não-Relacionais | IFCE Campus Tauá")
    print("=" * 80)

    try:
        r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
        r.ping()
        print(f"{VERDE}✓ Conectado com sucesso ao Redis em localhost:6379.{RESET}")
    except Exception as e:
        print(f"{VERMELHO}✗ Erro ao conectar ao Redis: {e}{RESET}")
        print("Certifique-se de que o Redis está rodando (redis-server ou docker compose up).")
        sys.exit(1)

    chave_fila = "fila:pedidos"
    print(f"\n{AMARELO}⚙ Escutando a fila '{chave_fila}' via BRPOP (Bloqueio Inteligente)...{RESET}")
    print("DICA: Acesse a página web (http://localhost:5000), monte um carrinho e clique em 'Finalizar Pedido'!\n")

    total_processados = 0

    while True:
        try:
            # BRPOP: Bloqueia o processo por até 5 segundos aguardando um novo item no final da lista
            resultado = r.brpop(chave_fila, timeout=5)

            if resultado is None:
                # Timeout de 5s sem pedidos na fila (aguardando novo ciclo sem sobrecarregar a CPU)
                sys.stdout.write(f"\r{AZUL}[IDLE]{RESET} Aguardando novos pedidos na fila... (Fila atual: {r.llen(chave_fila)} itens)")
                sys.stdout.flush()
                continue

            print()  # Quebra de linha após o status de IDLE
            nome_lista, pedido_raw = resultado
            pedido = json.loads(pedido_raw)
            total_processados += 1

            print(f"\n{VERDE}{NEGRITO}────────────────────────────────────────────────────────────────────────────{RESET}")
            print(f"{VERDE}📥 [NOVO PEDIDO RETIRADO DA FILA (BRPOP)] #{total_processados}{RESET}")
            print(f"   • ID do Pedido  : {NEGRITO}{pedido.get('id_pedido')}{RESET}")
            print(f"   • Timestamp     : {pedido.get('timestamp')}")
            print(f"   • Sessão Origem : {pedido.get('session_id')}")
            print(f"   • Valor Total   : {VERDE}R$ {pedido.get('total'):.2f}{RESET}")
            print(f"   • Itens Solicitados:")
            for item in pedido.get("itens", []):
                print(f"     - {item['quantidade']}x {item['nome']} (R$ {item['preco_unitario']:.2f}) = R$ {item['total']:.2f}")

            # Simula tempo de processamento de pagamento
            print(f"   {AMARELO}⏳ Processando pagamento e validando estoque...{RESET}")
            time.sleep(1.2)

            # Atualiza status do pedido em memória
            pedido["status"] = "PAGAMENTO_APROVADO_AGUARDANDO_ENVIO"
            pedido["processado_em"] = time.strftime("%Y-%m-%d %H:%M:%S")

            print(f"   {VERDE}✓ Pagamento aprovado com sucesso!{RESET}")

            # ==================================================================
            # GANCHO PEDAGÓGICO COM A AULA 06 (MONGODB):
            # ==================================================================
            print(f"   {CIANO}🔗 [PERSISTÊNCIA POLIGLOTA - PREVIEW DA AULA 06]:{RESET}")
            print(f"      Na próxima aula, este pedido será salvo no MongoDB:")
            print(f"      db.pedidos.insert_one({{")
            print(f"          _id: ObjectId(),")
            print(f"          id_pedido: '{pedido['id_pedido']}',")
            print(f"          total: {pedido['total']},")
            print(f"          itens: [...],  // Documento Embutido (Embedding)")
            print(f"          status: 'APROVADO'")
            print(f"      }})")
            print(f"{VERDE}{NEGRITO}────────────────────────────────────────────────────────────────────────────{RESET}")

        except KeyboardInterrupt:
            print(f"\n\n{AMARELO}Encerrando worker com segurança... Total de pedidos processados: {total_processados}{RESET}")
            break
        except Exception as err:
            print(f"\n{VERMELHO}Erro durante o processamento do pedido: {err}{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    iniciar_worker()
