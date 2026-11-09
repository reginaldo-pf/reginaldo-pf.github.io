"""
Módulo de Exceções de Domínio - BiblioTauá
Define as exceções de negócio mapeadas a partir dos Fluxos de Exceção da DUC UC04.

Instruções para o Aluno (Aula 24):
Consulte o Slide 12 e o guia_desenvolvedor.md para implementar as classes de exceção
que herdam de CupomInvalidoError.
"""

class BiblioTauaException(Exception):
    """Exceção base para regras de negócio do BiblioTauá."""
    pass


class CupomInvalidoError(BiblioTauaException):
    """Exceção geral disparada quando um cupom viola regras de negócio ou elegibilidade."""
    pass


# ==============================================================================
# TODO: [ALUNO - TAREFA 1] Implementar as subclasses de exceção da DUC UC04
# ==============================================================================

# TODO: 1. CupomInexistenteError(CupomInvalidoError)
# Mensagem: "Cupom '{codigo}' não encontrado no sistema."


# TODO: 2. CupomInativoError(CupomInvalidoError)
# Mensagem: "O cupom '{codigo}' encontra-se desativado temporariamente."


# TODO: 3. CupomExpiradoError(CupomInvalidoError)
# Mensagem: "O cupom '{codigo}' expirou em {validade_ate}."


# TODO: 4. CupomEsgotadoError(CupomInvalidoError)
# Mensagem: "O cupom '{codigo}' atingiu a quantidade máxima de {limite} usos e esgotou."


# TODO: 5. ValorMinimoNaoAtingidoError(CupomInvalidoError)
# Mensagem: "O cupom '{codigo}' exige pedido mínimo de R$ {valor_minimo:.2f}. Subtotal atual: R$ {subtotal_atual:.2f}."


# ==============================================================================
# Exceções Pré-existentes (v0.3.0)
# ==============================================================================
class EstoqueInsuficienteError(BiblioTauaException):
    """Lançada quando a quantidade solicitada de um livro supera o estoque disponível."""
    def __init__(self, livro_titulo: str, estoque_atual: int, solicitado: int):
        super().__init__(
            f"Estoque insuficiente para '{livro_titulo}'. Disponível: {estoque_atual}, Solicitado: {solicitado}."
        )
        self.livro_titulo = livro_titulo
        self.estoque_atual = estoque_atual
        self.solicitado = solicitado
