"""
Módulo de Exceções de Domínio - BiblioTauá
Define as exceções de negócio mapeadas a partir dos Fluxos de Exceção da Documentação do Caso de Uso (DUC).
"""

class BiblioTauaException(Exception):
    """Exceção base para regras de negócio do BiblioTauá."""
    pass


class CupomInvalidoError(BiblioTauaException):
    """Exceção geral disparada quando um cupom viola regras de negócio ou elegibilidade."""
    pass


class CupomInexistenteError(CupomInvalidoError):
    """Lançada quando o código de cupom informado não consta na base de dados (FE01)."""
    def __init__(self, codigo: str):
        super().__init__(f"Cupom '{codigo}' não encontrado no sistema.")
        self.codigo = codigo


class CupomInativoError(CupomInvalidoError):
    """Lançada quando o cupom existe mas foi desativado pela administração (FE01)."""
    def __init__(self, codigo: str):
        super().__init__(f"O cupom '{codigo}' encontra-se desativado temporariamente.")
        self.codigo = codigo


class CupomExpiradoError(CupomInvalidoError):
    """Lançada quando a data atual ultrapassa a data limite de validade do cupom (FE02)."""
    def __init__(self, codigo: str, validade_ate: str):
        super().__init__(f"O cupom '{codigo}' expirou em {validade_ate}.")
        self.codigo = codigo
        self.validade_ate = validade_ate


class CupomEsgotadoError(CupomInvalidoError):
    """Lançada quando o número de utilizações atinge a cota máxima permitida (FE03)."""
    def __init__(self, codigo: str, limite: int):
        super().__init__(f"O cupom '{codigo}' atingiu a quantidade máxima de {limite} usos e esgotou.")
        self.codigo = codigo
        self.limite = limite


class ValorMinimoNaoAtingidoError(CupomInvalidoError):
    """Lançada quando o subtotal do pedido é inferior ao mínimo estipulado pelo cupom (FE04)."""
    def __init__(self, codigo: str, valor_minimo: float, subtotal_atual: float):
        super().__init__(
            f"O cupom '{codigo}' exige pedido mínimo de R$ {valor_minimo:.2f}. "
            f"Subtotal atual: R$ {subtotal_atual:.2f}."
        )
        self.codigo = codigo
        self.valor_minimo = valor_minimo
        self.subtotal_atual = subtotal_atual


class EstoqueInsuficienteError(BiblioTauaException):
    """Lançada quando a quantidade solicitada de um livro supera o estoque disponível."""
    def __init__(self, livro_titulo: str, estoque_atual: int, solicitado: int):
        super().__init__(
            f"Estoque insuficiente para '{livro_titulo}'. Disponível: {estoque_atual}, Solicitado: {solicitado}."
        )
        self.livro_titulo = livro_titulo
        self.estoque_atual = estoque_atual
        self.solicitado = solicitado
