# Roteiro Prático do Aluno – Etapa 4 (GUI): Listagem de Receitas, Coleções Dinâmicas e Atualização do Menu

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Arquivo de Trabalho:** `projetinho/gui_main.py`
* **Arquivo Gabarito de Referência:** `etapas/etapa4_gui_customtkinter.py`

---

## 🎯 O que vamos construir hoje?

Nas etapas anteriores, criamos o esqueleto do nosso Dashboard em CustomTkinter, implementamos o cadastro rolável de despesas e a persistência em arquivo JSON.

Porém, tínhamos uma limitação séria de modelagem no nosso software:
1. **A receita era apenas um número flutuante solto (`renda_prevista = 0.0`)**, como se as pessoas tivessem apenas uma única entrada fixa por mês. Na vida real, recebemos salário, bolsas de estudo ou estágio, trabalhos freelance, rendimentos, vendas de itens usados, etc.
2. **Não tínhamos uma tela de listagem de receitas:** O menu só permitia listar as despesas (`3 - Listar Despesas`).

Hoje vamos dar um salto de maturidade no nosso software, alterando o formato atual para:

* **Reorganizar o menu principal com opções dedicadas:**
  * `1 - Cadastrar Receita`
  * `2 - Cadastrar Despesa`
  * `3 - Listar Receitas` (Nova funcionalidade!)
  * `4 - Listar Despesas` (Reorganizada para o botão 4)
  * `5 - Balanço 50-30-20` (Preparação para a Etapa 5)
  * `0 - Sair do Sistema`
* **Evoluir a receita para uma Lista de Dicionários (`receitas = []`):** Cada entrada financeira terá sua **Descrição/Origem** e seu **Valor (R$)**.
* **Criar um formulário modal dedicado (`CTkToplevel`) para Receitas:** Permitindo cadastrar múltiplas fontes de ganhos com validação defensiva.
* **Implementar a Listagem Dinâmica de Receitas (`listar_receitas`):** O painel rolável alternará com elegância entre a visualização de Receitas e a de Despesas!
* **Cálculo acumulador automático:** O Card de Resumo no topo calculará a soma de todas as receitas cadastradas em tempo real.
* **Atualização da Persistência JSON:** Salvando e carregando tanto a lista `receitas` quanto a lista `despesas`.

---

## 🧭 Visão Geral das Modificações no `gui_main.py`

```text
[Menu Lateral Reorganizado]
 1 - Cadastrar Receita  ──► Abre Subjanela Modal (Descrição + Valor) ──► receitas.append()
 2 - Cadastrar Despesa  ──► Abre Subjanela Modal (Desc + Categoria + Valor) ──► despesas.append()
 3 - Listar Receitas    ──► Desenha tabela de receitas no frame_lista_scroll
 4 - Listar Despesas    ──► Desenha tabela de despesas no frame_lista_scroll
 5 - Balanço 50-30-20   ──► [Em Construção - Etapa 5]
```

---

## 🧱 CENA 1: Reorganizando os Botões do Menu Lateral

Vamos começar ajustando os botões na barra lateral para abrir espaço para a nova opção de **Listar Receitas**.

1. Abra o arquivo `projetinho/gui_main.py`.
2. Localize a seção **`4. COMPONENTES DO MENU LATERAL`** (ou onde estão os botões `btn_receita`, `btn_adicionar`, etc.).
3. Substitua o bloco de botões pelo código reorganizado abaixo:

```python
# ==============================================================================
# MENU LATERAL REORGANIZADO COM OPÇÕES DEDICADAS (ETAPA 4)
# ==============================================================================
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

btn_sair = ctk.CTkButton(
    frame_menu,
    text="0 - Sair do Sistema",
    height=38,
    fg_color="#c0392b",
    hover_color="#922b21",
    command=sair_sistema
)
btn_sair.pack(side="bottom", pady=25, padx=20, fill="x")
```

> [!TIP]
> **Destaque Visual:** Note que colocamos o botão `3 - Listar Receitas` com a cor verde (`#27ae60`). Isso cria um contraste intuitivo entre as entradas financeiras (verde) e os demais controles!

🧪 **Teste 1:** Execute `python gui_main.py` e confira se os 6 botões aparecem alinhados e ordenados de 1 a 5 mais o botão de sair no rodapé. Feche a janela para continuar.

---

## 🧠 CENA 2: Evoluindo a Estrutura de Dados na Memória (`receitas = []`)

Agora vamos trocar a variável que guardava apenas um valor numérico por uma **lista dinâmica de dicionários**, igual à que usamos para as despesas!

### 2.1 Atualize a declaração de variáveis no topo do arquivo

Suba até a seção de dados em memória e **substitua** `renda_prevista = 0.0` por:

```python
# ==============================================================================
# DADOS EM MEMÓRIA E PERSISTÊNCIA EM JSON
# ==============================================================================
ARQUIVO_DADOS = "dados_financeiros.json"
receitas = []  # Lista de dicionários: [{"descricao": "Salário", "valor": 2500.0}, ...]
despesas = []  # Lista de dicionários: [{"descricao": "Aluguel", "valor": 900.0, "categoria": "Essencial"}, ...]
```

### 2.2 Crie as funções acumuladoras e atualizadoras de resumo

Logo abaixo da lista de despesas, adicione estas funções especializadas:

```python
def calcular_total_receitas():
    """Calcula a soma de todas as receitas cadastradas na lista."""
    return sum(item["valor"] for item in receitas)


def calcular_total_despesas():
    """Calcula a soma de todas as despesas cadastradas na lista."""
    return sum(item["valor"] for item in despesas)


def atualizar_card_resumo():
    """Atualiza o número grande verde do resumo e o contador de fontes cadastradas."""
    total = calcular_total_receitas()
    lbl_valor_receita.configure(text=f"R$ {total:.2f}")
    lbl_subtitulo_resumo.configure(
        text=f"Total acumulado: R$ {total:.2f} ({len(receitas)} fonte(s) registrada(s))"
    )
```

> [!NOTE]
> **O poder do `sum(...)` com expressões geradoras:**
> A expressão `sum(item["valor"] for item in receitas)` percorre cada dicionário da lista `receitas`, extrai a chave `"valor"` e soma tudo em uma única linha elegante, sem precisar escrever um laço `for` manual com variável acumuladora.

---

## 🎨 CENA 3: Criando a Função `listar_receitas()` e Ajustando o Painel

No nosso painel direito, temos uma área rolável (`frame_lista_scroll`). Quando o usuário clicar em **`3 - Listar Receitas`**, queremos que esse painel mostre a tabela de receitas!

### 3.1 Implemente a função `listar_receitas()`

No bloco de funções, adicione:

```python
def listar_receitas():
    """Desenha a tabela de receitas cadastradas na área rolável."""
    # 1. Configura títulos e cabeçalho para o modo Receitas
    lbl_titulo_painel.configure(text="💵 LISTA DE RECEITAS REGISTRADAS")
    lbl_colunas.configure(
        text="#     Descrição da Receita                                                Valor (R$)"
    )

    # 2. Limpa os elementos visuais antigos antes de redesenhar
    for widget in frame_lista_scroll.winfo_children():
        widget.destroy()

    # 3. Cláusula de guarda: lista vazia
    if not receitas:
        lbl_vazio = ctk.CTkLabel(
            frame_lista_scroll,
            text="🚧 Nenhuma receita cadastrada até o momento.\nClique em '1 - Cadastrar Receita' no menu lateral para registrar entradas.",
            font=ctk.CTkFont(size=14),
            text_color="gray60",
            justify="center"
        )
        lbl_vazio.pack(pady=40)
        lbl_status.configure(
            text="💵 Exibindo lista de receitas (0 registros).",
            text_color="gray70"
        )
        return

    # 4. Desenha as linhas formatadas de cada receita
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

### 3.2 Atualize a função `listar_despesas()`

Certifique-se de que a função `listar_despesas()` restaura o título e o cabeçalho original de despesas quando for clicada:

```python
def listar_despesas():
    """Desenha a tabela de despesas cadastradas na área rolável."""
    # 1. Configura títulos e cabeçalho para o modo Despesas
    lbl_titulo_painel.configure(text="📋 LISTA DE DESPESAS REGISTRADAS")
    lbl_colunas.configure(
        text="#     Descrição da Despesa                        Categoria               Valor (R$)"
    )

    # 2. Limpa os elementos visuais antigos antes de redesenhar
    for widget in frame_lista_scroll.winfo_children():
        widget.destroy()

    # 3. Cláusula de guarda: lista vazia
    if not despesas:
        lbl_vazio = ctk.CTkLabel(
            frame_lista_scroll,
            text="🚧 Nenhuma despesa cadastrada até o momento.\nClique em '2 - Adicionar Despesa' no menu lateral para registrar gastos.",
            font=ctk.CTkFont(size=14),
            text_color="gray60",
            justify="center"
        )
        lbl_vazio.pack(pady=40)
        lbl_status.configure(
            text="📋 Exibindo lista de despesas (0 registros).",
            text_color="gray70"
        )
        return

    # 4. Desenha as linhas formatadas de cada despesa
    for indice, item in enumerate(despesas, start=1):
        linha = ctk.CTkFrame(frame_lista_scroll, corner_radius=6, fg_color="gray17")
        linha.pack(fill="x", pady=3, padx=5)

        texto_linha = (
            f"{indice:<5} "
            f"{item['descricao'][:35]:<38} "
            f"{item['categoria']:<22} "
            f"R$ {item['valor']:>9.2f}"
        )

        lbl_item = ctk.CTkLabel(
            linha,
            text=texto_linha,
            font=ctk.CTkFont(family="monospace", size=12),
            anchor="w"
        )
        lbl_item.pack(fill="x", padx=10, pady=6)

    total = calcular_total_despesas()
    lbl_status.configure(
        text=f"📋 Exibindo {len(despesas)} despesa(s) registrada(s). Total de gastos: R$ {total:.2f}",
        text_color="#3498db"
    )
```

---

## 🪟 CENA 4: Formulário Modal de Cadastro de Receitas (`cadastrar_receita`)

Na etapa anterior, a função `cadastrar_receita()` usava um simples `CTkInputDialog` para pedir apenas o valor numérico.

Agora vamos transformá-la em uma subjanela completa (`CTkToplevel`) para capturar tanto a **Descrição da Origem** (ex: Salário, Estágio, Freelance) quanto o **Valor (R$)**, validando tudo com segurança!

Substitua a função `cadastrar_receita()` existente por:

```python
def cadastrar_receita():
    """Abre subjanela de formulário (CTkToplevel) para cadastrar uma nova fonte de receita."""
    popup = ctk.CTkToplevel(janela)
    popup.title("1 - Nova Receita")
    popup.geometry("400x320")
    popup.resizable(False, False)
    popup.transient(janela)  # Mantém o pop-up sempre na frente da janela principal
    popup.grab_set()         # Bloqueia cliques fora até fechar o pop-up

    # Campo 1: Descrição da Receita
    ctk.CTkLabel(popup, text="Descrição da Receita / Origem:", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(20, 5)
    )
    entry_descricao = ctk.CTkEntry(
        popup,
        placeholder_text="Ex: Salário Mensal, Bolsa de Estágio, Freelance..."
    )
    entry_descricao.pack(fill="x", padx=25)

    # Campo 2: Valor da Receita (R$)
    ctk.CTkLabel(popup, text="Valor da Receita (R$):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    entry_valor = ctk.CTkEntry(popup, placeholder_text="Ex: 2500.00")
    entry_valor.pack(fill="x", padx=25)

    # Rótulo para mensagens de validação
    lbl_erro_popup = ctk.CTkLabel(popup, text="", text_color="#e74c3c", font=ctk.CTkFont(size=12))
    lbl_erro_popup.pack(pady=(10, 0))

    def confirmar_cadastro():
        descricao = entry_descricao.get().strip()
        valor_texto = entry_valor.get().strip().replace(",", ".")

        # 1. Validação de campo não vazio
        if not descricao:
            lbl_erro_popup.configure(text="❌ A descrição não pode ficar vazia!")
            return

        # 2. Validação numérica com try/except
        try:
            valor = float(valor_texto)
            if valor < 0:
                lbl_erro_popup.configure(text="❌ O valor não pode ser negativo!")
                return
        except ValueError:
            lbl_erro_popup.configure(text="❌ Digite um valor numérico válido (ex: 1500.50)!")
            return

        # 3. Empacota no Dicionário e adiciona à Lista de Receitas
        nova_receita = {
            "descricao": descricao,
            "valor": valor
        }
        receitas.append(nova_receita)

        # 4. Salva em disco, atualiza o card e exibe a tabela de receitas
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

## 💾 CENA 5: Atualizando o Armazenamento JSON com Suporte a Migração

Como mudamos a estrutura de `renda_prevista` (float) para `receitas` (lista), precisamos atualizar as funções `salvar_dados()` e `carregar_dados()`.

### 5.1 Atualize `salvar_dados()`

```python
def salvar_dados():
    """Salva as listas de receitas e despesas no arquivo JSON."""
    pacote = {
        "receitas": receitas,
        "despesas": despesas
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(pacote, arquivo, indent=4, ensure_ascii=False)
```

### 5.2 Atualize `carregar_dados()` com migração suave

Se algum aluno já possuir um arquivo `dados_financeiros.json` criado na Etapa 3 anterior (que tinha a chave `"renda_prevista"`), o código abaixo converte essa renda automaticamente para um item na nova lista `receitas`!

```python
def carregar_dados():
    """Carrega os dados salvos do JSON com suporte a migração de versões anteriores."""
    global receitas, despesas

    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                pacote = json.load(arquivo)

                # Carregamento seguro da lista de receitas
                if "receitas" in pacote and isinstance(pacote["receitas"], list):
                    receitas = pacote["receitas"]
                elif "renda_prevista" in pacote and pacote["renda_prevista"] > 0:
                    # Migração suave da versão anterior
                    receitas = [{"descricao": "Receita Inicial (Migrada)", "valor": float(pacote["renda_prevista"])}]
                else:
                    receitas = []

                # Carregamento da lista de despesas
                despesas = pacote.get("despesas", [])
        except Exception:
            pass
```

### 5.3 Atualize a inicialização no final do arquivo

No final do arquivo `gui_main.py`, logo antes do `if __name__ == "__main__":`:

```python
# ==============================================================================
# CARREGAMENTO INICIAL E LOOP PRINCIPAL
# ==============================================================================
carregar_dados()
atualizar_card_resumo()
listar_receitas()  # Abre o sistema exibindo a tabela de receitas

if __name__ == "__main__":
    janela.mainloop()
```

---

## 🧪 Checklist de Validação da Etapa 4

Execute `python gui_main.py` e verifique cada ponto:

* [ ] **Menu com 6 Botões:** Os botões estão ordenados de 1 a 5, com destaque verde em `3 - Listar Receitas` e vermelho em `0 - Sair`.
* [ ] **Cadastro de Receita com Validação:**
  * Clique em `1 - Cadastrar Receita`.
  * Deixe a descrição em branco e tente salvar ➔ O sistema deve avisar: `❌ A descrição não pode ficar vazia!`.
  * Digite valor negativo ou letras ➔ O sistema deve barrar com mensagem amigável.
* [ ] **Registro de Múltiplas Entradas:**
  * Cadastre `Salário Mensal` com `R$ 2800.00`.
  * Cadastre `Bolsa de Estágio` com `R$ 600.00`.
* [ ] **Listagem de Receitas:** Clique em `3 - Listar Receitas`. Verifique se o título muda para `"💵 LISTA DE RECEITAS REGISTRADAS"` e se as duas receitas aparecem alinhadas com números em verde!
* [ ] **Card de Resumo Atualizado:** O valor em destaque no card deve exibir `R$ 3400.00` e no subtítulo `(2 fonte(s) registrada(s))`.
* [ ] **Alternância com Despesas:**
  * Clique em `4 - Listar Despesas`. O título do painel muda para `"📋 LISTA DE DESPESAS REGISTRADAS"` e o cabeçalho mostra `Categoria`.
  * Clique novamente em `3 - Listar Receitas` e veja a tabela voltar para as receitas instantaneamente!
* [ ] **Persistência em Arquivo:** Abra o arquivo `dados_financeiros.json` no VS Code e veja suas receitas e despesas salvas em formato estruturado. Feche e abra o programa para conferir se tudo continua lá!

---

## 🆘 Problemas Comuns (Troubleshooting)

1. **`NameError: name 'calcular_total_receitas' is not defined`:**
   * Certifique-se de que definiu as funções de cálculo **acima** de onde elas são chamadas (por exemplo, antes de `atualizar_card_resumo` e antes de `listar_receitas`).
2. **Ao clicar em `3 - Listar Receitas`, as linhas ficam em cima das despesas antigas:**
   * Verifique se no início de `listar_receitas()` você incluiu o loop de limpeza:
     ```python
     for widget in frame_lista_scroll.winfo_children():
         widget.destroy()
     ```
3. **O card de resumo continua mostrando `R$ 0.00` após cadastrar receita:**
   * Verifique se dentro de `confirmar_cadastro()` da receita você chamou `atualizar_card_resumo()`.

---

## 🚀 Desafios Extras

1. **Subtotal Informativo no Rodapé:** Ao alternar entre receitas e despesas, faça o rodapé exibir a média aritmética dos valores cadastrados (`total / len(receitas)`).
2. **Alerta de Saldo Provisório:** No card superior, adicione um pequeno texto mostrando o saldo parcial atual (`calcular_total_receitas() - calcular_total_despesas()`).
