# Roteiro de Live Coding e Gravação de Vídeo (Guia do Professor)
## Construindo o Dashboard Financeiro em CustomTkinter (Passo a Passo Interativo)

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Formato Metodológico:** **Construção Incremental Interativa (Visual ➔ Teste ➔ Função ➔ Teste)** — estruturado tanto para *Live Coding* em sala quanto como **roteiro de gravação de videoaula**.
* **Arquivos de Apoio:**
  * Código em construção da turma: [projetinho/gui_main.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/projetinho/gui_main.py)
  * Gabarito consolidado: [etapas/etapa2_gui_customtkinter.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa2_gui_customtkinter.py)

---

## 🎥 Como Conduzir a Aula / Gravação (Dinâmica "Sem Copiar e Colar")

> [!IMPORTANT]
> **Por que não escrevemos todas as funções no topo antes de criar a janela?**
> Quando o aluno digita 70 linhas de funções no início do arquivo sem ver nenhuma janela abrir, ele perde o engajamento e apenas copia código mecanicamente.
>
> **Nossa Regra de Ouro nesta Aula/Vídeo:**
> 1. **Fase 1 (Foco Visual):** Primeiro colocamos a janela em pé, dividimos as colunas, colocamos os botões **sem `command=`** e montamos os painéis da direita. A cada bloco adicionado, **rodamos o programa** para ver a interface nascendo!
> 2. **Fase 2 (Dando Vida um por um):** Com a janela 100% visível e funcionando, subimos no arquivo para criar **uma função por vez**, conectamos no respectivo botão e **testamos imediatamente**!

---

## 🎬 CENA 1: Criando a Janela Principal e Abertura Maximizada
*(Foco: Fazer a primeira janela abrir e resolver o problema do tamanho na tela)*

### 1.1 O que digitar no `gui_main.py` (Do zero):
Comece o arquivo apenas com a criação da janela e o loop principal no final:

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

# Atualiza os cálculos de geometria antes de continuar
janela.update_idletasks()


if __name__ == "__main__":
    janela.mainloop()
```

### 🎙️ Roteiro de Fala / Explicação Didática (Para Aula e Vídeo):
* **O papel do `janela.mainloop()`:** *"Pessoal, lembram do `while True:` que mantinha nosso menu vivo no terminal? Na interface gráfica, quem faz esse papel é o `janela.mainloop()`. Ele fica sempre na última linha do arquivo escutando cliques do mouse e teclado."*
* **O truque do `try / except` no `zoomed`:** *"Por que usamos `try: janela.state('zoomed')` e `except: janela.attributes('-zoomed', True)`? Porque no Windows o comando para maximizar é um, e no Linux (Ubuntu/Debian do laboratório) é outro! Com esse bloco `try/except`, nosso programa abre em tela cheia em qualquer sistema operacional sem quebrar."*
* **Dica extra sobre o `update_idletasks()`:** Ele força o sistema operacional a calcular imediatamente quantos pixels tem o monitor antes de desenharmos as colunas.

### 🧪 Checkpoint de Teste 1 (Executar ao vivo!):
* Rode `python gui_main.py`.
* **O que mostrar na tela:** A janela escura abre maximizada ocupando toda a tela. Feche no `X` e diga: *"A casa está de pé! Agora vamos levantar a parede que divide o Menu à esquerda e os Dados à direita."*

---

## 🎬 CENA 2: Dividindo a Janela em 2 Colunas (Sem Quebrar ao Maximizar)
*(Foco: Resolver de vez o problema de botões desalinhados em tela cheia)*

### 2.1 O que adicionar no código (Antes do `if __name__ == "__main__":`):

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

### 🎙️ Roteiro de Fala / Explicação Didática:
* **Por que os botões ficavam estranhos quando maximizávamos antes?** *"Se jogarmos botões soltos na janela, ao maximizar a tela eles se espalham ou esticam demais. O segredo profissional é criar duas caixas organizadoras (`CTkFrame`)."*
* **O segredo do `frame_menu.pack_propagate(False)`:** *"Gravem essa linha! Por padrão, um Frame no Tkinter encolhe para abraçar o tamanho do texto que está dentro dele. O `pack_propagate(False)` trava a parede em exatos `260` pixels de largura. Não importa o tamanho do monitor, nosso menu lateral nunca vai deformar!"*

### 🧪 Checkpoint de Teste 2 (Executar ao vivo!):
* Rode `python gui_main.py`.
* **O que mostrar na tela:** Aponte o mouse para a coluna cinza-escura perfeita de 260px na esquerda e todo o vão livre na direita.

---

## 🎬 CENA 3: Adicionando os Botões do Menu Lateral (Apenas Visual!)
*(Foco: Posicionar os botões primeiro SEM `command=`, para não dar erro de função inexistente)*

> [!WARNING]
> **Por que NÃO colocamos `command=cadastrar_receita` agora?**
> Se o aluno digitar `command=cadastrar_receita` neste momento e tentar rodar para ver como ficaram os botões, o Python vai travar com `NameError: name 'cadastrar_receita' is not defined`!
> Então, primeiro criamos os botões **sem `command`** para testar o visual, e na Cena 5 ligaremos os fios!

### 3.1 O que adicionar no código (Abaixo de `frame_conteudo.pack(...)`):

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

# Botões de Operação (Inicialmente apenas visuais!)
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

### 🎙️ Roteiro de Fala / Explicação Didática:
* **Destaque o primeiro argumento (`frame_menu`):** *"Reparem que todos esses botões têm `frame_menu` no primeiro parâmetro, e não `janela`. Eles moram dentro da coluna esquerda!"*
* **Destaque `anchor="w"` e `fill="x"`:** *"O `fill='x'` faz todos os botões terem a mesma largura elegante, e o `anchor='w'` (West/Oeste) alinha os textos à esquerda."*
* **Destaque `side="bottom"` no botão Sair:** *"Olhem que charme: enquanto os 4 primeiros botões empilham no topo, o botão vermelho `0 - Sair` usa `side='bottom'` para colar no chão da barra lateral!"*

### 🧪 Checkpoint de Teste 3 (Executar ao vivo!):
* Rode `python gui_main.py`.
* Clique nos botões na frente dos alunos. Eles fazem o efeito visual de clique, mas ainda não executam nada. Diga: *"Nosso menu lateral já está lindo e responsivo! Agora vamos desenhar o painel da direita antes de programar os cliques."*

---

## 🎬 CENA 4: Construindo o Painel Direito (Resumo de Receita + Lista de Despesas + Rodapé)
*(Foco: Completar 100% da estrutura visual da janela)*

### 4.1 O que adicionar no código (Abaixo de `btn_sair.pack(...)`):

```python
# ==============================================================================
# 5. COMPONENTES DO PAINEL DIREITO (frame_conteudo)
# ==============================================================================

# 5.1 - Card Superior: Resumo de Receitas (Compacto no topo)
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

# 5.2 - Painel Central: Lista de Despesas (Expande para ocupar o resto da tela)
frame_despesas = ctk.CTkFrame(frame_conteudo, corner_radius=10)
frame_despesas.pack(fill="both", expand=True)

lbl_titulo_despesas = ctk.CTkLabel(
    frame_despesas,
    text="📋 LISTA DE DESPESAS REGISTRADAS",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color="gray75"
)
lbl_titulo_despesas.pack(anchor="w", padx=20, pady=(15, 10))

# Cabeçalho das colunas com fonte monoespaçada (estilo tabela)
frame_cabecalho_lista = ctk.CTkFrame(frame_despesas, height=32, corner_radius=6, fg_color="gray20")
frame_cabecalho_lista.pack(fill="x", padx=20, pady=(0, 10))

lbl_colunas = ctk.CTkLabel(
    frame_cabecalho_lista,
    text="#     Descrição da Despesa                        Categoria               Valor (R$)",
    font=ctk.CTkFont(family="monospace", size=12, weight="bold")
)
lbl_colunas.pack(anchor="w", padx=15, pady=5)

# Aviso centralizado indicando o que será feito nas próximas etapas
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

# 5.3 - Barra de Status no Rodapé
lbl_status = ctk.CTkLabel(
    frame_conteudo,
    text="Sistema iniciado com sucesso. Escolha uma opção no menu lateral.",
    font=ctk.CTkFont(size=13),
    anchor="w"
)
lbl_status.pack(fill="x", pady=(12, 0))
```

### 🎙️ Roteiro de Fala / Explicação Didática:
* **Por que Receita é um Resumo (`fill="x"`) e Despesas é uma Lista (`expand=True`)?** *"No planejamento financeiro, a receita prevista é um indicador único de topo (por isso usamos um card compacto com letra grande verde `size=28`). Já as despesas são dezenas de itens ao longo do mês, então reservamos todo o salão principal (`fill='both', expand=True`) para listar cada gasto!"*
* **Importante mencionar sobre Persistência Futura:** *"Notem o aviso no centro da lista: por enquanto nossa janela é a fachada visual e os dados vão morar temporariamente na memória RAM enquanto o programa estiver aberto. Nas próximas etapas, além de listar as despesas aqui dentro, vamos implementar o **armazenamento permanente (persistência em arquivo)** para que nada se perca ao fechar o programa!"*

### 🧪 Checkpoint de Teste 4 (Executar ao vivo!):
* Rode `python gui_main.py`.
* **Comemore com a turma/espectadores:** A interface completa do Dashboard está pronta, alinhada e sem nenhum erro! Agora começa a **Fase 2: Dar vida aos botões, um por um**.

---

## 🎬 CENA 5: Primeira Funcionalidade – O Botão "0 - Sair" e os Botões de Aviso
*(Foco: Ensinar como um botão chama uma função através do `command=` e atualiza o rodapé)*

### 5.1 Passo A – Criar a variável e as funções simples no topo do arquivo:
Suba até logo abaixo de `ctk.set_default_color_theme("blue")` (antes de `janela = ctk.CTk()`) e adicione:

```python
# ==============================================================================
# DADOS EM MEMÓRIA E FUNÇÕES DOS BOTÕES (CALLBACKS)
# ==============================================================================
renda_prevista = 0.0


def sair_sistema():
    """Fecha a janela gráfica (equivalente ao break do terminal)."""
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

### 5.2 Passo B – Ligar o fio (`command=`) nos 4 botões correspondentes:
Desça até os botões `btn_adicionar`, `btn_listar`, `btn_balanco` e `btn_sair` e adicione o atributo `command=` em cada um:

```python
btn_adicionar = ctk.CTkButton(
    frame_menu,
    text="2 - Adicionar Despesa",
    height=40,
    anchor="w",
    command=adicionar_despesa  # <-- Ligamos a função aqui (SEM parênteses!)
)
```
*(Faça o mesmo para `btn_listar` com `command=listar_despesas`, `btn_balanco` com `command=exibir_balanco` e `btn_sair` com `command=sair_sistema`).*

### 🎙️ Roteiro de Fala / Explicação Didática:
* **Como o `.configure()` muda a tela ao vivo?** *"No terminal dávamos `print()`. Aqui na janela, o rótulo `lbl_status` já está colado lá no rodapé. Quando chamamos `lbl_status.configure(text=..., text_color=...)`, o CustomTkinter troca o texto e a cor na mesma hora sem precisar recriar a janela!"*
* **Alerta da Armadilha dos Parênteses:** *"Atenção máxima: escrevam `command=sair_sistema` **SEM parênteses**! Se você colocar `command=sair_sistema()`, o Python executa a função enquanto está desenhando o botão e fecha a janela antes mesmo de ela abrir!"*

### 🧪 Checkpoint de Teste 5 (Executar ao vivo!):
* Rode `python gui_main.py`.
* Clique nos botões `2`, `3` e `4` e mostre o rodapé mudando de texto e de cor (amarelo e azul).
* Clique no botão `0 - Sair do Sistema` e mostre a janela fechando suavemente!

---

## 🎬 CENA 6: A Estrela da Aula – A Janela de Entrada (`CTkInputDialog`) e Atualização da Receita
*(Foco: Explicar detalhadamente como abrir a subjanela de digitação, validar o dado e atualizar o painel verde de Resumo)*

### 6.1 Passo A – Criar a função `cadastrar_receita()` no bloco de funções:
Acima de `def sair_sistema():`, digite e explique bloco por bloco:

```python
def cadastrar_receita():
    """Abre uma janelinha pop-up para ler a receita, valida e atualiza o Resumo na tela."""
    global renda_prevista

    # 1. Cria e abre a subjanela (Pop-up) de entrada de dados
    dialogo = ctk.CTkInputDialog(
        text="Informe a receita líquida esperada (R$):",
        title="1 - Cadastrar Receita"
    )
    
    # 2. Pausa e espera o usuário digitar e clicar em OK (substitui o input() do terminal!)
    entrada = dialogo.get_input()

    # 3. Se o usuário clicou em Cancelar ou fechou a janelinha no X, entrada vem vazia (None)
    if entrada is None:
        return

    # 4. Limpa espaços e troca vírgula por ponto (permite digitar 2500,50)
    entrada = entrada.strip().replace(",", ".")

    # 5. Validação segura com try/except e atualização visual dos componentes
    try:
        valor = float(entrada)
        if valor >= 0:
            renda_prevista = valor
            # Atualiza o número grande verde lá no Card de Resumo!
            lbl_valor_receita.configure(text=f"R$ {renda_prevista:.2f}")
            # Atualiza a barra de status no rodapé!
            lbl_status.configure(
                text=f"✅ Receita atualizada na memória para R$ {renda_prevista:.2f}!",
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

### 6.2 Passo B – Conectar no botão `btn_receita`:
Desça até o `btn_receita` e adicione `command=cadastrar_receita`:

```python
btn_receita = ctk.CTkButton(
    frame_menu,
    text="1 - Cadastrar Receita",
    height=40,
    anchor="w",
    command=cadastrar_receita
)
```

### 🎙️ Roteiro de Fala / Explicação Profunda (Momento-Chave do Vídeo/Aula):

1. **Como funciona a janela que recebe a entrada (`CTkInputDialog`)?**
   * *"No terminal usávamos `input()`, mas em uma aplicação gráfica não queremos que o usuário volte para a tela preta para digitar. Por isso instanciamos o `ctk.CTkInputDialog(...)`."*
   * *"Quando chamamos `entrada = dialogo.get_input()`, o CustomTkinter abre uma janelinha filha na frente da tela, congela a função ali esperando o usuário digitar e, assim que ele clica em **Ok**, entrega o texto digitado dentro da variável `entrada`!"*
2. **O que acontece se o usuário desistir e clicar em Cancelar (`if entrada is None`)?**
   * *"Diferente do terminal, uma janela tem o botão **Cancel** e o botão **X**. Se o usuário clicar neles, o `get_input()` devolve `None` (nada). Essa linha `if entrada is None: return` aborta a função silenciosamente sem dar erro!"*
3. **Como a janela atualiza o valor da Receita no painel direito?**
   * *"Olhem a mágica na linha `lbl_valor_receita.configure(text=f'R$ {renda_prevista:.2f}')`: lembra daquele rótulo gigante verde que criamos lá na Cena 4 mostrando `R$ 0.00`? Nós guardamos o endereço dele na variável `lbl_valor_receita`. Ao chamar `.configure(text=...)`, o novo valor validado salta imediatamente da variável `renda_prevista` para dentro do Card de Resumo na tela!"*
4. **Explicação sobre Memória Volátil vs. Persistência Futura (Gancho para as próximas aulas):**
   * *"Por que usamos `global renda_prevista`? Para guardar esse valor na memória RAM da aplicação enquanto a janela estiver aberta (se você clicar no botão `4 - Balanço`, verá que ele lembra do valor!). Porém, se fecharmos o programa agora e abrirmos de novo, ele volta para `R$ 0.00`. Por quê? Porque ainda está apenas na memória RAM! Nas próximas etapas do nosso projeto, vamos construir o **armazenamento permanente (persistência em arquivo)** tanto das entradas (receitas) quanto das saídas (despesas)!"*

### 🧪 Checkpoint Final de Teste 6 (Demonstração Completa para Fechar o Vídeo/Aula):
1. Rode o programa (`python gui_main.py`).
2. Clique em `1 - Cadastrar Receita` e clique em **Cancel** ➔ Mostre que nada quebra.
3. Clique em `1 - Cadastrar Receita` e digite `mil reais` ➔ Mostre o aviso vermelho no rodapé (`❌ Erro: Digite um número válido`).
4. Clique em `1 - Cadastrar Receita` e digite `-500` ➔ Mostre o bloqueio de número negativo.
5. Clique em `1 - Cadastrar Receita` e digite `3850,75` ➔ Mostre o Card de Resumo no topo direito mudando instantaneamente para **`R$ 3850.75`** e o rodapé ficando verde!
6. Clique em `4 - Balanço 50-30-20` ➔ Mostre no rodapé que a variável `renda_prevista` guardou `R$ 3850.75` na memória!
7. Opcional: descomente a linha `janela.resizable(False, False)` se quiser mostrar como travar o botão de restaurar após a janela abrir maximizada.
