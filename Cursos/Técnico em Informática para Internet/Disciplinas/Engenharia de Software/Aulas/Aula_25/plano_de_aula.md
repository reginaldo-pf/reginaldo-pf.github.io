# Plano de Aula: Aula 25 - Persistência Relacional: Esquema SQLite e Padrão Repository (Sprint 04 - Encontro 2)

*   **Disciplina:** Engenharia de Software (Código: TSII.210 / 17.202.9 | Carga Horária: 80h)
*   **Curso:** Técnico em Informática para Internet
*   **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá
*   **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema da Sprint:** Construção de Artefatos de Software: Da Modelagem Relacional à Persistência com SQLite e Padrão Repository (Sprint 04: BiblioTauá).
*   **Encontro 2:** Aulas 3 e 4 de 50 minutos (Total: 100 minutos) — Semana 1.
*   **Referências Básicas:**
    *   PRESSMAN, Roger S.; MAXIM, Bruce R. *Engenharia de Software: Uma Abordagem Profissional*. 8ª Ed. Porto Alegre: AMGH, **Capítulos 10 e 11 (Projeto no Nível de Componente e Dados)**.
    *   GUEDES, Gilleanes T. A. *UML 2 – Uma abordagem prática*. São Paulo: Novatec Editora, **Capítulo 4 (Mapeamento Objeto-Relacional)**.

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o estudante a converter o modelo de classes de domínio para a arquitetura de persistência relacional, projetando o **Diagrama Entidade-Relacionamento (DER / Esquema Relacional)** no **SQLite** e implementando a camada de acesso a dados através do padrão de projeto **Repository**, garantindo blindagem estrita contra injeção SQL e operações concorrentes atômicas.

### Objetivos Específicos
*   **Compreender o Mapeamento Objeto-Relacional (ORM):** Mapear atributos da classe `Cupom` em colunas, tipos e restrições SQL (`INTEGER`, `REAL`, `TEXT`, `CHECK`, `NOT NULL`, `UNIQUE`).
*   **Projetar o Esquema Relacional (DER):** Modelar o relacionamento entre a tabela `pedidos` e a nova tabela `cupons` através da chave estrangeira (`cupom_id`).
*   **Analisar o Diagrama de Arquitetura em Camadas:** Identificar o isolamento entre Entidades de Domínio puras e o Repositório de Persistência no SQLite.
*   **Implementar o Esquema DDL no SQLite (`database.py`):** Criar a tabela `cupons` com todas as constraints que protegem a integridade dos dados no banco.
*   **Implementar o `CupomRepository` em Python (`repositories/cupom_repository.py`):**
    *   Método `salvar(cupom)` para inserção segura.
    *   Método `buscar_por_codigo(codigo)` com proteção absoluta contra SQL Injection utilizando parâmetros posicionais (`?`).
    *   Método `registrar_uso(cupom_id)` com incremento atômico e cláusula de guarda de concorrência (`usos_realizados < limite_usos`).
*   **Validar a Persistência Relacional:** Executar scripts de gravação e consulta no banco `bibliotaua.db`.
*   **Registrar a Daily Standup 2:** Registrar os avanços de banco e repositório no `guia_desenvolvedor.md`.

---

## ⏱️ 2. Cronograma do Encontro (100 Minutos: Aulas 3 e 4)

| Bloco | Duração | Conteúdo Programático e Metodologia | Recursos e Artefatos |
| :--- | :---: | :--- | :--- |
| **Abertura & DER** | 00 - 25 min | **Do Objeto ao Banco: Mapeamento Relacional e DER**<br>• Revisão rápida da entidade `Cupom` (Aula 24).<br>• Diagrama Entidade-Relacionamento (DER) em TikZ: tabelas `cupons`, `pedidos`, `itens_pedido`, `livros`.<br>• Chave estrangeira `cupom_id` e integridade referencial.<br>• Restrições `CHECK`: por que validar tanto no código Python quanto no banco de dados? | Slides 1 a 7<br>Diagrama DER TikZ |
| **Arquitetura & Repository** | 25 - 45 min | **Padrão Repository e Blindagem contra SQL Injection**<br>• Diagrama de Arquitetura em Camadas: Domínio $\leftrightarrow$ Repositório $\leftrightarrow$ SQLite.<br>• Por que nunca concatenar strings em queries SQL (`f"SELECT... {codigo}"`)?<br>• Uso do `sqlite3.Row` para conversão elegante de tuplas em dicionários/objetos. | Slides 8 a 13<br>Diagrama Arquitetura TikZ |
| **Mão na Massa: DDL SQLite** | 45 - 65 min | **Implementação Prática: Esquema e Banco (`database.py`)**<br>• Criação da instrução `CREATE TABLE IF NOT EXISTS cupons (...)`.<br>• Adição da chave estrangeira e índice de performance no código do cupom.<br>• Teste de inicialização do banco SQLite no terminal. | Slides 14 a 17<br>`database.py`<br>SQLite3 |
| **Mão na Massa: CupomRepository** | 65 - 90 min | **Implementação Prática: Repositório (`repositories/cupom_repository.py`)**<br>• Codificação dos métodos `salvar`, `buscar_por_codigo` e `listar_ativos`.<br>• Implementação de `registrar_uso` com incremento atômico (`UPDATE cupons SET usos_realizados = usos_realizados + 1...`).<br>• Verificação da persistência e consulta via script Python. | Slides 18 a 22<br>`cupom_repository.py`<br>Terminal Bash |
| **Daily Standup & Encerramento** | 90 - 100 min | **Registro Ágil & Preparação para a Aula 26**<br>• Preenchimento da anotação da Daily 2 no `guia_desenvolvedor.md`.<br>• Alinhamento para a Aula 26: Diagrama de Sequência e Integração do Pedido ao Checkout. | Slides 23 a 25<br>Template Daily 2 |

---

## 🛠️ 3. Estratégia Metodológica e Avaliação

*   **Ponte Modelo-Persistência:** O estudante enxerga visualmente como o modelo de classes desenhado na Aula 24 se desdobra em tabelas relacionais com restrições de integridade.
*   **Segurança desde a Base (Security by Design):** Demonstração empírica do risco de injeção de SQL e adoção incondicional de tuplas com queries parametrizadas.
*   **Evidências de Aprendizagem:**
    *   Script DDL `cupons` funcional em `database.py`.
    *   Classe `CupomRepository` implementada e testada.
    *   Registro da Daily 2 no diário de bordo.
