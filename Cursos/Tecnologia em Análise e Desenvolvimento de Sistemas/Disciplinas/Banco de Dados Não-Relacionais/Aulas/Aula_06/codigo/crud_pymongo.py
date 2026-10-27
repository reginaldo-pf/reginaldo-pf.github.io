#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina: Banco de Dados Não-Relacionais (ADS16) — Aula 06
Docente: Prof. Me. Reginaldo Fernandes

Script: crud_pymongo.py
Descrição:
  - Parte 1: Operações CRUD e consultas básicas com o driver Python (PyMongo)
  - Parte 2: Exemplos de modelagem de documentos (Embedded Data e References)
"""

from pprint import pprint
from bson import ObjectId
from pymongo import MongoClient, InsertOne, UpdateOne, DeleteOne


def etapa1_conexao_e_crud(client: MongoClient):
    """Executa passo a passo o CRUD com PyMongo."""
    print("=" * 76)
    print(" PARTE 1: OPERACOES CRUD PASSO A PASSO COM PYMONGO")
    print("=" * 76)

    # 1. Confirmando a conexão com ping
    client.admin.command("ping")
    print("[OK] Conectado ao MongoDB com sucesso!")

    # Seleciona o banco 'mongodb_books' e limpa para execução reproduzível
    client.drop_database("mongodb_books")
    db = client.mongodb_books
    books = db.books

    # 2. Inserindo documentos com insert_one e insert_many
    print("\n--- 1. Inserindo documento com insert_one() (ISBN 301) ---")
    book_301 = {
        "isbn": "301",
        "name": "Python and MongoDB",
        "meta": {"version": "MongoDB 7.0"},
        "price": 60,
    }
    insert_result = books.insert_one(book_301)
    print(f"Documento inserido com _id: {insert_result.inserted_id}")

    print("\n--- 2. Inserindo documentos adicionais (ISBN 302 e 303) ---")
    books.insert_many(
        [
            {
                "isbn": "302",
                "name": "Python and MongoDB",
                "meta": {"version": "MongoDB 7.0"},
                "price": 60,
            },
            {
                "isbn": "303",
                "name": "Advanced MongoDB Techniques",
                "price": 70,
            },
        ]
    )
    print("Coleções existentes em 'mongodb_books':", db.list_collection_names())

    # 3. Consultando documentos com find()
    print("\n--- 3. Buscando livros com name = 'Python and MongoDB' ---")
    for doc in books.find({"name": "Python and MongoDB"}):
        pprint(doc)

    # 4. Consultando subdocumento com Dot Notation ('meta.version') e $regex
    print("\n--- 4. Buscando no subdocumento 'meta.version' com $regex case-insensitive ---")
    query_regex = {
        "meta.version": {
            "$regex": r".*?g.*?7\.0$",
            "$options": "i",
        }
    }
    for doc in books.find(query_regex):
        pprint(doc)

    # 5. Operador de comparação $gt (price > 50)
    print("\n--- 5. Buscando livros com price > 50 ($gt) ---")
    for doc in books.find({"price": {"$gt": 50}}):
        pprint(doc)

    # 6. Condição lógica AND
    print("\n--- 6. Condição lógica AND (name = 'Advanced MongoDB Techniques' E price = 70) ---")
    query_and = {
        "name": "Advanced MongoDB Techniques",
        "price": 70,
    }
    for doc in books.find(query_and):
        pprint(doc)

    # 7. Condição lógica OR ($or)
    print("\n--- 7. Condição lógica $or (Advanced MongoDB Techniques OU isbn = '301') ---")
    query_or = {
        "$or": [
            {"name": "Advanced MongoDB Techniques"},
            {"isbn": "301"},
        ]
    }
    for doc in books.find(query_or):
        pprint(doc)

    # 8. Atualizando documento com update_one e $set
    print("\n--- 8. Atualizando price para 75 com update_one() e $set ---")
    update_result = books.update_one(
        {"name": "Advanced MongoDB Techniques"},
        {"$set": {"price": 75}},
    )
    print("Resultado bruto (raw_result):", update_result.raw_result)
    print("Documento após atualização:")
    pprint(books.find_one({"name": "Advanced MongoDB Techniques"}))

    # 9. Removendo documento com delete_one
    print("\n--- 9. Removendo o livro de ISBN '303' com delete_one() ---")
    delete_result = books.delete_one({"isbn": "303"})
    print("Resultado bruto (raw_result):", delete_result.raw_result)

    # 10. Operações em Lote com bulk_write
    print("\n--- 10. Operação em Lote (bulk_write) ---")
    bulk_result = books.bulk_write(
        [
            InsertOne({"isbn": "304", "name": "MongoDB 7.0 Guia Pratico", "price": 55}),
            UpdateOne({"isbn": "301"}, {"$set": {"price": 65}}),
            DeleteOne({"isbn": "302"}),
        ]
    )
    print(
        f"Resumo bulk_write -> Inseridos: {bulk_result.inserted_count}, "
        f"Modificados: {bulk_result.modified_count}, Removidos: {bulk_result.deleted_count}"
    )


def etapa2_exemplos_modelagem(client: MongoClient):
    """Demonstra exemplos de Schema Design (Polimorfismo, Aninhamento e Referencing)."""
    print("\n" + "=" * 76)
    print(" PARTE 2: EXEMPLOS DE MODELAGEM DE DADOS (SCHEMA DESIGN)")
    print("=" * 76)

    db = client.mongodb_books

    # 1. Polimorfismo e Aninhamento na coleção 'users'
    db.users.insert_many(
        [
            {
                "name": "Sherlock Holmes",
                "age": 34,
                "address": "221B Baker Street",
                "hobbies": ["Violin", "Boxing"],
            },
            {
                "name": "John Watson",
                "age": 36,
                "profession": "Doctor",
            },
            {
                "name": "Alice Smith",
                "age": 28,
                "addresses": [
                    {
                        "type": "home",
                        "street": "123 Maple Street",
                        "city": "Springfield",
                        "zip": "12345",
                    },
                    {
                        "type": "work",
                        "street": "456 Oak Street",
                        "city": "Springfield",
                        "zip": "67890",
                    },
                ],
                "certificates": ["First Aid", "Scuba Diving", "Python Programming"],
            },
        ]
    )
    print("[OK] Coleção 'users' criada com documentos polimórficos e aninhados.")

    # 2. Referencing: Coleção 'professors' e 'courses'
    prof_id = ObjectId("6533e70e87e74d44d8f67d2d")
    db.professors.insert_one(
        {
            "_id": prof_id,
            "name": "Alan Turing",
            "department": "Computer Science",
        }
    )
    db.courses.insert_one(
        {
            "courseName": "Introduction to Computer Science",
            "professor": prof_id,  # Referência por ObjectId
            "department": "Computer Science",
        }
    )
    print("[OK] Coleções 'professors' e 'courses' criadas com Referencing por ObjectId.")


if __name__ == "__main__":
    cliente_mongo = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    etapa1_conexao_e_crud(cliente_mongo)
    etapa2_exemplos_modelagem(cliente_mongo)
