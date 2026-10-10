"""
Banco de Dados - Tecnologia em Telemática (IFCE Campus Tauá)
Aula 04: Aplicação da Lista de Exercícios 01 (N1) - Atividade Avaliativa Assíncrona
Docente: Prof. Me. Reginaldo Pereira Fernandes

Script didático de apoio para verificação conceitual, validação de taxonomia
de atributos e geração automatizada de diagramas (Peter Chen e ANSI/SPARC) em
notação Mermaid para apoio à resolução da Lista de Exercícios 01 (N1).

OBSERVAÇÃO PEDAGÓGICA:
Esta avaliação é 100% conceitual e de modelagem. O discente NÃO precisa
escrever ou executar comandos SQL nesta etapa (o conteúdo de SQL será ministrado
no Período N2).
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Callable, Dict, Any


class TipoAtributo(Enum):
    IDENTIFICADOR = "Identificador (Chave Primária Conceitual - Sublinhado no DER)"
    SIMPLES = "Simples / Atômico (Elipse Sólida Simples)"
    COMPOSTO = "Composto (Elipse Ramificada)"
    MULTIVALORADO = "Multivalorado (Elipse Dupla Concêntrica)"
    DERIVADO = "Derivado (Elipse com Borda Tracejada)"


@dataclass
class DefinicaoAtributo:
    nome: str
    tipo: TipoAtributo
    subatributos: List['DefinicaoAtributo'] = field(default_factory=list)
    regra_derivacao: Optional[str] = None
    funcao_calculo: Optional[Callable[[Dict[str, Any]], Any]] = None
    permite_nulo: bool = False

    def validar_valor(self, valor: Any) -> bool:
        """Valida a conformidade conceitual do dado com o tipo do atributo."""
        if valor is None:
            return self.permite_nulo or self.tipo == TipoAtributo.DERIVADO

        if self.tipo == TipoAtributo.MULTIVALORADO:
            return isinstance(valor, (list, set, tuple))
        elif self.tipo == TipoAtributo.COMPOSTO:
            return isinstance(valor, dict)
        return True


@dataclass
class EsquemaEntidade:
    nome: str
    atributos: List[DefinicaoAtributo]

    def obter_identificador(self) -> Optional[DefinicaoAtributo]:
        for attr in self.atributos:
            if attr.tipo == TipoAtributo.IDENTIFICADOR:
                return attr
        return None

    def gerar_mermaid_chen(self) -> str:
        """
        Gera a definição em sintaxe Mermaid representando o Diagrama
        Entidade-Relacionamento canônico de Peter Chen (1976).
        """
        linhas = ["flowchart TD"]
        id_entidade = f"ent_{self.nome}"
        linhas.append(f'    {id_entidade}["{self.nome}"]:::entidade')

        for i, attr in enumerate(self.atributos):
            id_attr = f"attr_{self.nome}_{i}"
            
            if attr.tipo == TipoAtributo.IDENTIFICADOR:
                linhas.append(f'    {id_attr}(["<u>{attr.nome}</u>"]):::chave')
                linhas.append(f"    {id_entidade} --- {id_attr}")
                
            elif attr.tipo == TipoAtributo.SIMPLES:
                linhas.append(f'    {id_attr}(["{attr.nome}"]):::simples')
                linhas.append(f"    {id_entidade} --- {id_attr}")
                
            elif attr.tipo == TipoAtributo.MULTIVALORADO:
                linhas.append(f'    {id_attr}([["{attr.nome}"]]):::multivalorado')
                linhas.append(f"    {id_entidade} --- {id_attr}")
                
            elif attr.tipo == TipoAtributo.DERIVADO:
                linhas.append(f'    {id_attr}-.- {id_entidade}')
                linhas.append(f'    {id_attr}(["{attr.nome}"]):::derivado')
                
            elif attr.tipo == TipoAtributo.COMPOSTO:
                linhas.append(f'    {id_attr}(["{attr.nome}"]):::composto')
                linhas.append(f"    {id_entidade} --- {id_attr}")
                for j, sub in enumerate(attr.subatributos):
                    id_sub = f"{id_attr}_sub_{j}"
                    linhas.append(f'    {id_sub}(["{sub.nome}"]):::simples')
                    linhas.append(f"    {id_attr} --- {id_sub}")

        linhas.append("")
        linhas.append("    classDef entidade fill:#059669,stroke:#047857,stroke-width:2px,color:#ffffff,font-weight:bold;")
        linhas.append("    classDef chave fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1,font-weight:bold;")
        linhas.append("    classDef simples fill:#f1f5f9,stroke:#64748b,stroke-width:1.5px,color:#1e293b;")
        linhas.append("    classDef composto fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#92400e;")
        linhas.append("    classDef multivalorado fill:#fce7f3,stroke:#db2777,stroke-width:3px,color:#9d174d;")
        linhas.append("    classDef derivado fill:#ede9fe,stroke:#7c3aed,stroke-dasharray: 5 5,stroke-width:2px,color:#5b21b6;")

        return "\n".join(linhas)


def gerar_diagrama_ansisparc_mermaid() -> str:
    """Gera o diagrama Mermaid da Arquitetura ANSI/SPARC de 3 Níveis para a Questão 9."""
    return """flowchart TB
    subgraph NIVEL_EXTERNO ["NÍVEL EXTERNO (Visões de Usuários e Aplicações)"]
        direction LR
        V1["Visão 1: Portal do Operador do NOC<br/>(Topologia e Alarmes)"]
        V2["Visão 2: Dashboard do Gestor de TI<br/>(Uptime e Disponibilidade)"]
        V3["Visão 3: Faturamento do Provedor<br/>(Tráfego de Enlaces e Clientes)"]
    end

    subgraph MAPEAMENTO_1 ["Mapeamento Externo-Conceitual"]
        direction TB
        M1["Assegura Independência Lógica de Dados"]
    end

    subgraph NIVEL_CONCEITUAL ["NÍVEL CONCEITUAL (Esquema Lógico Global da Organização)"]
        C1["Esquema Conceitual Global Unificado<br/>Entidades: POP, ENLACE, DISPOSITIVO, CLIENTE<br/>Restrições de Integridade & Regras de Negócio"]
    end

    subgraph MAPEAMENTO_2 ["Mapeamento Conceitual-Interno"]
        direction TB
        M2["Assegura Independência Física de Dados"]
    end

    subgraph NIVEL_INTERNO ["NÍVEL INTERNO (Esquema Físico de Armazenamento)"]
        direction LR
        I1["Arquivos de Dados em Disco<br/>(Alocação Física)"]
        I2["Índices B-Tree & Hash<br/>(Aceleração de Busca)"]
        I3["Páginas de Buffer Pool<br/>(Gerenciamento de Memória)"]
    end

    subgraph CATALOGO ["CATÁLOGO DO SISTEMA (Dicionário de Metadados)"]
        CAT["Repositório Central de Metadados<br/>Definições de Esquemas, Tipos e Restrições<br/>Consultado por: Otimizador CBO e Motor de Segurança"]
    end

    NIVEL_EXTERNO <--> MAPEAMENTO_1
    MAPEAMENTO_1 <--> NIVEL_CONCEITUAL
    NIVEL_CONCEITUAL <--> MAPEAMENTO_2
    MAPEAMENTO_2 <--> NIVEL_INTERNO

    CAT -. Metadados de Visões .- NIVEL_EXTERNO
    CAT -. Esquema e Entidades .- NIVEL_CONCEITUAL
    CAT -. Índices e Armazenamento .- NIVEL_INTERNO

    classDef nivel fill:#f8fafc,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef catalogo fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f,font-weight:bold;
    class CAT catalogo;
"""


# ==============================================================================
# Modelos para as questões de diagramas da Lista 01 (N1)
# ==============================================================================

def construir_esquema_questao_13() -> EsquemaEntidade:
    """Modelo da Questão 13: SERVIDOR_VIRTUALIZADO."""
    return EsquemaEntidade(
        nome="SERVIDOR_VIRTUALIZADO",
        atributos=[
            DefinicaoAtributo(nome="uuid_maquina", tipo=TipoAtributo.IDENTIFICADOR),
            DefinicaoAtributo(nome="nome_virtual", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(nome="memoria_ram_gb", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(
                nome="alocacao_cluster",
                tipo=TipoAtributo.COMPOSTO,
                subatributos=[
                    DefinicaoAtributo(nome="nome_datacenter", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="host_fisico_id", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="storage_pool", tipo=TipoAtributo.SIMPLES),
                ]
            ),
            DefinicaoAtributo(nome="enderecos_ip_interfaces", tipo=TipoAtributo.MULTIVALORADO),
            DefinicaoAtributo(
                nome="custo_estimado_mensal",
                tipo=TipoAtributo.DERIVADO,
                regra_derivacao="(ram_gb * 15.00) + (storage_gb * 0.50)",
                funcao_calculo=lambda d: (d.get("memoria_ram_gb", 0) * 15.0) + (d.get("storage_capacidade_gb", 0) * 0.5)
            )
        ]
    )


def construir_esquemas_questao_14() -> List[EsquemaEntidade]:
    """Modelos da Questão 14: Minimundo do Backbone do IFCE."""
    ent_pop = EsquemaEntidade(
        nome="PONTO_DE_PRESENCA",
        atributos=[
            DefinicaoAtributo(nome="id_pop", tipo=TipoAtributo.IDENTIFICADOR),
            DefinicaoAtributo(nome="cidade", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(
                nome="endereco_completo",
                tipo=TipoAtributo.COMPOSTO,
                subatributos=[
                    DefinicaoAtributo(nome="logradouro", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="bairro", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="numero", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="cep", tipo=TipoAtributo.SIMPLES),
                ]
            ),
            DefinicaoAtributo(nome="telefones_contato", tipo=TipoAtributo.MULTIVALORADO),
            DefinicaoAtributo(
                nome="disponibilidade_anual_percentual",
                tipo=TipoAtributo.DERIVADO,
                regra_derivacao="(horas_uptime_ano / 8760.0) * 100.0"
            )
        ]
    )

    ent_enlace = EsquemaEntidade(
        nome="ENLACE_OPTICO",
        atributos=[
            DefinicaoAtributo(nome="codigo_enlace", tipo=TipoAtributo.IDENTIFICADOR),
            DefinicaoAtributo(nome="distancia_km", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(nome="atenuacao_db_km", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(nome="tipo_fibra", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(nome="comprimentos_onda_nm", tipo=TipoAtributo.MULTIVALORADO),
        ]
    )

    ent_equip = EsquemaEntidade(
        nome="EQUIPAMENTO_TRANSMISSAO",
        atributos=[
            DefinicaoAtributo(nome="patrimonio_id", tipo=TipoAtributo.IDENTIFICADOR),
            DefinicaoAtributo(nome="modelo", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(
                nome="slot_rack",
                tipo=TipoAtributo.COMPOSTO,
                subatributos=[
                    DefinicaoAtributo(nome="sala_noc", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="numero_rack", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="posicao_u", tipo=TipoAtributo.SIMPLES),
                ]
            ),
            DefinicaoAtributo(nome="data_instalacao", tipo=TipoAtributo.SIMPLES),
        ]
    )

    return [ent_pop, ent_enlace, ent_equip]


def construir_esquema_questao_15() -> EsquemaEntidade:
    """Modelo da Questão 15: ROTEADOR_CLIENTE desdobrado."""
    return EsquemaEntidade(
        nome="ROTEADOR_CLIENTE",
        atributos=[
            DefinicaoAtributo(nome="roteador_id", tipo=TipoAtributo.IDENTIFICADOR),
            DefinicaoAtributo(nome="fabricante", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(nome="modelo", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(
                nome="localizacao_fisica",
                tipo=TipoAtributo.COMPOSTO,
                subatributos=[
                    DefinicaoAtributo(nome="predio", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="sala", tipo=TipoAtributo.SIMPLES),
                    DefinicaoAtributo(nome="andar", tipo=TipoAtributo.SIMPLES),
                ]
            ),
            DefinicaoAtributo(nome="enderecos_dns_configurados", tipo=TipoAtributo.MULTIVALORADO),
            DefinicaoAtributo(nome="data_compra", tipo=TipoAtributo.SIMPLES),
            DefinicaoAtributo(
                nome="anos_de_uso",
                tipo=TipoAtributo.DERIVADO,
                regra_derivacao="ano_atual - ano_compra"
            )
        ]
    )


def validar_instancia_exemplo():
    """Demonstração de validação semântica em Python puro sem dependência de SQL."""
    esquema = construir_esquema_questao_13()
    
    dados_exemplo = {
        "uuid_maquina": "e4d3c2b1-a098-7654-3210-abcdef012345",
        "nome_virtual": "srv-monitor-ifce",
        "memoria_ram_gb": 64,
        "alocacao_cluster": {
            "nome_datacenter": "Datacenter IFCE Tauá",
            "host_fisico_id": "blade-cluster-01",
            "storage_pool": "ceph-pool-nvme"
        },
        "storage_capacidade_gb": 1000,
        "enderecos_ip_interfaces": ["10.0.1.10", "192.168.10.1", "200.17.42.1"]
    }
    
    print("=" * 70)
    print("VALIDAÇÃO CONCEITUAL DE INSTÂNCIA EM PYTHON (PETER CHEN)")
    print("=" * 70)
    print(f"Entidade: {esquema.nome}")
    print(f"Chave Identificadora: {esquema.obter_identificador().nome} -> {dados_exemplo['uuid_maquina']}")
    print(f"Atributo Composto (desdobrado): {dados_exemplo['alocacao_cluster']}")
    print(f"Atributo Multivalorado (conjunto de IPs): {dados_exemplo['enderecos_ip_interfaces']}")
    
    # Cálculo dinâmico do atributo derivado
    attr_derivado = [a for a in esquema.atributos if a.tipo == TipoAtributo.DERIVADO][0]
    custo_calculado = attr_derivado.funcao_calculo(dados_exemplo)
    print(f"Atributo Derivado '{attr_derivado.nome}' [{attr_derivado.regra_derivacao}]: R$ {custo_calculado:.2f}")
    print("=" * 70)


if __name__ == "__main__":
    print("\n[1] GERADOR DE DIAGRAMA MERMAID: PETER CHEN (Questão 13):")
    print("-" * 50)
    q13 = construir_esquema_questao_13()
    print(q13.gerar_mermaid_chen())
    print("-" * 50)

    print("\n[2] GERADOR DE DIAGRAMA MERMAID: ARQUITETURA ANSI/SPARC (Questão 9):")
    print("-" * 50)
    print(gerar_diagrama_ansisparc_mermaid())
    print("-" * 50)

    print("\n[3] VALIDAÇÃO CONCEITUAL DE ATRIBUTOS (SEM SQL):")
    validar_instancia_exemplo()
