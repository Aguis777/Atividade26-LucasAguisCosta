import tkinter as tk
from tkinter import messagebox

contador = 0

def adicionar():
    global contador
    contador += 1
    atualizar()

    if contador == 10:
        messagebox.showinfo("Parabéns", "Você chegou a 10!")

def diminuir():
    global contador
    if contador > 0:
        contador -= 1
    atualizar()

def zerar():
    global contador
    contador = 0
    atualizar()

def atualizar():
    numero.config(text=str(contador))

    if contador >= 10:
        numero.config(fg="red")
    else:
        numero.config(fg="black")

janela = tk.Tk()
janela.title("Contador de cliques")
janela.geometry("300x250")
janela.resizable(False, False)

numero = tk.Label(janela, text="0",
                  font=("Arial", 45, "bold"))
numero.pack(pady=20)

botao_mais = tk.Button(janela, text="+1",
                       command=adicionar, width=10)
botao_mais.pack(pady=5)

botao_menos = tk.Button(janela, text="-1",
                        command=diminuir, width=10)
botao_menos.pack(pady=5)

botao_zerar = tk.Button(janela, text="Zerar",
                        command=zerar, width=10)
botao_zerar.pack(pady=5)

janela.mainloop()