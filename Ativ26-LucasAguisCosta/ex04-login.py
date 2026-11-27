import tkinter as tk
from tkinter import messagebox

tentativas = 0

def entrar():
    global tentativas

    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "" or senha == "":
        messagebox.showwarning(
            "Atenção", "Preencha todos os campos"
        )

    elif usuario == "aluno" and senha == "1234":
        messagebox.showinfo(
            "Login", "Bem-vindo(a), aluno!"
        )

    else:
        tentativas += 1

        messagebox.showerror(
            "Erro", "Usuário ou senha incorretos"
        )

        if tentativas == 3:
            messagebox.showwarning(
                "Atenção", "Número máximo de tentativas atingido!"
            )
            janela.destroy()

def limpar():
    entrada_usuario.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)

janela = tk.Tk()
janela.title("Tela de login")
janela.geometry("300x220")
janela.resizable(False, False)

tk.Label(janela, text="Usuário:").pack(pady=5)
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

tk.Label(janela, text="Senha:").pack(pady=5)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

tk.Button(janela, text="Entrar",
          command=entrar).pack(pady=10)

tk.Button(janela, text="Limpar",
          command=limpar).pack()

janela.mainloop()
