"""
IFCE Campus Tauá - Tecnologia em Telemática
Disciplina: Banco de Dados (2026.2)
Aula 06: Entidades Fracas e Modelo EER (Especialização/Generalização)
Prof. Me. Reginaldo Fernandes

Script didático de validação conceitual em Python puro (sem SQL).
Demonstra em memória com cenários cotidianos e intuitivos:
1. Entidades Fracas, Discriminador e Dependência de Existência/Identificação (Hotel e Quarto).
2. Modelo EER: Superclasses, Subclasses, Herança de Atributos e Restrições de Disjunção (Veículo, Carro e Caminhão).
"""

from enum import Enum
from typing import List, Dict, Any, Optional, Set


# ==============================================================================
# ENUMERAÇÕES CONCEITUAIS DO MODELO EER
# ==============================================================================

class RestricaoDisjuncao(Enum):
    """Define se uma entidade pode pertencer a mais de uma subclasse."""
    DISJUNTA = "d"       # Disjoint: pertence a no maximo uma subclasse
    SOBREPOSTA = "o"     # Overlapping: pode pertencer a multiplas subclasses


class RestricaoIntegralidade(Enum):
    """Define se toda instancia da superclasse deve obrigatoriamente pertencer a uma subclasse."""
    TOTAL = "Total (Linha Dupla)"       # Mandatory: toda superclasse e especializada
    PARCIAL = "Parcial (Linha Simples)" # Optional: instancia pode ser apenas superclasse


# ==============================================================================
# PARTE 1: ENTIDADES FRACAS E RELACIONAMENTOS IDENTIFICADORES (CENÁRIO HOTELEIRO)
# ==============================================================================

class Hotel:
    """
    Representa uma entidade regular/forte no MER.
    Possui chave primaria propria e independente no minimundo.
    Exemplo: HOTEL (identificado unicamente por id_hotel).
    """
    def __init__(self, id_hotel: int, nome: str, cidade: str):
        self.id_hotel = id_hotel
        self.nome = nome
        self.cidade = cidade
        self.quartos_associados: Dict[str, 'Quarto'] = {}

    def __repr__(self) -> str:
        return f"<Hotel id={self.id_hotel} nome='{self.nome}' cidade='{self.cidade}'>"


class Quarto:
    """
    Representa uma entidade fraca no MER.
    NÃO possui chave primaria propria independente.
    Seu atributo 'numero_quarto' atua apenas como discriminador (chave parcial).
    Sua chave completa e a tupla (id_hotel, numero_quarto).
    """
    def __init__(self, numero_quarto: str, tipo_leito: str, valor_diaria: float):
        self.numero_quarto = numero_quarto  # Chave Parcial / Discriminador (ex: '101', '102')
        self.tipo_leito = tipo_leito        # Atributo descritivo (ex: 'Casal', 'Duplo Solteiro')
        self.valor_diaria = valor_diaria
        self.hotel: Optional[Hotel] = None

    @property
    def chave_completa(self) -> Optional[tuple]:
        """Calcula a chave identificadora composta: (PK_Proprietario, Discriminador)."""
        if not self.hotel:
            return None
        return (self.hotel.id_hotel, self.numero_quarto)

    def __repr__(self) -> str:
        chave = self.chave_completa or "SEM_HOTEL"
        return f"<Quarto {chave} ({self.tipo_leito}, R$ {self.valor_diaria:.2f})>"


class RelacionamentoIdentificador:
    """
    Representa o relacionamento identificador (Losango Duplo de Chen).
    Garante:
    1. Dependencia de Existencia: O quarto nao existe sem o hotel.
    2. Dependencia de Identificacao: Unicidade do discriminador dentro do mesmo hotel.
    """
    def __init__(self, nome: str = "POSSUI_QUARTO"):
        self.nome = nome
        self.ligacoes: Dict[tuple, Quarto] = {}

    def vincular_quarto(self, hotel: Hotel, quarto: Quarto) -> None:
        """Associa uma entidade fraca ao seu hotel aplicando as regras de integridade."""
        if not isinstance(hotel, Hotel):
            raise TypeError("A entidade proprietaria deve ser uma instancia valida de Hotel!")

        # Regra de Unicidade do Discriminador dentro da mesma entidade proprietaria
        if quarto.numero_quarto in hotel.quartos_associados:
            raise ValueError(
                f"[VIOLACAO DE DISCRIMINADOR] O hotel '{hotel.nome}' (ID: {hotel.id_hotel}) "
                f"ja possui um quarto de numero '{quarto.numero_quarto}' cadastrado!"
            )

        # Estabelece o vinculo de dependencia
        quarto.hotel = hotel
        hotel.quartos_associados[quarto.numero_quarto] = quarto
        self.ligacoes[quarto.chave_completa] = quarto


# ==============================================================================
# PARTE 2: MODELO EER (ESPECIALIZAÇÃO, GENERALIZAÇÃO E HERANÇA - CENÁRIO DE VEÍCULOS)
# ==============================================================================

class Veiculo:
    """
    Superclasse no Modelo EER.
    Contem atributos comuns compartilhados por todos os veiculos da frota.
    """
    def __init__(self, placa: str, marca: str, modelo: str, ano: int):
        self.placa = placa  # Chave Primaria Universal
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.subclasses_vinculadas: Set[str] = set()

    def obter_atributos_comuns(self) -> Dict[str, Any]:
        return {
            "placa": self.placa,
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano
        }

    def __repr__(self) -> str:
        return f"<Veiculo Placa={self.placa} [{self.marca} {self.modelo} ({self.ano})]>"


class Carro(Veiculo):
    """Subclasse especializada de Carro com atributos exclusivos."""
    def __init__(self, placa: str, marca: str, modelo: str, ano: int,
                 quantidade_portas: int, capacidade_porta_malas_litros: int):
        super().__init__(placa, marca, modelo, ano)
        self.quantidade_portas = quantidade_portas
        self.capacidade_porta_malas_litros = capacidade_porta_malas_litros

    def detalhes_completos(self) -> Dict[str, Any]:
        dados = self.obter_atributos_comuns()
        dados.update({
            "tipo": "CARRO",
            "quantidade_portas": self.quantidade_portas,
            "capacidade_porta_malas_litros": self.capacidade_porta_malas_litros
        })
        return dados


class Caminhao(Veiculo):
    """Subclasse especializada de Caminhao com atributos exclusivos."""
    def __init__(self, placa: str, marca: str, modelo: str, ano: int,
                 capacidade_carga_toneladas: float, quantidade_eixos: int):
        super().__init__(placa, marca, modelo, ano)
        self.capacidade_carga_toneladas = capacidade_carga_toneladas
        self.quantidade_eixos = quantidade_eixos

    def detalhes_completos(self) -> Dict[str, Any]:
        dados = self.obter_atributos_comuns()
        dados.update({
            "tipo": "CAMINHAO",
            "capacidade_carga_toneladas": self.capacidade_carga_toneladas,
            "quantidade_eixos": self.quantidade_eixos
        })
        return dados


class ValidadorEER:
    """Valida as restricoes de Disjuncao e Integralidade no metamodelo EER."""
    def __init__(self, nome_hierarquia: str,
                 disjuncao: RestricaoDisjuncao,
                 integralidade: RestricaoIntegralidade):
        self.nome_hierarquia = nome_hierarquia
        self.disjuncao = disjuncao
        self.integralidade = integralidade
        self.registro_superclasses: Dict[str, Veiculo] = {}
        self.classificacoes: Dict[str, Set[str]] = {}

    def registrar_veiculo(self, veiculo: Veiculo) -> None:
        self.registro_superclasses[veiculo.placa] = veiculo
        self.classificacoes[veiculo.placa] = set()

    def especializar(self, placa: str, tipo_subclasse: str) -> None:
        """Associa uma superclasse a uma subclasse, testando a restricao de disjuncao."""
        if placa not in self.registro_superclasses:
            raise KeyError(f"Placa '{placa}' nao registrada na superclasse Veiculo!")

        subclasses_atuais = self.classificacoes[placa]

        # Verificacao de Disjuncao (d)
        if self.disjuncao == RestricaoDisjuncao.DISJUNTA and len(subclasses_atuais) > 0:
            subclasse_existente = list(subclasses_atuais)[0]
            raise ValueError(
                f"[VIOLACAO DE DISJUNCAO (d)] O veiculo '{placa}' ja foi classificado como "
                f"'{subclasse_existente}' e nao pode ser cumulativamente um '{tipo_subclasse}'!"
            )

        subclasses_atuais.add(tipo_subclasse)

    def auditar_integralidade_total(self) -> List[str]:
        """Identifica veiculos sem especializacao quando a regra for Total."""
        violacoes = []
        if self.integralidade == RestricaoIntegralidade.TOTAL:
            for placa, subs in self.classificacoes.items():
                if len(subs) == 0:
                    violacoes.append(placa)
        return violacoes


# ==============================================================================
# DEMONSTRAÇÃO PEDAGÓGICA INTERATIVA
# ==============================================================================

def executar_demonstracao():
    print("=" * 80)
    print("IFCE TAUÁ - AULA 06: ENTIDADES FRACAS E MODELO EER (CENÁRIOS COTIDIANOS)")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # CENÁRIO 1: Entidade Fraca e Chave Parcial (Discriminador) em Hotelaria
    # --------------------------------------------------------------------------
    print("\n--- [CENÁRIO 1] Teste de Entidade Fraca e Chave Composta (Hotel e Quarto) ---")
    rel_identificador = RelacionamentoIdentificador("POSSUI_QUARTO")

    # Criando duas entidades fortes (Hotéis)
    hotel_taua = Hotel(101, "Hotel Tauá Palace", "Tauá - CE")
    hotel_fortaleza = Hotel(202, "Beira Mar Hotel", "Fortaleza - CE")

    # Criando entidades fracas (Quartos com o mesmo discriminador '101')
    q1 = Quarto("101", "Casal Standard", 180.00)
    q2 = Quarto("101", "Suíte Luxo", 350.00)
    q3 = Quarto("102", "Duplo Solteiro", 150.00)

    print(f"Hotel Forte 1: {hotel_taua}")
    print(f"Hotel Forte 2: {hotel_fortaleza}")

    # Vinculando quartos aos seus respectivos hotéis proprietários
    rel_identificador.vincular_quarto(hotel_taua, q1)
    rel_identificador.vincular_quarto(hotel_fortaleza, q2)
    rel_identificador.vincular_quarto(hotel_taua, q3)

    print(f"\n[SUCESSO] Quartos cadastrados com chave composta identificadora:")
    print(f" - {q1} -> Chave Completa: {q1.chave_completa}")
    print(f" - {q2} -> Chave Completa: {q2.chave_completa}")
    print(f" - {q3} -> Chave Completa: {q3.chave_completa}")
    print(">> Note que o quarto '101' existe em ambos os hotéis sem nenhum conflito de unicidade!")

    # Teste de violação de discriminador no mesmo hotel
    print("\n[TESTE DE BLOQUEIO] Tentando adicionar outro quarto '101' no Hotel Tauá Palace...")
    quarto_duplicado = Quarto("101", "Individual Simples", 120.00)
    try:
        rel_identificador.vincular_quarto(hotel_taua, quarto_duplicado)
    except ValueError as e:
        print(f" >> SUCESSO NO BLOQUEIO: {e}")

    # --------------------------------------------------------------------------
    # CENÁRIO 2: Modelo EER - Herança de Atributos e Especialização de Veículos
    # --------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("--- [CENÁRIO 2] Modelo EER: Herança de Tipos e Atributos Especializados ---")

    # Criando objetos especializados com herança de atributos da superclasse Veículo
    meu_carro = Carro(
        placa="POQ-7F89",
        marca="Toyota",
        modelo="Corolla",
        ano=2024,
        quantidade_portas=4,
        capacidade_porta_malas_litros=470
    )

    meu_caminhao = Caminhao(
        placa="KLY-9B34",
        marca="Volvo",
        modelo="FH 540",
        ano=2023,
        capacidade_carga_toneladas=30.5,
        quantidade_eixos=6
    )

    print("\n[OBJETO CARRO] Atributos herdados (Veiculo) e específicos (Carro):")
    for k, v in meu_carro.detalhes_completos().items():
        print(f"  • {k:30}: {v}")

    print("\n[OBJETO CAMINHÃO] Atributos herdados (Veiculo) e específicos (Caminhao):")
    for k, v in meu_caminhao.detalhes_completos().items():
        print(f"  • {k:30}: {v}")

    # --------------------------------------------------------------------------
    # CENÁRIO 3: Validação de Restrição de Disjunção (d) e Integralidade Total
    # --------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("--- [CENÁRIO 3] Auditoria de Restrições EER: Disjunta (d) & Total ---")
    validador = ValidadorEER(
        nome_hierarquia="Taxonomia de Veículos da Frota",
        disjuncao=RestricaoDisjuncao.DISJUNTA,
        integralidade=RestricaoIntegralidade.TOTAL
    )

    v1 = Veiculo("ABC-1D23", "Chevrolet", "Onix", 2023)
    v2 = Veiculo("XYZ-9E87", "Scania", "R450", 2022)
    v3 = Veiculo("MNO-4K56", "Ford", "Ranger", 2024)

    validador.registrar_veiculo(v1)
    validador.registrar_veiculo(v2)
    validador.registrar_veiculo(v3)

    # Classificando v1 como CARRO e v2 como CAMINHAO
    validador.especializar("ABC-1D23", "CARRO")
    validador.especializar("XYZ-9E87", "CAMINHAO")

    # Tentando classificar v1 também como CAMINHÃO (Violação da Disjunção 'd')
    print("\n[TESTE DE BLOQUEIO] Tentando classificar 'ABC-1D23' (já Carro) como CAMINHÃO...")
    try:
        validador.especializar("ABC-1D23", "CAMINHAO")
    except ValueError as e:
        print(f" >> SUCESSO NO BLOQUEIO: {e}")

    # Auditoria de Integralidade Total: v3 ainda não foi especializado!
    pendencias = validador.auditar_integralidade_total()
    print(f"\n[AUDITORIA DE INTEGRALIDADE TOTAL]")
    print(f" >> Veículos pendentes de especialização obrigatória: {pendencias}")
    print(" >> Isso viola a regra de especialização Total (linha dupla no EER)!")
    print("=" * 80)


if __name__ == "__main__":
    executar_demonstracao()
