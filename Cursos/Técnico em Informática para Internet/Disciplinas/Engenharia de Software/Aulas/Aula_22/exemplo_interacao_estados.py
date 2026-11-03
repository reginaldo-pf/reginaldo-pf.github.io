#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
IFCE Campus Tauá - Técnico em Informática para Internet
Disciplina: Engenharia de Software
Aula 22: Diagramas de Interação (Sequência e Comunicação) e Diagrama de Máquina de Estados

Demonstração Prática:
1. Mapeamento de Interação (Diagrama de Sequência - Cap. 7 de Guedes)
2. Rastreamento Hierárquico de Mensagens (Diagrama de Comunicação - Cap. 8 de Guedes)
3. Máquina de Estados Finita Reativa com Guardas e Ações (Diagrama de Máquina de Estados - Cap. 9 de Guedes)
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Callable, Dict, List, Optional, Tuple


# ==============================================================================
# 1. ENUMERAÇÃO DE ESTADOS DO PEDIDO (Capítulo 9 - Máquina de Estados)
# ==============================================================================
class StatusPedido(str, Enum):
    """
    Representa os estados possíveis no ciclo de vida de um Pedido (UML 2).
    """
    CRIADO = "CRIADO"
    AGUARDANDO_PAGAMENTO = "AGUARDANDO_PAGAMENTO"
    EM_PREPARO = "EM_PREPARO"
    PRONTO_PARA_COLETA = "PRONTO_PARA_COLETA"
    EM_ROTA_DE_ENTREGA = "EM_ROTA_DE_ENTREGA"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"


# ==============================================================================
# 2. MODELO DE DOMÍNIO E VALIDADORES (TauáDelivery Web)
# ==============================================================================
@dataclass
class ItemPedidoVO:
    id_produto: int
    nome_produto: str
    quantidade: int
    preco_unitario: float

    @property
    def subtotal(self) -> float:
        return self.quantidade * self.preco_unitario


@dataclass
class TransacaoPagamento:
    id_transacao: str
    forma_pagamento: str
    valor: float
    aprovado: bool
    mensagem_retorno: str
    data_hora: datetime = field(default_factory=datetime.now)


# ==============================================================================
# 3. MÁQUINA DE ESTADOS FINITA DO PEDIDO (Capítulo 9)
# ==============================================================================
class TransicaoInvalidaException(Exception):
    """Lançada quando um evento tenta disparar uma transição ilegal."""
    pass


class PedidoStateMachine:
    """
    Implementa a Máquina de Estados de um Pedido conforme as regras da UML 2:
    - Estados simples com atividades internas: entry / e exit /
    - Transições dirigidas por eventos com condições de guarda [guarda]
    - Histórico de auditoria de transições
    """

    def __init__(self, numero_pedido: int, cliente_nome: str):
        self.numero_pedido = numero_pedido
        self.cliente_nome = cliente_nome
        self.itens: List[ItemPedidoVO] = []
        self.taxa_entrega: float = 5.00
        self.entregador_alocado: Optional[str] = None
        self.codigo_otp_entrega: str = "7412"

        # Estado atual e histórico
        self.estado_atual: StatusPedido = StatusPedido.CRIADO
        self.historico_transicoes: List[str] = [
            f"[{datetime.now().strftime('%H:%M:%S')}] Estado Inicial -> CRIADO"
        ]

        # Callbacks de atividades internas (entry / e exit /)
        self._entry_actions: Dict[StatusPedido, List[Callable[[], None]]] = {
            StatusPedido.CRIADO: [lambda: print("   [entry / Pedido.CRIADO] Inicializando buffer do carrinho e calculando totais.")],
            StatusPedido.AGUARDANDO_PAGAMENTO: [lambda: print("   [entry / Pedido.AGUARDANDO_PAGAMENTO] Gerando QR Code PIX e iniciando timer de 15 min.")],
            StatusPedido.EM_PREPARO: [lambda: print("   [entry / Pedido.EM_PREPARO] Notificando painel KDS da cozinha do restaurante.")],
            StatusPedido.PRONTO_PARA_COLETA: [lambda: print("   [entry / Pedido.PRONTO_PARA_COLETA] Enviando sinal push de corrida para entregadores disponíveis.")],
            StatusPedido.EM_ROTA_DE_ENTREGA: [lambda: print("   [entry / Pedido.EM_ROTA_DE_ENTREGA] Ativando telemetria GPS e compartilhando rota com o cliente.")],
            StatusPedido.ENTREGUE: [lambda: print("   [entry / Pedido.ENTREGUE] Disparando pesquisa de satisfação e liberando repasse financeiro.")],
            StatusPedido.CANCELADO: [lambda: print("   [entry / Pedido.CANCELADO] Desfazendo reservas de itens e estornando cobranças, se houver.")],
        }

        self._exit_actions: Dict[StatusPedido, List[Callable[[], None]]] = {
            StatusPedido.AGUARDANDO_PAGAMENTO: [lambda: print("   [exit  / Pedido.AGUARDANDO_PAGAMENTO] Encerrando pooling do webhook do gateway de pagamento.")],
            StatusPedido.EM_ROTA_DE_ENTREGA: [lambda: print("   [exit  / Pedido.EM_ROTA_DE_ENTREGA] Finalizando rastreamento GPS e arquivando trajeto.")],
        }

        # Executa a ação de entrada do estado inicial
        self._executar_entry(StatusPedido.CRIADO)

    @property
    def valor_total(self) -> float:
        """Atributo derivado /valorTotal."""
        return sum(item.subtotal for item in self.itens) + self.taxa_entrega

    def adicionar_item(self, id_prod: int, nome: str, qtd: int, preco: float) -> None:
        if self.estado_atual != StatusPedido.CRIADO:
            raise TransicaoInvalidaException(
                f"Itens só podem ser alterados no estado CRIADO (Estado atual: {self.estado_atual.value})."
            )
        self.itens.append(ItemPedidoVO(id_prod, nome, qtd, preco))

    def _executar_exit(self, estado: StatusPedido) -> None:
        if estado in self._exit_actions:
            for acao in self._exit_actions[estado]:
                acao()

    def _executar_entry(self, estado: StatusPedido) -> None:
        if estado in self._entry_actions:
            for acao in self._entry_actions[estado]:
                acao()

    def transitar_para(self, novo_estado: StatusPedido, evento: str, guarda_ok: bool, motivo: str = "") -> None:
        """
        Executa uma transição de estado da UML:
        gatilho/evento [condicao_guarda] / acao_efeito
        """
        print(f"\n🔄 [Transição Solicitada] Evento: '{evento}' | De: {self.estado_atual.value} -> Para: {novo_estado.value}")

        if not guarda_ok:
            raise TransicaoInvalidaException(
                f"Transição rejeitada: Condição de Guarda FALHOU para o evento '{evento}' ({motivo})."
            )

        # Regras da matriz de transição
        transicoes_permitidas: Dict[StatusPedido, List[StatusPedido]] = {
            StatusPedido.CRIADO: [StatusPedido.AGUARDANDO_PAGAMENTO, StatusPedido.CANCELADO],
            StatusPedido.AGUARDANDO_PAGAMENTO: [StatusPedido.EM_PREPARO, StatusPedido.CANCELADO],
            StatusPedido.EM_PREPARO: [StatusPedido.PRONTO_PARA_COLETA, StatusPedido.CANCELADO],
            StatusPedido.PRONTO_PARA_COLETA: [StatusPedido.EM_ROTA_DE_ENTREGA, StatusPedido.CANCELADO],
            StatusPedido.EM_ROTA_DE_ENTREGA: [StatusPedido.ENTREGUE, StatusPedido.CANCELADO],
            StatusPedido.ENTREGUE: [],     # Estado Final
            StatusPedido.CANCELADO: []     # Estado Final
        }

        if novo_estado not in transicoes_permitidas.get(self.estado_atual, []):
            raise TransicaoInvalidaException(
                f"Transição proibida pela Máquina de Estados: Não é permitido ir de {self.estado_atual.value} para {novo_estado.value}."
            )

        # 1. Executa exit do estado de origem
        self._executar_exit(self.estado_atual)

        # 2. Executa a transição
        estado_anterior = self.estado_atual
        self.estado_atual = novo_estado
        log_msg = f"[{datetime.now().strftime('%H:%M:%S')}] {estado_anterior.value} --({evento})--> {novo_estado.value}"
        self.historico_transicoes.append(log_msg)
        print(f"   ✓ Efeito da Transição: {log_msg}")

        # 3. Executa entry do estado de destino
        self._executar_entry(self.estado_atual)


# ==============================================================================
# 4. SIMULAÇÃO DE INTERAÇÃO (SEQUÊNCIA E COMUNICAÇÃO - Caps. 7 e 8)
# ==============================================================================
class MessageLogger:
    """
    Rastreador de chamadas para ilustrar simultaneamente:
    - Diagrama de Sequência (ordenação cronológica de chamadas e retornos)
    - Diagrama de Comunicação (numeração aninhada hierárquica: 1, 1.1, 1.2, 1.2.1...)
    """
    _logs: List[Tuple[str, str, str, str, str]] = []

    @classmethod
    def log(cls, num_seq: str, origem: str, destino: str, msg: str, tipo: str = "Síncrona") -> None:
        cls._logs.append((num_seq, origem, destino, msg, tipo))
        print(f"   [Msg {num_seq:>7}] {origem:<20} --({tipo}: {msg})--> {destino}")

    @classmethod
    def clear(cls) -> None:
        cls._logs.clear()


class GatewayPagamentoService:
    """Simula um gateway de pagamento externo (ex.: Asaas / Mercado Pago)."""

    def processar_transacao(self, numero_pedido: int, valor: float, forma: str) -> TransacaoPagamento:
        MessageLogger.log("1.2.1", "PedidoService", "GatewayPagamentoService", f"debitar({forma}, {valor:.2f})")
        # Simula aprovação para pagamentos positivos
        if valor > 0:
            MessageLogger.log("1.2.1.r", "GatewayPagamentoService", "PedidoService", "Transacao(status=APROVADA)", "Retorno")
            return TransacaoPagamento(
                id_transacao=f"TX-{numero_pedido}-9912",
                forma_pagamento=forma,
                valor=valor,
                aprovado=True,
                mensagem_retorno="Transação PIX liquidada com sucesso no Banco Central."
            )
        else:
            MessageLogger.log("1.2.1.r", "GatewayPagamentoService", "PedidoService", "Transacao(status=RECUSADA)", "Retorno")
            return TransacaoPagamento(
                id_transacao=f"TX-{numero_pedido}-0000",
                forma_pagamento=forma,
                valor=valor,
                aprovado=False,
                mensagem_retorno="Valor inválido."
            )


class PedidoRepository:
    """Representa a camada de persistência (Padrão Repository - Cap. 7 de Guedes)."""
    _banco_dados: Dict[int, PedidoStateMachine] = {}

    def salvar(self, pedido: PedidoStateMachine) -> bool:
        MessageLogger.log("1.2.2", "PedidoService", "PedidoRepository", f"salvarPedido(#{pedido.numero_pedido})")
        self._banco_dados[pedido.numero_pedido] = pedido
        MessageLogger.log("1.2.2.r", "PedidoRepository", "PedidoService", "true (gravado com sucesso)", "Retorno")
        return True

    def obter_por_id(self, numero_pedido: int) -> Optional[PedidoStateMachine]:
        return self._banco_dados.get(numero_pedido)


class NotificacaoService:
    """Simula o envio assíncrono de notificações aos participantes."""

    def notificar_restaurante(self, numero_pedido: int) -> None:
        MessageLogger.log("1.2.3", "PedidoService", "NotificacaoService", f"enviarNotificacaoRestaurante(#{numero_pedido})", "Assíncrona")


class PedidoService:
    """Camada de serviço e controle de regras de negócio (<<control>>)."""

    def __init__(self):
        self.gateway = GatewayPagamentoService()
        self.repo = PedidoRepository()
        self.notificacao = NotificacaoService()

    def checkout_pedido(self, pedido: PedidoStateMachine, forma_pagto: str) -> bool:
        """
        Executa o fluxo do caso de uso 'Finalizar Pedido e Processar Pagamento':
        Fragmento Combinado alt [transacao.aprovado == True] / [else]
        """
        MessageLogger.log("1.2", "TelaCheckoutBoundary", "PedidoService", f"finalizarPedido(#{pedido.numero_pedido})")

        # Transição: CRIADO -> AGUARDANDO_PAGAMENTO
        pedido.transitar_para(
            StatusPedido.AGUARDANDO_PAGAMENTO,
            evento="checkoutAcionado",
            guarda_ok=(len(pedido.itens) > 0 and pedido.valor_total > 0),
            motivo="Carrinho deve conter pelo menos 1 item com valor positivo"
        )

        # 1.2.1: Envia para o Gateway
        transacao = self.gateway.processar_transacao(pedido.numero_pedido, pedido.valor_total, forma_pagto)

        # Fragmento Combinado: alt
        if transacao.aprovado:
            print("\n   [Fragmento Combinado: alt -> Ramo Aprovado]")
            # Transição: AGUARDANDO_PAGAMENTO -> EM_PREPARO
            pedido.transitar_para(
                StatusPedido.EM_PREPARO,
                evento="pagamentoConfirmado",
                guarda_ok=(transacao.valor == pedido.valor_total),
                motivo="Valor pago confere integralmente com o total do pedido"
            )

            # 1.2.2: Persiste no banco de dados via Repository
            self.repo.salvar(pedido)

            # 1.2.3: Notifica restaurante de forma assíncrona
            self.notificacao.notificar_restaurante(pedido.numero_pedido)

            MessageLogger.log("1.2.r", "PedidoService", "TelaCheckoutBoundary", "ResultadoCheckout(sucesso=True)", "Retorno")
            return True
        else:
            print("\n   [Fragmento Combinado: alt -> Ramo Recusado (else)]")
            pedido.transitar_para(
                StatusPedido.CANCELADO,
                evento="pagamentoRecusado",
                guarda_ok=True,
                motivo=transacao.mensagem_retorno
            )
            self.repo.salvar(pedido)
            MessageLogger.log("1.2.r", "PedidoService", "TelaCheckoutBoundary", f"ResultadoCheckout(sucesso=False, erro='{transacao.mensagem_retorno}')", "Retorno")
            return False


class TelaCheckoutBoundary:
    """Camada de interface e fronteira com o usuário (<<boundary>>)."""

    def __init__(self, service: PedidoService):
        self.service = service

    def submeter_pedido(self, pedido: PedidoStateMachine, forma_pagto: str) -> None:
        MessageLogger.log("1.1", "Cliente (Ator)", "TelaCheckoutBoundary", f"clicarConfirmarPedido(forma='{forma_pagto}')")
        sucesso = self.service.checkout_pedido(pedido, forma_pagto)
        if sucesso:
            MessageLogger.log("1.1.r", "TelaCheckoutBoundary", "Cliente (Ator)", "exibirTelaSucessoComAcompanhamento()", "Retorno")
        else:
            MessageLogger.log("1.1.r", "TelaCheckoutBoundary", "Cliente (Ator)", "exibirModalErro('Pagamento Recusado')", "Retorno")


# ==============================================================================
# 5. EXECUÇÃO DA SIMULAÇÃO INTEGRADA (HAPPY PATH E EDGE CASES)
# ==============================================================================
def demonstrar_interacao_e_estados():
    print("=" * 80)
    print("IFCE TAUÁ - ENGENHARIA DE SOFTWARE (AULA 22)")
    print("SIMULADOR DE DIAGRAMAS DE INTERAÇÃO E MÁQUINA DE ESTADOS (UML 2)")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # CENÁRIO 1: FLUXO FELIZ COMPLETO (Happy Path: da criação até a entrega)
    # --------------------------------------------------------------------------
    print("\n" + "▶" * 40)
    print(" CENÁRIO 1: FLUXO DE SUCESSO (CRIADO -> ENTREGUE)")
    print("◀" * 40)

    service = PedidoService()
    tela = TelaCheckoutBoundary(service)
    MessageLogger.clear()

    # 1. Instanciação e montagem do carrinho
    pedido1 = PedidoStateMachine(numero_pedido=101, cliente_nome="Maria das Dores")
    pedido1.adicionar_item(1, "Pizza Especial Tauá (Grande)", 1, 48.00)
    pedido1.adicionar_item(2, "Refrigerante Cajuína 1L", 2, 8.50)
    print(f"\n🛒 Pedido #101 criado para {pedido1.cliente_nome}. Subtotal itens: R$ {sum(i.subtotal for i in pedido1.itens):.2f} + Taxa Entrega: R$ {pedido1.taxa_entrega:.2f} = Total: R$ {pedido1.valor_total:.2f}")

    # 2. Execução da Sequência de Checkout
    print("\n--- INÍCIO DA TROCA DE MENSAGENS (DIAGRAMA DE SEQUÊNCIA / COMUNICAÇÃO) ---")
    MessageLogger.log("1", "Usuario", "Cliente (Ator)", "iniciarCheckout()")
    tela.submeter_pedido(pedido1, forma_pagto="PIX")

    # 3. Avanço dos estados pós-cozinha
    print("\n--- PROGRESSÃO DA MÁQUINA DE ESTADOS PELOS OPERADORES DO SISTEMA ---")
    # Concluir Preparo
    pedido1.transitar_para(
        StatusPedido.PRONTO_PARA_COLETA,
        evento="pratoFinalizadoPelaCozinha",
        guarda_ok=True,
        motivo="Todos os itens foram preparados e embalados"
    )

    # Alocar Entregador
    pedido1.entregador_alocado = "Carlos Motoboy (Placa: HYZ-9821)"
    pedido1.transitar_para(
        StatusPedido.EM_ROTA_DE_ENTREGA,
        evento="aceiteCorridaEntregador",
        guarda_ok=(pedido1.entregador_alocado is not None),
        motivo=f"Entregador {pedido1.entregador_alocado} assumiu o frete"
    )

    # Confirmar Entrega via OTP
    otp_informado = "7412"
    pedido1.transitar_para(
        StatusPedido.ENTREGUE,
        evento="informarCodigoOtpEntrega",
        guarda_ok=(otp_informado == pedido1.codigo_otp_entrega),
        motivo="Código OTP conferido com sucesso no smartphone do entregador"
    )

    # --------------------------------------------------------------------------
    # CENÁRIO 2: TESTE DE RESILIÊNCIA E CONDICIONAIS DE GUARDA (Falha / Cancelamento)
    # --------------------------------------------------------------------------
    print("\n\n" + "▶" * 40)
    print(" CENÁRIO 2: TESTE DE CONDIÇÕES DE GUARDA E TRANSIÇÃO INVÁLIDA")
    print("◀" * 40)

    pedido2 = PedidoStateMachine(numero_pedido=102, cliente_nome="João Paulo")
    # Tentativa de avançar carrinho sem itens (deve falhar na guarda)
    try:
        print("\nTentando avançar pedido vazio para AGUARDANDO_PAGAMENTO...")
        pedido2.transitar_para(
            StatusPedido.AGUARDANDO_PAGAMENTO,
            evento="checkoutAcionado",
            guarda_ok=(len(pedido2.itens) > 0),
            motivo="Pedido não possui nenhum item cadastrado"
        )
    except TransicaoInvalidaException as e:
        print(f"❌ [Exceção de Guarda Capturada com Sucesso]: {e}")

    # Tentativa de transição ilegal: de CRIADO direto para ENTREGUE
    try:
        print("\nTentando transição ilegal (pulo de ciclo: CRIADO -> ENTREGUE)...")
        pedido2.transitar_para(
            StatusPedido.ENTREGUE,
            evento="tentativaPuloIlegal",
            guarda_ok=True,
            motivo="Ignorando pagamento e preparo"
        )
    except TransicaoInvalidaException as e:
        print(f"❌ [Exceção da Máquina de Estados Capturada]: {e}")

    # --------------------------------------------------------------------------
    # AUDITORIA E HISTÓRICO DAS TRANSIÇÕES
    # --------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print(f"HISTÓRICO COMPLETO DE AUDITORIA DO PEDIDO #{pedido1.numero_pedido} (ESTADOS FINAIS):")
    print("=" * 80)
    for log in pedido1.historico_transicoes:
        print(f"  • {log}")
    print(f"Estado Final: {pedido1.estado_atual.value} (Instância arquivada com sucesso)")
    print("=" * 80)


if __name__ == "__main__":
    demonstrar_interacao_e_estados()
