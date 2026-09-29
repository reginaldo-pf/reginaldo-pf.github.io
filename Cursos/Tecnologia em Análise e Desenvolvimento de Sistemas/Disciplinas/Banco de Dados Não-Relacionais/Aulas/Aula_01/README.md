# Aula 01 -- Banco de Dados Não-Relacionais

**Disciplina:** Banco de Dados Não-Relacionais (ADS16)  
**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) -- IFCE Campus Tauá  
**Carga Horária do Encontro:** 2 horas (120 minutos)  
**Data Prevista:** 29/09/2026 (Terça-feira)  
**Professor:** Me. Reginaldo Pereira Fernandes  

---

## 📚 Bibliografia & Referências Integradas

### Bibliografia Básica:
1. **SADALAGE, Pramod J.; FOWLER, Martin.** *NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota.* São Paulo: Novatec Editora, 2014. ISBN 978-8575223383.
2. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados.* 7. ed. São Paulo: Pearson Education do Brasil, 2018. 1126 p.
3. **PANIZ, David.** *NoSQL: como armazenar os dados de uma aplicação moderna.* São Paulo: Casa do Código, 2016.

### Bibliografia Complementar & Leituras Recomendadas:
1. **FROZZA, Angelo Augusto; SCHREINER, Geomar André; MELLO, Ronaldo dos Santos.** *Projeto de Bancos de Dados NoSQL.* In: Minicurso SBC, Capítulo 2.
2. **SHAPIRA, Gwen; PALINO, Todd; SIVARAM, Rajini; PETTY, Krit.** *Kafka: The Definitive Guide - Real-Time Data and Stream Processing at Scale.* 2. ed. Sebastopol, CA: O'Reilly Media, 2021.
3. **ARBUES, Leandro.** *Desenvolvimento de aplicações distribuídas com o Apache Kafka: um guia prático.* São Paulo: Casa do Código, 2021.
4. **GUERRA, José Luiz.** *NoSQL: uma abordagem prática.* São Paulo: Novatec Editora, 2021.

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral:
Compreender as motivações históricas, arquiteturais e de negócio que impulsionaram o surgimento do movimento NoSQL (*Not Only SQL*), identificando as limitações do modelo relacional tradicional frente às demandas contemporâneas de alta escalabilidade, volume massivo, velocidade de ingestão e variedade de dados, capacitando o estudante a instalar e executar o serviço do MongoDB em seu sistema operacional.

### Objetivos Específicos:
1. Conhecer a estrutura, o cronograma semestral de 20 encontros e os critérios avaliativos da disciplina (AVT 40%, AVP 40%, Listas 20%).
2. Analisar a hegemonia relacional (Codd, 1970) e o ponto de inflexão gerado pela Web 2.0 e os 3 Vs do Big Data (Volume, Velocidade, Variedade).
3. Compreender a função de brokers distribuídos de streaming (Apache Kafka - Shapira et al., 2021) no desacoplamento da ingestão de alta velocidade antes do armazenamento NoSQL.
4. Contrastar visualmente a escalabilidade vertical (*Scale-Up*) com a escalabilidade horizontal (*Scale-Out*), compreendendo o gargalo de *Network Shuffle* em JOINs distribuídos.
5. Definir o *Descasamento de Impedância Objeto-Relacional* (*Object-Relational Impedance Mismatch*) e como a *Orientação a Agregados* (Sadalage & Fowler, 2014; Frozza et al.) resolve esse atrito nativamente.
6. Classificar a taxonomia NoSQL entre modelos orientados a agregados (Chave-Valor, Documentos, Família de Colunas) e não-agregados (Grafos e Relacional), além dos Bancos Vetoriais para Inteligência Artificial (RAG).
7. Instalar e gerenciar o **Serviço do MongoDB** no **Ubuntu (v8.0/v9.0)** e no **Windows**.
8. Executar comandos fundamentais no MongoDB (`mongosh` e Python/PyMongo) criando um banco, inserindo documentos agregados e realizando consultas por campos embutidos e atualizações atômicas.

---

## 📋 2. Diretrizes e Contrato Pedagógico da Disciplina

### 2.1. Composição da Média Semestral (N1 e N2)
A nota de cada período letivo é calculada pela média ponderada regimental:

$$\text{Nota do Período} = (\text{AVT} \times 0{,}40) + (\text{AVP} \times 0{,}40) + (\text{Listas} \times 0{,}20)$$

*   **AVT (40%):** Avaliação Teórica individual sem consulta (Fundamentos, Teorema CAP/PACELC, ACID vs BASE e persistência poliglota).
*   **AVP (40%):** Avaliação Prática em laboratório:
    *   **AVP1 (N1):** Desafio prático individual em laboratório (Modelagem de Documentos MongoDB + Caching Redis).
    *   **AVP2 (N2):** Projeto prático integrado desenvolvido e apresentado em duplas (aplicação conectada a bancos NoSQL).
*   **Listas (20%):** Avaliação contínua composta por listas de exercícios de fixação e desafios práticos entregues até a data da prova teórica.

### 2.2. Política de Sábados Letivos
*   **Dias sem conteúdo novo:** Os sábados letivos previstos no calendário acadêmico (**10/10/2026** e **14/11/2026**) serão utilizados exclusivamente para nivelamento prático (oficina de orquestração com Docker e Docker Compose), suporte orientado a exercícios e laboratório preparatório para as avaliações de N1.

---

## ⏱️ 3. Cronograma da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades |
| :---: | :---: | :--- |
| **Bloco 1** | 00 -- 20 min | **Acolhimento & Apresentação da Disciplina:** Apresentação docente, objetivos, sistema de avaliação (AVT 40%, AVP 40%, Listas 20%), bibliografia oficial e papel do laboratório. |
| **Bloco 2** | 20 -- 40 min | **Contexto Histórico & O Desafio dos Dados:** Hegemonia relacional (Codd, 1970; SQL e ACID); revolução da Web 2.0; os 3 Vs do Big Data; streaming contínuo e ingestão em larga escala com Apache Kafka (Shapira et al., 2021). |
| **Bloco 3** | 40 -- 65 min | **Gargalos Arquiteturais do Relacional:** Escala Vertical vs Escala Horizontal; custos de processamento e *Network Shuffle* em JOINs distribuídos; *Object-Relational Impedance Mismatch* e o atrito dos ORMs. |
| **Bloco 4** | 65 -- 90 min | **O Movimento NoSQL & Taxonomia de Agregados:** Origem histórica (Carlos Strozzi 1998, Google Bigtable 2006, Amazon Dynamo 2007, encontro de 2009); Not Only SQL; conceito de Orientação a Agregados (Fowler & Sadalage / Frozza et al.); Chave-Valor, Documentos, Família de Colunas, Grafos e Bancos Vetoriais (RAG / IA). |
| **Bloco 5** | 90 -- 120 min | **Prática Hands-On: Instalação e Execução do MongoDB:** Guia de instalação do serviço no Ubuntu e no Windows; comandos do serviço (`systemctl` / `services.msc`); execução prática no `mongosh` e via Python; orientações da Lista 1. |

---

## 🖼️ 4. Figuras e Elementos Visuais da Apresentação

Para maximizar a clareza didática, a apresentação incorpora diagramas vetoriais criados especificamente para a disciplina:

1. **[Arquitetura de Streaming e Persistência Poliglota](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/materiais/figuras/fig_streaming_pipeline.png):** Ilustra fontes de dados (IoT/Web), buffer distribuído com Apache Kafka e armazenamento especializado.
2. **[Escala Vertical (*Scale-Up*) vs Escala Horizontal (*Scale-Out*)](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/materiais/figuras/fig_escala.png):** Contraste entre máquina única com teto físico/custo exponencial vs cluster elástico e resiliente.
3. **[O Gargalo dos JOINs em Clusters (*Network Shuffle*)](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/materiais/figuras/fig_gargalo_joins.png):** Visualização do tráfego massivo de rede ao cruzar tabelas distribuídas em servidores distintos.
4. **[O Descasamento de Impedância Objeto-Relacional](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/materiais/figuras/fig_impedance_mismatch.png):** Fatiamento do objeto em 4 tabelas pelo ORM vs afinidade direta 1:1 com documentos BSON.
5. **[Taxonomia NoSQL & Orientação a Agregados](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/materiais/figuras/fig_modelos_agregados.png):** Classificação formal entre modelos orientados a agregados, não-agregados e bancos vetoriais.

---

## 🛠️ 5. Guia de Instalação do Serviço MongoDB

### A) Instalação no Ubuntu (v8.0 / v9.0 LTS)
```bash
# 1. Instalar dependências prévias
sudo apt update && sudo apt install -y gnupg curl

# 2. Importar a chave pública oficial GPG
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
  sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg --dearmor

# 3. Adicionar o repositório oficial da distribuição
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] \
  https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/8.0 multiverse" | \
  sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list

# 4. Atualizar o APT e instalar o servidor MongoDB e mongosh
sudo apt update
sudo apt install -y mongodb-org

# 5. Gerenciar o serviço via systemd
sudo systemctl start mongod      # Inicia o daemon do MongoDB
sudo systemctl status mongod     # Confere status ativo (running)
sudo systemctl enable mongod     # Habilita inicialização automática no boot

# 6. Conectar via terminal interativo
mongosh
```

### B) Instalação no Windows (Community Server)
1. Acesse o portal oficial: [MongoDB Community Server Download](https://www.mongodb.com/try/download/community) e baixe o instalador `.msi`.
2. Execute o instalador e escolha o tipo de instalação: **Complete**.
3. Na janela **Service Configuration**, certifique-se de manter marcada a opção:
   - `[X] Install MongoDB as a Service`
   - Service Name: `MongoDB`
4. Na tela seguinte, recomenda-se marcar `[X] Install MongoDB Compass` (interface gráfica visual).
5. Gerenciamento do Serviço no Windows:
   - **PowerShell Administrativo:**
     ```powershell
     Get-Service MongoDB        # Exibe status (Running/Stopped)
     Start-Service MongoDB      # Inicia o serviço
     Stop-Service MongoDB       # Interrompe o serviço
     ```
   - **Prompt CMD (Admin):**
     ```cmd
     net start MongoDB
     net stop MongoDB
     ```
   - **Interface Gráfica:** Pressione `Win + R`, digite `services.msc` e localize `MongoDB Server`.
6. Adicione `C:\Program Files\MongoDB\Server\<versao>\bin` ao PATH do sistema e teste no terminal com `mongosh`.

### C) Alternativa com Docker (Padrão de Laboratório IFCE)
```bash
docker run -d --name mongodb -p 27017:27017 -v mongo_dados:/data/db mongo:latest
docker exec -it mongodb mongosh
```

---

## 💻 6. Exemplo Prático: Executando um Banco no MongoDB (`mongosh`)

Após inicializar o serviço, abra o terminal e digite `mongosh`:

```javascript
// 1. Criar ou alternar para o banco de dados da aula
use ads_comercio;

// 2. Inserir documento de cliente com endereço e pedidos aninhados (Agregado)
db.clientes.insertOne({
  _id: 1,
  nome: "Maria Clara Silva",
  email: "maria.clara@aluno.ifce.edu.br",
  endereco: { cidade: "Tauá", uf: "CE" },
  pedidos: [
    {
      id_pedido: "PED-2026-001",
      data_emissao: "2026-09-29",
      itens: [
        { produto: "Notebook Dell", quantidade: 1, preco_unitario: 4500.00 },
        { produto: "Mouse Sem Fio", quantidade: 2, preco_unitario: 85.50 }
      ],
      total: 4671.00
    }
  ]
});

// 3. Consultar cliente filtrando por propriedade interna (Dot Notation)
db.clientes.find({ "endereco.cidade": "Tauá" }).pretty();

// 4. Atualizar atomicamente adicionando um produto ao pedido sem nenhum JOIN
db.clientes.updateOne(
  { _id: 1 },
  { $push: { "pedidos.0.itens": { produto: "Teclado Mecânico", quantidade: 1, preco_unitario: 250.00 } } }
);

// 5. Verificar a contagem de documentos
db.clientes.countDocuments();
```

---

## 🐍 7. Recursos Didáticos e Scripts de Apoio

*   **Script Python Didático:** [`codigo/demonstracao_aula01.py`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/codigo/demonstracao_aula01.py)  
    Demonstra benchmarks de escrita relacional (4 tabelas) vs serialização de documento, verificação ativa da porta 27017, comandos `mongosh` e execução real/simulada no MongoDB.
*   **Jupyter Notebook:** [`codigo/demonstracao_aula01.ipynb`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/codigo/demonstracao_aula01.ipynb)  
    Caderno interativo completo para execução local ou no Google Colab.
*   **Slides da Aula (PDF):** [`materiais/main.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_01/materiais/main.pdf)  
    Apresentação oficial de 30 slides em formato widescreen 16:9.

---

## 📝 8. Exercícios de Fixação (Lista 1 -- Bloco 1)

1. Explique por que os bancos de dados relacionais tradicionais (RDBMS) enfrentam dificuldades para escalar horizontalmente mantendo propriedades ACID estritas.
2. Defina com suas palavras o que é o *Descasamento de Impedância Objeto-Relacional* e como o modelo de documentos agregados mitiga esse problema (Sadalage & Fowler, 2014).
3. Diferencie escala vertical (*Scale-Up*) de escala horizontal (*Scale-Out*), citando vantagens, desvantagens e custos financeiros de cada abordagem.
4. Explique o que é o fenômeno do *Network Shuffle* durante a execução de consultas com múltiplos `JOIN`s em clusters particionados.
5. Qual a diferença fundamental entre bancos de dados *Orientados a Agregados* e bancos de dados *Não-Orientados a Agregados* segundo Frozza et al. e Fowler?
6. Descreva o procedimento para inicializar e verificar o status do serviço do MongoDB no sistema operacional que você utiliza (Ubuntu ou Windows).
