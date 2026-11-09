"""
Módulo de Banco de Dados SQLite: BiblioTauá
Gerencia conexão, execução de DDL (Schema) e inicialização de dados (Seeding).
"""
import sqlite3
import os
from typing import Optional

DB_FILE = os.path.join(os.path.dirname(__file__), "bibliotaua.db")

SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    matricula TEXT NOT NULL UNIQUE,
    ativo INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    isbn TEXT NOT NULL UNIQUE,
    preco REAL NOT NULL CHECK(preco >= 0),
    estoque INTEGER NOT NULL CHECK(estoque >= 0),
    categoria TEXT NOT NULL DEFAULT 'Geral'
);

CREATE TABLE IF NOT EXISTS cupons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL UNIQUE,
    tipo_desconto TEXT NOT NULL CHECK(tipo_desconto IN ('PERCENTUAL', 'VALOR_FIXO')),
    valor_desconto REAL NOT NULL CHECK(valor_desconto > 0),
    valor_minimo_pedido REAL NOT NULL DEFAULT 0.0 CHECK(valor_minimo_pedido >= 0),
    limite_usos INTEGER NOT NULL DEFAULT 100 CHECK(limite_usos > 0),
    usos_realizados INTEGER NOT NULL DEFAULT 0 CHECK(usos_realizados >= 0),
    validade_ate TEXT NOT NULL,
    ativo INTEGER NOT NULL DEFAULT 1 CHECK(ativo IN (0, 1))
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    cupom_id INTEGER,
    subtotal REAL NOT NULL,
    desconto_aplicado REAL NOT NULL DEFAULT 0.0,
    total REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'CRIADO',
    data_criacao TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (cupom_id) REFERENCES cupons(id)
);

CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
    preco_unitario REAL NOT NULL,
    subtotal REAL NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
"""

def obter_conexao(caminho_db: Optional[str] = None) -> sqlite3.Connection:
    """Retorna uma conexão ativa configurada com Row Factory."""
    caminho = caminho_db or DB_FILE
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def inicializar_banco(caminho_db: Optional[str] = None) -> None:
    """Executa o script DDL para criar as tabelas caso não existam."""
    conn = obter_conexao(caminho_db)
    with conn:
        conn.executescript(SCHEMA_SQL)
    conn.close()

def popular_dados_iniciais(caminho_db: Optional[str] = None) -> None:
    """Insere registros didáticos padrão de clientes, livros e cupons."""
    conn = obter_conexao(caminho_db)
    with conn:
        # Clientes de exemplo
        conn.execute("""
            INSERT OR IGNORE INTO clientes (id, nome, email, matricula) VALUES
            (1, 'Carlos Eduardo Santos', 'carlos.edu@aluno.ifce.edu.br', '2024101TII001'),
            (2, 'Ana Beatriz Lima', 'ana.lima@aluno.ifce.edu.br', '2024101TII002'),
            (3, 'Mariana Costa', 'mariana.costa@ifce.edu.br', '2024101TII003')
        """)

        # Livros de exemplo (acervo didático geral do cotidiano)
        conn.execute("""
            INSERT OR IGNORE INTO livros (id, titulo, autor, isbn, preco, estoque, categoria) VALUES
            (1, 'Engenharia de Software: Uma Abordagem Prática', 'Roger S. Pressman', '978-8580555332', 189.90, 15, 'Didático'),
            (2, 'UML 2: Uma Abordagem Prática', 'Gilleanes T. A. Guedes', '978-8575222812', 89.00, 20, 'Didático'),
            (3, 'Código Limpo: Habilidades Práticas do Agile Software', 'Robert C. Martin', '978-8576082675', 95.50, 10, 'Programação'),
            (4, 'O Pequeno Príncipe', 'Antoine de Saint-Exupéry', '978-8595081512', 29.90, 30, 'Literatura'),
            (5, 'Dom Casmurro', 'Machado de Assis', '978-8544001929', 24.50, 25, 'Literatura')
        """)

        # Cupons de exemplo para demonstrar todos os fluxos do DUC
        conn.execute("""
            INSERT OR IGNORE INTO cupons (id, codigo, tipo_desconto, valor_desconto, valor_minimo_pedido, limite_usos, usos_realizados, validade_ate, ativo) VALUES
            (1, 'BEMVINDO10', 'PERCENTUAL', 10.0, 50.0, 100, 5, '2027-12-31', 1),
            (2, 'FEIRA20', 'VALOR_FIXO', 20.0, 80.0, 50, 12, '2027-12-31', 1),
            (3, 'SUPER30', 'PERCENTUAL', 30.0, 150.0, 20, 2, '2027-12-31', 1),
            (4, 'EXPIRADO2023', 'PERCENTUAL', 15.0, 0.0, 100, 0, '2023-01-01', 1),
            (5, 'ESGOTADO', 'VALOR_FIXO', 10.0, 0.0, 3, 3, '2027-12-31', 1),
            (6, 'INATIVO50', 'PERCENTUAL', 50.0, 0.0, 10, 0, '2027-12-31', 0)
        """)
    conn.close()
