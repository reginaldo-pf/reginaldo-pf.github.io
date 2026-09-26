# Plano de Aula: 01 - Funções em Python para Redes de Computadores

*   **Módulo:** Lógica de Programação e Automação de Redes
*   **Público-Alvo:** 2º Ano do Ensino Médio Técnico em Redes de Computadores (IFCE Campus Tauá)
*   **Duração:** 90 minutos (2 horas-aula)

---

## 🎯 Objetivos de Aprendizagem

### Geral
*   Compreender o conceito de funções em Python e sua importância na modularização e automação de scripts de infraestrutura de redes.

### Específicos
*   Identificar os quatro tipos fundamentais de funções (com/sem parâmetros, com/sem retorno).
*   Escrever funções em Python utilizando a sintaxe correta (palavra-chave `def`, parênteses, dois-pontos e identação).
*   Diferenciar o comportamento de funções que exibem mensagens (sem retorno) daquelas que devolvem dados para variáveis (com retorno).
*   Desenvolver scripts simples de gerenciamento e testes de rede utilizando funções para evitar repetição de código.

---

## ⏰ Cronograma Recomendado

| Tempo | Atividade | Descrição |
| :--- | :--- | :--- |
| **15 min** | **Contextualização & Analogia** | Discussão sobre repetição de tarefas na gerência de redes (ex: configurar portas de switch manualmente vs automatizado). Apresentação da analogia do DHCP/Roteador como funções. |
| **15 min** | **Funções Sem Retorno (Tipos 1 e 2)** | Explicação de funções estáticas (Banners) e funções parametrizadas sem retorno (Simulador de Ping). |
| **20 min** | **Funções Com Retorno (Tipos 3 e 4)** | Explicação de retorno de dados (`return`). Exemplos práticos com IP Loopback e conversor de largura de banda Mbps para Kbps. |
| **15 min** | **Estudo de Caso & Classificador IP** | Demonstração passo a passo da função que valida se um IP é público ou privado. |
| **20 min** | **Laboratório Prático (Desafio)** | Alunos resolvem e executam o script de varredura de status de hosts utilizando funções. |
| **05 min** | **Encerramento & Feedback** | Resumo dos tipos de funções e introdução ao próximo tópico (Sockets em Python). |

---

## 🛝 Slides Sugeridos (Estrutura LaTeX Beamer)

A apresentação foi estruturada de forma modular em LaTeX Beamer utilizando os seguintes arquivos localizados em [/home/reginaldo-fernandes/logica/rotinas/](file:///home/reginaldo-fernandes/logica/rotinas/):

1.  **[main.tex](file:///home/reginaldo-fernandes/logica/rotinas/main.tex):** Arquivo principal de configuração de estilo (Tema Madrid e Whale), importação de pacotes e definições do Listings (exibição elegante do código Python).
2.  **[secao1_introducao.tex](file:///home/reginaldo-fernandes/logica/rotinas/secao1_introducao.tex):**
    *   *Tópico:* O problema do código repetitivo e a analogia de redes (DHCP, comandos do switch).
    *   *Nota do Professor:* Incentive os alunos a imaginarem funções como scripts armazenados no switch Cisco.
    *   *Elemento Visual:* Gráfico explicativo gerado [diagrama_funcao.jpg](file:///home/reginaldo-fernandes/logica/rotinas/diagrama_funcao.jpg).
3.  **[secao2_sem_param_sem_retorno.tex](file:///home/reginaldo-fernandes/logica/rotinas/secao2_sem_param_sem_retorno.tex):**
    *   *Tópico:* Definição de funções sem parâmetros e sem retorno.
    *   *Exemplos:* Exibição de banner estático da escola e alertas sonoros/visuais de reinicialização.
4.  **[secao3_com_param_sem_retorno.tex](file:///home/reginaldo-fernandes/logica/rotinas/secao3_com_param_sem_retorno.tex):**
    *   *Tópico:* Parâmetros e argumentos de entrada.
    *   *Exemplos:* Simulador de Ping customizado por IP e bloqueador de portas no Firewall (IPTables).
5.  **[secao4_sem_param_com_retorno.tex](file:///home/reginaldo-fernandes/logica/rotinas/secao4_sem_param_com_retorno.tex):**
    *   *Tópico:* O uso do `return` para devolver dados ao script.
    *   *Exemplos:* Função que obtém o IP de Loopback padrão (`127.0.0.1`) e gerador de chaves/tokens temporários para sessões SSH.
6.  **[secao5_com_param_com_retorno.tex](file:///home/reginaldo-fernandes/logica/rotinas/secao5_com_param_com_retorno.tex):**
    *   *Tópico:* Funções completas (Entrada + Processamento + Saída).
    *   *Exemplos:* Conversor de Megabits por segundo (Mbps) para Kilobits por segundo (Kbps) e classificador de IPs locais privados.
7.  **[secao6_conclusao.tex](file:///home/reginaldo-fernandes/logica/rotinas/secao6_conclusao.tex):**
    *   *Tópico:* Tabela comparativa resumida, boas práticas (DRY) e o Laboratório Prático de Redes.

---

## 🐍 Código Prático de Apoio (Scripts)

Abaixo estão os códigos principais abordados na apresentação para execução direta nos computadores do laboratório:

### 1. Classificador de IPs (Público vs Privado)
```python
def verificar_ip_privado(ip):
    # Verifica se o IP pertence as faixas privadas comuns (RFC 1918)
    if ip.startswith("192.168.") or ip.startswith("10."):
        return True
    return False

# Testando
print(verificar_ip_privado("192.168.1.25"))  # Retorna True
print(verificar_ip_privado("8.8.8.8"))       # Retorna False
```

### 2. Conversor de Banda
```python
def converter_mbps_para_kbps(mbps):
    # Converte a velocidade para configuracao em equipamentos
    return mbps * 1024

banda_calculada = converter_mbps_para_kbps(100)
print(f"Velocidade calculada para o switch: {banda_calculada} Kbps")
```

---

## ✍️ Exercícios / Desafio Prático

**Desafio: Scanner de Rede Escolar (Simulado)**

Peça aos alunos para implementarem um script que receba uma lista de IPs da rede e mostre o status de cada um. Eles devem usar uma função de validação para simular o teste:

```python
def ping_status(ip):
    # Simula status: se o ultimo octeto for par, o host esta ativo (True)
    ultimo_octeto = int(ip.split(".")[-1])
    return ultimo_octeto % 2 == 0

ips_do_laboratorio = [
    "192.168.10.1",
    "192.168.10.2",
    "192.168.10.12",
    "192.168.10.13"
]

print("Iniciando varredura no Laboratorio de Redes...")
for ip in ips_do_laboratorio:
    if ping_status(ip):
        print(f"[+] Host {ip} esta ONLINE e respondendo ping.")
    else:
        print(f"[-] Host {ip} esta OFFLINE (timeout).")
```
