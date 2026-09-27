#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Apoio Didático - Aula 02
Disciplina: Banco de Dados | Tecnologia em Telemática
IFCE Campus Tauá | Prof. Reginaldo Pereira Fernandes

Tópicos Abordados:
1. Arquitetura ANSI/SPARC e Níveis de Abstração
2. Introspecção do Catálogo do Sistema (sqlite_master / Dicionário de Dados)
3. Sublinguagens SQL: DDL, DML, DQL, DCL (Conceito) e TCL (Transações & Savepoints)
4. Independência Lógica e Física de Dados
"""

import sqlite3

def linha_divisoria(titulo=""):
    print("\n" + "=" * 70)
    if titulo:
        print(f" {titulo.upper()}")
        print("=" * 70)

def main():
    linha_divisoria("Aula 02: Catálogo do Sistema, Sublinguagens SQL e TCL")

    # 1. Conexão com SGBD Relacional (SQLite em memória para o laboratório)
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    print("[*] Conexão estabelecida com banco de dados relacional em memória.")

    # --------------------------------------------------------------------------
    # 2. DDL (Data Definition Language) - Criação do Esquema Conceitual
    # --------------------------------------------------------------------------
    linha_divisoria("2. DDL - Criação das Tabelas de Infraestrutura de Rede")
    
    ddl_roteadores = """
    CREATE TABLE roteadores_core (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hostname TEXT NOT NULL UNIQUE,
        ip_gerencia TEXT NOT NULL UNIQUE,
        fabricante TEXT NOT NULL,
        modelo TEXT NOT NULL,
        capacidade_gbps INTEGER NOT NULL CHECK (capacidade_gbps > 0)
    );
    """
    
    ddl_circuitos = """
    CREATE TABLE circuitos_fibra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_circuito TEXT NOT NULL UNIQUE,
        roteador_origem_id INTEGER NOT NULL,
        interface_local TEXT NOT NULL,
        banda_mbps INTEGER NOT NULL,
        status_operacional TEXT NOT NULL DEFAULT 'DOWN',
        FOREIGN KEY (roteador_origem_id) REFERENCES roteadores_core(id)
    );
    """
    
    cursor.execute(ddl_roteadores)
    cursor.execute(ddl_circuitos)
    print("✅ [DDL] Tabelas 'roteadores_core' e 'circuitos_fibra' criadas com sucesso.")

    # --------------------------------------------------------------------------
    # 3. CATÁLOGO DO SISTEMA (Dicionário de Dados / Metadados)
    # --------------------------------------------------------------------------
    linha_divisoria("3. Catálogo do Sistema - Introspecção de Metadados (sqlite_master)")
    
    # Consulta ao catálogo interno do SGBD para listar tabelas e esquemas registrados
    query_catalogo = """
    SELECT type, name, tbl_name, sql 
    FROM sqlite_master 
    WHERE type IN ('table', 'index') AND name NOT LIKE 'sqlite_%';
    """
    
    print("[-] Metadados registrados no Dicionário de Dados do SGBD:")
    cursor.execute(query_catalogo)
    for obj_type, name, tbl_name, sql_def in cursor.fetchall():
        print(f"\n-> Tipo de Objeto: {obj_type.upper()}")
        print(f"   Nome Identificador: {name}")
        print(f"   Tabela Associada:   {tbl_name}")
        print(f"   Definição DDL no Catálogo:\n   {sql_def.strip()}")

    # --------------------------------------------------------------------------
    # 4. DML (Data Manipulation Language) - Inserção de Dados
    # --------------------------------------------------------------------------
    linha_divisoria("4. DML - Inserção de Registros em roteadores_core")
    
    dml_insert_roteadores = """
    INSERT INTO roteadores_core (hostname, ip_gerencia, fabricante, modelo, capacidade_gbps)
    VALUES (?, ?, ?, ?, ?);
    """
    
    dados_roteadores = [
        ("TAU-CORE-01", "10.200.1.1", "Cisco", "ASR-9006", 400),
        ("TAU-EDGE-01", "10.200.1.2", "Juniper", "MX480", 240),
        ("TAU-DIST-01", "10.200.1.3", "Huawei", "NE40E", 100),
        ("TAU-WAN-01",  "10.200.1.4", "MikroTik", "CCR2216", 100)
    ]
    
    cursor.executemany(dml_insert_roteadores, dados_roteadores)
    conn.commit()
    print(f"✅ [DML] {len(dados_roteadores)} roteadores inseridos com sucesso.")

    # Inserção de circuitos associados
    dml_insert_circuitos = """
    INSERT INTO circuitos_fibra (codigo_circuito, roteador_origem_id, interface_local, banda_mbps, status_operacional)
    VALUES (?, ?, ?, ?, ?);
    """
    dados_circuitos = [
        ("CIRC-TAU-FOR-01", 1, "HundredGigE0/0/0/1", 100000, "UP"),
        ("CIRC-TAU-CRAT-01", 1, "TenGigE0/0/0/2", 10000, "UP"),
        ("CIRC-TAU-IGUA-01", 2, "xe-0/1/0", 10000, "UP"),
        ("CIRC-TAU-LOCAL-01", 3, "GigabitEthernet0/0/1", 1000, "DOWN")
    ]
    cursor.executemany(dml_insert_circuitos, dados_circuitos)
    conn.commit()
    print(f"✅ [DML] {len(dados_circuitos)} circuitos de fibra inseridos com sucesso.")

    # --------------------------------------------------------------------------
    # 5. DQL (Data Query Language) - Consulta Analítica
    # --------------------------------------------------------------------------
    linha_divisoria("5. DQL - Consulta de Circuitos Ativos com Junção Relacional")
    
    dql_query = """
    SELECT 
        c.codigo_circuito,
        r.hostname AS roteador,
        r.ip_gerencia,
        c.interface_local,
        c.banda_mbps,
        c.status_operacional
    FROM circuitos_fibra c
    JOIN roteadores_core r ON c.roteador_origem_id = r.id
    ORDER BY c.banda_mbps DESC;
    """
    
    cursor.execute(dql_query)
    resultados = cursor.fetchall()
    
    header = f"{'CIRCUITO':<18} | {'ROTEADOR':<12} | {'IP GERÊNCIA':<14} | {'INTERFACE':<20} | {'BANDA (M)':<9} | {'STATUS'}"
    print(header)
    print("-" * len(header))
    for row in resultados:
        print(f"{row[0]:<18} | {row[1]:<12} | {row[2]:<14} | {row[3]:<20} | {row[4]:<9} | {row[5]}")

    # --------------------------------------------------------------------------
    # 6. INDEPENDÊNCIA DE DADOS (Evolução do Esquema com DDL)
    # --------------------------------------------------------------------------
    linha_divisoria("6. Independência de Dados - Evolução de Esquema e Índices")
    
    print("[*] Demonstrando Independência Lógica: Adicionando coluna 'snmp_community' sem afetar consultas existentes:")
    cursor.execute("ALTER TABLE roteadores_core ADD COLUMN snmp_community TEXT DEFAULT 'public';")
    print("✅ [DDL] Coluna 'snmp_community' adicionada com sucesso.")
    
    print("\n[*] Demonstrando Independência Física: Criando índice secundário de busca por IP:")
    cursor.execute("CREATE INDEX idx_roteadores_ip ON roteadores_core (ip_gerencia);")
    print("✅ [DDL] Índice físico 'idx_roteadores_ip' criado. As consultas lógicas permanecem inalteradas.")

    # Re-inspeciona o catálogo para comprovar o registro do novo índice
    print("\n[-] Verificando a atualização automática no Catálogo do Sistema:")
    cursor.execute("SELECT name, type, sql FROM sqlite_master WHERE name = 'idx_roteadores_ip';")
    print("   Registro no Catálogo:", cursor.fetchone())

    # --------------------------------------------------------------------------
    # 7. TCL (Transaction Control Language) - Transações ACID e Savepoints
    # --------------------------------------------------------------------------
    linha_divisoria("7. TCL - Controle Transacional com SAVEPOINT e ROLLBACK")
    
    print("[*] Iniciando transação segura com Ponto de Salvamento (Savepoint)...")
    cursor.execute("SAVEPOINT sp_ponto_seguro;")
    
    # 1) Modificação temporária válida mas indesejada
    cursor.execute("UPDATE roteadores_core SET capacidade_gbps = 999 WHERE hostname = 'TAU-CORE-01';")
    print("⚠️  [DML] Atualização temporária executada (capacidade alterada para 999 Gbps).")
    
    cursor.execute("SELECT hostname, capacidade_gbps FROM roteadores_core WHERE hostname = 'TAU-CORE-01';")
    print("   Estado temporário (antes do rollback):", cursor.fetchone())
    
    # Reversão via TCL
    print("\n[*] Revertendo operação até o SAVEPOINT 'sp_ponto_seguro'...")
    cursor.execute("ROLLBACK TO sp_ponto_seguro;")
    print("✅ [TCL] Reversão (ROLLBACK TO SAVEPOINT) concluída com sucesso!")
    
    cursor.execute("SELECT hostname, capacidade_gbps FROM roteadores_core WHERE hostname = 'TAU-CORE-01';")
    print("   Estado restaurado com integridade:", cursor.fetchone())
    
    # 2) Simulação de falha de constraint CHECK capturada com Rollback
    print("\n[*] Testando violação de restrição CHECK (capacidade_gbps > 0) com tratamento:")
    try:
        cursor.execute("UPDATE roteadores_core SET capacidade_gbps = -10 WHERE hostname = 'TAU-CORE-01';")
    except sqlite3.IntegrityError as err:
        print(f"⚠️  [CHECK Constraint] O SGBD impediu a operação inválida: {err}")
        cursor.execute("ROLLBACK TO sp_ponto_seguro;")
        print("✅ [TCL] Estado protegido e mantido íntegro via TCL.")
        
    # Liberação do savepoint e confirmação final
    cursor.execute("RELEASE SAVEPOINT sp_ponto_seguro;")
    conn.commit()
    print("✅ [TCL] Savepoint liberado e transação confirmada (COMMIT) no SGBD.")

    # --------------------------------------------------------------------------
    # 8. DCL (Data Control Language) - Conceitual
    # --------------------------------------------------------------------------
    linha_divisoria("8. DCL - Controle de Acesso e Permissões (Conceito)")
    print("""
    No padrão SQL e em SGBDs cliente-servidor (PostgreSQL, Oracle, MySQL):
      - GRANT SELECT, INSERT ON roteadores_core TO operador_noc;
      - REVOKE DROP ON ALL TABLES FROM operador_estagiario;
    
    O SGBD valida as permissões em tempo de execução consultando o Catálogo do Sistema
    antes de autorizar o processamento de qualquer instrução DDL ou DML.
    """)

    conn.close()
    linha_divisoria("Laboratório Finalizado com Sucesso")

if __name__ == "__main__":
    main()
