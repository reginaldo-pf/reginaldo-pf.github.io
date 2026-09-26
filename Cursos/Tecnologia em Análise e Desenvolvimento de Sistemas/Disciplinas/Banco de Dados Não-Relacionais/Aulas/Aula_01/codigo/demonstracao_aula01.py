"""
=============================================================================
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina : Bancos de Dados Não-Relacionais (ADS16)
Aula 01    : Introdução ao NoSQL & Descasamento de Impedância Objeto-Relacional
Professor  : Reginaldo Fernandes
=============================================================================
Demonstração Prática:
1. Simulação do modelo relacional normalizado (RDBMS com chaves e JOINs).
2. Simulação do modelo orientado a documentos (NoSQL em formato agregado JSON).
3. Análise visual do "Object-Relational Impedance Mismatch" e trade-offs.
=============================================================================
"""

import json
import sqlite3
import time
from dataclasses import dataclass, field
from typing import List


# =============================================================================
# 1. MODELO DE DOMÍNIO ORIENTADO A OBJETOS (Aplicação Python)
# =============================================================================
@dataclass
class ItemPedido:
    produto: str
    quantidade: int
    preco_unitario: float


@dataclass
class Pedido:
    id_pedido: str
    data_emissao: str
    itens: List[ItemPedido] = field(default_factory=list)

    @property
    def total(self) -> float:
        return sum(item.quantidade * item.preco_unitario for item in self.itens)


@dataclass
class Cliente:
    id_cliente: int
    nome: str
    email: str
    cidade: str
    uf: str
    pedidos: List[Pedido] = field(default_factory=list)


# Dados de exemplo no mundo real
pedidos_exemplo = [
    Pedido(
        id_pedido="PED-2026-001",
        data_emissao="2026-09-29",
        itens=[
            ItemPedido("Notebook Dell", 1, 4500.00),
            ItemPedido("Mouse Sem Fio", 2, 85.50),
        ],
    ),
    Pedido(
        id_pedido="PED-2026-002",
        data_emissao="2026-10-01",
        itens=[ItemPedido("Monitor 27 Pol", 1, 1200.00)],
    ),
]

cliente_exemplo = Cliente(
    id_cliente=1,
    nome="Maria Clara Silva",
    email="maria.clara@aluno.ifce.edu.br",
    cidade="Tauá",
    uf="CE",
    pedidos=pedidos_exemplo,
)


# =============================================================================
# 2. ABORDAGEM RELACIONAL (RDBMS - Normalização 3NF com Chaves Estrangeiras)
# =============================================================================
def demonstrar_abordagem_relacional():
    print("\n" + "=" * 70)
    print(" 🏛️  ABORDAGEM RELACIONAL TRADICIONAL (RDBMS - SQLite)")
    print("=" * 70)

    # Criando banco relacional em memória
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Criação de 4 tabelas normalizadas
    cursor.executescript(
        """
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        );

        CREATE TABLE enderecos (
            id_cliente INTEGER PRIMARY KEY,
            cidade TEXT NOT NULL,
            uf TEXT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        );

        CREATE TABLE pedidos (
            id_pedido TEXT PRIMARY KEY,
            id_cliente INTEGER NOT NULL,
            data_emissao TEXT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        );

        CREATE TABLE itens_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pedido TEXT NOT NULL,
            produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
        );
    """
    )

    t0 = time.perf_counter()

    # Inserção fragmentada (Descasamento na escrita)
    cursor.execute(
        "INSERT INTO clientes VALUES (?, ?, ?)",
        (cliente_exemplo.id_cliente, cliente_exemplo.nome, cliente_exemplo.email),
    )
    cursor.execute(
        "INSERT INTO enderecos VALUES (?, ?, ?)",
        (cliente_exemplo.id_cliente, cliente_exemplo.cidade, cliente_exemplo.uf),
    )

    for pedido in cliente_exemplo.pedidos:
        cursor.execute(
            "INSERT INTO pedidos VALUES (?, ?, ?)",
            (pedido.id_pedido, cliente_exemplo.id_cliente, pedido.data_emissao),
        )
        for item in pedido.itens:
            cursor.execute(
                "INSERT INTO itens_pedido (id_pedido, produto, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
                (pedido.id_pedido, item.produto, item.quantidade, item.preco_unitario),
            )
    conn.commit()
    t_insert = (time.perf_counter() - t0) * 1000

    print(
        f"✅ Inserção Concluída: 1 Entidade de Domínio foi fragmentada em 4 tabelas!"
    )
    print(f"⏱️  Tempo de escrita relacional: {t_insert:.4f} ms")

    # Reconstrução do Objeto via Consulta com múltiplos JOINs
    print("\n🔍 Consulta SQL para remontar a entidade com JOINs:")
    sql = """
        SELECT c.nome, e.cidade, e.uf, p.id_pedido, p.data_emissao, i.produto, i.quantidade, i.preco_unitario
        FROM clientes c
        JOIN enderecos e ON c.id = e.id_cliente
        JOIN pedidos p ON c.id = p.id_cliente
        JOIN itens_pedido i ON p.id_pedido = i.id_pedido
        WHERE c.id = ?;
    """
    cursor.execute(sql, (cliente_exemplo.id_cliente,))
    linhas = cursor.fetchall()

    print(f"Linhas tabulares retornadas (com redundâncias de joins):")
    for linha in linhas:
        print(f"  -> {linha}")

    print(
        "\n⚠️  Desafio da Impedância Objeto-Relacional: O código precisa percorrer as linhas"
    )
    print(
        "   para agrupar os itens e reconstruir as listas do objeto original em memória!"
    )
    conn.close()


# =============================================================================
# 3. ABORDAGEM NÃO-RELACIONAL (NoSQL Orientado a Documentos - JSON nativo)
# =============================================================================
def demonstrar_abordagem_documento():
    print("\n" + "=" * 70)
    print(" 🍃 ABORDAGEM NÃO-RELACIONAL (NoSQL / Orientado a Documentos)")
    print("=" * 70)

    # Serialização direta do modelo de domínio em um único documento aninhado (BSON/JSON)
    documento_cliente = {
        "_id": cliente_exemplo.id_cliente,
        "nome": cliente_exemplo.nome,
        "email": cliente_exemplo.email,
        "endereco": {"cidade": cliente_exemplo.cidade, "uf": cliente_exemplo.uf},
        "pedidos": [
            {
                "id_pedido": p.id_pedido,
                "data_emissao": p.data_emissao,
                "total": p.total,
                "itens": [
                    {
                        "produto": item.produto,
                        "quantidade": item.quantidade,
                        "preco_unitario": item.preco_unitario,
                    }
                    for item in p.itens
                ],
            }
            for p in cliente_exemplo.pedidos
        ],
    }

    t0 = time.perf_counter()
    documento_serializado = json.dumps(documento_cliente, indent=2)
    t_serial = (time.perf_counter() - t0) * 1000

    print("✅ Documento Único Pronto para Gravação Atômica (Embedding):")
    print(documento_serializado)
    print(f"\n⏱️  Tempo de serialização direta do documento: {t_serial:.4f} ms")
    print("💡 Vantagem NoSQL:")
    print("   1. Leitura em 1 único I/O de disco (sem JOINs de 4 tabelas).")
    print(
        "   2. O formato de armazenamento é idêntico à representação da aplicação!"
    )
    print("   3. Flexibilidade: novos campos não exigem migração rígida de schema (ALTER TABLE).")


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    print("*" * 70)
    print(" IFCE Campus Tauá - ADS | Bancos de Dados Não-Relacionais")
    print(" Aula 01: Demonstração de Impedance Mismatch (Relacional vs NoSQL)")
    print("*" * 70)

    demonstrar_abordagem_relacional()
    demonstrar_abordagem_documento()

    print("\n" + "=" * 70)
    print(" 📊 RESUMO COMPARATIVO PARA TOMADA DE DECISÃO")
    print("=" * 70)
    print(" • Relacional (RDBMS): Excelente para dados altamente tabulares,")
    print("   onde a consistência estrita (ACID) supera o volume ou velocidade.")
    print(" • NoSQL (Documentos): Excelente para entidades completas e agregadas,")
    print("   alta escalabilidade horizontal e evolução ágil de schema.")
    print("=" * 70 + "\n")
