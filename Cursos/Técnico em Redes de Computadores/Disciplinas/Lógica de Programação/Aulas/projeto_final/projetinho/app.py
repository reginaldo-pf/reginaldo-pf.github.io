import tkinter as tk
from tkinter import messagebox

# Estrutura de dados simples (lógica de programação pura)
transacoes = []

def adicionar_transacao():
    descricao = entry_desc.get().strip()
    valor_str = entry_val.get().strip()
    
    if not descricao or not valor_str:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        valor = float(valor_str)
        transacoes.append({"descricao": descricao, "valor": valor})
        atualizar_extrato()
        entry_desc.delete(0, tk.END)
        entry_val.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "O valor deve ser numérico.")

def atualizar_extrato():
    lista_transacoes.delete(0, tk.END)
    saldo = 0.0
    for item in transacoes:
        lista_transacoes.insert(tk.END, f"{item['descricao']}: R$ {item['valor']:.2f}")
        saldo += item["valor"]
    
    lbl_saldo.config(text=f"Saldo Total: R$ {saldo:.2f}")

# Janela principal
root = tk.Tk()
root.title("Controle Financeiro")
root.geometry("380x420")

# Entradas
tk.Label(root, text="Descrição:").pack(pady=(10, 0))
entry_desc = tk.Entry(root, width=30)
entry_desc.pack()

tk.Label(root, text="Valor (R$):").pack(pady=(5, 0))
entry_val = tk.Entry(root, width=30)
entry_val.pack()

# Botão de Ação
tk.Button(root, text="Adicionar Transação", command=adicionar_transacao).pack(pady=10)

# Visualização de dados
tk.Label(root, text="Extrato:").pack(pady=(10, 0))
lista_transacoes = tk.Listbox(root, width=35, height=8)
lista_transacoes.pack()

lbl_saldo = tk.Label(root, text="Saldo Total: R$ 0.00", font=("Arial", 11, "bold"))
lbl_saldo.pack(pady=15)

root.mainloop()