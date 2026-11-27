import tkinter as tk
from tkinter import messagebox

def calcular():
    total = 0
    selecionados = 0

    if hamburguer.get():
        total += 18
        selecionados += 1

    if batata.get():
        total += 10
        selecionados += 1

    if refrigerante.get():
        total += 6
        selecionados += 1

    if suco.get():
        total += 7
        selecionados += 1

    if selecionados == 0:
        messagebox.showwarning(
            "Atenção", "Selecione pelo menos um item!"
        )
        return

    if gorjeta.get():
        total += total * 0.10

    resultado.config(
        text=f"Total: R$ {total:.2f}".replace(".", ",")
    )

def novo_pedido():
    hamburguer.set(False)
    batata.set(False)
    refrigerante.set(False)
    suco.set(False)
    gorjeta.set(False)

    resultado.config(text="Total: R$ 0,00")

janela = tk.Tk()
janela.title("Pedido de lanchonete")
janela.geometry("350x350")
janela.resizable(False, False)

tk.Label(janela, text="CARDÁPIO",
         font=("Arial", 16, "bold")).pack(pady=10)

hamburguer = tk.BooleanVar()
batata = tk.BooleanVar()
refrigerante = tk.BooleanVar()
suco = tk.BooleanVar()
gorjeta = tk.BooleanVar()

tk.Checkbutton(janela, text="Hambúrguer - R$ 18,00",
               variable=hamburguer).pack(anchor="w", padx=50)

tk.Checkbutton(janela, text="Batata frita - R$ 10,00",
               variable=batata).pack(anchor="w", padx=50)

tk.Checkbutton(janela, text="Refrigerante - R$ 6,00",
               variable=refrigerante).pack(anchor="w", padx=50)

tk.Checkbutton(janela, text="Suco - R$ 7,00",
               variable=suco).pack(anchor="w", padx=50)

tk.Checkbutton(janela, text="Adicionar gorjeta de 10%",
               variable=gorjeta).pack(pady=10)

tk.Button(janela, text="Calcular total",
          command=calcular).pack(pady=5)

resultado = tk.Label(janela, text="Total: R$ 0,00",
                     font=("Arial", 14, "bold"))
resultado.pack(pady=10)

tk.Button(janela, text="Novo pedido",
          command=novo_pedido).pack()

janela.mainloop()