#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Índices Textuais (Full-Text Search) e Relevância no MongoDB
Disciplina: Banco de Dados Não-Relacionais (ADS16) - Aula 07
IFCE Campus Tauá - Prof. Me. Reginaldo Fernandes
"""

import sys
from pymongo import MongoClient, TEXT
from pymongo.errors import ConnectionFailure

def conectar():
    try:
        client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=2000)
        client.admin.command("ping")
        return client["ecommerce_shopgrids"]
    except ConnectionFailure:
        print("❌ Erro de conexão com o MongoDB. Suba o serviço com 'docker compose up -d'.")
        sys.exit(1)

def configurar_indice_textual(db):
    print("=" * 70)
    print("1. CONFIGURAÇÃO DE ÍNDICE TEXTUAL COM PESOS (WEIGHTS)")
    print("=" * 70)

    # Remover índices textuais pré-existentes
    for idx in db.produtos.list_indexes():
        if "weights" in idx:
            print(f"🗑️ Removendo índice textual antigo: {idx['name']}")
            db.produtos.drop_index(idx["name"])

    # Criando o índice de texto ponderado
    # titulo tem peso 10, tags tem peso 5 e descricao tem peso 2
    resultado = db.produtos.create_index(
        [
            ("titulo", TEXT),
            ("tags", TEXT),
            ("descricao", TEXT)
        ],
        weights={
            "titulo": 10,
            "tags": 5,
            "descricao": 2
        },
        default_language="portuguese",
        name="idx_busca_textual_ponderada"
    )
    print(f"✅ Índice textual '{resultado}' criado com sucesso!")
    print("   Pesos: titulo=10 | tags=5 | descricao=2 | idioma=português")

def demonstrar_buscas_textuais(db):
    print("\n" + "=" * 70)
    print("2. EXECUÇÃO DE CONSULTAS TEXTUAIS E RANKING POR ESCORE")
    print("=" * 70)

    # A) Busca simples por termos (OR implícito)
    termo_a = "ergonômico silencioso"
    print(f"\n🔍 A) Busca por termos: '{termo_a}'")
    cursor_a = db.produtos.find(
        {"$text": {"$search": termo_a}},
        {"titulo": 1, "preco": 1, "score": {"$meta": "textScore"}, "_id": 0}
    ).sort([("score", {"$meta": "textScore"})]).limit(4)

    for item in cursor_a:
        print(f"   Score: {item.get('score', 0):.2f} | R$ {item['preco']:>7.2f} | {item['titulo']}")

    # B) Busca por Frase Exata (com aspas escapadas)
    termo_b = '\"sem fio\"'
    print(f"\n🔍 B) Busca por Frase Exata: {termo_b}")
    cursor_b = db.produtos.find(
        {"$text": {"$search": termo_b}},
        {"titulo": 1, "score": {"$meta": "textScore"}, "_id": 0}
    ).sort([("score", {"$meta": "textScore"})]).limit(3)

    for item in cursor_b:
        print(f"   Score: {item.get('score', 0):.2f} | {item['titulo']}")

    # C) Busca com Negação / Exclusão de Termo (-gamer)
    termo_c = "mecânico -gamer"
    print(f"\n🔍 C) Busca com Exclusão de Palavra: '{termo_c}' (Contém 'mecânico', mas NÃO contém 'gamer')")
    cursor_c = db.produtos.find(
        {"$text": {"$search": termo_c}},
        {"titulo": 1, "score": {"$meta": "textScore"}, "_id": 0}
    ).sort([("score", {"$meta": "textScore"})]).limit(3)

    for item in cursor_c:
        print(f"   Score: {item.get('score', 0):.2f} | {item['titulo']}")

def demonstrar_stemming_vs_regex(db):
    print("\n" + "=" * 70)
    print("3. STEMMING (RADICALIZAÇÃO) vs EXPRESSÃO REGULAR ($regex)")
    print("=" * 70)

    # Inserir produto com palavra conjugada/pluralizada
    doc_teste = {
        "sku": "SKU-STEMMING-TESTE",
        "titulo": "Cadeira Ergonômica com Ajuste de Altura",
        "descricao": "Projetada para excelente conforto e durabilidade.",
        "categoria": "Gamer",
        "preco": 1250.0,
        "status": "ATIVO",
        "tags": ["ergonomia", "escritorio"]
    }
    db.produtos.delete_one({"sku": "SKU-STEMMING-TESTE"})
    db.produtos.insert_one(doc_teste)

    # Busca textual por "ergonômico" (masculino) -> o índice encontra "Ergonômica" via stemming!
    busca_stem = db.produtos.find_one(
        {"$text": {"$search": "ergonômico"}, "sku": "SKU-STEMMING-TESTE"},
        {"titulo": 1, "score": {"$meta": "textScore"}, "_id": 0}
    )
    
    # Busca por regex estrito "ergonômico" (sem radical)
    busca_regex = db.produtos.find_one(
        {"titulo": {"$regex": "ergonômico", "$options": "i"}, "sku": "SKU-STEMMING-TESTE"}
    )

    print("🔎 Testando termo de busca: 'ergonômico' contra título 'Cadeira Ergonômica'")
    print(f"   -> Busca Textual (com Stemming português): {' ENCONTROU!' if busca_stem else '❌ NÃO'}")
    print(f"   -> Regex exato ('ergonômico'):              {' ENCONTROU!' if busca_regex else '❌ NÃO (Falha de flexão de gênero!)'}")
    print("\nConclusão: O Text Index reconhece o radical comum da língua portuguesa, oferecendo busca semântica natural.")

def main():
    db = conectar()
    configurar_indice_textual(db)
    demonstrar_buscas_textuais(db)
    demonstrar_stemming_vs_regex(db)
    print("\n✅ Demonstração de busca textual finalizada com sucesso!\n")

if __name__ == "__main__":
    main()
