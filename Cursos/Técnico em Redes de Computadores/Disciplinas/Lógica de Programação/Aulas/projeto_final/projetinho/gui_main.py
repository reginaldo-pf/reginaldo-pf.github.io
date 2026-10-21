import customtkinter as ctk

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL GLOBAL
# ==============================================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

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
    anchor="w",
    command=cadastrar_receita
)
btn_receita.pack(pady=6, padx=20, fill="x")

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

# Botão de Encerramento (Fixado na base da barra lateral com side="bottom")
btn_sair = ctk.CTkButton(
    frame_menu,
    text="0 - Sair do Sistema",
    height=40,
    fg_color="#c0392b",
    hover_color="#922b21",
    command=sair_sistema
)
btn_sair.pack(side="bottom", pady=25, padx=20, fill="x")

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

if __name__ == "__main__":
    janela.mainloop()
