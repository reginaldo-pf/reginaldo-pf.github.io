# Roteiro Prático do Aluno – Construindo nosso Dashboard Passo a Passo (CustomTkinter)

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Arquivo de Trabalho:** `projetinho/gui_main.py`

---

## 🎯 Como vamos construir nossa aplicação hoje?

Em vez de apenas copiar e colar um código gigante de uma só vez, vamos construir o nosso **Dashboard de Planejamento Financeiro** como programadores profissionais fazem: **em pequenas etapas interativas (Criar Visual ➔ Testar ➔ Criar Função ➔ Testar)**!

1. **Primeiro (Passos 1 a 4):** Vamos levantar a janela, dividir as duas colunas, colocar os botões no menu lateral e montar os painéis da direita. A cada passo, vamos **executar o programa** para ver a tela ganhando forma!
2. **Depois (Passos 5 e 6):** Com a janela pronta, vamos programar as funções dos botões e a **janela de entrada de dados (`CTkInputDialog`)** que atualiza o valor da receita ao vivo na tela!

```
+-------------------------------------------------------------------------------+
|  Sistema de Planejamento Financeiro - IFCE                         [_][□][X]  |
+----------------------+--------------------------------------------------------+
|  💰 Finanças IFCE    |  +--------------------------------------------------+  |
|     Menu Principal   |  | 📌 RESUMO DE RECEITAS (PREVISÃO MENSAL)          |  |
|                      |  | R$ 0.00                                          |  |
| [1 - Cadastrar Rec.] |  +--------------------------------------------------+  |
| [2 - Adic. Despesa ] |  +--------------------------------------------------+  |
| [3 - Listar Desp.  ] |  | 📋 LISTA DE DESPESAS REGISTRADAS                 |  |
| [4 - Balanço 50... ] |  | #     Descrição          Categoria        Valor  |  |
|                      |  |       🚧 Nenhuma despesa exibida.                |  |
|                      |  |       (Será continuado nas próx. aulas)          |  |
| [0 - Sair          ] |  +--------------------------------------------------+  |
|                      |  [ Status: Escolha uma opção no menu lateral.       ]  |
+----------------------+--------------------------------------------------------+
```

---

## ⚙️ Passo 0: Preparação do Ambiente

No terminal do VS Code, dentro da pasta `projetinho`, ative seu ambiente virtual (se já tiver criado) e garanta que o `customtkinter` está instalado:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install customtkinter
```

Abra o arquivo `gui_main.py` em branco para começarmos!

---

## 🧱 FASE 1: Construindo e Testando o Visual da Janela

### Passo 1: Criar a Janela Principal e Abrir em Tela Cheia

Vamos começar criando apenas a janela principal e o comando `janela.mainloop()` (que mantém a janela aberta na tela).

Digite no seu `gui_main.py`:

```python
import customtkinter as ctk

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL GLOBAL
# ==============================================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==============================================================================
# 2. JANELA PRINCIPAL E CONTROLE DE TELA
# ==============================================================================
janela = ctk.CTk()
janela.title("Sistema de Planejamento Financeiro - IFCE")
janela.geometry("850x520")
janela.minsize(750, 480)

# Abertura Maximizada Compatível (Linux / Windows)
try:
    janela.state("zoomed")
except Exception:
    janela.attributes("-zoomed", True)

# Atualiza os cálculos de geometria da tela
janela.update_idletasks()


if __name__ == "__main__":
    janela.mainloop()
```

🧪 **Hora de Testar (Teste 1):**
Execute no terminal: `python gui_main.py`.
* Veja que sua janela já abre maximizada em modo escuro! Feche a janela no `X` para continuar.

---

### Passo 2: Dividir a Janela em 2 Colunas (Esquerda e Direita)

Para que o nosso layout nunca quebre quando a janela estiver maximizada, vamos criar dois quadros organizadores (`CTkFrame`):
* **`frame_menu` (na esquerda):** Largura fixa de `260` pixels. Usamos `pack_propagate(False)` para travar essa largura e impedir que os botões deformem!
* **`frame_conteudo` (na direita):** Usa `expand=True` para ocupar todo o espaço restante do monitor.

Adicione **acima** do `if __name__ == "__main__":`:

```python
# ==============================================================================
# 3. CONTAINERS PRINCIPAIS (DIVISÃO EM COLUNAS)
# ==============================================================================

# Coluna da Esquerda: Menu Lateral (Largura rígida de 260px)
frame_menu = ctk.CTkFrame(janela, width=260, corner_radius=0)
frame_menu.pack(side="left", fill="y")
frame_menu.pack_propagate(False)  # Impede que elementos filhos alterem os 260px

# Coluna da Direita: Área de Conteúdo / Dados (Absorve todo o restante da tela)
frame_conteudo = ctk.CTkFrame(janela, fg_color="transparent")
frame_conteudo.pack(side="right", fill="both", expand=True, padx=20, pady=20)
```

🧪 **Hora de Testar (Teste 2):**
Execute `python gui_main.py`.
* Observe que agora existe uma coluna lateral destacada na esquerda e uma área ampla na direita! Feche a janela para ir ao Passo 3.

---

### Passo 3: Adicionar os Botões no Menu Lateral (Apenas Visual)

Agora vamos colocar o título e os 5 botões dentro da coluna esquerda (`frame_menu`).
> 💡 **Por que ainda não colocamos `command=` nos botões?** Porque primeiro queremos ver e testar os botões na tela! No Passo 5 vamos criar as funções e conectá-las aos botões.

Adicione logo abaixo do código do Passo 2 (ainda **antes** do `if __name__ == "__main__":`):

```python
# ==============================================================================
# 4. COMPONENTES DO MENU LATERAL (frame_menu)
# ==============================================================================

lbl_logo = ctk.CTkLabel(
    frame_menu,
    text="💰 Finanças IFCE",
    font=ctk.CTkFont(size=20, weight="bold")
)
lbl_logo.pack(pady=(30, 5), padx=20)

lbl_subtitulo = ctk.CTkLabel(
    frame_menu,
    text="Menu Principal",
    font=ctk.CTkFont(size=13),
    text_color="gray70"
)
lbl_subtitulo.pack(pady=(0, 25), padx=20)

# Botões de Operação
btn_receita = ctk.CTkButton(
    frame_menu,
    text="1 - Cadastrar Receita",
    height=40,
    anchor="w"
)
btn_receita.pack(pady=6, padx=20, fill="x")

btn_adicionar = ctk.CTkButton(
    frame_menu,
    text="2 - Adicionar Despesa",
    height=40,
    anchor="w"
)
btn_adicionar.pack(pady=6, padx=20, fill="x")

btn_listar = ctk.CTkButton(
    frame_menu,
    text="3 - Listar Despesas",
    height=40,
    anchor="w"
)
btn_listar.pack(pady=6, padx=20, fill="x")

btn_balanco = ctk.CTkButton(
    frame_menu,
    text="4 - Balanço 50-30-20",
    height=40,
    anchor="w"
)
btn_balanco.pack(pady=6, padx=20, fill="x")

# Botão de Encerramento (Fixado na base da barra lateral com side="bottom")
btn_sair = ctk.CTkButton(
    frame_menu,
    text="0 - Sair do Sistema",
    height=40,
    fg_color="#c0392b",
    hover_color="#922b21"
)
btn_sair.pack(side="bottom", pady=25, padx=20, fill="x")
```

🧪 **Hora de Testar (Teste 3):**
Execute `python gui_main.py`.
* Veja todos os 5 botões alinhados na esquerda e o botão vermelho **0 - Sair do Sistema** posicionado lá embaixo! Se você clicar neles agora, ainda não acontece nada. Feche no `X` para construirmos o lado direito!

---

### Passo 4: Construir a Área da Direita (Resumo de Receita + Lista de Despesas)

No espaço da direita (`frame_conteudo`), vamos colocar:
1. **No Topo (`frame_resumo`):** Um card compacto para exibir o **Resumo de Receitas** (`R$ 0.00`).
2. **No Centro (`frame_despesas`):** Um painel grande para a **Lista de Despesas** (indicando que o cadastro de despesas e o salvamento em arquivo serão feitos nas próximas aulas).
3. **No Rodapé (`lbl_status`):** Uma barra de texto para exibir avisos e confirmações.

Adicione logo abaixo do código do Passo 3 (antes do `if __name__ == "__main__":`):

```python
# ==============================================================================
# 5. COMPONENTES DO PAINEL DIREITO (frame_conteudo)
# ==============================================================================

# 5.1 - Card Superior: Resumo de Receitas
frame_resumo = ctk.CTkFrame(frame_conteudo, corner_radius=10)
frame_resumo.pack(fill="x", pady=(0, 15))

lbl_titulo_resumo = ctk.CTkLabel(
    frame_resumo,
    text="📌 RESUMO DE RECEITAS (PREVISÃO MENSAL)",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color="gray75"
)
lbl_titulo_resumo.pack(anchor="w", padx=20, pady=(15, 2))

lbl_valor_receita = ctk.CTkLabel(
    frame_resumo,
    text="R$ 0.00",
    font=ctk.CTkFont(size=28, weight="bold"),
    text_color="#2ecc71"
)
lbl_valor_receita.pack(anchor="w", padx=20, pady=(0, 15))

# 5.2 - Painel Central: Lista de Despesas
frame_despesas = ctk.CTkFrame(frame_conteudo, corner_radius=10)
frame_despesas.pack(fill="both", expand=True)

lbl_titulo_despesas = ctk.CTkLabel(
    frame_despesas,
    text="📋 LISTA DE DESPESAS REGISTRADAS",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color="gray75"
)
lbl_titulo_despesas.pack(anchor="w", padx=20, pady=(15, 10))

# Cabeçalho da tabela com fonte monoespaçada
frame_cabecalho_lista = ctk.CTkFrame(frame_despesas, height=32, corner_radius=6, fg_color="gray20")
frame_cabecalho_lista.pack(fill="x", padx=20, pady=(0, 10))

lbl_colunas = ctk.CTkLabel(
    frame_cabecalho_lista,
    text="#     Descrição da Despesa                        Categoria               Valor (R$)",
    font=ctk.CTkFont(family="monospace", size=12, weight="bold")
)
lbl_colunas.pack(anchor="w", padx=15, pady=5)

# Mensagem central explicando a continuidade nas próximas etapas
lbl_placeholder_lista = ctk.CTkLabel(
    frame_despesas,
    text=(
        "🚧 Nenhuma despesa exibida.\n\n"
        "O cadastro de despesas e a persistência dos dados (salvar em arquivo)\n"
        "serão implementados nas próximas etapas do projeto!"
    ),
    font=ctk.CTkFont(size=14),
    text_color="gray60",
    justify="center"
)
lbl_placeholder_lista.pack(expand=True, pady=20)

# 5.3 - Rodapé de Status
lbl_status = ctk.CTkLabel(
    frame_conteudo,
    text="Sistema iniciado com sucesso. Escolha uma opção no menu lateral.",
    font=ctk.CTkFont(size=13),
    anchor="w"
)
lbl_status.pack(fill="x", pady=(12, 0))
```

🧪 **Hora de Testar (Teste 4):**
Execute `python gui_main.py`.
* Parabéns! Todo o layout visual da nossa aplicação já está completo na tela! Agora vamos programar as funções dos botões.

---

## ⚡ FASE 2: Incrementando as Funcionalidades e Testando os Cliques

### Passo 5: Ativar o Botão "0 - Sair" e os Avisos dos Botões 2, 3 e 4

Para que um botão execute uma ação ao ser clicado, fazemos duas coisas:
1. Criamos a função no topo do arquivo (antes da criação da janela).
2. Adicionamos `command=nome_da_funcao` dentro do botão correspondente.

#### 5.1 Crie as funções no topo do arquivo:
Suba até o início do arquivo, logo abaixo de `ctk.set_default_color_theme("blue")`, e adicione:

```python
# ==============================================================================
# DADOS EM MEMÓRIA E FUNÇÕES DOS BOTÕES (CALLBACKS)
# ==============================================================================
renda_prevista = 0.0


def sair_sistema():
    """Encerra a janela principal com segurança."""
    janela.destroy()


def adicionar_despesa():
    lbl_status.configure(
        text="🚧 [EM CONSTRUÇÃO] O cadastro e armazenamento de despesas serão feitos na Etapa 3.",
        text_color="#f39c12"
    )


def listar_despesas():
    lbl_status.configure(
        text="🚧 [EM CONSTRUÇÃO] A listagem dinâmica será implementada nas próximas aulas.",
        text_color="#f39c12"
    )


def exibir_balanco():
    lbl_status.configure(
        text=f"📊 [EM CONSTRUÇÃO] Balanço 50-30-20 | Receita atual na memória: R$ {renda_prevista:.2f}",
        text_color="#3498db"
    )
```

#### 5.2 Conecte o `command=` nos botões `btn_adicionar`, `btn_listar`, `btn_balanco` e `btn_sair`:
Desça até onde você criou esses 4 botões (no Passo 3) e adicione a linha `command=...` em cada um deles:

```python
btn_adicionar = ctk.CTkButton(
    frame_menu,
    text="2 - Adicionar Despesa",
    height=40,
    anchor="w",
    command=adicionar_despesa
)
btn_adicionar.pack(pady=6, padx=20, fill="x")

btn_listar = ctk.CTkButton(
    frame_menu,
    text="3 - Listar Despesas",
    height=40,
    anchor="w",
    command=listar_despesas
)
btn_listar.pack(pady=6, padx=20, fill="x")

btn_balanco = ctk.CTkButton(
    frame_menu,
    text="4 - Balanço 50-30-20",
    height=40,
    anchor="w",
    command=exibir_balanco
)
btn_balanco.pack(pady=6, padx=20, fill="x")

btn_sair = ctk.CTkButton(
    frame_menu,
    text="0 - Sair do Sistema",
    height=40,
    fg_color="#c0392b",
    hover_color="#922b21",
    command=sair_sistema
)
btn_sair.pack(side="bottom", pady=25, padx=20, fill="x")
```

> [!WARNING]
> **Cuidado:** Nunca coloque parênteses `()` depois do nome da função no `command=`! Escreva `command=sair_sistema` e não `command=sair_sistema()`.

🧪 **Hora de Testar (Teste 5):**
Execute `python gui_main.py`.
* Clique nos botões `2`, `3` e `4` e veja o texto no rodapé mudar de cor e mensagem!
* Clique em `0 - Sair do Sistema` e veja a janela fechar!

---

### Passo 6: Criar a Janela de Entrada de Receita (`CTkInputDialog`) e Atualizar o Resumo

Agora vamos programar o botão **1 - Cadastrar Receita**!

#### 🧠 Como funciona a entrada de dados na Interface Gráfica?
1. **A Subjanela de Digitação (`CTkInputDialog`):** Em vez de usar o `input()` no terminal, o comando `ctk.CTkInputDialog(...)` abre uma janelinha pop-up no meio da tela para o usuário digitar o valor.
2. **Capturando o Texto (`dialogo.get_input()`):** Espera o usuário clicar em *Ok* e guarda o que foi digitado na variável `entrada`. Se o usuário clicar em *Cancel*, ela devolve `None` e a função encerra sem erro.
3. **Atualizando o Valor na Tela (`lbl_valor_receita.configure(...)`):** Depois de validar com `try/except` se o número é válido e positivo, guardamos na variável `renda_prevista` e usamos `.configure(text=...)` para trocar imediatamente o texto `R$ 0.00` lá no **Card de Resumo de Receitas** pelo novo valor!
4. **Sobre o Armazenamento Futuro (Persistência):** Nesta etapa, o valor de `renda_prevista` fica guardado na memória RAM enquanto o programa estiver aberto. Nas próximas etapas do projeto, vamos implementar a **persistência em arquivo** para salvar permanentemente todas as entradas (receitas) e saídas (despesas) no computador!

#### 6.1 Adicione a função `cadastrar_receita()` no bloco de funções (acima de `def sair_sistema():`):

```python
def cadastrar_receita():
    """Abre caixa de diálogo para pedir a receita, valida e atualiza o Resumo."""
    global renda_prevista

    dialogo = ctk.CTkInputDialog(
        text="Informe a receita líquida esperada (R$):",
        title="1 - Cadastrar Receita"
    )
    entrada = dialogo.get_input()

    # Se o usuário clicou em Cancelar ou fechou a janelinha
    if entrada is None:
        return

    # Aceita vírgula ou ponto nos centavos e limpa espaços extras
    entrada = entrada.strip().replace(",", ".")

    try:
        valor = float(entrada)
        if valor >= 0:
            renda_prevista = valor
            # Atualiza o número grande verde no Card de Resumo!
            lbl_valor_receita.configure(text=f"R$ {renda_prevista:.2f}")
            # Mostra confirmação na barra de status!
            lbl_status.configure(
                text=f"✅ Receita atualizada com sucesso para R$ {renda_prevista:.2f}!",
                text_color="#2ecc71"
            )
        else:
            lbl_status.configure(
                text="❌ Erro: O valor da receita não pode ser negativo!",
                text_color="#e74c3c"
            )
    except ValueError:
        lbl_status.configure(
            text="❌ Erro: Digite um número válido (ex: 2500.50)!",
            text_color="#e74c3c"
        )
```

#### 6.2 Conecte o `command=cadastrar_receita` no botão `btn_receita`:
Localize o `btn_receita` (que você criou no Passo 3) e adicione o `command=cadastrar_receita`:

```python
btn_receita = ctk.CTkButton(
    frame_menu,
    text="1 - Cadastrar Receita",
    height=40,
    anchor="w",
    command=cadastrar_receita
)
btn_receita.pack(pady=6, padx=20, fill="x")
```

---

## 🧪 Teste Final Completo (Checklist de Validação)

Execute o seu programa (`python gui_main.py`) e faça a bateria final de testes:

- [ ] **Teste 1 (Botão Cancelar):** Clique em `1 - Cadastrar Receita` e clique em *Cancel*. O programa deve continuar funcionando normalmente sem erro.
- [ ] **Teste 2 (Proteção contra Letras):** Clique em `1 - Cadastrar Receita`, digite `abc` e clique em *Ok*. O rodapé deve ficar vermelho avisando `❌ Erro: Digite um número válido!`.
- [ ] **Teste 3 (Proteção contra Negativos):** Clique em `1 - Cadastrar Receita`, digite `-300` e clique em *Ok*. O rodapé deve avisar que a receita não pode ser negativa.
- [ ] **Teste 4 (Atualização do Resumo de Receita):** Clique em `1 - Cadastrar Receita` e digite `3500,50`. Veja o número gigante verde no card **Resumo de Receitas** mudar imediatamente para **`R$ 3500.50`**!
- [ ] **Teste 5 (Memória em Funcionamento):** Clique no botão `4 - Balanço 50-30-20` e veja no rodapé que o sistema lembra do valor `R$ 3500.50` armazenado na memória!
