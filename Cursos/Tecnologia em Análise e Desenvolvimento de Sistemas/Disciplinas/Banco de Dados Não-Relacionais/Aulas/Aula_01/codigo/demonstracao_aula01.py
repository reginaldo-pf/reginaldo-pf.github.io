"""
=============================================================================
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina : Bancos de Dados Não-Relacionais (ADS16)
Aula 01    : Introdução ao NoSQL, Descasamento de Impedância & Primeiro Banco MongoDB
Professor  : Reginaldo Fernandes
Semestre   : 2026.2
=============================================================================
Referências Bibliográficas Integradas:
1. SADALAGE, P. J.; FOWLER, M. NoSQL Essencial: Um Guia Conciso para o Mundo
   Emergente da Persistência Poliglota. São Paulo: Novatec, 2014.
2. FROZZA, A. A.; SCHREINER, G. A.; MELLO, R. S. Projeto de Bancos de Dados
   NoSQL. Minicurso SBC, Capítulo 2.
3. SHAPIRA, G. et al. Kafka: The Definitive Guide - Real-Time Data and Stream
   Processing at Scale. 2. ed. O'Reilly Media, 2021.
4. ELMASRI, R.; NAVATHE, S. B. Sistemas de Banco de Dados. 7. ed. Pearson, 2018.
=============================================================================
Conteúdo Deste Roteiro Prático:
1. Guia Oficial de Instalação do Serviço MongoDB (Ubuntu v8/v9 e Windows).
2. Simulação do modelo relacional normalizado (RDBMS com chaves e 3 JOINs).
3. Simulação da persistência orientada a documentos (NoSQL Agregado JSON).
4. Execução Prática de um Banco de Dados no MongoDB (via PyMongo ou mongosh).
=============================================================================
"""

import json
import socket
import sqlite3
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List


# =============================================================================
# 1. GUIA DE INSTALAÇÃO DO SERVIÇO MONGODB (UBUNTU & WINDOWS)
# =============================================================================
GUIA_INSTALACAO_UBUNTU = """
-----------------------------------------------------------------------------
📦 GUIA DE INSTALAÇÃO DO SERVIÇO MONGODB NO UBUNTU (v8.0 / v9.0 LTS)
-----------------------------------------------------------------------------
1. Instalar dependências prévias:
   $ sudo apt update && sudo apt install -y gnupg curl

2. Importar a chave pública oficial GPG do repositório MongoDB:
   $ curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \\
       sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg --dearmor

3. Registrar a lista de fontes do repositório oficial da distribuição:
   $ echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] \\
       https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/8.0 multiverse" | \\
       sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list

4. Atualizar o índice do APT e instalar o pacote completo do servidor:
   $ sudo apt update
   $ sudo apt install -y mongodb-org

5. Gerenciar o Serviço via systemd:
   $ sudo systemctl start mongod      # Inicia o daemon em segundo plano
   $ sudo systemctl status mongod     # Confere se está "active (running)"
   $ sudo systemctl enable mongod     # Ativa para inicializar com o sistema

6. Conectar no terminal interativo do MongoDB:
   $ mongosh
-----------------------------------------------------------------------------
"""

GUIA_INSTALACAO_WINDOWS = """
-----------------------------------------------------------------------------
🪟 GUIA DE INSTALAÇÃO DO SERVIÇO MONGODB NO WINDOWS (COMMUNITY SERVER)
-----------------------------------------------------------------------------
1. Download do Instalador Oficial:
   - Acesse: https://www.mongodb.com/try/download/community
   - Selecione a versão estável mais recente (Windows x64) e baixe o arquivo .msi.

2. Execução do Assistente de Instalação:
   - Abra o instalador .msi.
   - Escolha o tipo de instalação: "Complete".
   - Na tela "Service Configuration", certifique-se de MARCAR a opção:
     [X] "Install MongoDB as a Service"
     - Service Name: MongoDB
     - Data Directory: C:\\Program Files\\MongoDB\\Server\\<versao>\\data\\
     - Log Directory:  C:\\Program Files\\MongoDB\\Server\\<versao>\\log\\
   - Na tela seguinte, recomenda-se manter marcado:
     [X] "Install MongoDB Compass" (GUI visual oficial para acompanhar as coleções).

3. Gerenciamento do Serviço no Windows:
   - Via PowerShell Administrativo:
     > Get-Service MongoDB          # Verifica status
     > Start-Service MongoDB        # Inicia o serviço
     > Stop-Service MongoDB         # Para o serviço
   - Via Prompt de Comando (CMD como Administrador):
     > net start MongoDB
     > net stop MongoDB
   - Via Painel de Serviços do Windows:
     Pressione Win + R, digite "services.msc" e localize "MongoDB Server".

4. Configuração da Variável de Ambiente PATH:
   - Adicione o diretório "bin" ao PATH do sistema:
     C:\\Program Files\\MongoDB\\Server\\<versao>\\bin\\
   - Abra um novo PowerShell/CMD e digite:
     > mongosh
-----------------------------------------------------------------------------
"""

GUIA_DOCKER_IFCE = """
-----------------------------------------------------------------------------
🐳 ALTERNATIVA RÁPIDA: CONTAINER DOCKER (PADRÃO DE LABORATÓRIO IFCE)
-----------------------------------------------------------------------------
$ docker run -d --name mongodb -p 27017:27017 -v mongo_data:/data/db mongo:latest
$ docker exec -it mongodb mongosh
-----------------------------------------------------------------------------
"""


# =============================================================================
# 2. MODELO DE DOMÍNIO ORIENTADO A OBJETOS (Aplicação Python)
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


# Dados de exemplo do domínio de negócio (IFCE Tauá)
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
# 3. ABORDAGEM RELACIONAL (RDBMS - Normalização 3NF com Chaves Estrangeiras)
# =============================================================================
def demonstrar_abordagem_relacional():
    print("\n" + "=" * 70)
    print(" 🏛️  1. ABORDAGEM RELACIONAL TRADICIONAL (RDBMS - SQLite)")
    print("=" * 70)

    # Criando banco relacional em memória
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Criação de 4 tabelas normalizadas em 3NF
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

    # Inserção fragmentada (Descasamento na escrita: fatiamento obrigatório)
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
    print(f"⏱️  Tempo de escrita relacional (4 INSERTs separados): {t_insert:.4f} ms")

    # Reconstrução da Entidade via Consulta com múltiplos JOINs
    print("\n🔍 Consulta SQL para remontar a entidade com 3 JOINs:")
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

    print(f"Linhas tabulares retornadas (com redundâncias a cada produto):")
    for linha in linhas:
        print(f"  -> {linha}")

    print(
        "\n⚠️  Desafio do Object-Relational Impedance Mismatch (Fowler, 2014):"
    )
    print("   O código da aplicação precisa iterar sobre o conjunto de tuplas para")
    print("   remontar manualmente as listas de Pedidos e Itens em memória.")
    conn.close()


# =============================================================================
# 4. ABORDAGEM NÃO-RELACIONAL (NoSQL Orientado a Documentos - Formato Agregado)
# =============================================================================
def gerar_documento_agregado() -> Dict[str, Any]:
    """Serializa a entidade de domínio em um único documento hierárquico BSON/JSON."""
    return {
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


def demonstrar_abordagem_documento():
    print("\n" + "=" * 70)
    print(" 🍃 2. ABORDAGEM NÃO-RELACIONAL (Orientação a Agregados - Fowler & Sadalage)")
    print("=" * 70)

    t0 = time.perf_counter()
    documento = gerar_documento_agregado()
    doc_json = json.dumps(documento, indent=2, ensure_ascii=False)
    t_serial = (time.perf_counter() - t0) * 1000

    print("✅ Documento Único BSON/JSON Pronto para Gravação Atômica (Embedding):")
    print(doc_json)
    print(f"\n⏱️  Tempo de serialização direta: {t_serial:.4f} ms")
    print("💡 Vantagens Imediatas:")
    print("   1. Leitura em 1 único I/O de disco (sem JOINs de 4 tabelas).")
    print("   2. O formato de armazenamento coincide com o grafo de objetos em memória.")
    print("   3. Schemaless: Novos campos (ex: telefone, tags) podem ser incluídos sem 'ALTER TABLE'.")


# =============================================================================
# 5. EXECUÇÃO PRÁTICA DE UM BANCO NO MONGODB (REAL OU SIMULADO)
# =============================================================================
def testar_servico_mongodb_ativo(host: str = "localhost", port: int = 27017, timeout: float = 0.5) -> bool:
    """Verifica se a porta do serviço MongoDB está aceitando conexões locais."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (OSError, ConnectionRefusedError):
        return False


def demonstrar_execucao_mongodb():
    print("\n" + "=" * 70)
    print(" 🚀 3. DEMONSTRAÇÃO PRÁTICA: EXECUTANDO UM BANCO NO MONGODB")
    print("=" * 70)

    doc_cliente = gerar_documento_agregado()
    servico_ativo = testar_servico_mongodb_ativo("localhost", 27017)

    # -------------------------------------------------------------------------
    # Script Equivalente para Execução no Terminal do mongosh
    # -------------------------------------------------------------------------
    print("📝 Comandos Interativos para o terminal mongosh:\n")
    print("// 1. Conectar ou criar o banco de dados da aula")
    print("use ads_comercio;\n")
    print("// 2. Inserir documento agregado na coleção 'clientes'")
    print(f"db.clientes.insertOne({json.dumps(doc_cliente, ensure_ascii=False)});\n")
    print("// 3. Consultar cliente filtrando por atributo embutido (dot notation)")
    print('db.clientes.find({ "endereco.cidade": "Tauá" }).pretty();\n')
    print("// 4. Atualizar atomicamente adicionando um novo item ao pedido (sem JOINs)")
    print('db.clientes.updateOne(')
    print('  { _id: 1 },')
    print('  { $push: { "pedidos.0.itens": { produto: "Teclado Mecânico", quantidade: 1, preco_unitario: 250.0 } } }')
    print(');\n')

    # -------------------------------------------------------------------------
    # Execução Real via PyMongo (caso disponível e serviço ativo)
    # -------------------------------------------------------------------------
    pymongo_disponivel = False
    try:
        import pymongo  # type: ignore
        pymongo_disponivel = True
    except ImportError:
        pass

    if pymongo_disponivel and servico_ativo:
        print("🔗 Conectando ao serviço local MongoDB (localhost:27017) via PyMongo...")
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
            db = client["ads_comercio"]
            col = db["clientes"]

            # Limpa registro anterior de teste para idempotência
            col.delete_one({"_id": doc_cliente["_id"]})

            # Inserção
            res_insert = col.insert_one(doc_cliente)
            print(f"✅ Inserção Real Realizada no MongoDB com sucesso! _id={res_insert.inserted_id}")

            # Consulta por campo embutido
            doc_encontrado = col.find_one({"endereco.cidade": "Tauá"})
            print(f"🔍 Documento recuperado por chave aninhada 'endereco.cidade':")
            print(f"   Nome: {doc_encontrado['nome']} | Pedidos: {len(doc_encontrado['pedidos'])}")

            # Atualização atômica ($push)
            novo_item = {"produto": "Teclado Mecânico", "quantidade": 1, "preco_unitario": 250.0}
            col.update_one({"_id": 1}, {"$push": {"pedidos.0.itens": novo_item}})
            print("⚡ Atualização atômica ($push) realizada sem nenhum JOIN!")

            doc_atualizado = col.find_one({"_id": 1})
            qtd_itens = len(doc_atualizado["pedidos"][0]["itens"])
            print(f"📦 Total de itens no Pedido 1 após atualização: {qtd_itens}")
            client.close()
            return
        except Exception as e:
            print(f"⚠️  Aviso ao comunicar com o MongoDB: {e}")

    # -------------------------------------------------------------------------
    # Simulação Didática Fiel (caso o serviço não esteja rodando nesta máquina)
    # -------------------------------------------------------------------------
    print("ℹ️  Status do Serviço MongoDB local: ", end="")
    if not servico_ativo:
        print("❌ Inativo na porta 27017")
        print("   -> Para iniciar o serviço no Ubuntu : sudo systemctl start mongod")
        print("   -> Para iniciar o serviço no Windows: net start MongoDB ou Start-Service MongoDB")
        print("   -> Para iniciar via Docker          : docker run -d -p 27017:27017 mongo:latest")
    else:
        print("✅ Porta 27017 aberta (PyMongo não instalado no ambiente do interpretador)")

    print("\n🧪 Executando Simulação Didática do Motor de Documentos MongoDB:")
    banco_em_memoria: Dict[int, Dict[str, Any]] = {}

    # 1. Inserção
    banco_em_memoria[doc_cliente["_id"]] = doc_cliente
    print(f"   [MongoDB engine] insertOne -> Documento inserido com _id: {doc_cliente['_id']}")

    # 2. Consulta filtrando por campo aninhado (Dot notation: endereco.cidade)
    resultado = [
        doc for doc in banco_em_memoria.values()
        if doc.get("endereco", {}).get("cidade") == "Tauá"
    ]
    print(f"   [MongoDB engine] find({{\"endereco.cidade\": \"Tauá\"}}) -> {len(resultado)} documento(s) retornado(s)")

    # 3. Operador de atualização $push
    banco_em_memoria[1]["pedidos"][0]["itens"].append({
        "produto": "Teclado Mecânico",
        "quantidade": 1,
        "preco_unitario": 250.0
    })
    print("   [MongoDB engine] updateOne($push) -> Item adicionado atomicamente no array interno!")
    print("   [Resultado] Entidade completa persistida sem necessidade de reconstrução relacional.")


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    print("*" * 75)
    print(" IFCE Campus Tauá - ADS | Bancos de Dados Não-Relacionais")
    print(" Aula 01: Demonstração de Impedance Mismatch, Modelos NoSQL & MongoDB")
    print("*" * 75)

    # 1. Demonstração Relacional (SQLite)
    demonstrar_abordagem_relacional()

    # 2. Demonstração de Documento (Orientado a Agregados)
    demonstrar_abordagem_documento()

    # 3. Execução Prática do Banco no MongoDB
    demonstrar_execucao_mongodb()

    print("\n" + "=" * 75)
    print(" 📖 ROTEIRO PARA INSTALAÇÃO DO SERVIÇO EM SEU SISTEMA OPERACIONAL:")
    print("=" * 75)
    print(GUIA_INSTALACAO_UBUNTU)
    print(GUIA_INSTALACAO_WINDOWS)
    print(GUIA_DOCKER_IFCE)
    print("=" * 75)
    print(" 📊 RESUMO DE APRENDIZAGEM (Aula 01)")
    print("=" * 75)
    print(" • RDBMS Relacional : Excelente para transações financeiras estritas (ACID),")
    print("   porém custoso para escalar horizontalmente sob grandes volumes.")
    print(" • NoSQL Documentos: Armazena o agregado como unidade atômica (1 I/O),")
    print("   suporta escala horizontal nativa e evolução de esquema sem atrito.")
    print("=" * 75 + "\n")
