"""
Projeto Final: Planejamento Financeiro (Versão Interface Gráfica - CustomTkinter)
Etapa 4: Listagem de Receitas, Expansão para Lista Dinâmica e Atualização do Menu

Novos conceitos trabalhados nesta etapa:
- Evolução de estado único para coleção: substituição de valor float por Lista de Dicionários (`receitas = []`)
- Subjanela de formulário modal (`CTkToplevel`) dedicada para cadastro de receitas com Descrição e Valor
- Alternância dinâmica de visões no painel rolável (`frame_lista_scroll`): visualização de Receitas x Despesas
- Funções acumuladoras e cálculo de total dinâmico com expressões geradoras (`sum(item['valor'] for item in receitas)`)
- Reorganização do menu lateral com opções dedicadas (1-Receita, 2-Despesa, 3-Listar Receitas, 4-Listar Despesas, 5-Balanço)
- Persistência estruturada em JSON contendo coleções completas de receitas e despesas com migração retrocompatível
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
# 2. DADOS EM MEMÓRIA E PERSISTÊNCIA EM JSON
# ==============================================================================
ARQUIVO_DADOS = "dados_financeiros.json"
receitas = []  # Lista que guardará os dicionários de cada receita: {"descricao": str, "valor": float}
despesas = []  # Lista que guardará os dicionários de cada despesa: {"descricao": str, "valor": float, "categoria": str}


def salvar_dados():
    """Salva as listas de receitas e despesas no arquivo JSON."""
    pacote = {
        "receitas": receitas,
        "despesas": despesas
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(pacote, arquivo, indent=4, ensure_ascii=False)


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
                    # Migração suave caso o aluno venha da Etapa 3 com renda fixa única
                    receitas = [{"descricao": "Receita Inicial (Migrada)", "valor": float(pacote["renda_prevista"])}]
                else:
                    receitas = []

                # Carregamento da lista de despesas
                despesas = pacote.get("despesas", [])
        except Exception:
            pass


def calcular_total_receitas():
    """Calcula a soma de todas as receitas cadastradas."""
    return sum(item["valor"] for item in receitas)


def calcular_total_despesas():
    """Calcula a soma de todas as despesas cadastradas."""
    return sum(item["valor"] for item in despesas)


def atualizar_card_resumo():
    """Atualiza o número grande verde do resumo e o contador de fontes cadastradas."""
    total = calcular_total_receitas()
    lbl_valor_receita.configure(text=f"R$ {total:.2f}")
    lbl_subtitulo_resumo.configure(
        text=f"Total acumulado: R$ {total:.2f} ({len(receitas)} fonte(s) registrada(s))"
    )


# ==============================================================================
# 3. FUNÇÕES DE ATUALIZAÇÃO VISUAL DAS TABELAS (RECEITAS E DESPESAS)
# ==============================================================================
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


# ==============================================================================
# 4. FORMULÁRIOS DE CADASTRO (SUBJANELAS MODAIS CTkToplevel)
# ==============================================================================
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

        # Empacota no Dicionário e adiciona à Lista de Receitas
        nova_receita = {
            "descricao": descricao,
            "valor": valor
        }
        receitas.append(nova_receita)

        # Salva em disco, atualiza o card e exibe a tabela de receitas
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


def adicionar_despesa():
    """Abre subjanela de formulário (CTkToplevel) para cadastrar uma nova despesa."""
    popup = ctk.CTkToplevel(janela)
    popup.title("2 - Nova Despesa")
    popup.geometry("400x380")
    popup.resizable(False, False)
    popup.transient(janela)
    popup.grab_set()

    # Campo 1: Descrição
    ctk.CTkLabel(popup, text="Descrição da Despesa:", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(20, 5)
    )
    entry_descricao = ctk.CTkEntry(popup, placeholder_text="Ex: Aluguel, Supermercado, Internet...")
    entry_descricao.pack(fill="x", padx=25)

    # Campo 2: Valor (R$)
    ctk.CTkLabel(popup, text="Valor da Despesa (R$):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    entry_valor = ctk.CTkEntry(popup, placeholder_text="Ex: 120.50")
    entry_valor.pack(fill="x", padx=25)

    # Campo 3: Categoria (Menu Dropdown)
    ctk.CTkLabel(popup, text="Categoria (Regra 50-30-20):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    combo_categoria = ctk.CTkOptionMenu(
        popup,
        values=["Essencial", "Estilo de Vida", "Reserva"]
    )
    combo_categoria.pack(fill="x", padx=25)

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

        # Empacota no Dicionário e adiciona à Lista de Despesas
        nova_despesa = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        }
        despesas.append(nova_despesa)

        # Salva em disco e atualiza a tabela de despesas
        salvar_dados()
        listar_despesas()

        lbl_status.configure(
            text=f"✅ Despesa '{descricao}' (R$ {valor:.2f}) salva com sucesso!",
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


def exibir_balanco():
    """Stub preparado para a Etapa 5 (Balanço Orçamentário e Regra 50-30-20)."""
    total_rec = calcular_total_receitas()
    total_desp = calcular_total_despesas()
    saldo = total_rec - total_desp

    lbl_status.configure(
        text=f"📊 [EM CONSTRUÇÃO - ETAPA 5] Receitas: R$ {total_rec:.2f} | Despesas: R$ {total_desp:.2f} | Saldo: R$ {saldo:.2f}",
        text_color="#3498db"
    )


def sair_sistema():
    """Fecha a aplicação de forma segura."""
    janela.destroy()


# ==============================================================================
# 5. CONSTRUÇÃO DA INTERFACE PRINCIPAL
# ==============================================================================
janela = ctk.CTk()
janela.title("Sistema de Planejamento Financeiro - IFCE Campus Tauá")
janela.geometry("900x560")
janela.minsize(800, 500)

try:
    janela.state("zoomed")
except Exception:
    janela.attributes("-zoomed", True)

janela.update_idletasks()

# Divisão Principal em 2 Colunas
frame_menu = ctk.CTkFrame(janela, width=270, corner_radius=0)
frame_menu.pack(side="left", fill="y")
frame_menu.pack_propagate(False)

frame_conteudo = ctk.CTkFrame(janela, fg_color="transparent")
frame_conteudo.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# ------------------------------------------------------------------------------
# 5.1 Menu Lateral de Ações (frame_menu)
# ------------------------------------------------------------------------------
lbl_logo = ctk.CTkLabel(
    frame_menu,
    text="💰 Finanças IFCE",
    font=ctk.CTkFont(size=20, weight="bold")
)
lbl_logo.pack(pady=(30, 5), padx=20)

lbl_subtitulo_menu = ctk.CTkLabel(
    frame_menu,
    text="Menu Principal • Etapa 4",
    font=ctk.CTkFont(size=12),
    text_color="gray70"
)
lbl_subtitulo_menu.pack(pady=(0, 20), padx=20)

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

# ------------------------------------------------------------------------------
# 5.2 Painel Direito de Conteúdo (frame_conteudo)
# ------------------------------------------------------------------------------

# Card de Resumo de Receitas
frame_resumo = ctk.CTkFrame(frame_conteudo, corner_radius=10)
frame_resumo.pack(fill="x", pady=(0, 15))

lbl_titulo_resumo = ctk.CTkLabel(
    frame_resumo,
    text="📌 RESUMO DE RECEITAS PREVISTAS",
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
lbl_valor_receita.pack(anchor="w", padx=20, pady=(0, 2))

lbl_subtitulo_resumo = ctk.CTkLabel(
    frame_resumo,
    text="Total acumulado: R$ 0.00 (0 fonte(s) registrada(s))",
    font=ctk.CTkFont(size=12),
    text_color="gray65"
)
lbl_subtitulo_resumo.pack(anchor="w", padx=20, pady=(0, 15))

# Painel Central com Título, Cabeçalho e Lista Rolável
frame_tabela = ctk.CTkFrame(frame_conteudo, corner_radius=10)
frame_tabela.pack(fill="both", expand=True)

lbl_titulo_painel = ctk.CTkLabel(
    frame_tabela,
    text="💵 LISTA DE RECEITAS REGISTRADAS",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color="gray75"
)
lbl_titulo_painel.pack(anchor="w", padx=20, pady=(15, 10))

# Faixa de Cabeçalho das Colunas
frame_cabecalho_lista = ctk.CTkFrame(frame_tabela, height=32, corner_radius=6, fg_color="gray20")
frame_cabecalho_lista.pack(fill="x", padx=20, pady=(0, 10))

lbl_colunas = ctk.CTkLabel(
    frame_cabecalho_lista,
    text="#     Descrição da Receita                                                Valor (R$)",
    font=ctk.CTkFont(family="monospace", size=12, weight="bold")
)
lbl_colunas.pack(anchor="w", padx=15, pady=5)

# Área Rolável onde as linhas são desenhadas dinamicamente
frame_lista_scroll = ctk.CTkScrollableFrame(frame_tabela, fg_color="transparent")
frame_lista_scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))

# Barra de Status no Rodapé
lbl_status = ctk.CTkLabel(
    frame_conteudo,
    text="Sistema iniciado com sucesso. Escolha uma opção no menu lateral.",
    font=ctk.CTkFont(size=13),
    anchor="w"
)
lbl_status.pack(fill="x", pady=(12, 0))

# ==============================================================================
# 6. INICIALIZAÇÃO DE ESTADO E LOOP DA APLICAÇÃO
# ==============================================================================
carregar_dados()
atualizar_card_resumo()
# Inicia exibindo a nova listagem de receitas implementada na Etapa 4
listar_receitas()

if __name__ == "__main__":
    janela.mainloop()
