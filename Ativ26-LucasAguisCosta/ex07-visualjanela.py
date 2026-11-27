import tkinter as tk

def mudar_visual():
    cor = cor_escolhida.get()
    tamanho = tamanho_escolhido.get()

    janela.config(bg=cor)

    texto.config(
        bg=cor,
        font=("Arial", tamanho, "bold" if negrito.get() else "normal")
    )

    informacao.config(
        text=f"Cor: {cor} | Letra: {tamanho}",
        bg=cor
    )

def restaurar():
    cor_escolhida.set("lightblue")
    tamanho_escolhido.set(16)
    negrito.set(False)
    mudar_visual()

janela = tk.Tk()
janela.title("Mudando o visual")
janela.geometry("400x450")
janela.resizable(False, False)

cor_escolhida = tk.StringVar(value="lightblue")
tamanho_escolhido = tk.IntVar(value=16)
negrito = tk.BooleanVar(value=False)

texto = tk.Label(
    janela,
    text="Este é o meu texto",
    font=("Arial", 16),
    bg="lightblue"
)
texto.pack(pady=20)

tk.Label(janela, text="Escolha a cor:").pack()

cores = [
    ("Azul claro", "lightblue"),
    ("Verde claro", "lightgreen"),
    ("Amarelo", "lightyellow"),
    ("Rosa", "pink")
]

for nome, cor in cores:
    tk.Radiobutton(
        janela,
        text=nome,
        variable=cor_escolhida,
        value=cor,
        command=mudar_visual
    ).pack()

tk.Label(janela, text="Tamanho da letra:").pack(pady=10)

tamanhos = [
    ("Pequena (12)", 12),
    ("Média (16)", 16),
    ("Grande (22)", 22)
]

for nome, tamanho in tamanhos:
    tk.Radiobutton(
        janela,
        text=nome,
        variable=tamanho_escolhido,
        value=tamanho,
        command=mudar_visual
    ).pack()

tk.Checkbutton(
    janela,
    text="Negrito",
    variable=negrito,
    command=mudar_visual
).pack(pady=10)

informacao = tk.Label(janela, text="Cor: lightblue | Letra: 16")
informacao.pack(pady=5)

tk.Button(janela, text="Restaurar",
          command=restaurar).pack(pady=10)

janela.mainloop()