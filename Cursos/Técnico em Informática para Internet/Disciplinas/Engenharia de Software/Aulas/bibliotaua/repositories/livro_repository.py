"""
Repositório de Persistência SQLite: LivroRepository
"""
import sqlite3
from typing import List, Optional
from bibliotaua.models.livro import Livro

class LivroRepository:
    def __init__(self, conexao: sqlite3.Connection):
        self.conn = conexao

    def salvar(self, livro: Livro) -> Livro:
        if livro.id is None:
            cursor = self.conn.execute("""
                INSERT INTO livros (titulo, autor, isbn, preco, estoque, categoria)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (livro.titulo, livro.autor, livro.isbn, livro.preco, livro.estoque, livro.categoria))
            livro.id = cursor.lastrowid
        else:
            self.conn.execute("""
                UPDATE livros SET
                    titulo = ?, autor = ?, isbn = ?, preco = ?, estoque = ?, categoria = ?
                WHERE id = ?
            """, (livro.titulo, livro.autor, livro.isbn, livro.preco, livro.estoque, livro.categoria, livro.id))
        self.conn.commit()
        return livro

    def buscar_por_id(self, livro_id: int) -> Optional[Livro]:
        cursor = self.conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
        row = cursor.fetchone()
        if not row:
            return None
        return Livro(
            id=row["id"],
            titulo=row["titulo"],
            autor=row["autor"],
            isbn=row["isbn"],
            preco=float(row["preco"]),
            estoque=int(row["estoque"]),
            categoria=row["categoria"]
        )

    def listar_todos(self) -> List[Livro]:
        cursor = self.conn.execute("SELECT * FROM livros ORDER BY titulo ASC")
        return [
            Livro(
                id=row["id"],
                titulo=row["titulo"],
                autor=row["autor"],
                isbn=row["isbn"],
                preco=float(row["preco"]),
                estoque=int(row["estoque"]),
                categoria=row["categoria"]
            )
            for row in cursor.fetchall()
        ]

    def atualizar_estoque(self, livro_id: int, novo_estoque: int) -> None:
        self.conn.execute("UPDATE livros SET estoque = ? WHERE id = ?", (novo_estoque, livro_id))
        self.conn.commit()
