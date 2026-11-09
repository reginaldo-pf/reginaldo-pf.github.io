"""
Repositório de Persistência SQLite: CupomRepository (TASK-204)
Implementa operações CRUD e métodos de consulta para a entidade Cupom.
"""
import sqlite3
from typing import List, Optional
from bibliotaua.models.cupom import Cupom, TipoDesconto
from bibliotaua.exceptions import CupomInexistenteError

class CupomRepository:
    def __init__(self, conexao: sqlite3.Connection):
        self.conn = conexao

    def salvar(self, cupom: Cupom) -> Cupom:
        """Salva ou atualiza um cupom no banco de dados SQLite."""
        if cupom.id is None:
            cursor = self.conn.execute("""
                INSERT INTO cupons (
                    codigo, tipo_desconto, valor_desconto, valor_minimo_pedido,
                    limite_usos, usos_realizados, validade_ate, ativo
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                cupom.codigo,
                cupom.tipo_desconto.value,
                cupom.valor_desconto,
                cupom.valor_minimo_pedido,
                cupom.limite_usos,
                cupom.usos_realizados,
                cupom.validade_ate if isinstance(cupom.validade_ate, str) else cupom.validade_ate.strftime("%Y-%m-%d"),
                1 if cupom.ativo else 0
            ))
            cupom.id = cursor.lastrowid
        else:
            self.conn.execute("""
                UPDATE cupons SET
                    tipo_desconto = ?,
                    valor_desconto = ?,
                    valor_minimo_pedido = ?,
                    limite_usos = ?,
                    usos_realizados = ?,
                    validade_ate = ?,
                    ativo = ?
                WHERE id = ?
            """, (
                cupom.tipo_desconto.value,
                cupom.valor_desconto,
                cupom.valor_minimo_pedido,
                cupom.limite_usos,
                cupom.usos_realizados,
                cupom.validade_ate if isinstance(cupom.validade_ate, str) else cupom.validade_ate.strftime("%Y-%m-%d"),
                1 if cupom.ativo else 0,
                cupom.id
            ))
        self.conn.commit()
        return cupom

    def buscar_por_codigo(self, codigo: str) -> Cupom:
        """Recupera um cupom pelo código ou lança CupomInexistenteError."""
        codigo_formatado = codigo.strip().upper()
        cursor = self.conn.execute(
            "SELECT * FROM cupons WHERE codigo = ?",
            (codigo_formatado,)
        )
        row = cursor.fetchone()
        if not row:
            raise CupomInexistenteError(codigo_formatado)
        return self._instanciar_cupom(row)

    def buscar_por_id(self, cupom_id: int) -> Optional[Cupom]:
        """Recupera um cupom pela chave primária."""
        cursor = self.conn.execute("SELECT * FROM cupons WHERE id = ?", (cupom_id,))
        row = cursor.fetchone()
        if not row:
            return None
        return self._instanciar_cupom(row)

    def listar_todos(self) -> List[Cupom]:
        """Lista todos os cupons cadastrados."""
        cursor = self.conn.execute("SELECT * FROM cupons ORDER BY codigo ASC")
        return [self._instanciar_cupom(row) for row in cursor.fetchall()]

    def registrar_uso(self, codigo: str) -> None:
        """Incrementa atômica e seguramente o contador de usos no SQLite."""
        cupom = self.buscar_por_codigo(codigo)
        cupom.registrar_uso()
        self.conn.execute(
            "UPDATE cupons SET usos_realizados = ? WHERE id = ?",
            (cupom.usos_realizados, cupom.id)
        )
        self.conn.commit()

    def _instanciar_cupom(self, row: sqlite3.Row) -> Cupom:
        """Converte uma linha relacional do SQLite para o objeto de domínio Cupom."""
        return Cupom(
            id=row["id"],
            codigo=row["codigo"],
            tipo_desconto=TipoDesconto(row["tipo_desconto"]),
            valor_desconto=float(row["valor_desconto"]),
            valor_minimo_pedido=float(row["valor_minimo_pedido"]),
            limite_usos=int(row["limite_usos"]),
            usos_realizados=int(row["usos_realizados"]),
            validade_ate=row["validade_ate"],
            ativo=bool(row["ativo"])
        )
