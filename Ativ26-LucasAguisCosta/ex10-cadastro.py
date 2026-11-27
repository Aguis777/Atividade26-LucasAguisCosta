import tkinter as tk
from tkinter import ttk, messagebox

def cadastrar():
    nome = entrada_nome.get().strip()
    turma = turma_escolhida.get()
    periodo_atual = periodo.get()

    # Verificar nome
    if nome == "":
        messagebox.showwarning(
            "Atenção", "Digite seu nome completo!"
        )
        return

    # Verificar turma
    if turma == "":
        messagebox.showwarning(
            "Atenção", "Selecione uma turma!"
        )
        return

    # Verificar período
    if periodo_atual == "":
        messagebox.showwarning(
            "Atenção", "Selecione um período!"
        )
        return

    # Verificar regras
    if not aceitou.get():
        messagebox.showwarning(
            "Atenção", "Você precisa aceitar as regras!"
        )
        return

    # Verificar interesses
    lista_interesses = [
        nome for nome, variavel in interesses
        if variavel.get()
    ]

    if len(lista_interesses) == 0:
        lista_interesses = ["Nenhum"]

    # Adicionar aluno na lista
    alunos.insert(tk.END, f"{nome} - {turma}")

    # Mostrar confirmação
    mensagem = (
        f"Nome: {nome}\n"
        f"Turma: {turma}\n"
        f"Período: {periodo_atual}\n"
        f"Interesses: {', '.join(lista_interesses)}"
    )

    messagebox.showinfo("Cadastro realizado!", mensagem)

def limpar():
    entrada_nome.delete(0, tk.END)
    turma_escolhida.set("")
    periodo.set("")

    for nome, variavel in interesses:
        variavel.set(False)

    aceitou.set(False)

def remover():
    selecionado = alunos.curselection()

    if not selecionado:
        messagebox.showinfo(
            "Atenção", "Selecione um aluno para remover!"
        )
    else:
        alunos.delete(selecionado[0])

def sair():
    resposta = messagebox.askyesno(
        "Sair", "Deseja realmente sair?"
    )

    if resposta:
        janela.destroy()

# Criar janela
janela = tk.Tk()
janela.title("Cadastro de alunos")
janela.geometry("450x680")
janela.resizable(False, False)

# Título
tk.Label(
    janela,
    text="FICHA DE CADASTRO",
    font=("Arial", 18, "bold")
).grid(row=0, column=0, columnspan=2, pady=15)

# Nome
tk.Label(janela, text="Nome completo:").grid(
    row=1, column=0, sticky="w", padx=15, pady=5
)

entrada_nome = tk.Entry(janela, width=30)
entrada_nome.grid(row=1, column=1, pady=5)

# Turma
tk.Label(janela, text="Turma:").grid(
    row=2, column=0, sticky="w", padx=15, pady=5
)

turma_escolhida = tk.StringVar()

turma = ttk.Combobox(
    janela,
    textvariable=turma_escolhida,
    values=["1MI", "1MA", "1ML"],
    state="readonly",
    width=27
)
turma.grid(row=2, column=1, pady=5)

# Período
tk.Label(janela, text="Período:").grid(
    row=3, column=0, sticky="w", padx=15, pady=5
)

periodo = tk.StringVar(value="")

tk.Radiobutton(
    janela, text="Manhã",
    variable=periodo, value="Manhã"
).grid(row=3, column=1, sticky="w")

tk.Radiobutton(
    janela, text="Tarde",
    variable=periodo, value="Tarde"
).grid(row=4, column=1, sticky="w")

tk.Radiobutton(
    janela, text="Noite",
    variable=periodo, value="Noite"
).grid(row=5, column=1, sticky="w")

# Interesses
tk.Label(janela, text="Interesses:").grid(
    row=6, column=0, sticky="w", padx=15, pady=5
)

programacao = tk.BooleanVar()
redes = tk.BooleanVar()
design = tk.BooleanVar()

interesses = [
    ("Programação", programacao),
    ("Redes", redes),
    ("Design", design)
]

for i, (nome, variavel) in enumerate(interesses):
    tk.Checkbutton(
        janela,
        text=nome,
        variable=variavel
    ).grid(row=6+i, column=1, sticky="w")

# Aceitar regras
aceitou = tk.BooleanVar()

tk.Checkbutton(
    janela,
    text="Li e aceito as regras",
    variable=aceitou
).grid(row=9, column=0, columnspan=2, pady=10)

# Botões
tk.Button(
    janela, text="Cadastrar",
    command=cadastrar, width=15
).grid(row=10, column=0, pady=5)

tk.Button(
    janela, text="Limpar",
    command=limpar, width=15
).grid(row=10, column=1, pady=5)

# Lista de alunos
tk.Label(
    janela,
    text="Alunos cadastrados:",
    font=("Arial", 11, "bold")
).grid(row=11, column=0, columnspan=2, pady=5)

alunos = tk.Listbox(janela, width=45, height=7)
alunos.grid(row=12, column=0, columnspan=2, pady=5)

# Remover aluno
tk.Button(
    janela,
    text="Remover selecionado",
    command=remover
).grid(row=13, column=0, columnspan=2, pady=5)

# Sair
tk.Button(
    janela,
    text="Sair",
    command=sair,
    width=15
).grid(row=14, column=0, columnspan=2, pady=10)

janela.mainloop()