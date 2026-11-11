# Roteiro de Live Coding e Gravação de Vídeo (Guia do Professor)

## Etapa 4 (GUI): Evolução para Lista de Receitas, Tabela Dinâmica e Reorganização do Menu

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Formato Metodológico:** **Construção Incremental Interativa (Visual ➔ Teste ➔ Função ➔ Teste)** — ponto de partida no arquivo [projetinho/gui_main.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/projetinho/gui_main.py) finalizado na Etapa 3.
* **Arquivo Gabarito de Apoio:** [etapas/etapa4_gui_customtkinter.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa4_gui_customtkinter.py)

---

## 🧭 Decisão Arquitetural e Pedagógica: Por Que Transformar a Receita em Lista?

Antes de ligar o projetor ou iniciar a gravação, entenda os motivos pedagógicos desta mudança:

> [!IMPORTANT]
> **O Salto Cognitivo da Etapa 4:**
> 1. **Do Dado Primitivo à Coleção Dinâmica:** Na Etapa 2/3, usamos `renda_prevista = 0.0` como um valor escalar (`float`). Isso serviu para ensinar variáveis simples e `try/except`. Agora, os alunos aprendem que **tanto entradas quanto saídas são coleções de entidades do mundo real**, modeladas como listas de dicionários:
>    * `despesas = [{"descricao": "...", "categoria": "...", "valor": ...}]`
>    * `receitas = [{"descricao": "...", "valor": ...}]`
> 2. **Reuso de Paradigmas de Interface:** O aluno já aprendeu a criar uma área rolável (`CTkScrollableFrame`) na aula passada para despesas. Hoje ele aprende a **reutilizar o mesmo container visual para renderizar duas visões diferentes (Receitas x Despesas)** alternadas pelo menu!
> 3. **Preparação para a Regra 50-30-20 (Etapa 5):** No balanço final, a renda base de cálculo não será mais digitada manualmente, mas calculada somando todas as fontes de receita registradas (`sum(...)`).

---

## 🎬 CENA 1: Reorganizando o Menu Lateral (Adicionando a Opção 3 Dedicada)

> **Foco Visual:** Abrir espaço no menu para acomodar as duas listagens (`3 - Listar Receitas` e `4 - Listar Despesas`) e empurrar o Balanço para a opção 5.

### 🎙️ Roteiro de Fala / Contextualização (Cena 1)

* *"Pessoal, observem o nosso menu lateral atual: temos '1 - Cadastrar Receita', '2 - Adicionar Despesa', '3 - Listar Despesas' e '4 - Balanço'. Mas pensem no usuário: e se ele quiser conferir quais fontes de receita já cadastrou no mês? Como ele faz? Hoje ele não consegue! Vamos reorganizar nosso menu criando uma opção dedicada para **Listar Receitas** no botão 3 e movendo a listagem de despesas para o botão 4."*

### 1.1 O que alterar no bloco `frame_menu` (no final do arquivo)

Substitua os botões do menu lateral por:

```python
btn_cadastrar_receita = ctk.CTkButton(
    frame_menu,
    text="1 - Cadastrar Receita",
    height=38,
    anchor="w",
    command=cadastrar_receita
)
btn_cadastrar_receita.pack(pady=4, padx=20, fill="x")

btn_cadastrar_despesa = ctk.CTkButton(
    frame_menu,
    text="2 - Cadastrar Despesa",
    height=38,
    anchor="w",
    command=adicionar_despesa
)
btn_cadastrar_despesa.pack(pady=4, padx=20, fill="x")

btn_listar_receitas = ctk.CTkButton(
    frame_menu,
    text="3 - Listar Receitas",
    height=38,
    anchor="w",
    fg_color="#27ae60",
    hover_color="#1e8449",
    command=listar_receitas
)
btn_listar_receitas.pack(pady=4, padx=20, fill="x")

btn_listar_despesas = ctk.CTkButton(
    frame_menu,
    text="4 - Listar Despesas",
    height=38,
    anchor="w",
    command=listar_despesas
)
btn_listar_despesas.pack(pady=4, padx=20, fill="x")

btn_balanco = ctk.CTkButton(
    frame_menu,
    text="5 - Balanço 50-30-20",
    height=38,
    anchor="w",
    command=exibir_balanco
)
btn_balanco.pack(pady=4, padx=20, fill="x")
```

### 🧪 Checkpoint de Teste 1 (Executar ao vivo!)

* Execute `python gui_main.py`.
* **O que mostrar:** O menu lateral agora possui 6 botões simétricos, com `3 - Listar Receitas` em destaque verde, preparando a turma para as novas funcionalidades.

---

## 🎬 CENA 2: Da Variável Escalar para a Lista de Dicionários (`receitas = []`)

> **Foco Funcional:** Substituir `renda_prevista = 0.0` por `receitas = []` e construir funções acumuladoras com expressões geradoras (`sum(...)`).

### 🎙️ Roteiro de Fala / Explicação Didática (Cena 2)

* *"Na Etapa 2, quando criamos a receita, usamos uma variável float simples: `renda_prevista = 0.0`. Mas se um estudante de Tauá recebe R$ 700 de bolsa de estágio e faz um bico de fim de semana de R$ 300, como ele registra isso? Não dava! Ele precisava somar de cabeça antes de digitar. Agora vamos tratar a receita como tratamos as despesas: uma **Lista de Dicionários**, onde cada item tem sua descrição e seu valor!"*

### 2.1 O que alterar na seção de estado (topo do arquivo)

Substitua `renda_prevista = 0.0` por:

```python
receitas = []  # Lista de dicionários: [{"descricao": str, "valor": float}]
despesas = []  # Lista de dicionários: [{"descricao": str, "valor": float, "categoria": str}]


def calcular_total_receitas():
    """Calcula a soma de todas as receitas cadastradas."""
    return sum(item["valor"] for item in receitas)


def calcular_total_despesas():
    """Calcula a soma de todas as despesas cadastradas."""
    return sum(item["valor"] for item in despesas)


def atualizar_card_resumo():
    """Atualiza o número grande verde do resumo e o contador de fontes."""
    total = calcular_total_receitas()
    lbl_valor_receita.configure(text=f"R$ {total:.2f}")
    lbl_subtitulo_resumo.configure(
        text=f"Total acumulado: R$ {total:.2f} ({len(receitas)} fonte(s) registrada(s))"
    )
```

### 💡 Ponto Didático para Destacar à Turma:
Mostre a elegância de `sum(item["valor"] for item in receitas)`. Explique que isso equivale ao padrão clássico:
```python
total = 0.0
for item in receitas:
    total += item["valor"]
```
E que em Python moderno usamos essa síntese de forma natural e legível.

---

## 🎬 CENA 3: Construindo a Listagem Dinâmica de Receitas (`listar_receitas`)

> **Foco Visual e Lógico:** Criar a função que limpa o painel rolável, atualiza o cabeçalho e desenha cada receita com números em verde.

### 🎙️ Roteiro de Fala / Explicação Didática (Cena 3)

* *"Vejam como a arquitetura que criamos na aula passada é flexível: não precisamos criar uma segunda caixa de rolagem! Nós usamos o mesmo `frame_lista_scroll`. Quando o usuário clica em '3 - Listar Receitas', nós mudamos o título para 'LISTA DE RECEITAS', limpamos os cartões velhos com `winfo_children()` e desenhamos as linhas de receitas. Quando ele clica em '4 - Listar Despesas', fazemos o mesmo para os gastos!"*

### 3.1 Implementar `listar_receitas()` e harmonizar `listar_despesas()`

```python
def listar_receitas():
    """Desenha a tabela de receitas cadastradas na área rolável."""
    lbl_titulo_painel.configure(text="💵 LISTA DE RECEITAS REGISTRADAS")
    lbl_colunas.configure(
        text="#     Descrição da Receita                                                Valor (R$)"
    )

    for widget in frame_lista_scroll.winfo_children():
        widget.destroy()

    if not receitas:
        lbl_vazio = ctk.CTkLabel(
            frame_lista_scroll,
            text="🚧 Nenhuma receita cadastrada até o momento.\nClique em '1 - Cadastrar Receita' no menu lateral para registrar entradas.",
            font=ctk.CTkFont(size=14),
            text_color="gray60",
            justify="center"
        )
        lbl_vazio.pack(pady=40)
        lbl_status.configure(text="💵 Exibindo lista de receitas (0 registros).", text_color="gray70")
        return

    for indice, item in enumerate(receitas, start=1):
        linha = ctk.CTkFrame(frame_lista_scroll, corner_radius=6, fg_color="gray17")
        linha.pack(fill="x", pady=3, padx=5)

        texto_linha = (
            f"{indice:<5} "
            f"{item['descricao'][:50]:<60} "
            f"R$ {item['valor']:>10.2f}"
        )

        lbl_item = ctk.CTkLabel(
            linha,
            text=texto_linha,
            font=ctk.CTkFont(family="monospace", size=12),
            text_color="#2ecc71",
            anchor="w"
        )
        lbl_item.pack(fill="x", padx=10, pady=6)

    total = calcular_total_receitas()
    lbl_status.configure(
        text=f"💵 Exibindo {len(receitas)} receita(s) registrada(s). Total: R$ {total:.2f}",
        text_color="#2ecc71"
    )
```

### 🧪 Checkpoint de Teste 2 (Executar ao vivo!)

* Teste com `receitas = [{"descricao": "Salário Mensal", "valor": 2800.0}, {"descricao": "Bolsa IFCE", "valor": 700.0}]`.
* Mostre a tabela renderizada com os valores em verde.
* Alterne clicando em `4 - Listar Despesas` e depois em `3 - Listar Receitas`. Os alunos verão a tela alternar suavemente sem piscar nem travar!

---

## 🎬 CENA 4: Criando o Formulário Modal de Receitas (`CTkToplevel`)

> **Foco Funcional:** Trocar o antigo `CTkInputDialog` por um formulário modal elegante com dois campos: Descrição da Origem e Valor (R$).

### 4.1 Substituir `cadastrar_receita()`

```python
def cadastrar_receita():
    """Abre subjanela de formulário (CTkToplevel) para cadastrar uma nova fonte de receita."""
    popup = ctk.CTkToplevel(janela)
    popup.title("1 - Nova Receita")
    popup.geometry("400x320")
    popup.resizable(False, False)
    popup.transient(janela)
    popup.grab_set()

    # Campo 1: Descrição
    ctk.CTkLabel(popup, text="Descrição da Receita / Origem:", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(20, 5)
    )
    entry_descricao = ctk.CTkEntry(
        popup,
        placeholder_text="Ex: Salário Mensal, Bolsa de Estágio, Freelance..."
    )
    entry_descricao.pack(fill="x", padx=25)

    # Campo 2: Valor (R$)
    ctk.CTkLabel(popup, text="Valor da Receita (R$):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    entry_valor = ctk.CTkEntry(popup, placeholder_text="Ex: 2500.00")
    entry_valor.pack(fill="x", padx=25)

    lbl_erro_popup = ctk.CTkLabel(popup, text="", text_color="#e74c3c", font=ctk.CTkFont(size=12))
    lbl_erro_popup.pack(pady=(10, 0))

    def confirmar_cadastro():
        descricao = entry_descricao.get().strip()
        valor_texto = entry_valor.get().strip().replace(",", ".")

        if not descricao:
            lbl_erro_popup.configure(text="❌ A descrição não pode ficar vazia!")
            return

        try:
            valor = float(valor_texto)
            if valor < 0:
                lbl_erro_popup.configure(text="❌ O valor não pode ser negativo!")
                return
        except ValueError:
            lbl_erro_popup.configure(text="❌ Digite um valor numérico válido (ex: 1500.50)!")
            return

        # Dicionário da nova receita
        nova_receita = {
            "descricao": descricao,
            "valor": valor
        }
        receitas.append(nova_receita)

        salvar_dados()
        atualizar_card_resumo()
        listar_receitas()

        lbl_status.configure(
            text=f"✅ Receita '{descricao}' (R$ {valor:.2f}) cadastrada com sucesso!",
            text_color="#2ecc71"
        )
        popup.destroy()

    btn_salvar = ctk.CTkButton(
        popup,
        text="💾 Salvar Receita",
        height=38,
        fg_color="#27ae60",
        hover_color="#1e8449",
        command=confirmar_cadastro
    )
    btn_salvar.pack(fill="x", padx=25, pady=(15, 20))
```

---

## 🎬 CENA 5: Atualizando o JSON com Migração Suave

> **Foco de Engenharia de Software:** Garantir que o sistema salve o novo formato (`"receitas": [...]`) sem perder arquivos `.json` gerados na Etapa 3.

```python
def salvar_dados():
    """Salva as listas de receitas e despesas no arquivo JSON."""
    pacote = {
        "receitas": receitas,
        "despesas": despesas
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(pacote, arquivo, indent=4, ensure_ascii=False)


def carregar_dados():
    """Carrega dados salvos com suporte a migração suave de versões anteriores."""
    global receitas, despesas

    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                pacote = json.load(arquivo)

                if "receitas" in pacote and isinstance(pacote["receitas"], list):
                    receitas = pacote["receitas"]
                elif "renda_prevista" in pacote and pacote["renda_prevista"] > 0:
                    receitas = [{"descricao": "Receita Inicial (Migrada)", "valor": float(pacote["renda_prevista"])}]
                else:
                    receitas = []

                despesas = pacote.get("despesas", [])
        except Exception:
            pass
```

---

## 🎯 Síntese Pedagógica da Etapa 4

| Elemento no Código | Conceito de Programação | Impacto Prático na Aplicação |
| :--- | :--- | :--- |
| `receitas = []` | Coleção Dinâmica de Entidades | Permite cadastrar $N$ fontes de renda sem limite fixo. |
| `nova_receita = {"descricao": ..., "valor": ...}` | Dicionários (`dict`) | Empacota atributos heterogêneos (texto e float) em um registro coeso. |
| `sum(item['valor'] for item in receitas)` | Expressão Geradora com `sum` | Reduz código boilerplate e calcula totais em tempo de execução. |
| `listar_receitas()` e `listar_despesas()` | Reuso de Container Visual | Alterna visões no mesmo painel rolável sem poluir a interface com janelas duplicadas. |
| `migração suave no json.load` | Manutenibilidade e Retrocompatibilidade | Evita quebra de software quando a estrutura de dados evolui entre versões. |

---

## 🛠️ Guia Rápido de Troubleshooting no Laboratório

| Sintoma na tela do aluno | Causa Provável | Como orientar pedagogicamente |
| :--- | :--- | :--- |
| Ao cadastrar uma receita, ela não aparece na lista | Esqueceu de chamar `listar_receitas()` no final de `confirmar_cadastro()`. | *"O dado entrou na lista na memória RAM, mas você avisou a tela para redesenhar a tabela?"* |
| O Card de Resumo no topo não atualiza o valor total | Não chamou `atualizar_card_resumo()` dentro de `confirmar_cadastro()`. | *"O card é como o velocímetro de um carro: quando o motor acelera, precisamos atualizar o painel."* |
| As receitas e despesas aparecem misturadas na tabela | Faltou limpar o container rolável com o loop `for widget in frame_lista_scroll.winfo_children(): widget.destroy()`. | *"Lembre-se de apagar a lousa antes de escrever a nova matéria."* |
| Erro `TypeError: unsupported operand type(s) for +: 'float' and 'dict'` | O aluno tentou fazer `sum(receitas)` em vez de `sum(item['valor'] for item in receitas)`. | *"O Python não sabe somar dois dicionários inteiros com o sinal de mais. Você precisa dizer qual chave quer somar: o 'valor'."* |
