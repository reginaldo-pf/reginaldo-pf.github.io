"""
Projeto Final: Planejamento Financeiro (Versão Interface Gráfica - CustomTkinter)
Etapa 3: Cadastro de Despesas (Listas e Dicionários), Listagem no Painel e Persistência em JSON

Ordem de Construção Interativa (Visual -> Teste -> Função -> Teste):
- Cena 1: Preparar a Área Rolável (`CTkScrollableFrame`) na direita para listar as despesas
- Cena 2: Criar a Janela Pop-up de Cadastro de Despesa (`CTkToplevel`) com Descrição, Valor e Categoria
- Cena 3: Validar os campos, empacotar no Dicionário (`dict`), guardar na Lista (`despesas.append`) e desenhar na tela
- Cena 4: Persistência Mínima com `json` (`salvar_dados` e `carregar_dados`) para nunca perder os dados ao fechar!
"""

import json
import os
import customtkinter as ctk

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL GLOBAL
# ==============================================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==============================================================================
# DADOS EM MEMÓRIA E PERSISTÊNCIA MÍNIMA EM JSON
# ==============================================================================
ARQUIVO_DADOS = "dados_financeiros.json"
renda_prevista = 0.0
despesas = []  # Lista que guardará os dicionários de cada despesa


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


# ==============================================================================
# FUNÇÕES DE ATUALIZAÇÃO VISUAL E BOTÕES (CALLBACKS)
# ==============================================================================
def sair_sistema():
    """Fecha a janela gráfica."""
    janela.destroy()


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

    # 3. Percorre a lista de dicionários com enumerate e cria uma linha para cada gasto
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


def adicionar_despesa():
    """Abre uma subjanela de formulário (CTkToplevel) para cadastrar uma nova despesa."""
    popup = ctk.CTkToplevel(janela)
    popup.title("2 - Nova Despesa")
    popup.geometry("400x380")
    popup.resizable(False, False)
    popup.transient(janela)  # Mantém o pop-up sempre na frente da janela principal
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

    # Rótulo para erro interno do pop-up
    lbl_erro_popup = ctk.CTkLabel(popup, text="", text_color="#e74c3c", font=ctk.CTkFont(size=12))
    lbl_erro_popup.pack(pady=(10, 0))

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

        # Empacota no Dicionário e adiciona na Lista
        nova_despesa = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        }
        despesas.append(nova_despesa)

        # Salva no arquivo JSON e atualiza a lista na tela!
        salvar_dados()
        atualizar_lista_visual()

        lbl_status.configure(
            text=f"✅ Despesa '{descricao}' (R$ {valor:.2f}) salva com sucesso! Total de itens: {len(despesas)}",
            text_color="#2ecc71"
        )
        popup.destroy()

    btn_salvar = ctk.CTkButton(
        popup,
        text="💾 Salvar Despesa",
        height=38,
        fg_color="#27ae60",
        hover_color="#1e8449",
        command=confirmar_cadastro
    )
    btn_salvar.pack(fill="x", padx=25, pady=(15, 20))


def listar_despesas():
    """Atualiza a visualização da tabela e informa a quantidade cadastrada."""
    atualizar_lista_visual()
    lbl_status.configure(
        text=f"📋 Lista atualizada! Exibindo {len(despesas)} despesa(s) registrada(s).",
        text_color="#3498db"
    )


def exibir_balanco():
    lbl_status.configure(
        text=f"📊 [EM CONSTRUÇÃO] Balanço 50-30-20 | Receita: R$ {renda_prevista:.2f} | Despesas: {len(despesas)} item(ns)",
        text_color="#3498db"
    )


def cadastrar_receita():
    """Abre uma janelinha pop-up para ler a receita, valida, atualiza o Resumo e salva em JSON."""
    global renda_prevista

    dialogo = ctk.CTkInputDialog(
        text="Informe a receita líquida esperada (R$):",
        title="1 - Cadastrar Receita"
    )
    entrada = dialogo.get_input()

    if entrada is None:
        return

    entrada = entrada.strip().replace(",", ".")

    try:
        valor = float(entrada)
        if valor >= 0:
            renda_prevista = valor
            salvar_dados()  # Salva automaticamente no JSON!
            lbl_valor_receita.configure(text=f"R$ {renda_prevista:.2f}")
            lbl_status.configure(
                text=f"✅ Receita atualizada e salva para R$ {renda_prevista:.2f}!",
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

try:
    janela.state("zoomed")
except Exception:
    janela.attributes("-zoomed", True)

janela.update_idletasks()

# ==============================================================================
# 3. CONTAINERS PRINCIPAIS (DIVISÃO EM COLUNAS)
# ==============================================================================
frame_menu = ctk.CTkFrame(janela, width=260, corner_radius=0)
frame_menu.pack(side="left", fill="y")
frame_menu.pack_propagate(False)

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

# Cabeçalho das colunas
frame_cabecalho_lista = ctk.CTkFrame(frame_despesas, height=32, corner_radius=6, fg_color="gray20")
frame_cabecalho_lista.pack(fill="x", padx=20, pady=(0, 10))

lbl_colunas = ctk.CTkLabel(
    frame_cabecalho_lista,
    text="#     Descrição da Despesa                        Categoria               Valor (R$)",
    font=ctk.CTkFont(family="monospace", size=12, weight="bold")
)
lbl_colunas.pack(anchor="w", padx=15, pady=5)

# Área rolável onde as linhas de despesas serão inseridas dinamicamente
frame_lista_scroll = ctk.CTkScrollableFrame(frame_despesas, fg_color="transparent")
frame_lista_scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))

# 5.3 - Barra de Status no Rodapé
lbl_status = ctk.CTkLabel(
    frame_conteudo,
    text="Sistema iniciado com sucesso. Escolha uma opção no menu lateral.",
    font=ctk.CTkFont(size=13),
    anchor="w"
)
lbl_status.pack(fill="x", pady=(12, 0))

# ==============================================================================
# 6. CARREGAMENTO INICIAL DOS DADOS SALVOS E LOOP PRINCIPAL
# ==============================================================================
carregar_dados()
lbl_valor_receita.configure(text=f"R$ {renda_prevista:.2f}")
atualizar_lista_visual()

if __name__ == "__main__":
    janela.mainloop()
