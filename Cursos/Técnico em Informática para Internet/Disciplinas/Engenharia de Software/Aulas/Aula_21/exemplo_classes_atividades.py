#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
IFCE Campus Tauá - Técnico em Informática para Internet
Disciplina: Engenharia de Software
Aula 21: Aprofundamento no Diagrama de Classes e Diagrama de Atividades

Mapeamento entre Modelos UML 2 (Capítulos 4 e 10) e Código Orientado a Objetos
Baseado no livro: "UML 2 - Uma abordagem prática" (Gilleanes T. A. Guedes)
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional


# ==============================================================================
# 1. ASSOCIAÇÃO UNÁRIA / REFLEXIVA COM PAPÉIS (Figuras 4.4 e 4.5 do Livro)
# ==============================================================================
class Funcionario:
    """
    Representa a classe Funcionario com associação reflexiva 'Gerencia' (Fig. 4.5):
    - Papel +chefe (multiplicidade 0..1)
    - Papel +subordinados (multiplicidade 0..*)
    """

    def __init__(self, nome: str, cargo: str):
        self.nome = nome
        self.cargo = cargo
        self.chefe: Optional["Funcionario"] = None
        self.subordinados: List["Funcionario"] = []

    def adicionar_subordinado(self, subordinado: "Funcionario") -> None:
        if subordinado is self:
            raise ValueError("Um funcionário não pode ser chefe de si mesmo (restrição OCL).")
        if subordinado not in self.subordinados:
            self.subordinados.append(subordinado)
            subordinado.chefe = self

    def __str__(self) -> str:
        nome_chefe = self.chefe.nome if self.chefe else "Nenhum (Diretoria)"
        qtd_sub = len(self.subordinados)
        return f"[Funcionario] {self.nome} ({self.cargo}) | Chefe: {nome_chefe} | Subordinados: {qtd_sub}"


# ==============================================================================
# 2. AGREGAÇÃO (TODO-PARTE FRACA) E ATRIBUTOS DERIVADOS (Figuras 4.3, 4.10 e 4.51)
# ==============================================================================
class ContaComum:
    """
    Classe ContaComum (Figuras 4.3, 4.10 e 4.51 do livro de Guedes).
    Demonstra:
    - Atributo com restrição {readOnly}: numeroConta, /aberturaConta
    - Atributo derivado (/): /saldoConta recalculado em depósitos e saques
    - Navegabilidade e agregação com Pessoa
    """

    def __init__(self, numero_conta: int, senha_conta: int):
        self.__numero_conta = numero_conta         # {readOnly}
        self.__abertura_conta = date.today()       # /aberturaConta {readOnly}
        self.__fechamento_conta: Optional[date] = None
        self._situacao_conta: int = 1              # Valor inicial = 1 (Ativa)
        self._senha_conta: int = senha_conta
        self._historico_movimentos: List[float] = []

    @property
    def numero_conta(self) -> int:
        """Propriedade somente leitura ({readOnly} na UML)."""
        return self.__numero_conta

    @property
    def abertura_conta(self) -> date:
        """Propriedade derivada somente leitura (/aberturaConta {readOnly})."""
        return self.__abertura_conta

    @property
    def saldo_conta(self) -> float:
        """
        Atributo derivado (/saldoConta: double = 0 na Figura 4.3):
        Calculado dinamicamente a partir das movimentações registradas.
        """
        return sum(self._historico_movimentos)

    def validar_senha(self, senha: int) -> bool:
        return self._senha_conta == senha

    def depositar(self, valor: float) -> bool:
        if self._situacao_conta == 1 and valor > 0:
            self._historico_movimentos.append(valor)
            return True
        return False

    def sacar(self, valor: float) -> bool:
        if self._situacao_conta == 1 and 0 < valor <= self.saldo_conta:
            self._historico_movimentos.append(-valor)
            return True
        return False

    def __str__(self) -> str:
        status = "Ativa" if self._situacao_conta == 1 else "Encerrada"
        return (f"ContaComum Nº {self.numero_conta} ({status}) | "
                f"Abertura: {self.abertura_conta} | /saldoConta: R$ {self.saldo_conta:.2f}")


class Pessoa(ABC):
    """
    Classe Abstrata Pessoa (nome em itálico nas Figuras 4.10, 4.12 e 4.51).
    Mantém uma Agregação (losango vazio <>--) com ContaComum (1..* para 1..*):
    Se o objeto Pessoa deixar de existir em memória, a ContaComum pode continuar
    associada a outro cotitular ou preservada no histórico bancário.
    """

    def __init__(self, nome: str, endereco: str, renda: float):
        self._nome_pessoa = nome
        self._endereco_pessoa = endereco
        self._renda_pessoa = renda
        self._situacao_pessoa: int = 1
        self.contas: List[ContaComum] = []  # Agregação: lista de referências externas

    def vincular_conta(self, conta: ContaComum) -> None:
        if conta not in self.contas:
            self.contas.append(conta)

    @abstractmethod
    def documento_principal(self) -> str:
        pass


class PessoaFisica(Pessoa):
    """Subclasse concreta PessoaFisica (Figura 4.12 e 4.51)."""

    def __init__(self, nome: str, endereco: str, renda: float, cpf: str, idade: int):
        if idade < 18:
            # Restrição OCL da Figura 4.25: context PessoaFisica inv: self.idade >= 18
            raise ValueError("Violação de restrição OCL: PessoaFisica deve ter idade >= 18.")
        super().__init__(nome, endereco, renda)
        self.__cpf_pessoa = cpf
        self.__idade_pessoa = idade

    def documento_principal(self) -> str:
        return f"CPF: {self.__cpf_pessoa}"


# ==============================================================================
# 3. COMPOSIÇÃO (TODO-PARTE FORTE) (Figura 4.11 do Livro)
# ==============================================================================
class Artigo:
    """Objeto-Parte de uma Edicao (Figura 4.11)."""

    def __init__(self, titulo_artigo: str):
        self.titulo_artigo = titulo_artigo

    def __str__(self) -> str:
        return f"Artigo: '{self.titulo_artigo}'"


class Edicao:
    """
    Objeto-Parte de RevistaCientifica e Objeto-Todo de Artigo (Figura 4.11).
    Composição: Uma Edicao contém de 6..10 artigos (aqui exemplificado com criação interna).
    """

    def __init__(self, numero_edicao: int, volume_edicao: int, titulos_artigos: List[str]):
        self.numero_edicao = numero_edicao
        self.volume_edicao = volume_edicao
        self.data_edicao = date.today()
        # Composição forte: os objetos Artigo são instanciados e possuídos exclusivamente pela Edicao
        self.__artigos: List[Artigo] = [Artigo(t) for t in titulos_artigos]

    @property
    def artigos(self) -> List[Artigo]:
        return list(self.__artigos)

    def __str__(self) -> str:
        return f"Edição Nº {self.numero_edicao} (Vol. {self.volume_edicao}) com {len(self.__artigos)} artigos"


class RevistaCientifica:
    """
    Objeto-Todo na Composição (Figura 4.11 do livro de Guedes).
    Se a RevistaCientifica for destruída, suas Edicoes e respectivos Artigos
    perdem existência independente (ciclo de vida estritamente acoplado).
    """

    def __init__(self, titulo_revista: str, issn_revista: int, periodo_revista: str):
        self.titulo_revista = titulo_revista
        self.issn_revista = issn_revista
        self.periodo_revista = periodo_revista
        self.__edicoes: List[Edicao] = []

    def publicar_edicao(self, numero: int, volume: int, titulos_artigos: List[str]) -> Edicao:
        nova_edicao = Edicao(numero, volume, titulos_artigos)
        self.__edicoes.append(nova_edicao)
        return nova_edicao

    @property
    def edicoes(self) -> List[Edicao]:
        return list(self.__edicoes)


# ==============================================================================
# 4. CLASSE ASSOCIATIVA E REALIZAÇÃO DE INTERFACE (Figuras 4.13 e 4.18)
# ==============================================================================
class Ator:
    def __init__(self, nome_ator: str):
        self.nome_ator = nome_ator


class Filme:
    def __init__(self, titulo_filme: str, duracao_min: int):
        self.titulo_filme = titulo_filme
        self.duracao_min = duracao_min


class Atua:
    """
    Classe Associativa Atua (Figura 4.13 do livro de Guedes).
    Armazena o atributo 'papelAtorFilme', que pertence ao vínculo entre Ator e Filme,
    e não isoladamente ao Ator nem ao Filme.
    """

    def __init__(self, ator: Ator, filme: Filme, papel_ator_filme: str):
        self.ator = ator
        self.filme = filme
        self.papel_ator_filme = papel_ator_filme

    def __str__(self) -> str:
        return f"[Classe Associativa Atua] {self.ator.nome_ator} interpreta '{self.papel_ator_filme}' em '{self.filme.titulo_filme}'"


class Pagamento(ABC):
    """
    <<interface>> Pagamento (Figura 4.18 do livro de Guedes).
    Define o contrato público +quitarPedido() sem implementação concreta.
    """

    @abstractmethod
    def quitar_pedido(self, valor: float) -> str:
        pass


class PagamentoBoleto(Pagamento):
    """Realiza (implementa) a interface Pagamento via Boleto Bancário."""

    def quitar_pedido(self, valor: float) -> str:
        return f"Pagamento de R$ {valor:.2f} processado via Boleto Bancário (compensação em até 1 dia útil)."


class PagamentoCartaoCredito(Pagamento):
    """Realiza (implementa) a interface Pagamento via Cartão de Crédito."""

    def quitar_pedido(self, valor: float) -> str:
        return f"Pagamento de R$ {valor:.2f} autorizado instantaneamente via Cartão de Crédito."


class PagamentoCartaoDebito(Pagamento):
    """Realiza (implementa) a interface Pagamento via Cartão de Débito."""

    def quitar_pedido(self, valor: float) -> str:
        return f"Pagamento de R$ {valor:.2f} debitado em conta via Cartão de Débito."


class Pedido:
    """Classe Pedido associada à interface Pagamento (Figura 4.18)."""

    def __init__(self, nota_fiscal: int, valor_total: float, estrategia_pagamento: Pagamento):
        self._nota_fiscal_pedido = nota_fiscal
        self._valor_total_pedido = valor_total
        self._pagamento = estrategia_pagamento

    def processar_quitacao(self) -> str:
        return f"[NF #{self._nota_fiscal_pedido}] {self._pagamento.quitar_pedido(self._valor_total_pedido)}"


# ==============================================================================
# 5. EXECUÇÃO DE DIAGRAMA DE ATIVIDADE (Capítulo 10 - Figura 10.7)
# ==============================================================================
def atividade_emitir_saldo(banco_contas: dict, numero_informado: int, senha_informada: int) -> None:
    """
    Tradução algorítmica direta do Diagrama de Atividade 'Emitir Saldo'
    (Figura 10.7 do livro de Guedes):
    - Nó Inicial -> Ação: Receber número da conta -> Ação: Consultar conta
    - Nó de Decisão 1: [Conta inválida] -> Nó Final | [Conta válida] -> Ação: Receber senha
    - Ação: Validar senha
    - Nó de Decisão 2: [Senha inválida] -> Nó Final | [Senha válida] -> Ação: Consultar saldo
    - Ação: Apresentar saldo -> Nó de Final de Atividade
    """
    print(f"\n  [Nó Inicial] Iniciando atividade 'Emitir Saldo'...")
    print(f"  [Ação 1] Receber número da conta: {numero_informado}")
    print(f"  [Ação 2] Consultar conta no repositório...")
    conta: Optional[ContaComum] = banco_contas.get(numero_informado)

    # Nó de Decisão 1
    if conta is None:
        print("  [Decisão 1 -> Guarda: Conta inválida] Conta não encontrada! Encerrando no Nó Final.")
        return

    print("  [Decisão 1 -> Guarda: Conta válida] Prosseguindo fluxo de controle...")
    print(f"  [Ação 3] Receber senha informada pelo cliente: {'*' * len(str(senha_informada))}")
    print("  [Ação 4] Validar senha...")

    # Nó de Decisão 2
    if not conta.validar_senha(senha_informada):
        print("  [Decisão 2 -> Guarda: Senha inválida] Autenticação recusada! Encerrando no Nó Final.")
        return

    print("  [Decisão 2 -> Guarda: Senha válida] Senha autenticada com sucesso!")
    saldo = conta.saldo_conta
    print(f"  [Ação 5] Consultar saldo do objeto ContaComum...")
    print(f"  [Ação 6] Apresentar saldo ao cliente: R$ {saldo:.2f}")
    print("  [Nó de Final de Atividade] Atividade concluída com sucesso.")


# ==============================================================================
# DEMONSTRAÇÃO GERAL DA AULA 21
# ==============================================================================
def executar():
    print("=" * 78)
    print("IFCE TAUÁ - ENGENHARIA DE SOFTWARE - AULA 21")
    print("Diagrama de Classes em Detalhes (Cap. 4) e Diagrama de Atividade (Cap. 10)")
    print("=" * 78)

    # 1. Associação Reflexiva com Papéis
    print("\n--- [1] ASSOCIAÇÃO REFLEXIVA / UNÁRIA E PAPÉIS (Fig. 4.4 e 4.5) ---")
    gerente = Funcionario("Carlos Eduardo", "Gerente de TI")
    dev1 = Funcionario("Ana Beatriz", "Desenvolvedora Back-End")
    dev2 = Funcionario("Lucas Mateus", "Desenvolvedor Front-End")
    gerente.adicionar_subordinado(dev1)
    gerente.adicionar_subordinado(dev2)
    print(gerente)
    print(dev1)
    print(dev2)

    # 2. Agregação, Herança, Restrição OCL e Atributo Derivado
    print("\n--- [2] AGREGAÇÃO, ATRIBUTO DERIVADO (/) E RESTRIÇÃO OCL (Fig. 4.10, 4.25, 4.51) ---")
    cliente_pf = PessoaFisica("Mariana Costa", "Av. Coronel Lourenço, Tauá-CE", 4500.0, "111.222.333-44", 24)
    conta = ContaComum(numero_conta=10509, senha_conta=123456)
    conta.depositar(1200.00)
    conta.sacar(350.00)
    cliente_pf.vincular_conta(conta)
    print(f"Titular: {cliente_pf._nome_pessoa} ({cliente_pf.documento_principal()})")
    print(f"Conta agregada: {cliente_pf.contas[0]}")

    # 3. Composição (Todo-Parte Forte)
    print("\n--- [3] COMPOSIÇÃO TODO-PARTE FORTE (Fig. 4.11) ---")
    revista = RevistaCientifica("Revista Brasileira de Engenharia de Software", 20269981, "Quadrimestral")
    ed1 = revista.publicar_edicao(
        numero=42,
        volume=14,
        titulos_artigos=[
            "Modelagem UML 2 em Sistemas Web Modernos",
            "Arquitetura em Camadas com Padrões Repository e DAO",
            "Verificação Formal com Restrições OCL",
        ],
    )
    print(f"Revista (Todo): {revista.titulo_revista} (ISSN: {revista.issn_revista})")
    print(f"  └── {ed1}")
    for art in ed1.artigos:
        print(f"        └── {art}")

    # 4. Classe Associativa e Realização de Interface
    print("\n--- [4] CLASSE ASSOCIATIVA E REALIZAÇÃO DE INTERFACE (Fig. 4.13 e 4.18) ---")
    ator = Ator("Wagner Moura")
    filme = Filme("Tropa de Elite", 115)
    vinculo = Atua(ator, filme, "Capitão Nascimento")
    print(vinculo)

    pedidos = [
        Pedido(501, 149.90, PagamentoCartaoCredito()),
        Pedido(502, 89.50, PagamentoCartaoDebito()),
        Pedido(503, 320.00, PagamentoBoleto()),
    ]
    for p in pedidos:
        print(" ", p.processar_quitacao())

    # 5. Execução Procedural do Diagrama de Atividade (Fig. 10.7)
    print("\n--- [5] EXECUÇÃO DO DIAGRAMA DE ATIVIDADE: EMITIR SALDO (Fig. 10.7) ---")
    repositorio_contas = {conta.numero_conta: conta}
    print("\nCenário A (Caminho Feliz - Guardas [Conta válida] e [Senha válida]):")
    atividade_emitir_saldo(repositorio_contas, numero_informado=10509, senha_informada=123456)

    print("\nCenário B (Desvio Condicional - Guarda [Senha inválida]):")
    atividade_emitir_saldo(repositorio_contas, numero_informado=10509, senha_informada=999999)

    print("=" * 78)


if __name__ == "__main__":
    executar()
