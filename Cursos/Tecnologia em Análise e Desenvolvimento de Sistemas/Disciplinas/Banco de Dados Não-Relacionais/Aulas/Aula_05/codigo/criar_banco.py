# Arquivo: criar_banco.py
# Objetivo: Criar o banco de dados SQLite 'shopgrids.db' e popular a tabela 'categories'

# Importa a biblioteca nativa do Python para banco de dados relacional SQLite
import os
import sqlite3

# Define o caminho absoluto para o arquivo shopgrids.db na pasta codigo/
DB_PATH = os.path.join(os.path.dirname(__file__), "shopgrids.db")


# Define a função que criará a estrutura da tabela e os registros iniciais
def inicializar_banco():
    # Conecta ao arquivo 'shopgrids.db' (cria o arquivo no disco caso ainda não exista)
    conn = sqlite3.connect(DB_PATH)

    # Cria o objeto cursor, responsável por enviar comandos SQL ao banco de dados
    cursor = conn.cursor()

    # Remove a tabela 'categories' se ela já existir, garantindo que o teste comece limpo
    cursor.execute("DROP TABLE IF EXISTS categories")

    # Cria a tabela 'categories' com 4 colunas (id, name, image, is_featured)
    cursor.execute("""
        CREATE TABLE categories (
            id INTEGER PRIMARY KEY,                 -- Identificador único da categoria
            name TEXT NOT NULL,                     -- Nome exibido no Front-end
            image TEXT NOT NULL,                    -- Nome da imagem/ícone da categoria
            is_featured INTEGER NOT NULL DEFAULT 0  -- 1 = Em destaque na Home | 0 = Não destacada
        )
    """)

    # Lista de tuplas com as categorias iniciais da loja ShopGrids:
    # As 4 primeiras possuem is_featured = 1 (aparecem na Home)
    # As últimas possuem is_featured = 0 (ocultas inicialmente)
    categorias = [
        (1, "TV & Áudio", "fa-tv", 1),                     # Destaque ativo (1)
        (2, "Desktop & Laptop", "fa-laptop", 1),           # Destaque ativo (1)
        (3, "Smartphones", "fa-mobile-screen-button", 1),  # Destaque ativo (1)
        (4, "Acessórios Gamer", "fa-gamepad", 1),          # Destaque ativo (1)
        (5, "Moda Inverno", "fa-mitten", 0),               # Destaque inativo (0)
        (6, "Aquecedores", "fa-temperature-arrow-up", 0),  # Destaque inativo (0)
    ]

    # Insere todas as 6 categorias de uma só vez substituindo os '?' pelos dados de cada tupla
    cursor.executemany(
        "INSERT INTO categories (id, name, image, is_featured) VALUES (?, ?, ?, ?)",
        categorias
    )

    # Grava (commita) as alterações permanentemente no arquivo 'shopgrids.db'
    conn.commit()

    # Encerra a conexão com o arquivo do banco de dados
    conn.close()

    # Informa no terminal que o banco foi preparado com sucesso
    print("✓ Banco 'shopgrids.db' criado com sucesso com 6 categorias (4 em destaque)!")


# Executa a função quando o arquivo é chamado diretamente pelo comando 'python criar_banco.py'
if __name__ == "__main__":
    inicializar_banco()
