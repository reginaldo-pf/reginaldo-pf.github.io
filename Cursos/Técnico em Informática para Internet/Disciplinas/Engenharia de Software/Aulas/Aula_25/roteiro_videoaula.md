# Roteiro de Produção de Videoaula: Aula 25 (Encontro 2)
## Persistência Relacional com SQLite e Padrão Repository (100 Minutos)

---

## 🎬 Metadados e Diretrizes Audiovisuais

*   **Curso:** Técnico em Informática para Internet — IFCE Campus Tauá
*   **Disciplina:** Engenharia de Software | **Professor:** Prof. Me. Reginaldo Pereira Fernandes
*   **Tema:** Sprint 04: Persistência Relacional com SQLite e Padrão Repository (BiblioTauá)
*   **Duração Total:** 100 minutos (Bloco 1: 50 min — DER & Arquitetura; Bloco 2: 50 min — DDL & Repository)
*   **Padrão de Câmeras:**
    *   **[CÂMERA 1 - PRINCIPAL]:** Plano Médio do Professor.
    *   **[TELA CHEIA]:** Slides Beamer com Diagrama DER TikZ e terminal SQLite.
    *   **[SPLIT-SCREEN]:** Professor no canto inferior com VS Code em destaque.

---

## ⏱️ BLOCO 1 (00:00 - 50:00): Do Modelo Conceitual ao DER Físico

### Cena 1: Abertura e Desafio da Persistência (00:00 - 15:00)
*   **Visual:** [CÂMERA 1] Vinheta IFCE Tauá -> Corte para o Professor. Em seguida, [SPLIT-SCREEN] com o banco `bibliotaua.db`.
*   **Áudio / Professor:**
    > *"Olá a todos! Sejam muito bem-vindos ao nosso Encontro 2! Na Aula 24, colocamos a mão na massa e criamos a entidade `Cupom` em Python com suas regras de negócio. Mas se o servidor for reiniciado, esses dados desaparecem. Hoje vamos conectá-los ao disco persistente usando o banco relacional SQLite e o padrão Repository!"*

### Cena 2: Diagrama Entidade-Relacionamento (DER) (15:00 - 35:00)
*   **Visual:** [TELA CHEIA] Slide Beamer com o Diagrama DER em TikZ. Foco nas tabelas `cupons` e `pedidos` e na chave estrangeira `cupom_id`.
*   **Áudio / Professor:**
    > *"Observem o nosso DER: a tabela `cupons` possui restrições severas de integridade: `CHECK(valor_desconto > 0)` e `UNIQUE(codigo)`. Isso é defesa em profundidade: tanto o Python quanto o motor SQL barram inconsistências."*

### Cena 3: Diagrama de Arquitetura e Blindagem contra SQL Injection (35:00 - 50:00)
*   **Visual:** [TELA CHEIA] Diagrama de Arquitetura em Camadas. Destaque para o slide de vulnerabilidade comparando concatenação `f""` vs parâmetros com `?`.
*   **Áudio / Professor:**
    > *"Nunca, em hipótese alguma, concatenem strings no SQL! Na nossa equipe do BiblioTauá, usamos sempre consultas parametrizadas com tuplas. O driver SQLite trata qualquer entrada maldosa como texto inerte."*

---

## ⏱️ BLOCO 2 (50:00 - 100:00): Live Coding — DDL e Repositório

### Cena 4: Implementação do DDL SQLite (50:00 - 70:00)
*   **Visual:** [SPLIT-SCREEN] Professor no canto; VS Code editando `bibliotaua/database.py`.
*   **Áudio / Professor:**
    > *"Vamos criar a tabela `cupons` e criar um índice `idx_cupons_codigo` para que a busca por código promocional seja instantânea, mesmo com milhares de registros na Feira do Livro."*

### Cena 5: Implementação do `CupomRepository` (70:00 - 90:00)
*   **Visual:** [TELA CHEIA] VS Code com `bibliotaua/repositories/cupom_repository.py`.
*   **Áudio / Professor:**
    > *"Aqui está o nosso `CupomRepository`. Implementamos `salvar`, `buscar_por_codigo` e o método crítico `registrar_uso`. Reparem na cláusula `WHERE usos_realizados < limite_usos`: ela garante atomicidade nativa no banco, blindando o sistema contra race conditions!"*

### Cena 6: Teste de Persistência e Fechamento da Daily 2 (90:00 - 100:00)
*   **Visual:** [SPLIT-SCREEN] Terminal executando script de teste e confirmando inserção e busca de cupom no SQLite.
*   **Áudio / Professor:**
    > *"Nossa persistência está concluída e homologada! No Encontro 3, estudaremos o Diagrama de Sequência e conectaremos o cupom ao agregado Pedido e ao serviço de checkout. Até a próxima aula!"*
