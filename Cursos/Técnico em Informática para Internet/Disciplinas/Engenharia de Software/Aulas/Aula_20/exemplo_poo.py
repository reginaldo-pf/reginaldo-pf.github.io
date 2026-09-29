#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
IFCE Campus Tauá - Técnico em Informática para Internet
Disciplina: Engenharia de Software
Aula 20: Introdução à UML, Revisão de OO e Casos de Uso

Mapeamento entre Modelos UML e Código Orientado a Objetos
Baseado nos Capítulos 1 e 2 do livro:
"UML 2 - Uma abordagem prática" (Gilleanes T. A. Guedes)
"""

from typing import List


# ==============================================================================
# 1. CLASSE PESSOA (Figuras 2.1 a 2.4 do Livro)
# ==============================================================================
class Pessoa:
    """
    Representação da classe Pessoa (Figura 2.4 do livro de Guedes).
    
    Notação UML correspondente:
    -----------------------------------
    |             Pessoa              |
    -----------------------------------
    | - cpf: str                      |
    | - nome: str                     |
    | - idade: int                    |
    -----------------------------------
    | + pensar(): str                 |
    | + get_cpf(): str                |
    | + get_nome(): str               |
    | + get_idade(): int              |
    | + set_idade(nova_idade: int)    |
    -----------------------------------
    """

    def __init__(self, cpf: str, nome: str, idade: int):
        # Visibilidade privada na UML (-) mapeada com prefixo duplo sublinhado (__):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = max(0, idade)

    # Métodos de Acesso (Getters / Setters) para Encapsulamento:
    @property
    def cpf(self) -> str:
        """Acesso somente leitura ao CPF (privado)."""
        return self.__cpf

    @property
    def nome(self) -> str:
        """Acesso ao nome (privado)."""
        return self.__nome

    @property
    def idade(self) -> int:
        """Acesso à idade (privado)."""
        return self.__idade

    @idade.setter
    def idade(self, nova_idade: int):
        """Validação de integridade ao alterar a idade."""
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            raise ValueError("Idade nao pode ser negativa.")

    # Operação / Método de Comportamento (+):
    def pensar(self) -> str:
        """Operação pública +pensar() da Figura 2.4."""
        return f"{self.__nome} está pensando em soluções de software..."

    def __str__(self) -> str:
        return f"[Pessoa] Nome: {self.__nome} | CPF: {self.__cpf} | Idade: {self.__idade} anos"


# ==============================================================================
# 2. HIERARQUIA ANIMAL E HERANÇA MÚLTIPLA (Figuras 2.5 e 2.6 do Livro)
# ==============================================================================
class Animal:
    """Superclasse genérica com comportamento comum (Figura 2.5)."""

    def __init__(self, especie: str):
        self._especie = especie  # Visibilidade protegida (#)

    def locomover(self) -> str:
        """Operação comum a todos os animais."""
        return f"O animal da espécie {self._especie} está se locomovendo."


class Mamifero(Animal):
    """Subclasse de Animal que herda locomover() e adiciona características de mamíferos."""

    def __init__(self, especie: str, tem_pelos: bool = True):
        super().__init__(especie)
        self._tem_pelos = tem_pelos  # Atributo protegido (#)

    def mamar(self) -> str:
        return f"{self._especie} está amamentando seus filhotes."


class Ave(Animal):
    """Subclasse de Animal que herda locomover() e adiciona características de aves."""

    def __init__(self, especie: str, formato_bico: str = "curvo"):
        super().__init__(especie)
        self._formato_bico = formato_bico  # Atributo protegido (#)

    def por_ovos(self) -> str:
        return f"{self._especie} colocou ovos no ninho."


class Ornitorrinco(Mamifero, Ave):
    """
    Exemplo de Herança Múltipla (Figura 2.6 do livro de Guedes).
    O Ornitorrinco herda comportamentos e atributos de Mamifero e Ave simultaneamente.
    """

    def __init__(self, nome: str):
        # Inicialização cooperativa respeitando o MRO do Python:
        Animal.__init__(self, especie="Ornithorhynchus anatinus")
        self._tem_pelos = True
        self._formato_bico = "formato de pato"
        self.nome = nome

    def emitir_som(self) -> str:
        return f"O ornitorrinco {self.nome} produz ruídos característicos!"


# ==============================================================================
# 3. POLIMORFISMO E SOBRESCRITA DE MÉTODOS (Figura 2.7 do Livro)
# ==============================================================================
class ContaComum:
    """
    Superclasse de Conta Bancária (Figura 2.7 do livro de Guedes).
    
    Notação UML:
    -----------------------------------
    |           ContaComum            |
    -----------------------------------
    | # numero: str                   |
    | # saldo: float                  |
    -----------------------------------
    | + depositar(valor: float): bool |
    | + saque(valor: float): bool     |
    -----------------------------------
    """

    def __init__(self, numero: str, saldo_inicial: float = 0.0):
        self._numero = numero
        self._saldo = float(saldo_inicial)

    @property
    def numero(self) -> str:
        return self._numero

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            return True
        return False

    def saque(self, valor: float) -> bool:
        """
        Saque da ContaComum: restrito estritamente ao saldo disponível em conta.
        """
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    def __str__(self) -> str:
        return f"ContaComum Nº {self._numero} | Saldo: R$ {self._saldo:.2f}"


class ContaEspecial(ContaComum):
    """
    Subclasse com Sobrescrita Polimórfica (Figura 2.7 do livro de Guedes).
    
    Notação UML:
    -----------------------------------
    |          ContaEspecial          |
    -----------------------------------
    | # limite: float                 |
    -----------------------------------
    | + saque(valor: float): bool     |
    -----------------------------------
    """

    def __init__(self, numero: str, saldo_inicial: float = 0.0, limite: float = 500.0):
        super().__init__(numero, saldo_inicial)
        self._limite = float(limite)

    @property
    def limite(self) -> float:
        return self._limite

    def saque(self, valor: float) -> bool:
        """
        Polimorfismo (Override): A ContaEspecial permite saques que ultrapassem
        o saldo atual, desde que não excedam (saldo + limite).
        """
        saldo_total_disponivel = self._saldo + self._limite
        if 0 < valor <= saldo_total_disponivel:
            self._saldo -= valor
            return True
        return False

    def __str__(self) -> str:
        return (f"ContaEspecial Nº {self._numero} | Saldo: R$ {self._saldo:.2f} "
                f"| Limite de Crédito: R$ {self._limite:.2f} "
                f"| Disponível Total: R$ {(self._saldo + self._limite):.2f}")


# ==============================================================================
# EXECUÇÃO E TESTES
# ==============================================================================
def executar():
    print("=" * 70)
    print("IFCE TAUÁ - ENGENHARIA DE SOFTWARE - AULA 20: POO E UML")
    print("Exemplos dos Capítulos 1 e 2 (Gilleanes Guedes)")
    print("=" * 70)

    # 1. Demonstração de Classe, Atributos, Métodos e Visibilidade
    print("\n--- [1] CLASSE, ENCAPSULAMENTO E VISIBILIDADE (Fig. 2.1 a 2.4) ---")
    p1 = Pessoa(cpf="123.456.789-00", nome="Maria Silva", idade=19)
    print(p1)
    print(p1.pensar())
    try:
        # Tentativa de acesso direto a atributo privado da UML:
        print(p1.__cpf)
    except AttributeError:
        print("[Encapsulamento Ativo]: Atributo __cpf é privado e não pode ser acessado de fora da classe!")

    # 2. Demonstração de Herança Simples e Múltipla
    print("\n--- [2] HERANÇA SIMPLES E MÚLTIPLA (Fig. 2.5 e 2.6) ---")
    ornit = Ornitorrinco(nome="Perry")
    print(f"Instância criada: {ornit.nome}")
    print(f"• Método herdado de Animal: {ornit.locomover()}")
    print(f"• Método herdado de Mamifero: {ornit.mamar()}")
    print(f"• Método herdado de Ave: {ornit.por_ovos()}")
    print(f"• Atributo herdado de Ave: Bico com {ornit._formato_bico}")
    print(f"• Som próprio: {ornit.emitir_som()}")
    print(f"• Ordem de Resolução de Métodos (MRO): {[c.__name__ for c in Ornitorrinco.__mro__]}")

    # 3. Demonstração de Polimorfismo
    print("\n--- [3] POLIMORFISMO E SOBRESCRITA DE MÉTODOS (Fig. 2.7) ---")
    conta_comum = ContaComum(numero="1001-X", saldo_inicial=200.0)
    conta_especial = ContaEspecial(numero="2002-Y", saldo_inicial=200.0, limite=500.0)

    contas: List[ContaComum] = [conta_comum, conta_especial]
    valor_saque = 400.0

    print(f"Tentativa de saque de R$ {valor_saque:.2f} em ambas as contas:\n")
    for c in contas:
        print(f"Antes: {c}")
        sucesso = c.saque(valor_saque)
        resultado = "EFETUADO COM SUCESSO" if sucesso else "RECUSADO (SALDO INSUFICIENTE)"
        print(f"Saque de R$ {valor_saque:.2f} -> {resultado}")
        print(f"Depois: {c}\n")

    print("=" * 70)
    print("O mesmo método saque() executa comportamentos diferentes")
    print("dinamicamente dependendo da classe instanciada (Polimorfismo).")
    print("=" * 70)


if __name__ == "__main__":
    executar()
