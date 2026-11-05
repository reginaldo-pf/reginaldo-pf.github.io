# Guia Passo a Passo: Laboratório de Fixação e Simulado Integrado N1 (Redis + MongoDB)

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá  
* **Disciplina:** Banco de Dados Não-Relacionais (ADS16) — Aula 09 (Sábado Letivo)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Ambiente de Trabalho:** Linux / Docker / Redis 7.4 / MongoDB 8.0 / Python 3 (`redis-py`, `pymongo`)  

---

## Parte 1: Revisão Conceitual e Teoremas Distribuídos (Preparação para a AVT1)

### 1.1 O Teorema CAP (Eric Brewer)
Em qualquer sistema distribuído de banco de dados, é fisicamente impossível garantir de forma simultânea as três propriedades:
* **C (Consistency - Consistência Estrita):** Toda operação de leitura retorna a escrita mais recente ou resulta em erro.
* **A (Availability - Disponibilidade):** Toda requisição recebida por um nó não-defeituoso recebe uma resposta válida e sem falha.
* **P (Partition Tolerance - Tolerância a Partições):** O sistema continua operacional mesmo quando mensagens entre nós da rede são perdidas ou atrasadas.

Como as redes de computadores físicas sofrem falhas inevitáveis ($P$), os arquitetos são forçados a escolher entre:
1. **Sistemas CP (ex.: MongoDB):** Preferem abortar operações ou bloquear leituras em nós isolados para garantir que os dados não divirjam.
2. **Sistemas AP (ex.: Apache Cassandra / DynamoDB):** Aceitam escritas e leituras mesmo em nós isolados pela partição, garantindo resposta imediata ao custo de consistência eventual.

---

### 1.2 O Teorema PACELC (Daniel Abadi)
O Teorema PACELC expande o CAP ao observar que a rede opera a maior parte do tempo em regime normal (sem partições ativas):
$$\text{Se houver } \mathbf{P} \text{ (Partição)} \implies \text{escolhe-se entre } \mathbf{A} \text{ ou } \mathbf{C}; \quad \mathbf{E}\text{lse (Regime Normal)} \implies \text{escolhe-se entre } \mathbf{L} \text{ (Latência) ou } \mathbf{C} \text{ (Consistência)}.$$

* **MongoDB (PC/EC):** Prioriza consistência tanto na partição (PC) quanto sob operação normal (EC), gravando primariamente no nó líder (*Primary Node*).
* **Redis (PA/EL):** Em sua configuração comum distribuída, prioriza disponibilidade contínua (PA) e latência ultrabaixa em memória (EL).

---

### 1.3 Contraste de Propriedades: ACID vs BASE

| Propriedade ACID (Relacional RDBMS) | Propriedade BASE (Não-Relacional NoSQL) |
| :--- | :--- |
| **A**tomicidade (tudo ou nada em transação) | **B**asically **A**vailable (o cluster se mantém operando mesmo com nós caídos) |
| **C**onsistência (esquema rígido e chaves estrangeiras) | **S**oft State (o estado do dado pode ser transitório e convergir gradualmente) |
| **I**solamento (transações concorrentes sem efeitos colaterais) | **E**ventual Consistency (se não houver novas escritas, todos os nós convergirão) |
| **D**urabilidade (gravação síncrona definitiva em disco) | Foco em vazão maciça e escalabilidade horizontal (*Sharding*) |

---

## Parte 2: Revisão Prática do Redis (Terminal `redis-cli` e Python)

### 2.1 Estruturas Nativas e Comandos Essenciais
O Redis opera como um servidor de estruturas de dados residente em memória RAM com complexidade temporal $\mathcal{O}(1)$ para a maioria das operações:

1. **Strings e TTL (Expiração):**
   ```bash
   # Gravando chave com expiração automática de 60 segundos
   SET produto:SKU-001 '{"nome":"Notebook","preco":3800}' EX 60
   TTL produto:SKU-001
   ```

2. **Hashes (Objetos e Carrinhos):**
   ```bash
   # Manipulando um carrinho de compras
   HSET carrinho:cli_55 SKU-001 2 SKU-002 1
   HINCRBY carrinho:cli_55 SKU-001 1
   HGETALL carrinho:cli_55
   ```

3. **Filas com Listas (Produtor/Consumidor FIFO):**
   ```bash
   LPUSH fila:pedidos "PED-1001"
   RPOP fila:pedidos
   ```

---

## Parte 3: Revisão Prática do MongoDB (Operadores Atômicos e Regra ESR)

### 3.1 Operadores Atômicos em Nível de Documento
Para suportar concorrência maciça sem a necessidade de travas distribuídas complexas (*locks*), o MongoDB disponibiliza operadores de mutação atômica:

```javascript
// Atualização de estoque sem risco de sobrescrita concorrente
db.produtos.updateOne(
  { sku: "SKU-ELE-001" },
  { $inc: { estoque: -1 } }
);

// Filtro seguro em subdocumentos de array evitando falsos positivos
db.pedidos.find({
  itens: {
    $elemMatch: {
      preco_unitario: { $gte: 500.0 },
      quantidade: { $gte: 2 }
    }
  }
});
```

---

### 3.2 A Regra de Ouro ESR (*Equality, Sort, Range*)
A ordem em que os atributos são declarados na criação de um índice composto determina se a busca conseguirá eliminar varreduras desnecessárias e evitar ordenações custosas na memória RAM:

1. **E (Equality):** Atributos com operadores de correspondência exata (`status: "entregue"`).
2. **S (Sort):** Atributo utilizado na cláusula de ordenação (`sort({ data_pedido: -1 })`).
3. **R (Range):** Atributos com operadores de faixa ou desigualdade (`valor_total: { $gte: 200 }`).

```javascript
// Criando índice estritamente alinhado com a Regra ESR:
db.pedidos.createIndex({
  status: 1,        // Equality
  data_pedido: -1,  // Sort
  valor_total: 1    // Range
});
```

---

## Parte 4: Implementação Integrada do Padrão Cache-Aside

O padrão arquitetural **Cache-Aside** (também denominado *Lazy Loading*) delega à aplicação a responsabilidade de coordenar as leituras e gravações entre a memória e o disco.

```
                  +--------------------------+
                  |    Aplicação (Python)    |
                  +--------------------------+
                     /                      \
      1. Lê Cache   /                        \  2. Se Cache Miss
     (latência     v                          v (latência ~1 ms)
      < 0.1 ms) +-------+                  +----------+
                | Redis | <--------------- | MongoDB  |
                +-------+  3. Hidratação   +----------+
                           com TTL (RAM)
```

### Código Completo de Referência em Python:
```python
import json
import redis
from pymongo import MongoClient

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
db = MongoClient("mongodb://localhost:27017")["ecommerce_shopgrids"]

def obter_produto_cache_aside(sku: str, ttl_segundos: int = 60) -> dict:
    chave = f"produto:{sku}"
    
    # 1. Tenta recuperar do Redis (Memória RAM)
    dados = r.get(chave)
    if dados:
        produto = json.loads(dados)
        produto["_origem"] = "CACHE_HIT"
        return produto

    # 2. Se falhar, consulta o banco primário (MongoDB)
    doc = db.produtos.find_one({"sku": sku})
    if not doc:
        return None

    # 3. Serializa e armazena no Redis com expiração
    doc["_id"] = str(doc["_id"])
    r.setex(chave, ttl_segundos, json.dumps(doc))
    doc["_origem"] = "CACHE_MISS"
    return doc
```

---

## Parte 5: Execução do Simulado Prático (AVP1)

Para praticar em laboratório e validar o ambiente antes do exame prático oficial:

1. Inicie a infraestrutura de containers na pasta `codigo/`:
   ```bash
   cd codigo
   docker compose up -d
   ```
2. Instale as dependências no ambiente virtual Python:
   ```bash
   pip install -r requirements.txt
   ```
3. Abra o arquivo `simulado_n1_desafios.py` e verifique cada uma das 5 funções.
4. Execute os testes automatizados para verificar sua nota e pontuação:
   ```bash
   python3 simulado_n1_desafios.py
   ```
5. Compare sua solução com o arquivo comentado `solucao_simulado_n1.py`.
