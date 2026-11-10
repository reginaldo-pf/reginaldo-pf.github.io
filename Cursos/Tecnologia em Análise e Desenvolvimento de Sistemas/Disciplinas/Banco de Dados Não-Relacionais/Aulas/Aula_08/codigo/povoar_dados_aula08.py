#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Povoamento de Dados para a Aula 08: MongoDB Aggregation Framework
Disciplina: Banco de Dados Não-Relacionais (ADS16) - IFCE Campus Tauá
Professor: Prof. Me. Reginaldo Fernandes

Povoa o banco `ecommerce_shopgrids` com o schema canônico completo:
- `clientes`: 2.500 documentos (cliente_id de 1001 a 3500, cidades do CE e Brasil, dados de contato e segmento)
- `produtos`: 50.000 documentos com categorias, preços, estoque e tags
- `pedidos`: 10.000 documentos com subdocumentos de itens, pagamento e status
- `avaliacoes`: 25.000 documentos vinculados a produtos (sku) e clientes (cliente_id)

Também cria índices de suporte à agregação, cria a view `cliente` (alias)
e exporta amostras para o MongoDB Compass.

Uso:
    python povoar_dados_aula08.py
    python povoar_dados_aula08.py --produtos 10000 --pedidos 5000
"""

import argparse
import json
import os
import random
import sys
import time
from datetime import datetime, timedelta, timezone

from bson import ObjectId, json_util
from pymongo import InsertOne, MongoClient
from pymongo.errors import ConnectionFailure

# ---------------------------------------------------------------------------
# CONFIGURAÇÕES
# ---------------------------------------------------------------------------
URI_PADRAO = "mongodb://localhost:27017"
NOME_BANCO = "ecommerce_shopgrids"
TAMANHO_LOTE = 5_000
PADRAO_PRODUTOS = 50_000
PADRAO_PEDIDOS = 10_000
PADRAO_CLIENTES = 2_500
PADRAO_AVALIACOES = 25_000

CATEGORIAS = {
    "Informática": "INF",
    "Eletrônicos": "ELE",
    "Periféricos": "PER",
    "Smartphones": "SMA",
    "Gamer": "GAM",
    "Acessórios": "ACE",
    "Áudio": "AUD",
    "Armazenamento": "ARM",
    "Redes": "RED",
    "Monitores": "MON",
}

TITULOS = {
    "Informática": (
        ["Notebook", "Desktop", "Mini PC", "Workstation", "Placa de Vídeo", "Processador", "Memória RAM"],
        ["Ultrafino", "Profissional", "Compacto", "Turbo", "Performance", "Silencioso"],
        ["Core i5", "Ryzen 7", "16GB DDR5", "RTX 4060", "Pro 15", "Slim 14"],
    ),
    "Eletrônicos": (
        ["Smart TV", "Smartwatch", "Projetor", "Carregador", "Câmera de Segurança", "Fone Inteligente"],
        ["Inteligente", "Portátil", "Full HD", "Wi-Fi", "Automático", "Premium"],
        ["Série X", "Plus", "Max", "Lite", "2025", "Neo"],
    ),
    "Periféricos": (
        ["Teclado Mecânico", "Mouse Óptico", "Webcam", "Mousepad", "Mesa Digitalizadora", "Hub USB"],
        ["RGB", "Sem Fio", "Ergonômico", "Compacto", "Silencioso", "Retroiluminado"],
        ["K550", "M720", "Pro 1080p", "XL", "Tenkeyless", "Hot-Swap"],
    ),
    "Smartphones": (
        ["Smartphone", "Celular", "Telefone Dobrável", "Smartphone Rugged"],
        ["5G", "Dual Chip", "Tela AMOLED", "Bateria Longa", "Câmera Tripla", "Desbloqueado"],
        ["128GB", "256GB", "Note 12", "Galaxy A", "Edge 40", "Pro Max"],
    ),
    "Gamer": (
        ["Headset Gamer", "Cadeira Gamer", "Controle", "Teclado Gamer", "Mouse Gamer", "Placa Capture"],
        ["RGB", "Pro", "Elite", "Sem Fio", "Competitivo", "Ergonômico"],
        ["Hunter 7.1", "Striker X", "Titan 3000", "Viper", "Phantom", "Apex 2500"],
    ),
    "Acessórios": (
        ["Cabo USB-C", "Capa Protetora", "Suporte Articulado", "Película de Vidro", "Carregador Veicular", "Adaptador HDMI"],
        ["Reforçado", "Trançado", "Universal", "Dobrável", "Magnético", "Rápido"],
        ["1,5m", "2m", "65W", "100W", "Slim", "Duo"],
    ),
    "Áudio": (
        ["Fone de Ouvido", "Caixa de Som", "Soundbar", "Microfone", "Fone Intra-auricular", "Mesa de Som"],
        ["Bluetooth", "Sem Fio", "com Cancelamento de Ruído", "Portátil", "Estéreo", "Hi-Fi"],
        ["BT500", "Bass Boost", "ANC Pro", "Studio 2", "Mini", "Stage 300"],
    ),
    "Armazenamento": (
        ["SSD NVMe", "SSD SATA", "HD Externo", "Pen Drive", "Cartão MicroSD", "HD Interno"],
        ["Ultrarrápido", "Portátil", "Resistente", "Compacto", "de Alta Capacidade", "Industrial"],
        ["500GB", "1TB", "2TB", "128GB", "Gen4", "USB 3.2"],
    ),
    "Redes": (
        ["Roteador", "Switch", "Repetidor", "Access Point", "Placa de Rede", "Modem"],
        ["Wi-Fi 6", "Gigabit", "Dual Band", "Mesh", "Gerenciável", "PoE"],
        ["AX3000", "AC1200", "8 Portas", "16 Portas", "Tri-Band", "Enterprise"],
    ),
    "Monitores": (
        ["Monitor", "Monitor UltraWide", "Monitor Curvo", "Monitor Gamer", "Monitor Profissional"],
        ["4K", "Full HD", "QHD", "IPS", "144Hz", "HDR"],
        ["24 pol", "27 pol", "29 pol", "32 pol", "34 pol", "UltraSharp"],
    ),
}

DESCRICOES = {
    "Informática": [
        "Equipamento com processador multinúcleo de alto desempenho e memória DDR5 expansível.",
        "Armazenamento NVMe com leitura sequencial acelerada e tecnologia de refrigeração otimizada.",
        "Ideal para virtualização, desenvolvimento de software e processamento de dados.",
        "Conectividade moderna com Thunderbolt, USB-C e Wi-Fi 6E.",
    ],
    "Eletrônicos": [
        "Dispositivo com conectividade Wi-Fi, Bluetooth 5.3 e integração com assistentes de voz.",
        "Painel de alta resolução com processamento de imagem e baixo consumo de energia.",
        "Compatível com automação residencial, aplicativo dedicado e atualizações via firmware.",
        "Construção robusta com bateria de longa duração e carregamento rápido.",
    ],
    "Periféricos": [
        "Switches mecânicos com atuação precisa, anti-ghosting e polling rate de 1000Hz.",
        "Sensor óptico de alta precisão com DPI ajustável e iluminação RGB personalizável.",
        "Design ergonômico que reduz a fadiga em longas jornadas de trabalho.",
        "Conexão sem fio de baixa latência via receptor 2.4GHz ou Bluetooth.",
    ],
    "Smartphones": [
        "Tela AMOLED com taxa de atualização de 120Hz e brilho adaptativo.",
        "Câmera principal com estabilização óptica, modo noturno e gravação em 4K.",
        "Processador octa-core com suporte a 5G e memória RAM de alta velocidade.",
        "Bateria de grande capacidade com carregamento rápido e carregamento sem fio.",
    ],
    "Gamer": [
        "Projetado para jogos competitivos com latência ultrabaixa e resposta imediata.",
        "Áudio surround virtual 7.1 com microfone destacável e cancelamento de ruído.",
        "Iluminação RGB sincronizável por software com perfis e macros programáveis.",
        "Estrutura reforçada para sessões longas de jogo em alta taxa de quadros.",
    ],
    "Acessórios": [
        "Material resistente com acabamento premium e proteção contra impactos e arranhões.",
        "Compatível com diversos dispositivos, com suporte a Power Delivery e transferência de dados rápida.",
        "Cabo trançado com conectores reforçados e proteção contra sobrecarga.",
        "Design compacto e portátil, ideal para uso doméstico, escritório e viagens.",
    ],
    "Áudio": [
        "Drivers dinâmicos com graves profundos, resposta de frequência ampla e baixa distorção.",
        "Bluetooth 5.3 com codec aptX, cancelamento ativo de ruído e modo ambiente.",
        "Bateria com autonomia de até 40 horas e carregamento via USB-C.",
        "Microfone com tecnologia de redução de ruído para chamadas e gravações.",
    ],
    "Armazenamento": [
        "Velocidades de leitura e escrita sequencial elevadas, com controladora de última geração.",
        "Tecnologia NAND 3D com alta durabilidade (TBW) e proteção contra falhas de energia.",
        "Interface NVMe PCIe Gen4 ou SATA III, compatível com notebooks e desktops.",
        "Resistente a choques e vibrações, com criptografia por hardware AES de 256 bits.",
    ],
    "Redes": [
        "Wi-Fi 6 com tecnologia MU-MIMO, OFDMA e beamforming para maior cobertura.",
        "Portas Gigabit Ethernet com suporte a QoS, VLAN e controle de banda.",
        "Segurança com criptografia WPA3, firewall integrado e rede para convidados.",
        "Gerenciamento centralizado por aplicativo, com configuração simplificada e topologia mesh.",
    ],
    "Monitores": [
        "Painel IPS com cobertura de 99% sRGB, tempo de resposta de 1ms e taxa de atualização elevada.",
        "Tecnologia HDR10, Adaptive-Sync e baixa emissão de luz azul para maior conforto visual.",
        "Entradas HDMI 2.1, DisplayPort e USB-C com Power Delivery.",
        "Base ajustável em altura, inclinação e rotação, com suporte VESA.",
    ],
}

TAGS_POOL = [
    "gamer", "rgb", "sem fio", "usb-c", "ergonomico", "bluetooth", "promocao", "4k",
    "wi-fi 6", "nvme", "hdmi", "portatil", "lancamento", "premium", "custo-beneficio",
    "bateria longa", "full hd", "mecanico", "silencioso", "compacto",
]

PRENOMES = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena",
    "Igor", "Juliana", "Lucas", "Mariana", "Nicolas", "Olivia", "Paulo", "Quezia",
    "Rafael", "Sabrina", "Tiago", "Vanessa", "Mateus", "Larissa", "Rodrigo", "Beatriz",
    "Felipe", "Camila", "Gustavo", "Aline", "Vinicius", "Jessica", "Renato", "Leticia",
    "Diego", "Amanda", "Marcio", "Bruna", "Danilo", "Patricia", "Leonardo", "Renata",
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Lima", "Pereira", "Costa", "Martins",
    "Ferreira", "Rocha", "Alves", "Ribeiro", "Dias", "Mendes", "Carvalho", "Gomes",
    "Barbosa", "Castro", "Moreira", "Cardoso", "Freitas", "Araujo", "Nunes", "Teixeira",
    "Pinto", "Cunha", "Farias", "Sales", "Cavalcante", "Nascimento", "Monteiro",
]

CIDADES_ESTADOS = [
    ("Tauá", "CE"), ("Fortaleza", "CE"), ("Iguatu", "CE"), ("Sobral", "CE"),
    ("Juazeiro do Norte", "CE"), ("Crateús", "CE"), ("Quixadá", "CE"),
    ("Recife", "PE"), ("Caruaru", "PE"), ("Petrolina", "PE"),
    ("Salvador", "BA"), ("Feira de Santana", "BA"), ("Vitória da Conquista", "BA"),
    ("Natal", "RN"), ("Mossoró", "RN"),
    ("João Pessoa", "PB"), ("Campina Grande", "PB"),
    ("Teresina", "PI"), ("Parnaíba", "PI"), ("Picos", "PI"),
    ("São Paulo", "SP"), ("Campinas", "SP"), ("Santos", "SP"),
    ("Rio de Janeiro", "RJ"), ("Niterói", "RJ"),
    ("Belo Horizonte", "MG"), ("Uberlândia", "MG"),
    ("Curitiba", "PR"), ("Porto Alegre", "RS"), ("Brasília", "DF")
]

SEGMENTOS = ["Varejo", "VIP", "Corporativo"]
PESOS_SEGMENTOS = [70, 20, 10]

STATUS_PRODUTO = ["ATIVO", "INATIVO", "ESGOTADO"]
PESOS_STATUS_PRODUTO = [70, 15, 15]

STATUS_PEDIDO = ["PENDENTE", "PAGO", "EM_TRANSPORTE", "ENTREGUE", "CANCELADO"]
PESOS_STATUS_PEDIDO = [15, 25, 20, 30, 10]
STATUS_COM_PAGAMENTO = {"PAGO", "EM_TRANSPORTE", "ENTREGUE"}

TITULOS_AVALIACAO = {
    5: ["Excelente produto!", "Superou as expectativas", "Qualidade impressionante", "Recomendo fortemente", "Perfeito para o dia a dia"],
    4: ["Muito bom", "Ótimo custo-benefício", "Atendeu bem", "Entrega rápida e bom produto", "Recomendo"],
    3: ["Produto razoável", "Cumpre o básico", "Dentro do esperado", "Razoável pelo preço", "Poderia ser melhor"],
    2: ["Esperava mais", "Acabamento fraco", "Não gostei muito", "Decepcionou em alguns pontos", "Pelo preço não compensa"],
    1: ["Péssima experiência", "Chegou com defeito", "Não recomendo", "Parou de funcionar rápido", "Muito ruim"]
}

COMENTARIOS_AVALIACAO = {
    5: ["Desempenho incrível, acabamento premium e entrega pontual.", "Muito satisfeito com a compra, produto robusto e veloz.", "Excelente compra! Uso diariamente para estudos e trabalho."],
    4: ["Bom custo-benefício, acabamento correto e atende muito bem.", "Ótimo produto, apenas a embalagem poderia vir mais reforçada.", "Funciona perfeitamente, entrega foi antes do prazo estipulado."],
    3: ["Produto razoável, construção intermediária mas funciona.", "Pelo valor compensa se você não tiver exigência profissional.", "Atende ao básico, nada excepcional."],
    2: ["Qualidade abaixo do que as fotos mostravam no anúncio.", "Apresentou pequenas falhas nas primeiras semanas de uso.", "Achei o material frágil demais pelo preço cobrado."],
    1: ["Não funcionou de acordo com as especificações. Solicitei devolução.", "Quebrou em poucos dias de uso moderado. Muito decepcionado.", "Péssima durabilidade, suporte demorou a responder."]
}

# ---------------------------------------------------------------------------
# GERADORES DE DOCUMENTOS
# ---------------------------------------------------------------------------
def gerar_cliente(cliente_id, agora):
    """Gera documento da coleção `clientes`."""
    nome = f"{random.choice(PRENOMES)} {random.choice(SOBRENOMES)} {random.choice(SOBRENOMES)}"
    cidade, uf = random.choice(CIDADES_ESTADOS)
    ddd = "88" if uf == "CE" and cidade in ["Tauá", "Iguatu", "Crateús", "Juazeiro do Norte", "Sobral", "Quixadá"] else "85" if uf == "CE" else "11" if uf == "SP" else "21" if uf == "RJ" else "81" if uf == "PE" else "71"
    telefone = f"({ddd}) 9{random.randint(8000, 9999)}-{random.randint(1000, 9999)}"
    email_user = nome.lower().replace(" ", ".")[:20]
    email = f"{email_user}{cliente_id}@exemplo.com.br"
    segmento = random.choices(SEGMENTOS, weights=PESOS_SEGMENTOS, k=1)[0]
    data_cadastro = agora - timedelta(seconds=random.randint(30 * 24 * 3600, 730 * 24 * 3600))

    return {
        "_id": ObjectId(),
        "cliente_id": cliente_id,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "cidade": cidade,
        "estado": uf,
        "segmento": segmento,
        "data_cadastro": data_cadastro,
    }

def gerar_produto(numero, agora):
    """Gera documento da coleção `produtos`."""
    categoria = random.choice(list(CATEGORIAS))
    cod = CATEGORIAS[categoria]
    substantivos, adjetivos, modelos = TITULOS[categoria]

    titulo = f"{random.choice(substantivos)} {random.choice(adjetivos)} {random.choice(modelos)} {numero}"
    descricao = (
        f"{titulo}. "
        + " ".join(random.sample(DESCRICOES[categoria], k=2))
        + f" Garantia de {random.choice([6, 12, 18, 24])} meses."
    )

    minimo = random.randint(5, 20)
    atual = random.randint(minimo, 150)
    preco = round(random.uniform(29.90, 8999.00), 2)
    data_cadastro = agora - timedelta(seconds=random.randint(0, 730 * 24 * 3600))

    return {
        "sku": f"SKU-{cod}-{numero:06d}",
        "titulo": titulo,
        "descricao": descricao,
        "categoria": categoria,
        "preco": preco,
        "estoque": {"atual": atual, "minimo": minimo},
        "status": random.choices(STATUS_PRODUTO, weights=PESOS_STATUS_PRODUTO, k=1)[0],
        "tags": random.sample(TAGS_POOL, k=random.randint(2, 4)),
        "data_cadastro": data_cadastro,
    }

def montar_itens(skus):
    quantidade_itens = random.randint(1, 4)
    skus_escolhidos = random.sample(skus, k=min(quantidade_itens, len(skus)))
    itens = []
    for sku in skus_escolhidos:
        itens.append({
            "sku": sku,
            "preco": round(random.uniform(29.90, 4999.00), 2),
            "qtd": random.randint(1, 4),
            "status_entrega": "PENDENTE",
        })
    return itens

def gerar_pedido(numero, skus, min_cliente_id, max_cliente_id, agora):
    """Gera documento da coleção `pedidos`."""
    itens = montar_itens(skus)
    status = random.choices(STATUS_PEDIDO, weights=PESOS_STATUS_PEDIDO, k=1)[0]
    subtotal = round(sum(i["preco"] * i["qtd"] for i in itens), 2)
    if status in STATUS_COM_PAGAMENTO:
        total_pago = round(subtotal * (1 - random.choice([0, 0, 0.05, 0.10])), 2)
    else:
        total_pago = 0.0

    data_criacao = agora - timedelta(seconds=random.randint(0, 180 * 24 * 3600))

    return {
        "codigo": f"PED-2026-{numero:06d}",
        "cliente_id": random.randint(min_cliente_id, max_cliente_id),
        "status": status,
        "itens": itens,
        "pagamento": {"subtotal": subtotal, "total_pago": total_pago},
        "data_criacao": data_criacao,
    }

def gerar_avaliacao(numero, skus, clientes_dict, agora):
    """Gera documento da coleção `avaliacoes`."""
    sku = random.choice(skus)
    cliente_id = random.choice(list(clientes_dict.keys()))
    cliente_nome = clientes_dict[cliente_id]["nome"]
    nota = random.choices([5, 4, 3, 2, 1], weights=[45, 30, 12, 8, 5], k=1)[0]
    titulo = random.choice(TITULOS_AVALIACAO[nota])
    comentario = random.choice(COMENTARIOS_AVALIACAO[nota])
    data_avaliacao = agora - timedelta(seconds=random.randint(0, 120 * 24 * 3600))

    return {
        "_id": ObjectId(),
        "avaliacao_id": f"AVAL-{numero:06d}",
        "sku": sku,
        "cliente_id": cliente_id,
        "cliente_nome": cliente_nome,
        "nota": nota,
        "titulo": titulo,
        "comentario": comentario,
        "util_sim": random.randint(0, 25),
        "recomendaria": nota >= 3,
        "data_avaliacao": data_avaliacao,
    }

# ---------------------------------------------------------------------------
# INSERÇÃO EM LOTES
# ---------------------------------------------------------------------------
def inserir_em_lotes(colecao, total, gerador, rotulo, tamanho_lote=TAMANHO_LOTE):
    inseridos = 0
    inicio = time.perf_counter()
    lote = []

    for i in range(1, total + 1):
        lote.append(InsertOne(gerador(i)))
        if len(lote) >= tamanho_lote:
            colecao.bulk_write(lote, ordered=False)
            inseridos += len(lote)
            lote.clear()
            print(f"   [{rotulo}] {inseridos:,} / {total:,} inseridos...".replace(",", "."))

    if lote:
        colecao.bulk_write(lote, ordered=False)
        inseridos += len(lote)
        lote.clear()

    tempo = time.perf_counter() - inicio
    print(f"   ✓ {rotulo}: {inseridos:,} documentos inseridos em {tempo:.2f}s".replace(",", "."))

# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Povoamento completo do MongoDB para a Aula 08 (com clientes e avaliações).")
    parser.add_argument("--clientes", type=int, default=PADRAO_CLIENTES)
    parser.add_argument("--produtos", type=int, default=PADRAO_PRODUTOS)
    parser.add_argument("--pedidos", type=int, default=PADRAO_PEDIDOS)
    parser.add_argument("--avaliacoes", type=int, default=PADRAO_AVALIACOES)
    parser.add_argument("--uri", default=URI_PADRAO)
    parser.add_argument("--lote", type=int, default=TAMANHO_LOTE)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)

    print("=" * 65)
    print(" POVOAMENTO DO BANCO ecommerce_shopgrids (AULA 08 - COMPLETO)")
    print("=" * 65)

    client = MongoClient(args.uri, serverSelectionTimeoutMS=4000)
    try:
        client.admin.command("ping")
    except ConnectionFailure:
        print("[ERRO] Não foi possível conectar ao MongoDB em", args.uri)
        sys.exit(1)

    db = client[NOME_BANCO]
    agora = datetime.now(timezone.utc).replace(microsecond=0)

    # 1. Limpeza
    print("\n[1/6] Limpando coleções e views existentes...")
    for col_name in ["clientes", "produtos", "pedidos", "avaliacoes", "cliente"]:
        try:
            db[col_name].drop()
        except Exception:
            pass

    # 2. Clientes (ID de 1001 a 1001 + total)
    print(f"\n[2/6] Inserindo {args.clientes:,} clientes...".replace(",", "."))
    min_cid = 1001
    max_cid = min_cid + args.clientes - 1
    clientes_dict = {}

    def gerar_e_guardar_cliente(n):
        cid = min_cid + n - 1
        doc = gerar_cliente(cid, agora)
        clientes_dict[cid] = {"nome": doc["nome"], "cidade": doc["cidade"], "estado": doc["estado"]}
        return doc

    inserir_em_lotes(db.clientes, args.clientes, gerar_e_guardar_cliente, "clientes", args.lote)

    # Criação de view 'cliente' -> 'clientes' para interoperabilidade total
    try:
        db.command("create", "cliente", viewOn="clientes", pipeline=[])
    except Exception:
        pass

    # 3. Produtos
    print(f"\n[3/6] Inserindo {args.produtos:,} produtos...".replace(",", "."))
    skus = []
    def gerar_e_guardar_sku(n):
        p = gerar_produto(n, agora)
        skus.append(p["sku"])
        return p

    inserir_em_lotes(db.produtos, args.produtos, gerar_e_guardar_sku, "produtos", args.lote)

    # 4. Pedidos
    print(f"\n[4/6] Inserindo {args.pedidos:,} pedidos...".replace(",", "."))
    inserir_em_lotes(db.pedidos, args.pedidos, lambda n: gerar_pedido(n, skus, min_cid, max_cid, agora), "pedidos", args.lote)

    # 5. Avaliações
    print(f"\n[5/6] Inserindo {args.avaliacoes:,} avaliações...".replace(",", "."))
    inserir_em_lotes(db.avaliacoes, args.avaliacoes, lambda n: gerar_avaliacao(n, skus, clientes_dict, agora), "avaliacoes", args.lote)

    # 6. Índices Estratégicos
    print("\n[6/6] Criando índices otimizados para pipelines de agregação...")
    db.clientes.create_index([("cliente_id", 1)], unique=True, name="idx_clientes_cliente_id")
    db.clientes.create_index([("estado", 1)], name="idx_clientes_estado")
    db.produtos.create_index([("sku", 1)], unique=True, name="idx_produtos_sku")
    db.produtos.create_index([("categoria", 1)], name="idx_produtos_categoria")
    db.pedidos.create_index([("status", 1), ("data_criacao", -1)], name="idx_pedidos_status_data")
    db.pedidos.create_index([("cliente_id", 1)], name="idx_pedidos_cliente_id")
    db.pedidos.create_index([("itens.sku", 1)], name="idx_pedidos_itens_sku")
    db.avaliacoes.create_index([("sku", 1)], name="idx_avaliacoes_sku")
    db.avaliacoes.create_index([("cliente_id", 1)], name="idx_avaliacoes_cliente_id")
    db.avaliacoes.create_index([("nota", 1)], name="idx_avaliacoes_nota")

    # Exportar amostras em JSON para apoio no Compass
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    amostras_pedidos = list(db.pedidos.find().limit(5))
    with open(os.path.join(diretorio_atual, "pedidos_amostra_aula08.json"), "w", encoding="utf-8") as f:
        f.write(json_util.dumps(amostras_pedidos, indent=2, ensure_ascii=False))

    amostras_clientes = list(db.clientes.find().limit(5))
    with open(os.path.join(diretorio_atual, "clientes_amostra_aula08.json"), "w", encoding="utf-8") as f:
        f.write(json_util.dumps(amostras_clientes, indent=2, ensure_ascii=False))

    amostras_avaliacoes = list(db.avaliacoes.find().limit(5))
    with open(os.path.join(diretorio_atual, "avaliacoes_amostra_aula08.json"), "w", encoding="utf-8") as f:
        f.write(json_util.dumps(amostras_avaliacoes, indent=2, ensure_ascii=False))

    print(f"   ✓ Amostras JSON exportadas para apoio didático no Compass.")
    print("=" * 65)
    print(" POVOAMENTO CONCLUÍDO COM SUCESSO!")
    print(f" • Clientes:   {db.clientes.count_documents({}):,} documentos".replace(",", "."))
    print(f" • Produtos:   {db.produtos.count_documents({}):,} documentos".replace(",", "."))
    print(f" • Pedidos:    {db.pedidos.count_documents({}):,} documentos".replace(",", "."))
    print(f" • Avaliações: {db.avaliacoes.count_documents({}):,} documentos".replace(",", "."))
    print(f" • View:       db.cliente (espelho de db.clientes)")
    print("=" * 65)

if __name__ == "__main__":
    main()
