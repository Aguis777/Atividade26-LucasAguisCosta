import tkinter as tk

janela = tk.Tk()
janela.title("Cartão de visita")
janela.geometry("360x200")
janela.resizable(False, False)
janela.config(bg="#eeeeee")

# Faixa superior
faixa = tk.Frame(janela, bg="#1e3a8a", height=45)
faixa.pack(fill="x")

titulo = tk.Label(faixa, text="MEU CARTÃO DE VISITA",
                  font=("Arial", 12, "bold"),
                  fg="white", bg="#1e3a8a")
titulo.pack(pady=10)

# Informações pessoais
nome = tk.Label(janela, text="Lucas Aguis Costa",
                font=("Arial", 18, "bold"),
                fg="darkblue", bg="#eeeeee")
nome.place(x=65, y=65)

curso = tk.Label(janela, text="Curso: Informática",
                 font=("Arial", 12),
                 fg="green", bg="#eeeeee")
curso.place(x=110, y=110)

escola = tk.Label(janela, text="Etec Alberto Santos Dumont",
                  font=("Arial", 10),
                  fg="red", bg="#eeeeee")
escola.place(x=75, y=140)

# Botão fechar
botao = tk.Button(janela, text="Fechar",
                  command=janela.destroy)
botao.place(x=150, y=165)

janela.mainloop()