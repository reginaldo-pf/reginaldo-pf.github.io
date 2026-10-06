"""
=============================================================================
IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
Disciplina : Bancos de Dados Não-Relacionais (ADS16)
Aula 02    : Fundamentos Arquiteturais: Teorema CAP, PACELC e Propriedades BASE vs ACID
Professor  : Prof. Me. Reginaldo Fernandes
Semestre   : 2026.2
=============================================================================
Referências Bibliográficas Integradas:
1. BREWER, Eric. "CAP twelve years later: How the 'rules' have changed".
   Computer, IEEE, v. 45, n. 2, p. 23-29, 2012.
2. ABADI, Daniel J. "Consistency tradeoffs in modern distributed database
   system design: CAP is only part of the story". Computer, IEEE, v. 45, n. 2,
   p. 37-42, 2012. (Definição formal do Teorema PACELC).
3. VOGELS, Werner. "Eventually Consistent". Communications of the ACM,
   v. 52, n. 1, p. 40-44, 2008. (Arquiteto-chefe da Amazon).
4. SADALAGE, P. J.; FOWLER, M. NoSQL Essencial: Um Guia Conciso para o Mundo
   Emergente da Persistência Poliglota. São Paulo: Novatec, 2014.
5. GRAY, Jim. "The Transaction Concept: Virtues and Limitations". VLDB, 1981.
   (Fundamentos formais das propriedades ACID).
=============================================================================
Conteúdo Deste Roteiro Prático Interativo:
1. Simulação de Cluster Distribuído com 3 Nós (A, B, C) e Injeção de Falhas.
2. Demonstração Prática do Teorema CAP:
   - Partição de Rede (Split-Brain) ativada em tempo real.
   - Modo CP (Consistência Estrita via Quórum): Rejeita escrita na minoria.
   - Modo AP (Alta Disponibilidade): Permite escrita, gera leitura defasada
     e demonstra a Reconciliação por Consistência Eventual (Last-Write-Wins).
3. Demonstração Prática do Teorema PACELC:
   - Medição de Latência (L) vs Consistência (C) no estado normal (Else).
4. Prática Real/Simulada com MongoDB:
   - Níveis de Garantia de Escrita (Write Concern: w=1 vs w='majority').
   - Níveis de Leitura (Read Concern: 'local' vs 'majority').
5. Comparativo Prático de Cenários do Mundo Real (PIX/Fintech vs Curtidas TikTok).
=============================================================================
"""

import sys
import time
import json
import random
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field

# Tentativa de carregar pymongo caso o ambiente possua
try:
    from pymongo import MongoClient
    from pymongo.write_concern import WriteConcern
    from pymongo.read_concern import ReadConcern
    from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
    PYMONGO_DISPONIVEL = True
except ImportError:
    PYMONGO_DISPONIVEL = False


# =============================================================================
# CORES ANSI PARA VISUALIZAÇÃO ELEGANTE NO TERMINAL
# =============================================================================
class Cores:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    VERMELHO = "\033[38;5;196m"
    VERDE = "\033[38;5;46m"
    AMARELO = "\033[38;5;214m"
    AZUL = "\033[38;5;39m"
    MAGENTA = "\033[38;5;201m"
    CIANO = "\033[38;5;51m"
    CINZA = "\033[38;5;245m"
    FUNDO_AZUL = "\033[48;5;24m"
    FUNDO_VERDE = "\033[48;5;22m"
    FUNDO_VERM = "\033[48;5;52m"


def cabecalho(titulo: str, emoji: str = "🚀"):
    print(f"\n{Cores.FUNDO_AZUL}{Cores.NEGRITO}  {emoji} {titulo.upper()}  {Cores.RESET}")
    print(f"{Cores.CIANO}{'=' * 75}{Cores.RESET}")


def subcabecalho(titulo: str):
    print(f"\n{Cores.AMARELO}{Cores.NEGRITO}▸ {titulo}{Cores.RESET}")
    print(f"{Cores.CINZA}{'-' * 60}{Cores.RESET}")


# =============================================================================
# 1. ARQUITETURA DO SIMULADOR DE CLUSTER DISTRIBUÍDO (3 NÓS)
# =============================================================================

@dataclass
class RegistroDado:
    chave: str
    valor: Any
    versao: int
    timestamp_ms: float
    no_origem: str


class NoDistribuido:
    """
    Representa um nó individual em um cluster de banco de dados distribuído.
    """
    def __init__(self, id_no: str, regiao: str):
        self.id_no = id_no
        self.regiao = regiao
        self.dados: Dict[str, RegistroDado] = {}
        self.relogio_logico = 0
        self.total_leituras = 0
        self.total_escritas = 0

    def gravar_local(self, chave: str, valor: Any, timestamp_ms: float, no_origem: str) -> RegistroDado:
        self.relogio_logico += 1
        registro = RegistroDado(
            chave=chave,
            valor=valor,
            versao=self.relogio_logico,
            timestamp_ms=timestamp_ms,
            no_origem=no_origem
        )
        self.dados[chave] = registro
        self.total_escritas += 1
        return registro

    def ler_local(self, chave: str) -> Optional[RegistroDado]:
        self.total_leituras += 1
        return self.dados.get(chave)


class ClusterDistribuido:
    """
    Simula uma topologia distribuída com latências de rede e injeção de falhas (partições).
    """
    def __init__(self, nomes_nos: List[str] = None):
        if nomes_nos is None:
            nomes_nos = ["No-A (São Paulo)", "No-B (Fortaleza)", "No-C (Tauá)"]
        self.nos: Dict[str, NoDistribuido] = {nome: NoDistribuido(nome, nome.split()[1]) for nome in nomes_nos}
        # Matriz de partição de rede: se (u, v) estiver no conjunto, há corte de comunicação
        self.links_rompidos: set = set()
        # Latências médias simuladas em milissegundos entre nós
        self.latencias_ms = {
            ("No-A (São Paulo)", "No-B (Fortaleza)"): 45.0,
            ("No-B (Fortaleza)", "No-A (São Paulo)"): 45.0,
            ("No-B (Fortaleza)", "No-C (Tauá)"): 12.0,
            ("No-C (Tauá)", "No-B (Fortaleza)"): 12.0,
            ("No-A (São Paulo)", "No-C (Tauá)"): 55.0,
            ("No-C (Tauá)", "No-A (São Paulo)"): 55.0,
        }

    def isolar_no(self, id_no: str):
        """Injeta uma partição de rede isolando completamente um nó dos demais."""
        for outro in self.nos:
            if outro != id_no:
                self.links_rompidos.add((id_no, outro))
                self.links_rompidos.add((outro, id_no))

    def restaurar_rede(self):
        """Cura a partição de rede (Network Heal), reconectando todos os nós."""
        self.links_rompidos.clear()

    def consegue_comunicar(self, no1: str, no2: str) -> bool:
        if no1 == no2:
            return True
        return (no1, no2) not in self.links_rompidos

    def obter_particao_visivel(self, no_origem: str) -> List[str]:
        """Retorna todos os nós acessíveis a partir de um dado nó."""
        return [n for n in self.nos if self.consegue_comunicar(no_origem, n)]


# =============================================================================
# 2. DEMONSTRAÇÃO PRÁTICA: O TEOREMA CAP EM AÇÃO
# =============================================================================

def demonstrar_teorema_cap():
    cabecalho("Demonstração Prática do Teorema CAP (Brewer, 2000 / 2012)", "⚡")
    print(f"""{Cores.NEGRITO}Contextualização Pedagógica:{Cores.RESET}
O Teorema CAP postula que, em qualquer sistema distribuído de dados sujeito a uma
{Cores.AMARELO}Partição de Rede (P){Cores.RESET} inevitável, o arquiteto de software é obrigado a escolher entre:
  1. {Cores.VERDE}Consistência Estrita (CP):{Cores.RESET} Todo nó responde o dado mais recente ou retorna ERRO.
  2. {Cores.AZUL}Alta Disponibilidade (AP):{Cores.RESET} Todo nó responde com o dado que possui, mesmo defasado.

{Cores.VERMELHO}Aviso Crucial:{Cores.RESET} Não existe 'sistema CA' na internet. Redes reais sofrem falhas de
cabo, switch e latência. Portanto, a tolerância a partições (P) é mandatória!
""")

    cluster = ClusterDistribuido()
    nomes = list(cluster.nos.keys())
    no_primario = nomes[0]  # No-A (São Paulo)
    no_remoto = nomes[2]    # No-C (Tauá)

    # Estado Inicial
    print(f"{Cores.NEGRITO}[Passo 1] Estado Inicial sem Partição de Rede:{Cores.RESET}")
    print("Gravando saldo bancário inicial da conta 'CTA-8842' = R$ 1.000,00 nos 3 nós...")
    t_inicio = time.time() * 1000
    for no in cluster.nos.values():
        no.gravar_local("saldo:CTA-8842", 1000.00, t_inicio, "Sistema-Central")
    print(f"{Cores.VERDE}✓ Dado replicado sincronamente em todos os nós com sucesso.{Cores.RESET}")

    # Injeção de Falha: Rompimento de Fibra Óptica (Partição de Rede)
    subcabecalho("INJEÇÃO DE FALHA: Cabo Rompido! O Nó C (Tauá) fica isolado dos nós A e B")
    cluster.isolar_no(no_remoto)
    print(f"{Cores.VERMELHO}[ALERTA DE INFRAESTRUTURA] Partição de Rede Detectada!{Cores.RESET}")
    print(f"  • Componente Maioritário (Quórum): {nomes[0]} e {nomes[1]} (2 nós de 3 = 66,7% > 50%)")
    print(f"  • Componente Minoritário (Isolado): {nomes[2]} (1 nó de 3 = 33,3% < 50%)")

    # CENÁRIO 1: Abordagem CP (Consistency + Partition Tolerance) - Ex: MongoDB (w:majority), Raft, HBase
    subcabecalho("CENÁRIO CP (Consistência Estrita): Protegendo contra Saldo Duplicado")
    print("Tentativa de atualizar saldo na partição maioritária (No-A): Novo Saldo = R$ 1.500,00 (Depósito Pix)")
    # No CP, a escrita no No-A exige confirmação da maioria (2 de 3 nós).
    vizinhos_a = cluster.obter_particao_visivel(no_primario)
    quorum_minimo = len(cluster.nos) // 2 + 1  # 2 nós

    if len(vizinhos_a) >= quorum_minimo:
        t_now = time.time() * 1000
        for n_id in vizinhos_a:
            cluster.nos[n_id].gravar_local("saldo:CTA-8842", 1500.00, t_now, no_primario)
        print(f"  {Cores.VERDE}✓ Sucesso na partição maioritária:{Cores.RESET} Quórum de {len(vizinhos_a)}/{len(cluster.nos)} nós atingido.")
        print(f"    Saldo em {nomes[0]}: R$ {cluster.nos[nomes[0]].ler_local('saldo:CTA-8842').valor:.2f}")
        print(f"    Saldo em {nomes[1]}: R$ {cluster.nos[nomes[1]].ler_local('saldo:CTA-8842').valor:.2f}")

    print("\nTentativa de saque de R$ 900,00 na agência de Tauá (No-C isolado):")
    vizinhos_c = cluster.obter_particao_visivel(no_remoto)
    print(f"  Nós que No-C consegue enxergar: {len(vizinhos_c)} (Apenas ele mesmo)")
    if len(vizinhos_c) < quorum_minimo:
        print(f"  {Cores.VERMELHO}✗ ERRO CP (ConsensusLostException / WriteConcernError):{Cores.RESET}")
        print(f"    O Nó C NÃO possui quórum ({len(vizinhos_c)} < {quorum_minimo}).")
        print(f"    {Cores.NEGRITO}Ação CP:{Cores.RESET} A transação é REJEITADA e bloqueada para impedir gasto duplo (Double-Spending)!")
        print(f"    Cliente recebe: {Cores.VERMELHO}[503 Service Unavailable: Conexão com Quórum Perdida]{Cores.RESET}")

    # CENÁRIO 2: Abordagem AP (Availability + Partition Tolerance) - Ex: Apache Cassandra, Amazon DynamoDB
    subcabecalho("CENÁRIO AP (Alta Disponibilidade): Foco em Nunca Perder a Requisição")
    print("Imagine o mesmo cenário no TikTok ou Instagram (Likes em uma foto) ou Carrinho de Compras:")
    print("Usuário em Tauá clica em 'Curtir' ou 'Adicionar Produto no Carrinho' conectado ao Nó C isolado:")

    t_like = time.time() * 1000 + 200
    cluster.nos[no_remoto].gravar_local("item:carrinho", "Smartphone Galaxy", t_like, no_remoto)
    print(f"  {Cores.VERDE}✓ Sucesso AP no Nó C:{Cores.RESET} Requisição aceita localmente em 0.5 ms sem esperar quórum!")
    print(f"    Estado no Nó C (Tauá): item={cluster.nos[no_remoto].ler_local('item:carrinho').valor}")

    dado_no_a = cluster.nos[no_primario].ler_local("item:carrinho")
    valor_a = dado_no_a.valor if dado_no_a else "[Vazio / Não Existe]"
    print(f"    Estado no Nó A (São Paulo): item={valor_a}")
    print(f"  {Cores.AMARELO}⚠ Leitura Defasada (Stale Read):{Cores.RESET} Os nós possuem versões divergentes temporariamente.")

    # Reconciliação (Cura da Rede)
    subcabecalho("RECUPERAÇÃO DA REDE: Consistência Eventual (Eventual Consistency)")
    print("O cabo de fibra óptica é consertado pelos técnicos. Restaurando conexões...")
    cluster.restaurar_rede()
    time.sleep(0.1)

    print("Executando protocolo de sincronização em segundo plano (Gossip / Read Repair / LWW)...")
    # Algoritmo Last-Write-Wins (LWW)
    registro_recente = cluster.nos[no_remoto].ler_local("item:carrinho")
    cluster.nos[no_primario].dados["item:carrinho"] = registro_recente
    cluster.nos[nomes[1]].dados["item:carrinho"] = registro_recente

    print(f"{Cores.VERDE}✓ Convergência Atingida!{Cores.RESET} Todos os nós agora possuem o estado final unificado:")
    for n_id, n_obj in cluster.nos.items():
        reg = n_obj.ler_local("item:carrinho")
        print(f"  • {n_id}: item='{reg.valor}' (Versão={reg.versao}, Timestamp={reg.timestamp_ms:.0f})")


# =============================================================================
# 3. DEMONSTRAÇÃO PRÁTICA: O TEOREMA PACELC (Daniel Abadi, 2012)
# =============================================================================

def demonstrar_teorema_pacelc():
    cabecalho("Demonstração Prática do Teorema PACELC (Daniel Abadi, 2012)", "⚖️")
    print(f"""{Cores.NEGRITO}Por que o Teorema CAP é Insuficiente no Dia a Dia dos Engenheiros?{Cores.RESET}
O Teorema CAP só descreve o comportamento do sistema quando há uma {Cores.VERMELHO}Partição (P){Cores.RESET}.
Porém, redes de nuvem modernas (AWS, Google Cloud, Azure) passam {Cores.VERDE}99,99% do tempo sem partição{Cores.RESET}!

O {Cores.NEGRITO}Teorema PACELC{Cores.RESET} preenche essa lacuna com a regra mnemônica:
  • Se houver {Cores.VERMELHO}P{Cores.RESET}artição: Escolha entre {Cores.AZUL}A{Cores.RESET}vailability ou {Cores.VERDE}C{Cores.RESET}onsistency;
  • {Cores.AMARELO}E{Cores.RESET}lse (Senão, em operação normal): Escolha entre {Cores.MAGENTA}L{Cores.RESET}atency ou {Cores.VERDE}C{Cores.RESET}onsistency.
""")

    print(f"{Cores.NEGRITO}Simulação de Benchmark: Custo da Consistência Normal (Latency vs Consistency){Cores.RESET}\n")

    # Cenário PC/EC (Ex: MongoDB com w='majority' ou RDBMS com Replicação Síncrona 2PC)
    subcabecalho("Cenário PC/EC: Priorizando CONSISTÊNCIA tanto na partição quanto no estado normal")
    print("Operação: Gravação de dados exigindo confirmação síncrona de 3 data centers geograficamente distantes.")

    latencias_exemplo = [1.2, 45.0, 55.0]  # Local SP, Remoto Fortaleza, Remoto Tauá
    print(f"  • Latência até Nó Local: {latencias_exemplo[0]} ms")
    print(f"  • Latência até Réplica 1 (Fortaleza): {latencias_exemplo[1]} ms")
    print(f"  • Latência até Réplica 2 (Tauá): {latencias_exemplo[2]} ms")

    tempo_sincrono = max(latencias_exemplo) + 2.5  # Espera o nó mais lento confirmar
    print(f"\n  ⏱️  {Cores.VERMELHO}Latência Total no Cliente (PC/EC): ~{tempo_sincrono:.1f} ms{Cores.RESET}")
    print(f"  {Cores.VERDE}✓ Benefício:{Cores.RESET} Garantia matemática de que qualquer leitura subsequente terá o dado idêntico.")
    print(f"  {Cores.VERMELHO}✗ Custo:{Cores.RESET} Cada requisição fica refém do RTT da conexão mais lenta.")

    # Cenário PA/EL (Ex: Cassandra, DynamoDB, MongoDB com w=1)
    subcabecalho("Cenário PA/EL: Priorizando BAIXA LATÊNCIA no estado normal e DISPONIBILIDADE na partição")
    print("Operação: Gravação confirmada assim que o nó primário local grava em memória/disco (W=1).")
    print("As demais réplicas recebem os dados assincronamente em segundo plano.")

    tempo_assincrono = latencias_exemplo[0] + 0.3
    print(f"\n  ⏱️  {Cores.VERDE}Latência Total no Cliente (PA/EL): ~{tempo_assincrono:.1f} ms{Cores.RESET}")
    print(f"  {Cores.VERDE}✓ Benefício:{Cores.RESET} Resposta {tempo_sincrono / tempo_assincrono:.1f}x mais rápida! Escalabilidade brutal de escrita.")
    print(f"  {Cores.AMARELO}⚠ Custo:{Cores.RESET} Janela de inconsistência transitória onde uma leitura em outro nó pode retornar dado antigo.")

    print(f"\n{Cores.NEGRITO}Matriz de Classificação PACELC dos Principais Bancos Modernos:{Cores.RESET}")
    print(f"""
  +----------------------+--------------------+--------------------+
  | Banco de Dados       | Na Partição (P/A)  | Em Normalidade (E) |
  +----------------------+--------------------+--------------------+
  | MongoDB (padrão)     | PC (Consistente)   | EC (Consistente)   |
  | MongoDB (w=1, unack) | PC (Consistente)   | EL (Baixa Latência)|
  | Apache Cassandra     | PA (Disponível)    | EL (Baixa Latência)|
  | Amazon DynamoDB      | PA (Disponível)    | EL (Baixa Latência)|
  | PostgreSQL Tradic.   | PC (Consistente)   | EC (Consistente)   |
  | Redis Standalone     | PC (Consistente)   | EL (Baixa Latência)|
  +----------------------+--------------------+--------------------+
""")


# =============================================================================
# 4. PRÁTICA COM MONGODB: NÍVEIS DE WRITE CONCERN E READ CONCERN
# =============================================================================

def demonstrar_mongodb_pratico():
    cabecalho("Prática com MongoDB: Níveis de Garantia de Escrita e Leitura", "🍃")
    print(f"""{Cores.NEGRITO}Como os Engenheiros Ajustam o PACELC no Código?{Cores.RESET}
No MongoDB moderno, você não precisa aceitar uma configuração rígida. O desenvolvedor
define por consulta o trade-off entre segurança e velocidade via:
  • {Cores.AMARELO}Write Concern:{Cores.RESET} Quantas réplicas devem confirmar o dado antes de liberar o cliente.
    - w: 1            -> Grava no nó primário local e retorna imediatamente (Foco: Baixa Latência / EL).
    - w: 'majority'   -> Espera a maioria absoluta dos nós confirmar (Foco: Consistência / EC).
    - j: true         -> Exige persistência em disco físico (Journaling / Durabilidade ACID).
  • {Cores.AMARELO}Read Concern:{Cores.RESET} Nível de isolamento da leitura ('local', 'majority', 'linearizable').
""")

    subcabecalho("Testando Conexão com o Serviço MongoDB (Porta 27017)...")

    cliente_mongo = None
    if PYMONGO_DISPONIVEL:
        try:
            cliente_mongo = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1500)
            cliente_mongo.admin.command('ping')
            print(f"{Cores.VERDE}✓ Conexão com o MongoDB REAL estabelecida com sucesso na porta 27017!{Cores.RESET}")
        except Exception:
            cliente_mongo = None
            print(f"{Cores.CINZA}ℹ MongoDB local não detectado ativo no momento. Ativando emulador didático de protocolo.{Cores.RESET}")
    else:
        print(f"{Cores.CINZA}ℹ Driver pymongo não instalado neste ambiente. Executando emulador didático.{Cores.RESET}")

    if cliente_mongo:
        db = cliente_mongo["ads_aula02_tradeoffs"]
        colecao = db["pedidos_teste"]
        colecao.drop()

        subcabecalho("Benchmark Prático: w=1 vs w='majority' no MongoDB Real")

        # Escrita com w=1 (Rápida / Foco em Latência)
        colecao_w1 = colecao.with_options(write_concern=WriteConcern(w=1))
        t0 = time.perf_counter()
        for i in range(50):
            colecao_w1.insert_one({"_id": f"W1-{i}", "item": "Sensor IoT", "temp": 28.5})
        tempo_w1 = (time.perf_counter() - t0) * 1000

        # Escrita com w='majority' e Journal (Alta Consistência e Durabilidade)
        colecao_wmaj = colecao.with_options(write_concern=WriteConcern(w="majority", j=True))
        t0 = time.perf_counter()
        for i in range(50):
            colecao_wmaj.insert_one({"_id": f"WMAJ-{i}", "item": "Sensor IoT", "temp": 28.5})
        tempo_wmaj = (time.perf_counter() - t0) * 1000

        print(f"  • Tempo para 50 inserções com w=1           : {Cores.VERDE}{tempo_w1:.2f} ms{Cores.RESET}")
        print(f"  • Tempo para 50 inserções com w='majority'+j: {Cores.AMARELO}{tempo_wmaj:.2f} ms{Cores.RESET}")
        print(f"  • Variação de latência: {tempo_wmaj / max(tempo_w1, 0.001):.1f}x mais criterioso na durabilidade.")
    else:
        # Modo Emulador Didático
        subcabecalho("Sintaxe Oficial e Comandos Equivalentes no mongosh / PyMongo:")
        print(f"""{Cores.CIANO}// 1. Inserção com foco em Alta Performance / Baixa Latência (w=1):
db.pedidos.insertOne(
  {{ _id: "PED-1001", cliente: "Ana Lima", valor: 350.00 }},
  {{ writeConcern: {{ w: 1, wtimeout: 1000 }} }}
);

// 2. Inserção com foco em Alta Consistência e Durabilidade Bancária (w='majority'):
db.pedidos.insertOne(
  {{ _id: "PED-1002", cliente: "Carlos Souza", valor: 9800.00 }},
  {{ writeConcern: {{ w: "majority", j: true, wtimeout: 5000 }} }}
);

// 3. Leitura com garantia de que o dado não será revertido por Rollback:
db.pedidos.find({{ cliente: "Carlos Souza" }}).readConcern("majority");{Cores.RESET}
""")


# =============================================================================
# 5. GUIA DECISÓRIO: ACID VS BASE NO MUNDO REAL
# =============================================================================

def demonstrar_acid_vs_base():
    cabecalho("Duelo dos Paradigmas: ACID vs BASE na Engenharia de Software", "🥊")
    print(f"""
{Cores.NEGRITO}ACID (Modelo Relacional / RDBMS Tradicional):{Cores.RESET}
  • {Cores.VERDE}A - Atomicidade:{Cores.RESET} Tudo ou nada (Commit ou Rollback completo).
  • {Cores.VERDE}C - Consistência:{Cores.RESET} Transições estritas respeitando regras de integridade (PK, FK, Check).
  • {Cores.VERDE}I - Isolamento:{Cores.RESET} Transações concorrentes não interferem umas nas outras (Locks / Bloqueios).
  • {Cores.VERDE}D - Durabilidade:{Cores.RESET} Dado confirmado é gravado de forma perene no disco físico (WAL).
  {Cores.CINZA}Filosofia: Pessimista. Prefere travar ou falhar a deixar passar um dado imperfeito.{Cores.RESET}

{Cores.NEGRITO}BASE (Modelo NoSQL Distribuído):{Cores.RESET}
  • {Cores.AZUL}BA - Basically Available:{Cores.RESET} O sistema continua respondendo requisições mesmo com falhas parciais.
  • {Cores.AZUL}S  - Soft state:{Cores.RESET} O estado dos dados pode fluir ou mudar mesmo sem novas requisições externas.
  • {Cores.AZUL}E  - Eventual consistency:{Cores.RESET} Os nós convergirão para um estado idêntico após determinado tempo.
  {Cores.CINZA}Filosofia: Otimista. Prefere acolher o usuário e conciliar os dados de forma assíncrona.{Cores.RESET}

{Cores.AMARELO}CASOS PRÁTICOS DE MERCADO PARA O ENGENHEIRO ESCOLHER:{Cores.RESET}
  ┌─────────────────────────────────────┬──────────────────────┬─────────────┐
  │ Cenário de Aplicação                │ Paradigma Recomendado│ Motivo Real │
  ├─────────────────────────────────────┼──────────────────────┼─────────────┤
  │ Transferência PIX / Saldo de Banco  │ ACID / CP            │ Não há tol- │
  │                                     │                      │ erância a   │
  │                                     │                      │ saldo falso │
  ├─────────────────────────────────────┼──────────────────────┼─────────────┤
  │ Curtidas / Visualizações no TikTok  │ BASE / AP            │ Se perder 2 │
  │                                     │                      │ curtidas em │
  │                                     │                      │ 1M, nada cai│
  ├─────────────────────────────────────┼──────────────────────┼─────────────┤
  │ Carrinho de Compras da Amazon       │ BASE / AP            │ Perder o car│
  │                                     │                      │ rinho é per-│
  │                                     │                      │ der a venda │
  ├─────────────────────────────────────┼──────────────────────┼─────────────┤
  │ Inscrição de Vagas no SISU / ENEM   │ ACID / CP            │ Disputa por │
  │                                     │                      │ milésimo de │
  │                                     │                      │ vaga única  │
  └─────────────────────────────────────┴──────────────────────┴─────────────┘
""")


# =============================================================================
# MENU PRINCIPAL INTERATIVO
# =============================================================================

def menu_principal():
    while True:
        print("\n" + "=" * 75)
        print(f"{Cores.NEGRITO}{Cores.VERDE}   AULA 02: BANCOS NÃO-RELACIONAIS -- IFCE CAMPUS TAUÁ (ADS16){Cores.RESET}")
        print(f"{Cores.CIANO}   Laboratório Prático: Teoremas CAP & PACELC e Modelo ACID vs BASE{Cores.RESET}")
        print("=" * 75)
        print(f" {Cores.AMARELO}1.{Cores.RESET} Executar Simulação Prática do Teorema CAP (Falha de Rede & Quórum)")
        print(f" {Cores.AMARELO}2.{Cores.RESET} Executar Demonstração do Teorema PACELC (Trade-off Latency vs Consistency)")
        print(f" {Cores.AMARELO}3.{Cores.RESET} Executar Prática com MongoDB (Write Concern w=1 vs w='majority')")
        print(f" {Cores.AMARELO}4.{Cores.RESET} Exibir Análise Comparativa ACID vs BASE (Tabela Decisória)")
        print(f" {Cores.AMARELO}5.{Cores.RESET} Executar TODAS as Demonstrações em Sequência")
        print(f" {Cores.VERMELHO}0.{Cores.RESET} Sair")
        print("-" * 75)

        if len(sys.argv) > 1 and sys.argv[1] in ["--all", "-a", "--run-all"]:
            opcao = "5"
        else:
            try:
                opcao = input(f"{Cores.NEGRITO}Escolha uma opção didática (0-5): {Cores.RESET}").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nEncerrando...")
                break

        if opcao == "1":
            demonstrar_teorema_cap()
        elif opcao == "2":
            demonstrar_teorema_pacelc()
        elif opcao == "3":
            demonstrar_mongodb_pratico()
        elif opcao == "4":
            demonstrar_acid_vs_base()
        elif opcao == "5":
            demonstrar_teorema_cap()
            demonstrar_teorema_pacelc()
            demonstrar_mongodb_pratico()
            demonstrar_acid_vs_base()
            if len(sys.argv) > 1:
                break
        elif opcao == "0":
            print(f"{Cores.VERDE}Encontro finalizado! Bons estudos e até a próxima aula.{Cores.RESET}")
            break
        else:
            print(f"{Cores.VERMELHO}Opção inválida! Escolha um número entre 0 e 5.{Cores.RESET}")

        if len(sys.argv) > 1:
            break


if __name__ == "__main__":
    menu_principal()
