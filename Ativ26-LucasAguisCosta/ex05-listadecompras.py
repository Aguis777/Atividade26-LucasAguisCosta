import tkinter as tk
from tkinter import messagebox

def atualizar_total():
    total.config(text=f"Itens: {lista.size()}")

def adicionar():
    item = entrada.get().strip()

    if item == "":
        messagebox.showwarning(
            "Atenção", "Digite um item!"
        )

    elif item in lista.get(0, tk.END):
        messagebox.showwarning(
            "Atenção", "Esse item já está na lista!"
        )

    else:
        lista.insert(tk.END, item)
        entrada.delete(0, tk.END)

    atualizar_total()

def remover():
    selecionado = lista.curselection()

    if not selecionado:
        messagebox.showinfo(
            "Atenção", "Selecione um item para remover!"
        )
    else:
        lista.delete(selecionado[0])

    atualizar_total()

def limpar():
    resposta = messagebox.askyesno(
        "Confirmar", "Deseja apagar todos os itens?"
    )

    if resposta:
        lista.delete(0, tk.END)

    atualizar_total()

janela = tk.Tk()
janela.title("Lista de compras")
janela.geometry("350x400")
janela.resizable(False, False)

tk.Label(janela, text="Digite um item:").pack(pady=5)

entrada = tk.Entry(janela, width=30)
entrada.pack()

tk.Button(janela, text="Adicionar",
          command=adicionar).pack(pady=5)

lista = tk.Listbox(janela, width=35, height=12)
lista.pack(pady=10)

total = tk.Label(janela, text="Itens: 0",
                 font=("Arial", 12, "bold"))
total.pack(pady=5)

tk.Button(janela, text="Remover selecionado",
          command=remover).pack(pady=5)

tk.Button(janela, text="Limpar lista",
          command=limpar).pack(pady=5)

janela.mainloop()
