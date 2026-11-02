#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
povoar_banco.py
Povoa o banco `ecommerce_shopgrids` (MongoDB 7.0 / 8.0) para a aula prática
de "CRUD Avançado e Indexação de Alta Performance".

Uso:
    python povoar_banco.py
    python povoar_banco.py --produtos 100000 --pedidos 20000
    python povoar_banco.py --uri mongodb://localhost:27017 --seed 42

Requisito:
    pip install pymongo
"""

import argparse
import random
import sys
import time
from datetime import datetime, timedelta, timezone

from pymongo import InsertOne, MongoClient
from pymongo.errors import BulkWriteError, ConnectionFailure

# ---------------------------------------------------------------------------
# CONFIGURAÇÕES
# ---------------------------------------------------------------------------
URI_PADRAO = "mongodb://localhost:27017"
NOME_BANCO = "ecommerce_shopgrids"
TAMANHO_LOTE = 5_000
PADRAO_PRODUTOS = 50_000
PADRAO_PEDIDOS = 10_000

# categoria -> código de 3 letras usado no SKU
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

# categoria -> (substantivos, adjetivos, modelos de sufixo)
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

# categoria -> frases técnicas para a descrição (úteis para busca textual)
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

AUTORES = [
    "Ana Souza", "Bruno Lima", "Carla Mendes", "Diego Alves", "Elisa Rocha", "Fábio Nunes",
    "Gabriela Costa", "Henrique Dias", "Isabela Martins", "João Pereira", "Karina Teixeira",
    "Lucas Ribeiro", "Mariana Freitas", "Natan Barros", "Olívia Cardoso", "Paulo Moreira",
    "Quézia Araújo", "Rafael Gomes", "Sabrina Pinto", "Thiago Cunha",
]

COMENTARIOS = {
    1: ["Chegou com defeito.", "Não recomendo, qualidade muito abaixo do esperado.", "Parou de funcionar em poucos dias."],
    2: ["Esperava mais pelo preço.", "Funciona, mas tem acabamento fraco.", "Atende, porém decepcionou em alguns pontos."],
    3: ["Produto razoável, cumpre o básico.", "Bom para o preço, nada excepcional.", "Mediano, entrega conforme o anunciado."],
    4: ["Muito bom, recomendo.", "Ótimo custo-benefício e entrega rápida.", "Qualidade acima da média, gostei bastante."],
    5: ["Excelente! Superou as expectativas.", "Perfeito, compraria novamente.", "Produto incrível, desempenho impecável."],
}

STATUS_PRODUTO = ["ATIVO", "INATIVO", "ESGOTADO"]
PESOS_STATUS_PRODUTO = [70, 15, 15]

STATUS_PEDIDO = ["PENDENTE", "PAGO", "EM_TRANSPORTE", "ENTREGUE", "CANCELADO"]
PESOS_STATUS_PEDIDO = [15, 25, 20, 30, 10]
STATUS_COM_PAGAMENTO = {"PAGO", "EM_TRANSPORTE", "ENTREGUE"}

# fração de pedidos (com 2+ itens) que seguem o padrão "caro/qtd baixa + barato/qtd alta"
FRACAO_PADRAO_ELEMMATCH = 0.25
# fração de produtos com estoque abaixo do mínimo
FRACAO_ESTOQUE_CRITICO = 0.10


# ---------------------------------------------------------------------------
# GERAÇÃO DE PRODUTOS
# ---------------------------------------------------------------------------
def gerar_produto(numero, agora):
    """Gera um documento da coleção `produtos`."""
    # Produtos didáticos determinísticos para garantir execução exata dos exemplos de aula
    if numero == 101:
        return {
            "sku": "SKU-INF-000101",
            "titulo": "Teclado Mecânico RGB Gamer Pro",
            "descricao": "Switches mecânicos táteis de alta durabilidade com iluminação RGB individual e descanso de punho magnético. Ideal para desenvolvimento de software e jogos competitivos.",
            "categoria": "Informática",
            "preco": 349.90,
            "historico": {"menor_preco": 349.90},
            "estoque": {"atual": 18, "minimo": 10},
            "status": "ATIVO",
            "tags": ["gamer", "mecanico", "rgb", "usb-c"],
            "data_cadastro": agora - timedelta(days=60),
            "ultimas_avaliacoes": [
                {"nota": 5, "autor": "Lucas Farias", "comentario": "Excelente resposta e construção sólida."},
                {"nota": 4, "autor": "Mariana Sales", "comentario": "Muito bom, cabo resistente."},
                {"nota": 5, "autor": "Carlos Eduardo", "comentario": "Switch excelente e iluminação vibrante."}
            ],
        }

    if numero == 49999:
        return {
            "sku": "SKU-INF-049999",
            "titulo": "Processador Core i9 14900K Ultra Performance",
            "descricao": "Processador multinúcleo para estações de trabalho e virtualização intensiva. Arquitetura híbrida de alto rendimento.",
            "categoria": "Informática",
            "preco": 3899.00,
            "historico": {"menor_preco": 3899.00},
            "estoque": {"atual": 12, "minimo": 5},
            "status": "ATIVO",
            "tags": ["alta performance", "gamer", "promocao"],
            "data_cadastro": agora - timedelta(days=120),
            "ultimas_avaliacoes": [
                {"nota": 5, "autor": "Prof. Reginaldo", "comentario": "Desempenho extremo para benchmarks e carga pesada."}
            ],
        }

    categoria = random.choice(list(CATEGORIAS))
    cod = CATEGORIAS[categoria]
    substantivos, adjetivos, modelos = TITULOS[categoria]

    titulo = f"{random.choice(substantivos)} {random.choice(adjetivos)} {random.choice(modelos)}"
    descricao = (
        f"{titulo}. "
        + " ".join(random.sample(DESCRICOES[categoria], k=3))
        + f" Garantia de {random.choice([6, 12, 18, 24])} meses e nota fiscal inclusa."
    )

    # Estoque: ~10% com atual < mínimo (para demonstrar o operador $expr)
    minimo = random.randint(5, 20)
    if random.random() < FRACAO_ESTOQUE_CRITICO:
        atual = random.randint(0, minimo - 1)
    else:
        atual = random.randint(minimo, 150)

    preco = round(random.uniform(29.90, 8999.00), 2)
    data_cadastro = agora - timedelta(seconds=random.randint(0, 730 * 24 * 3600))

    avaliacoes = []
    for _ in range(random.randint(1, 3)):
        nota = random.randint(1, 5)
        avaliacoes.append({
            "nota": nota,
            "autor": random.choice(AUTORES),
            "comentario": random.choice(COMENTARIOS[nota]),
        })

    return {
        "sku": f"SKU-{cod}-{numero:06d}",
        "titulo": titulo,
        "descricao": descricao,
        "categoria": categoria,
        "preco": preco,
        "historico": {"menor_preco": round(preco * 1.05, 2)},
        "estoque": {"atual": atual, "minimo": minimo},
        "status": random.choices(STATUS_PRODUTO, weights=PESOS_STATUS_PRODUTO, k=1)[0],
        "tags": random.sample(TAGS_POOL, k=random.randint(2, 4)),
        "data_cadastro": data_cadastro,
        "ultimas_avaliacoes": avaliacoes,
    }


# ---------------------------------------------------------------------------
# GERAÇÃO DE PEDIDOS
# ---------------------------------------------------------------------------
def montar_itens(skus):
    """
    Monta o array `itens` de um pedido (1 a 4 itens, SKUs distintos).
    Em parte dos pedidos com 2+ itens aplica o padrão necessário para
    demonstrar $elemMatch e arrayFilters:
      - item A: preço alto e qtd = 1
      - item B: preço baixo e qtd alta (4 a 6)
    """
    quantidade_itens = random.randint(1, 4)
    skus_escolhidos = random.sample(skus, k=min(quantidade_itens, len(skus)))
    itens = []

    for sku in skus_escolhidos:
        itens.append({
            "sku": sku,
            "preco": round(random.uniform(29.90, 8999.00), 2),
            "qtd": random.randint(1, 6),
            "status_entrega": "PENDENTE",
        })

    if len(itens) >= 2 and random.random() < FRACAO_PADRAO_ELEMMATCH:
        itens[0]["preco"] = round(random.uniform(200.00, 1500.00), 2)
        itens[0]["qtd"] = 1
        itens[1]["preco"] = round(random.uniform(29.90, 60.00), 2)
        itens[1]["qtd"] = random.randint(4, 6)

    return itens


def gerar_pedido(numero, skus, agora, forcar_exemplo=False):
    """Gera um documento da coleção `pedidos`."""
    # Pedidos determinísticos para suportar testes diretos das queries de aula
    if numero == 1:
        # Pedido correspondente exato aos slides (secao2: PED-2026-001 e ITEM-A)
        return {
            "codigo": "PED-2026-001",
            "cliente_id": 1001,
            "status": "PENDENTE",
            "itens": [
                {"sku": "ITEM-A", "preco": 250.00, "qtd": 1, "status_entrega": "PENDENTE"},
                {"sku": "ITEM-B", "preco": 30.00, "qtd": 6, "status_entrega": "PENDENTE"},
            ],
            "pagamento": {"subtotal": 430.00, "total_pago": 430.00},
            "data_criacao": agora - timedelta(days=2),
        }

    if numero == 2:
        # Pedido com código PED-MOSH-TESTE para o script de mongosh
        return {
            "codigo": "PED-MOSH-TESTE",
            "cliente_id": 1001,
            "status": "PENDENTE",
            "itens": [
                {"sku": "ITEM-A", "preco": 250.00, "qtd": 1, "status_entrega": "PENDENTE"},
                {"sku": "ITEM-B", "preco": 30.00, "qtd": 6, "status_entrega": "PENDENTE"},
            ],
            "pagamento": {"subtotal": 430.00, "total_pago": 430.00},
            "data_criacao": agora - timedelta(days=1),
        }

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
        "cliente_id": random.randint(1001, 3500),
        "status": status,
        "itens": itens,
        "pagamento": {"subtotal": subtotal, "total_pago": total_pago},
        "data_criacao": data_criacao,
    }


# ---------------------------------------------------------------------------
# INSERÇÃO EM LOTES
# ---------------------------------------------------------------------------
def inserir_em_lotes(colecao, total, gerador, rotulo, tamanho_lote=TAMANHO_LOTE):
    """
    Gera e insere `total` documentos em lotes usando bulk_write(ordered=False).
    Mantém no máximo `tamanho_lote` documentos na memória por vez.
    """
    inseridos = 0
    inicio = time.perf_counter()

    for primeiro in range(1, total + 1, tamanho_lote):
        ultimo = min(primeiro + tamanho_lote - 1, total)
        operacoes = [InsertOne(gerador(n)) for n in range(primeiro, ultimo + 1)]

        try:
            resultado = colecao.bulk_write(operacoes, ordered=False)
            inseridos += resultado.inserted_count
        except BulkWriteError as erro:
            inseridos += erro.details.get("nInserted", 0)
            print(f"   [!] Erros no lote {primeiro}-{ultimo}: {erro.details.get('writeErrors', [])[:3]}")

        percentual = inseridos / total * 100
        print(f"   [{rotulo}] {inseridos:>7,}/{total:,} inseridos ({percentual:5.1f}%)".replace(",", "."))

    duracao = time.perf_counter() - inicio
    print(f"   [{rotulo}] concluído em {duracao:.2f}s\n")
    return inseridos


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------
def ler_argumentos():
    parser = argparse.ArgumentParser(description="Povoa o MongoDB `ecommerce_shopgrids` para a aula de indexação.")
    parser.add_argument("--produtos", type=int, default=PADRAO_PRODUTOS,
                        help=f"quantidade de produtos (padrão: {PADRAO_PRODUTOS})")
    parser.add_argument("--pedidos", type=int, default=PADRAO_PEDIDOS,
                        help=f"quantidade de pedidos (padrão: {PADRAO_PEDIDOS})")
    parser.add_argument("--uri", default=URI_PADRAO, help=f"URI de conexão (padrão: {URI_PADRAO})")
    parser.add_argument("--lote", type=int, default=TAMANHO_LOTE,
                        help=f"tamanho do lote de inserção (padrão: {TAMANHO_LOTE})")
    parser.add_argument("--seed", type=int, default=None,
                        help="semente aleatória para resultados reproduzíveis (opcional)")
    args = parser.parse_args()

    if args.produtos < 0 or args.pedidos < 0 or args.lote <= 0:
        parser.error("as quantidades devem ser positivas e o lote deve ser maior que zero.")
    return args


def main():
    args = ler_argumentos()
    if args.seed is not None:
        random.seed(args.seed)

    print("=" * 60)
    print(" POVOAMENTO DO BANCO ecommerce_shopgrids")
    print("=" * 60)

    client = MongoClient(args.uri, serverSelectionTimeoutMS=4000)
    try:
        client.admin.command("ping")
    except ConnectionFailure:
        print("\n[ERRO] Não foi possível conectar ao MongoDB em", args.uri)
        print("       Verifique se o servidor/contêiner está ativo, por exemplo:")
        print("       docker start mongodb   (ou)   docker run -d -p 27017:27017 --name mongodb mongo:7.0")
        sys.exit(1)

    db = client[NOME_BANCO]
    agora = datetime.now(timezone.utc).replace(microsecond=0)

    # Limpeza prévia
    print("\n[1/3] Limpando coleções existentes...")
    db.produtos.drop()
    db.pedidos.drop()

    # Produtos (guarda apenas os SKUs para reaproveitar nos pedidos)
    print(f"\n[2/3] Inserindo {args.produtos:,} produtos em lotes de {args.lote:,}...".replace(",", "."))
    skus = []

    def gerar_e_registrar_produto(numero):
        doc = gerar_produto(numero, agora)
        skus.append(doc["sku"])
        return doc

    inserir_em_lotes(db.produtos, args.produtos, gerar_e_registrar_produto, "produtos", args.lote)

    # Pedidos
    print(f"[3/3] Inserindo {args.pedidos:,} pedidos em lotes de {args.lote:,}...".replace(",", "."))
    if not skus and args.pedidos > 0:
        print("   [!] Sem produtos gerados: pedidos usarão SKUs sintéticos.")
        skus = [f"SKU-INF-{n:06d}" for n in range(1, 101)]

    inserir_em_lotes(
        db.pedidos,
        args.pedidos,
        lambda n: gerar_pedido(n, skus, agora, forcar_exemplo=(n == 1)),
        "pedidos",
        args.lote,
    )

    # Resumo final
    print("=" * 60)
    print(" RESUMO FINAL")
    print("=" * 60)
    print(f" Banco ............ {NOME_BANCO}")
    print(f" produtos ......... {db.produtos.count_documents({}):,} documentos".replace(",", "."))
    print(f" pedidos .......... {db.pedidos.count_documents({}):,} documentos".replace(",", "."))
    print(" Índices .......... apenas _id (índices secundários ficam para os alunos)")
    print("=" * 60)

    client.close()


if __name__ == "__main__":
    main()
