# Roteiro Prático do Aluno – Etapa 3 (GUI): Cadastro de Despesas e Salvamento Automático (JSON)

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Arquivo de Trabalho:** `projetinho/gui_main.py`

---

## 🎯 O que vamos construir hoje?

Na etapa anterior, deixamos o nosso **Dashboard de Planejamento Financeiro** funcionando com o menu lateral e o cadastro da **Receita Prevista**. Porém:
1. O botão **`2 - Adicionar Despesa`** ainda estava em construção.
2. Quando fechávamos a janela do programa, o valor da receita sumia porque estava apenas na **memória RAM**.

Hoje vamos continuar o nosso `gui_main.py` no mesmo formato interativo (**Criar Visual ➔ Testar ➔ Criar Função ➔ Testar**) para:
* Transformar o painel direito em uma **Tabela Rolável (`CTkScrollableFrame`)** para listar dezenas de despesas.
* Criar uma **Subjanela de Formulário (`CTkToplevel`)** para cadastrar cada despesa (Descrição, Valor e Categoria) usando **Dicionários (`dict`)** e **Listas (`list`)**.
* Implementar o **Armazenamento em Arquivo (`JSON`)** para que suas receitas e despesas fiquem salvas permanentemente no computador!

---

## 🧱 CENA 1: Transformando o Painel de Despesas em uma Área Rolável

Se cadastrarmos 20 despesas no mês, elas precisam de uma **barra de rolagem** para caberem dentro do painel direito.

1. Abra o seu arquivo `gui_main.py`.
2. Vá até o final do arquivo, na seção **`5.2 - Painel Central: Lista de Despesas`**.
3. Apague o antigo `lbl_placeholder_lista` (e o `lbl_placeholder_lista.pack(...)`) e coloque no lugar dele o componente rolável `CTkScrollableFrame`:

```python
# Substitua o antigo lbl_placeholder_lista por esta área rolável:
frame_lista_scroll = ctk.CTkScrollableFrame(frame_despesas, fg_color="transparent")
frame_lista_scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))
```

🧪 **Teste 1:** Execute `python gui_main.py` e veja que agora o painel de despesas possui uma barra de rolagem na lateral direita! Feche a janela para ir à Cena 2.

---

## 🎨 CENA 2: Criando a Função que Desenha a Lista na Tela

Agora vamos criar a lista `despesas = []` e uma função chamada `atualizar_lista_visual()`, que percorre todos os dicionários de despesas cadastrados e cria uma linha visual para cada um dentro do `frame_lista_scroll`.

### 2.1 Adicione a lista e a função no topo do arquivo:
Suba até logo abaixo de `renda_prevista = 0.0` e adicione:

```python
despesas = []  # Lista que guardará os dicionários de cada despesa


def atualizar_lista_visual():
    """Limpa o painel de listagem e redesenha todas as despesas da lista."""
    # 1. Remove os itens visuais antigos antes de redesenhar
    for widget in frame_lista_scroll.winfo_children():
        widget.destroy()

    # 2. Se a lista estiver vazia, mostra o aviso amigável
    if not despesas:
        lbl_vazio = ctk.CTkLabel(
            frame_lista_scroll,
            text="🚧 Nenhuma despesa cadastrada até o momento.\nClique em '2 - Adicionar Despesa' no menu lateral.",
            font=ctk.CTkFont(size=14),
            text_color="gray60",
            justify="center"
        )
        lbl_vazio.pack(pady=40)
        return

    # 3. Percorre a lista de dicionários e cria uma linha para cada gasto
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
```

### 2.2 Chame a função no final do arquivo:
Lá nas últimas linhas do seu `gui_main.py`, logo **antes** de `if __name__ == "__main__":`, adicione:

```python
atualizar_lista_visual()

if __name__ == "__main__":
    janela.mainloop()
```

🧪 **Teste 2:** Execute `python gui_main.py`. Como a lista `despesas` está vazia, você verá o aviso `"🚧 Nenhuma despesa cadastrada até o momento..."` dentro da área rolável!

---

## 🪟 CENA 3: Criando a Subjanela de Formulário de Despesas (Visual)

Quando clicarmos em **`2 - Adicionar Despesa`**, precisamos pedir **3 dados**: Descrição, Valor e Categoria. Para isso, vamos abrir uma subjanela de formulário usando `ctk.CTkToplevel(janela)`.

Localize a função `def adicionar_despesa():` no topo do seu arquivo e substitua o conteúdo dela pelo código abaixo (inicialmente apenas o visual da janelinha):

```python
def adicionar_despesa():
    """Abre uma subjanela de formulário (CTkToplevel) para cadastrar uma nova despesa."""
    popup = ctk.CTkToplevel(janela)
    popup.title("2 - Nova Despesa")
    popup.geometry("400x380")
    popup.resizable(False, False)
    popup.transient(janela)  # Mantém o pop-up na frente da janela principal
    popup.grab_set()         # Foca os cliques apenas no pop-up até fechar

    # Campo 1: Descrição
    ctk.CTkLabel(popup, text="Descrição da Despesa:", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(20, 5)
    )
    entry_descricao = ctk.CTkEntry(popup, placeholder_text="Ex: Conta de Internet, Aluguel...")
    entry_descricao.pack(fill="x", padx=25)

    # Campo 2: Valor (R$)
    ctk.CTkLabel(popup, text="Valor da Despesa (R$):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    entry_valor = ctk.CTkEntry(popup, placeholder_text="Ex: 120.50")
    entry_valor.pack(fill="x", padx=25)

    # Campo 3: Categoria (Menu de Seleção)
    ctk.CTkLabel(popup, text="Categoria (Regra 50-30-20):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    combo_categoria = ctk.CTkOptionMenu(
        popup,
        values=["Essencial", "Estilo de Vida", "Reserva"]
    )
    combo_categoria.pack(fill="x", padx=25)

    # Rótulo para exibir mensagens de erro dentro do pop-up
    lbl_erro_popup = ctk.CTkLabel(popup, text="", text_color="#e74c3c", font=ctk.CTkFont(size=12))
    lbl_erro_popup.pack(pady=(10, 0))

    # Botão Salvar
    btn_salvar = ctk.CTkButton(
        popup,
        text="💾 Salvar Despesa",
        height=38,
        fg_color="#27ae60",
        hover_color="#1e8449"
    )
    btn_salvar.pack(fill="x", padx=25, pady=(15, 20))
```

🧪 **Teste 3:** Execute `python gui_main.py` e clique no botão **`2 - Adicionar Despesa`**. Veja a subjanela abrir com as caixas de texto e o menu de seleção de categorias! Feche para programarmos o botão Salvar.

---

## ⚡ CENA 4: Programando o Botão "Salvar Despesa" (Dicionário + Lista)

Agora vamos criar a função `confirmar_cadastro()` dentro de `adicionar_despesa()` para validar o que o usuário digitou, guardar em um **Dicionário (`dict`)**, adicionar na **Lista (`despesas.append`)** e atualizar a tabela!

### 4.1 Adicione `confirmar_cadastro()` dentro de `adicionar_despesa()` (logo acima do `btn_salvar`):

```python
    def confirmar_cadastro():
        descricao = entry_descricao.get().strip()
        valor_texto = entry_valor.get().strip().replace(",", ".")
        categoria = combo_categoria.get()

        if not descricao:
            lbl_erro_popup.configure(text="❌ A descrição não pode ficar vazia!")
            return

        try:
            valor = float(valor_texto)
            if valor < 0:
                lbl_erro_popup.configure(text="❌ O valor não pode ser negativo!")
                return
        except ValueError:
            lbl_erro_popup.configure(text="❌ Digite um valor numérico válido!")
            return

        # Cria o Dicionário da despesa e adiciona na Lista!
        nova_despesa = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        }
        despesas.append(nova_despesa)

        # Atualiza a tabela na tela e fecha o pop-up!
        atualizar_lista_visual()
        lbl_status.configure(
            text=f"✅ Despesa '{descricao}' (R$ {valor:.2f}) adicionada! Total: {len(despesas)}",
            text_color="#2ecc71"
        )
        popup.destroy()
```

### 4.2 Conecte o `command=confirmar_cadastro` no `btn_salvar`:
Logo abaixo, no `btn_salvar`, adicione `command=confirmar_cadastro`:

```python
    btn_salvar = ctk.CTkButton(
        popup,
        text="💾 Salvar Despesa",
        height=38,
        fg_color="#27ae60",
        hover_color="#1e8449",
        command=confirmar_cadastro
    )
    btn_salvar.pack(fill="x", padx=25, pady=(15, 20))
```

Aproveite também para atualizar a função `listar_despesas()` (do botão 3) para atualizar a lista quando clicada:

```python
def listar_despesas():
    atualizar_lista_visual()
    lbl_status.configure(
        text=f"📋 Lista atualizada! Exibindo {len(despesas)} despesa(s) registrada(s).",
        text_color="#3498db"
    )
```

🧪 **Teste 4:** Execute `python gui_main.py`, clique em `2 - Adicionar Despesa` e cadastre 2 gastos (ex: `Aluguel - 1200` e `Internet - 110`). Veja como eles aparecem alinhados na tabela!
* **Porém, faça um teste:** Feche o programa e abra de novo. Os dados sumiram! Vamos resolver isso agora no último passo!

---

## 💾 CENA 5: Armazenamento Permanente em Arquivo (`JSON`)

> 🧠 **Como funciona o Armazenamento (Persistência)?**
> Variáveis como `renda_prevista` e `despesas` ficam na **memória RAM**, que é apagada assim que o programa fecha. Para que os dados fiquem salvos permanentemente no computador, usamos a biblioteca nativa **`json`** do Python, que grava nosso dicionário de receita e lista de despesas dentro de um arquivo chamado `dados_financeiros.json`!

### 5.1 Importe `json` e `os` nas primeiras linhas do arquivo:
No topo do `gui_main.py`, adicione:

```python
import json
import os
import customtkinter as ctk
```

### 5.2 Crie as funções `salvar_dados()` e `carregar_dados()`:
Logo abaixo de `despesas = []`, adicione:

```python
ARQUIVO_DADOS = "dados_financeiros.json"


def salvar_dados():
    """Salva a receita e a lista de despesas em um arquivo JSON."""
    pacote = {
        "renda_prevista": renda_prevista,
        "despesas": despesas
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(pacote, arquivo, indent=4, ensure_ascii=False)


def carregar_dados():
    """Carrega os dados do arquivo JSON se ele já existir no computador."""
    global renda_prevista, despesas

    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                pacote = json.load(arquivo)
                renda_prevista = pacote.get("renda_prevista", 0.0)
                despesas = pacote.get("despesas", [])
        except Exception:
            pass
```

### 5.3 Ative o salvamento e o carregamento automático (3 linhas!):
1. **Na função `cadastrar_receita()`:** Logo abaixo de `renda_prevista = valor`, chame `salvar_dados()`.
2. **Na função `confirmar_cadastro()` (dentro de `adicionar_despesa`):** Logo abaixo de `despesas.append(nova_despesa)`, chame `salvar_dados()`.
3. **No final do arquivo (antes do `if __name__ == "__main__":`):** Chame `carregar_dados()` e atualize o texto da receita:

```python
carregar_dados()
lbl_valor_receita.configure(text=f"R$ {renda_prevista:.2f}")
atualizar_lista_visual()

if __name__ == "__main__":
    janela.mainloop()
```

---

## 🧪 Checklist Final de Validação

Execute `python gui_main.py` e confira:

- [ ] **Teste 1 (Cadastro de Despesas):** Clique em `2 - Adicionar Despesa`, tente salvar vazio (veja a validação bloquear) e depois cadastre 3 despesas nas diferentes categorias (`Essencial`, `Estilo de Vida` e `Reserva`).
- [ ] **Teste 2 (Arquivo JSON Criado):** Olhe na barra de arquivos do VS Code e abra o arquivo `dados_financeiros.json` que foi criado automaticamente com os seus dados!
- [ ] **Teste 3 (Persistência Funcionando!):** Feche a janela completamente no botão `0 - Sair do Sistema` e execute `python gui_main.py` novamente. Verifique se sua **Receita Prevista** e todas as suas **Despesas** continuam lá na tela!
