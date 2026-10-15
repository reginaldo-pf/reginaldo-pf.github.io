"""
IFCE Campus Tauá - Tecnologia em Telemática
Disciplina: Banco de Dados (2026.2)
Aula 06: Entidades Fracas e Modelo EER (Especialização/Generalização)
Prof. Me. Reginaldo Fernandes

Script didático de validação conceitual em Python puro (sem SQL).
Demonstra em memória:
1. Entidades Fracas, Discriminador e Dependência de Existência/Identificação.
2. Modelo EER: Superclasses, Subclasses, Herança de Atributos e Restrições de Disjunção.
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
    TOTAL = "Total (Linha Dupla)"     # Mandatory: toda superclasse e especializada
    PARCIAL = "Parcial (Linha Simples)" # Optional: instancia pode ser apenas superclasse


# ==============================================================================
# PARTE 1: ENTIDADES FRACAS E RELACIONAMENTOS IDENTIFICADORES
# ==============================================================================

class EntidadeForte:
    """
    Representa uma entidade regular/forte no MER.
    Possui chave primaria propria e independente no minimundo.
    Exemplo: DISPOSITIVO_REDE (identificado unicamente por ip_gestao).
    """
    def __init__(self, ip_gestao: str, hostname: str, localizacao: str):
        self.ip_gestao = ip_gestao
        self.hostname = hostname
        self.localizacao = localizacao
        self.portas_associadas: Dict[str, 'PortaInterface'] = {}

    def __repr__(self) -> str:
        return f"<Dispositivo ip={self.ip_gestao} host={self.hostname}>"


class PortaInterface:
    """
    Representa uma entidade fraca no MER.
    NÃO possui chave primaria propria independente.
    Seu atributo 'numero_porta' atua apenas como discriminador (chave parcial).
    Sua chave completa e a tupla (ip_gestao, numero_porta).
    """
    def __init__(self, numero_porta: str, tipo_midia: str, velocidade_mbps: int):
        self.numero_porta = numero_porta  # Chave Parcial / Discriminador
        self.tipo_midia = tipo_midia      # Atributo descritivo (ex: 'Fibra', 'Par Trancado')
        self.velocidade_mbps = velocidade_mbps
        self.dispositivo_proprietario: Optional[EntidadeForte] = None

    @property
    def chave_completa(self) -> Optional[tuple]:
        """Calcula a chave identificadora composta: (PK_Proprietario, Discriminador)."""
        if not self.dispositivo_proprietario:
            return None
        return (self.dispositivo_proprietario.ip_gestao, self.numero_porta)

    def __repr__(self) -> str:
        chave = self.chave_completa or "SEM_PROPRIETARIO"
        return f"<Porta {chave} ({self.tipo_midia}, {self.velocidade_mbps}Mbps)>"


class RelacionamentoIdentificador:
    """
    Representa o relacionamento identificador (Losango Duplo de Chen).
    Garante:
    1. Dependencia de Existencia: A porta nao existe sem o dispositivo.
    2. Dependencia de Identificacao: Unicidade do discriminador dentro do mesmo dispositivo.
    """
    def __init__(self, nome: str = "CONTEM_PORTA"):
        self.nome = nome
        self.ligacoes: Dict[tuple, PortaInterface] = {}

    def vincular_porta(self, dispositivo: EntidadeForte, porta: PortaInterface) -> None:
        """Associa uma entidade fraca ao seu proprietario aplicando as regras de integridade."""
        if not isinstance(dispositivo, EntidadeForte):
            raise TypeError("A entidade proprietaria deve ser uma EntidadeForte valida!")

        # Regra de Unicidade do Discriminador dentro da mesma entidade proprietaria
        if porta.numero_porta in dispositivo.portas_associadas:
            raise ValueError(
                f"[VIOLACAO DE DISCRIMINADOR] O dispositivo '{dispositivo.hostname}' "
                f"ja possui uma porta '{porta.numero_porta}' cadastrada!"
            )

        # Estabelece o vinculo de dependencia
        porta.dispositivo_proprietario = dispositivo
        dispositivo.portas_associadas[porta.numero_porta] = porta
        self.ligacoes[porta.chave_completa] = porta


# ==============================================================================
# PARTE 2: MODELO EER (ESPECIALIZAÇÃO, GENERALIZAÇÃO E HERANÇA)
# ==============================================================================

class DispositivoGenerico:
    """
    Superclasse no Modelo EER.
    Contem atributos comuns compartilhados por todos os dispositivos da infraestrutura.
    """
    def __init__(self, patrimonio: str, fabricante: str, modelo: str):
        self.patrimonio = patrimonio  # Chave Primaria Universal
        self.fabricante = fabricante
        self.modelo = modelo
        self.subclasses_vinculadas: Set[str] = set()

    def obter_atributos_comuns(self) -> Dict[str, Any]:
        return {
            "patrimonio": self.patrimonio,
            "fabricante": self.fabricante,
            "modelo": self.modelo
        }

    def __repr__(self) -> str:
        return f"<DispositivoGenerico #{self.patrimonio} [{self.fabricante} {self.modelo}]>"


class Roteador(DispositivoGenerico):
    """Subclasse especializada de Roteador com atributos exclusivos."""
    def __init__(self, patrimonio: str, fabricante: str, modelo: str,
                 tabela_rotas_max: int, suporta_bgp: bool):
        super().__init__(patrimonio, fabricante, modelo)
        self.tabela_rotas_max = tabela_rotas_max
        self.suporta_bgp = suporta_bgp

    def detalhes_completos(self) -> Dict[str, Any]:
        dados = self.obter_atributos_comuns()
        dados.update({
            "tipo": "ROTEADOR",
            "tabela_rotas_max": self.tabela_rotas_max,
            "suporta_bgp": self.suporta_bgp
        })
        return dados


class Switch(DispositivoGenerico):
    """Subclasse especializada de Switch com atributos exclusivos."""
    def __init__(self, patrimonio: str, fabricante: str, modelo: str,
                 quantidade_portas: int, capacidade_switching_gbps: float):
        super().__init__(patrimonio, fabricante, modelo)
        self.quantidade_portas = quantidade_portas
        self.capacidade_switching_gbps = capacidade_switching_gbps

    def detalhes_completos(self) -> Dict[str, Any]:
        dados = self.obter_atributos_comuns()
        dados.update({
            "tipo": "SWITCH",
            "quantidade_portas": self.quantidade_portas,
            "capacidade_switching_gbps": self.capacidade_switching_gbps
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
        self.registro_superclasses: Dict[str, DispositivoGenerico] = {}
        self.classificacoes: Dict[str, Set[str]] = {}

    def registrar_dispositivo(self, disp: DispositivoGenerico) -> None:
        self.registro_superclasses[disp.patrimonio] = disp
        self.classificacoes[disp.patrimonio] = set()

    def especializar(self, patrimonio: str, tipo_subclasse: str) -> None:
        """Associa uma superclasse a uma subclasse, testando a restricao de disjuncao."""
        if patrimonio not in self.registro_superclasses:
            raise KeyError(f"Patrimonio '{patrimonio}' nao registrado na superclasse!")

        subclasses_atuais = self.classificacoes[patrimonio]

        # Verificacao de Disjuncao (d)
        if self.disjuncao == RestricaoDisjuncao.DISJUNTA and len(subclasses_atuais) > 0:
            subclasse_existente = list(subclasses_atuais)[0]
            raise ValueError(
                f"[VIOLACAO DE DISJUNCAO (d)] O equipamento '{patrimonio}' ja foi classificado como "
                f"'{subclasse_existente}' e nao pode ser cumulativamente um '{tipo_subclasse}'!"
            )

        subclasses_atuais.add(tipo_subclasse)

    def auditar_integralidade_total(self) -> List[str]:
        """Identifica equipamentos sem especializacao quando a regra for Total."""
        violacoes = []
        if self.integralidade == RestricaoIntegralidade.TOTAL:
            for pat, subs in self.classificacoes.items():
                if len(subs) == 0:
                    violacoes.append(pat)
        return violacoes


# ==============================================================================
# DEMONSTRAÇÃO PEDAGÓGICA INTERATIVA
# ==============================================================================

def executar_demonstracao():
    print("=" * 80)
    print("IFCE TAUÁ - AULA 06: ENTIDADES FRACAS E MODELO EER EM TELEMÁTICA")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # CENÁRIO 1: Entidade Fraca e Chave Parcial (Discriminador)
    # --------------------------------------------------------------------------
    print("\n--- [CENÁRIO 1] Teste de Entidade Fraca e Chave Composta ---")
    rel_identificador = RelacionamentoIdentificador("CONTEM_PORTA")

    # Criando duas entidades fortes (Roteadores)
    rt_taua = EntidadeForte("10.0.1.1", "RT-IFCE-TAUA", "Rack Central Tauá")
    sw_taua = EntidadeForte("10.0.1.2", "SW-CORE-TAUA", "Rack Central Tauá")

    # Criando entidades fracas (Portas com o mesmo discriminador 'Gi0/1')
    p1 = PortaInterface("Gi0/1", "Fibra Óptica", 1000)
    p2 = PortaInterface("Gi0/1", "Par Trançado", 1000)
    p3 = PortaInterface("Gi0/2", "Par Trançado", 1000)

    print(f"Dispositivo Forte 1: {rt_taua}")
    print(f"Dispositivo Forte 2: {sw_taua}")

    # Vinculando portas aos seus respectivos proprietarios
    rel_identificador.vincular_porta(rt_taua, p1)
    rel_identificador.vincular_porta(sw_taua, p2)
    rel_identificador.vincular_porta(rt_taua, p3)

    print(f"\n[SUCESSO] Portas cadastradas com chave composta:")
    print(f" - {p1} -> Chave: {p1.chave_completa}")
    print(f" - {p2} -> Chave: {p2.chave_completa}")
    print(f" - {p3} -> Chave: {p3.chave_completa}")
    print(">> Note que 'Gi0/1' pode existir em ambos os dispositivos sem conflito de PK!")

    # Teste de violacao de discriminador no mesmo dispositivo
    print("\n[TESTE DE BLOQUEIO] Tentando adicionar outra porta 'Gi0/1' no RT-IFCE-TAUA...")
    porta_duplicada = PortaInterface("Gi0/1", "Par Trançado", 100)
    try:
        rel_identificador.vincular_porta(rt_taua, porta_duplicada)
    except ValueError as e:
        print(f" >> SUCESSO NO BLOQUEIO: {e}")

    # --------------------------------------------------------------------------
    # CENÁRIO 2: Modelo EER - Herança de Atributos e Especialização Disjunta
    # --------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("--- [CENÁRIO 2] Modelo EER: Herança de Tipos e Restrições ---")

    # Criando objetos especializados com herança de atributos
    meu_roteador = Roteador(
        patrimonio="PAT-2026-001",
        fabricante="Cisco Systems",
        modelo="ASR 1001-X",
        tabela_rotas_max=1000000,
        suporta_bgp=True
    )

    meu_switch = Switch(
        patrimonio="PAT-2026-002",
        fabricante="Huawei",
        modelo="CloudEngine S5735",
        quantidade_portas=48,
        capacidade_switching_gbps=176.0
    )

    print("\n[OBJETO ROTEADOR] Atributos herdados e especializados:")
    for k, v in meu_roteador.detalhes_completos().items():
        print(f"  • {k:22}: {v}")

    print("\n[OBJETO SWITCH] Atributos herdados e especializados:")
    for k, v in meu_switch.detalhes_completos().items():
        print(f"  • {k:22}: {v}")

    # --------------------------------------------------------------------------
    # CENÁRIO 3: Validação de Restrição de Disjunção (d) e Integralidade Total
    # --------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("--- [CENÁRIO 3] Auditoria de Restrições EER: Disjunta (d) & Total ---")
    validador = ValidadorEER(
        nome_hierarquia="Taxonomia de Equipamentos",
        disjuncao=RestricaoDisjuncao.DISJUNTA,
        integralidade=RestricaoIntegralidade.TOTAL
    )

    d1 = DispositivoGenerico("PAT-101", "Cisco", "Catalyst 2960")
    d2 = DispositivoGenerico("PAT-102", "MikroTik", "CCR1036")
    d3 = DispositivoGenerico("PAT-103", "Dell", "PowerEdge R740")

    validador.registrar_dispositivo(d1)
    validador.registrar_dispositivo(d2)
    validador.registrar_dispositivo(d3)

    # Classificando d1 como Switch e d2 como Roteador
    validador.especializar("PAT-101", "SWITCH")
    validador.especializar("PAT-102", "ROTEADOR")

    # Tentando classificar d1 tambem como ROTEADOR (Violacao da Disjuncao)
    print("\n[TESTE DE BLOQUEIO] Tentando classificar PAT-101 (Switch) como ROTEADOR...")
    try:
        validador.especializar("PAT-101", "ROTEADOR")
    except ValueError as e:
        print(f" >> SUCESSO NO BLOQUEIO: {e}")

    # Auditoria de Integralidade Total: d3 ainda nao foi especializado!
    pendencias = validador.auditar_integralidade_total()
    print(f"\n[AUDITORIA DE INTEGRALIDADE TOTAL]")
    print(f" >> Equipamentos pendentes de especialização obrigatória: {pendencias}")
    print(" >> Isso viola a regra de especialização Total (linha dupla no EER)!")
    print("=" * 80)


if __name__ == "__main__":
    executar_demonstracao()
