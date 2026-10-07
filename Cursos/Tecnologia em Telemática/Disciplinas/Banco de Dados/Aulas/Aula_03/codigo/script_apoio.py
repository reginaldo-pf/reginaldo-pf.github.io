#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Apoio Didático - Aula 03
Disciplina: Banco de Dados | Tecnologia em Telemática
IFCE Campus Tauá | Prof. Reginaldo Pereira Fernandes

Tópicos Abordados:
1. Ciclo de Vida do Projeto de Banco de Dados (Requisitos -> Conceitual -> Lógico -> Físico)
2. Modelo Entidade-Relacionamento (MER): Peter Chen (1976)
3. Conceitos de Entidade, Conjunto de Entidades (Entity Set) e Instância
4. Taxonomia Completa de Atributos:
   - Atributo Identificador (Chave Conceitual)
   - Atributos Simples (Atômicos)
   - Atributos Compostos (Hierárquicos)
   - Atributos Multivalorados (Conjuntos)
   - Atributos Armazenados vs. Derivados (Cálculo dinâmico)
5. Simulação de Mapeamento Pré-Relacional no SQLite (1FN e Decomposição)
"""

from enum import Enum
from datetime import datetime, date
from typing import Any, Dict, List, Optional, Callable
import sqlite3


# ==============================================================================
# 1. METAMODELO CONCEITUAL DO MER EM PYTHON
# ==============================================================================

class TipoAtributo(Enum):
    IDENTIFICADOR = "Chave Identificadora (Sublinhado no DER)"
    SIMPLES = "Simples / Atômico (Elipse simples no DER)"
    COMPOSTO = "Composto (Elipse ramificada no DER)"
    MULTIVALORADO = "Multivalorado (Elipse dupla no DER)"
    DERIVADO = "Derivado (Elipse tracejada no DER)"


class DefinicaoAtributo:
    """Representa a especificação conceitual de um atributo no MER."""
    def __init__(
        self,
        nome: str,
        tipo: TipoAtributo,
        descricao: str,
        sub_atributos: Optional[List['DefinicaoAtributo']] = None,
        funcao_derivacao: Optional[Callable[[Dict[str, Any]], Any]] = None,
        obrigatorio: bool = True
    ):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.sub_atributos = sub_atributos or []
        self.funcao_derivacao = funcao_derivacao
        self.obrigatorio = obrigatorio

    def __repr__(self) -> str:
        return f"<Atributo '{self.nome}' ({self.tipo.name})>"


class EsquemaEntidade:
    """Representa um Conjunto de Entidades (Entity Set) no MER."""
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao
        self.atributos: Dict[str, DefinicaoAtributo] = {}
        self.instancias: List[Dict[str, Any]] = []

    def adicionar_atributo(self, atributo: DefinicaoAtributo):
        self.atributos[atributo.nome] = atributo

    def validar_e_inserir(self, dados_instancia: Dict[str, Any]):
        """Valida semanticamente uma nova instância de entidade antes da inserção."""
        # 1. Validar identificador único
        id_attr = next((a for a in self.atributos.values() if a.tipo == TipoAtributo.IDENTIFICADOR), None)
        if id_attr:
            val_id = dados_instancia.get(id_attr.nome)
            if val_id is None:
                raise ValueError(f"Violação conceitual: Atributo identificador '{id_attr.nome}' não pode ser nulo.")
            for inst in self.instancias:
                if inst.get(id_attr.nome) == val_id:
                    raise ValueError(f"Violação de unicidade: Já existe entidade com '{id_attr.nome}' = '{val_id}'.")

        # 2. Validar atributos obrigatórios
        for nome_attr, attr in self.atributos.items():
            if attr.tipo != TipoAtributo.DERIVADO and attr.obrigatorio:
                if nome_attr not in dados_instancia or dados_instancia[nome_attr] is None:
                    raise ValueError(f"Atributo obrigatório '{nome_attr}' ausente na entidade '{self.nome}'.")

        # 3. Computar atributos derivados dinamicamente
        for nome_attr, attr in self.atributos.items():
            if attr.tipo == TipoAtributo.DERIVADO and attr.funcao_derivacao:
                dados_instancia[nome_attr] = attr.funcao_derivacao(dados_instancia)

        self.instancias.append(dados_instancia)


# ==============================================================================
# FUNÇÕES AUXILIARES DE FORMATAÇÃO DIDÁTICA
# ==============================================================================

def imprimir_cabecalho(titulo: str):
    print("\n" + "=" * 78)
    print(f" {titulo.upper()}")
    print("=" * 78)


def imprimir_divisor(subtitulo: str = ""):
    print("\n" + "-" * 78)
    if subtitulo:
        print(f" [*] {subtitulo}")
        print("-" * 78)


# ==============================================================================
# 2. MODELAGEM DO MINIMUNDO: NOC E DATACENTER DO IFCE TAUÁ
# ==============================================================================

def criar_esquema_dispositivo_rede() -> EsquemaEntidade:
    """
    Cria a especificação conceitual da entidade DISPOSITIVO_REDE
    contemplando rigorosamente todos os tipos canônicos de atributos do MER.
    """
    entidade = EsquemaEntidade(
        nome="DISPOSITIVO_REDE",
        descricao="Equipamentos ativos que compõem a topologia de rede e telecomunicações do campus."
    )

    # 1. Atributo Identificador (Chave Primária Conceitual)
    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="patrimonio_id",
        tipo=TipoAtributo.IDENTIFICADOR,
        descricao="Número tombado de patrimônio institucional gravado no chassi (único)."
    ))

    # 2. Atributos Simples / Atômicos
    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="hostname",
        tipo=TipoAtributo.SIMPLES,
        descricao="Nome FQDN ou mnemônico do dispositivo na topologia de rede."
    ))
    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="ip_loopback",
        tipo=TipoAtributo.SIMPLES,
        descricao="Endereço IPv4 de gerência atribuído à interface loopback0."
    ))
    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="fabricante",
        tipo=TipoAtributo.SIMPLES,
        descricao="Fabricante do hardware (ex: Cisco, Juniper, Huawei, MikroTik)."
    ))
    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="data_instalacao",
        tipo=TipoAtributo.SIMPLES,
        descricao="Data física de ativação do equipamento no datacenter (armazenado)."
    ))

    # 3. Atributo Composto (Hierárquico com subatributos)
    sub_rack = [
        DefinicaoAtributo("bloco", TipoAtributo.SIMPLES, "Bloco predial (ex: Bloco Administrativo)"),
        DefinicaoAtributo("sala_noc", TipoAtributo.SIMPLES, "Identificação da sala técnica (ex: Sala 104)"),
        DefinicaoAtributo("rack_id", TipoAtributo.SIMPLES, "Identificador do rack (ex: RACK-A01)"),
        DefinicaoAtributo("posicao_u", TipoAtributo.SIMPLES, "Unidade de altura no rack (ex: U24-U26)")
    ]
    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="localizacao_rack",
        tipo=TipoAtributo.COMPOSTO,
        descricao="Localização física detalhada dentro do datacenter.",
        sub_atributos=sub_rack
    ))

    # 4. Atributo Multivalorado (Conjunto de valores para uma mesma entidade)
    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="vlan_tags",
        tipo=TipoAtributo.MULTIVALORADO,
        descricao="Lista de IDs de VLAN IEEE 802.1Q que trafegam pelo equipamento."
    ))

    # 5. Atributo Derivado (Calculado dinamicamente a partir de data_instalacao)
    def calcular_dias_operacao(dados: Dict[str, Any]) -> int:
        data_inst = dados.get("data_instalacao")
        if isinstance(data_inst, str):
            dt_inst = datetime.strptime(data_inst, "%Y-%m-%d").date()
        elif isinstance(data_inst, (date, datetime)):
            dt_inst = data_inst if isinstance(data_inst, date) else data_inst.date()
        else:
            return 0
        data_referencia = date(2026, 10, 6)  # Data corrente da disciplina
        return (data_referencia - dt_inst).days

    entidade.adicionar_atributo(DefinicaoAtributo(
        nome="dias_operacao",
        tipo=TipoAtributo.DERIVADO,
        descricao="Tempo decorrido em dias de operação desde a data de instalação.",
        funcao_derivacao=calcular_dias_operacao,
        obrigatorio=False
    ))

    return entidade


# ==============================================================================
# 3. DEMONSTRAÇÃO PRÁTICA: INSTANCIAÇÃO E INSPEÇÃO CONCEITUAL
# ==============================================================================

def demonstrar_modelo_conceitual():
    imprimir_cabecalho("Aula 03: Introdução ao MER e Classificação de Atributos")

    esquema = criar_esquema_dispositivo_rede()

    imprimir_divisor("Dicionário Conceitual de Atributos da Entidade: " + esquema.nome)
    print(f"Descrição da Entidade: {esquema.descricao}\n")
    print(f"{'Atributo':<20} | {'Tipo Conceitual (Chen)':<32} | {'Representação DER'}")
    print("-" * 78)

    for attr in esquema.atributos.values():
        notacao = ""
        if attr.tipo == TipoAtributo.IDENTIFICADOR:
            notacao = "Elipse com texto sublinhado (chave primária)"
        elif attr.tipo == TipoAtributo.SIMPLES:
            notacao = "Elipse simples ligada ao retângulo"
        elif attr.tipo == TipoAtributo.COMPOSTO:
            notacao = "Elipse com ramos ligados a sub-elipses"
        elif attr.tipo == TipoAtributo.MULTIVALORADO:
            notacao = "Elipse dupla concêntrica"
        elif attr.tipo == TipoAtributo.DERIVADO:
            notacao = "Elipse com linha tracejada / pontilhada"

        print(f"{attr.nome:<20} | {attr.tipo.name:<32} | {notacao}")
        if attr.sub_atributos:
            for sub in attr.sub_atributos:
                print(f"  └──> {sub.nome:<15} | {'Sub-atributo (Atômico)':<32} | Elipse folha conectada ao composto")

    # Inserção de instâncias concretas do mundo real (Dispositivos do IFCE Tauá)
    imprimir_divisor("Instanciação de Entidades Concretas com Validação Semântica")

    roteador_core = {
        "patrimonio_id": "IFCE-TAU-00101",
        "hostname": "TAU-RTR-CORE-01",
        "ip_loopback": "10.200.0.1",
        "fabricante": "Cisco Systems",
        "data_instalacao": "2024-02-15",
        "localizacao_rack": {
            "bloco": "Bloco Principal",
            "sala_noc": "NOC Sala 102",
            "rack_id": "RACK-01",
            "posicao_u": "U40-U42"
        },
        "vlan_tags": [10, 20, 30, 99, 100, 200]
    }

    switch_dist = {
        "patrimonio_id": "IFCE-TAU-00102",
        "hostname": "TAU-SW-DIST-01",
        "ip_loopback": "10.200.0.2",
        "fabricante": "Huawei",
        "data_instalacao": "2025-05-10",
        "localizacao_rack": {
            "bloco": "Bloco Didático",
            "sala_noc": "Armário Telecom 02",
            "rack_id": "RACK-03",
            "posicao_u": "U22-U23"
        },
        "vlan_tags": [10, 20, 100]
    }

    esquema.validar_e_inserir(roteador_core)
    esquema.validar_e_inserir(switch_dist)
    print("✅ Duas instâncias inseridas com sucesso no conjunto de entidades.")

    # Exibição detalhada das instâncias com atributo derivado calculado
    for idx, inst in enumerate(esquema.instancias, 1):
        print(f"\n[Instância #{idx}] Dispositivo: {inst['hostname']}")
        print(f"  • Identificador (Chave):   {inst['patrimonio_id']}")
        print(f"  • IP de Loopback:          {inst['ip_loopback']} (Fabricante: {inst['fabricante']})")
        print(f"  • Localização (Composto):  {inst['localizacao_rack']['bloco']}, {inst['localizacao_rack']['sala_noc']} -> {inst['localizacao_rack']['rack_id']} ({inst['localizacao_rack']['posicao_u']})")
        print(f"  • VLANs (Multivalorado):   {inst['vlan_tags']} (Total de {len(inst['vlan_tags'])} tags)")
        print(f"  • Data de Ativação:        {inst['data_instalacao']}")
        print(f"  • Dias Operando (Derivado): {inst['dias_operacao']} dias ininterruptos")

    # Teste didático de violação de integridade conceitual (Chave Duplicada)
    imprimir_divisor("Teste de Violação de Chave Conceitual (Unicidade do Identificador)")
    try:
        instancia_invalida = {
            "patrimonio_id": "IFCE-TAU-00101",  # Mesmo ID já existente!
            "hostname": "TAU-RTR-BACKUP-01",
            "ip_loopback": "10.200.0.99",
            "fabricante": "MikroTik",
            "data_instalacao": "2026-01-01",
            "localizacao_rack": {"bloco": "B", "sala_noc": "S1", "rack_id": "R1", "posicao_u": "U10"},
            "vlan_tags": [10]
        }
        esquema.validar_e_inserir(instancia_invalida)
    except ValueError as e:
        print(f"⚠️  Exceção esperada capturada: {e}")
        print("   O metamodelo impediu a duplicação de uma entidade com a mesma chave primária!")


# ==============================================================================
# 4. MAPEAMENTO CONCEITUAL -> RELACIONAL (SQLite)
# ==============================================================================

def demonstrar_mapeamento_relacional():
    """
    Demonstra a transição metodológica da Aula 03 (Modelo Conceitual MER)
    para o Modelo Lógico Relacional (SQLite), ilustrando por que a Primeira Forma
    Normal (1FN) proíbe atributos compostos e multivalorados em colunas únicas.
    """
    imprimir_cabecalho("Ponte Metodológica: Do Modelo Conceitual ao Modelo Relacional")

    print("""
    No MER de Chen:
      - Atributos Compostos e Multivalorados são perfeitamente válidos e expressivos.
    
    No Modelo Lógico Relacional (Codd, 1970):
      - 1ª Forma Normal (1FN): Todo atributo deve conter apenas valores ATÔMICOS (indivisíveis).
      - Regra 1: O atributo COMPOSTO é 'achatado' (flattened) em múltiplas colunas atômicas.
      - Regra 2: O atributo MULTIVALORADO requer uma TABELA AUXILIAR associativa ligada por FK.
      - Regra 3: O atributo DERIVADO não é persistido fisicamente; é calculado em uma VIEW.
    """)

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # DDL: Tabela principal com colunas atômicas (composto planificado)
    cursor.execute("""
    CREATE TABLE dispositivos_rede (
        patrimonio_id TEXT PRIMARY KEY,
        hostname TEXT NOT NULL UNIQUE,
        ip_loopback TEXT NOT NULL UNIQUE,
        fabricante TEXT NOT NULL,
        data_instalacao DATE NOT NULL,
        -- Decomposição do atributo composto localizacao_rack:
        rack_bloco TEXT NOT NULL,
        rack_sala TEXT NOT NULL,
        rack_id TEXT NOT NULL,
        rack_posicao_u TEXT NOT NULL
    );
    """)

    # DDL: Tabela auxiliar para o atributo multivalorado vlan_tags
    cursor.execute("""
    CREATE TABLE dispositivo_vlans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dispositivo_patrimonio TEXT NOT NULL,
        vlan_id INTEGER NOT NULL CHECK (vlan_id BETWEEN 1 AND 4094),
        FOREIGN KEY (dispositivo_patrimonio) REFERENCES dispositivos_rede(patrimonio_id) ON DELETE CASCADE,
        UNIQUE (dispositivo_patrimonio, vlan_id)
    );
    """)

    # DDL: Visão (VIEW) para o atributo derivado dias_operacao
    cursor.execute("""
    CREATE VIEW vw_dispositivos_com_uptime AS
    SELECT 
        d.patrimonio_id,
        d.hostname,
        d.fabricante,
        d.ip_loopback,
        d.rack_id,
        d.data_instalacao,
        CAST((julianday('2026-10-06') - julianday(d.data_instalacao)) AS INTEGER) AS dias_operacao_derivado
    FROM dispositivos_rede d;
    """)

    # Carga de dados DML
    cursor.execute("""
    INSERT INTO dispositivos_rede VALUES (
        'IFCE-TAU-00101', 'TAU-RTR-CORE-01', '10.200.0.1', 'Cisco Systems', '2024-02-15',
        'Bloco Principal', 'NOC Sala 102', 'RACK-01', 'U40-U42'
    );
    """)
    cursor.execute("""
    INSERT INTO dispositivos_rede VALUES (
        'IFCE-TAU-00102', 'TAU-SW-DIST-01', '10.200.0.2', 'Huawei', '2025-05-10',
        'Bloco Didático', 'Armário Telecom 02', 'RACK-03', 'U22-U23'
    );
    """)

    # Carga dos valores multivalorados
    vlans_core = [( 'IFCE-TAU-00101', v) for v in [10, 20, 30, 99, 100, 200]]
    vlans_switch = [('IFCE-TAU-00102', v) for v in [10, 20, 100]]
    cursor.executemany("INSERT INTO dispositivo_vlans (dispositivo_patrimonio, vlan_id) VALUES (?, ?);", vlans_core + vlans_switch)

    conn.commit()

    # Consulta demonstrativa via VIEW (com atributo derivado)
    imprimir_divisor("Consulta à VIEW com Atributo Derivado e Composto Planificado")
    cursor.execute("SELECT patrimonio_id, hostname, rack_id, data_instalacao, dias_operacao_derivado FROM vw_dispositivos_com_uptime;")
    for row in cursor.fetchall():
        print(f"-> Dispositivo: {row[1]:<16} | Rack: {row[2]:<8} | Instalado: {row[3]} | Uptime: {row[4]} dias")

    # Consulta demonstrativa agregando atributo multivalorado
    imprimir_divisor("Consulta Agregada com GROUP_CONCAT para Reconstituir o Atributo Multivalorado")
    cursor.execute("""
    SELECT 
        d.hostname,
        d.ip_loopback,
        GROUP_CONCAT(v.vlan_id, ', ') AS vlans_associadas
    FROM dispositivos_rede d
    LEFT JOIN dispositivo_vlans v ON d.patrimonio_id = v.dispositivo_patrimonio
    GROUP BY d.patrimonio_id;
    """)
    for row in cursor.fetchall():
        print(f"-> Host: {row[0]:<16} | IP: {row[1]:<12} | VLANs: [{row[2]}]")

    print("\n✅ Mapeamento conceitual -> relacional validado com integridade total.")
    conn.close()


def main():
    demonstrar_modelo_conceitual()
    demonstrar_mapeamento_relacional()
    imprimir_cabecalho("Fim da Execução - Laboratório da Aula 03 Concluído")


if __name__ == "__main__":
    main()
