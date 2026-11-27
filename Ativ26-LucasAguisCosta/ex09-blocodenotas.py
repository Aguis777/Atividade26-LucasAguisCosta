
import tkinter as tk
from tkinter import messagebox

def contar():
    conteudo = texto.get("1.0", "end-1c")

    if conteudo.strip() == "":
        messagebox.showwarning(
            "Atenção", "Não há nada escrito!"
        )
        return

    palavras = len(conteudo.split())
    caracteres = len(conteudo)

    messagebox.showinfo(
        "Contagem",
        f"Palavras: {palavras}\nCaracteres: {caracteres}"
    )

    total.config(text=f"Caracteres: {caracteres}")

def maiusculas():
    conteudo = texto.get("1.0", "end-1c")

    if conteudo.strip() == "":
        messagebox.showwarning(
            "Atenção", "Não há nada escrito!"
        )
        return

    texto.delete("1.0", tk.END)
    texto.insert("1.0", conteudo.upper())

    total.config(text=f"Caracteres: {len(conteudo)}")

def limpar():
    resposta = messagebox.askyesno(
        "Confirmar", "Deseja apagar tudo?"
    )

    if resposta:
        texto.delete("1.0", tk.END)
        total.config(text="Caracteres: 0")

def sair():
    resposta = messagebox.askyesno(
        "Sair", "Deseja realmente sair?"
    )

    if resposta:
        janela.destroy()

janela = tk.Tk()
janela.title("Bloco de notas")
janela.geometry("450x400")
janela.resizable(False, False)

tk.Label(janela, text="Meu bloco de notas",
         font=("Arial", 16, "bold")).pack(pady=10)

texto = tk.Text(janela, width=50, height=12)
texto.pack(padx=10, pady=5)

tk.Button(janela, text="Contar palavras",
          command=contar).pack(pady=3)

tk.Button(janela, text="Maiúsculas",
          command=maiusculas).pack(pady=3)

tk.Button(janela, text="Limpar",
          command=limpar).pack(pady=3)

tk.Button(janela, text="Sair",
          command=sair).pack(pady=3)

total = tk.Label(janela, text="Caracteres: 0")
total.pack(pady=5)

janela.mainloop()
