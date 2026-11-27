import tkinter as tk
from tkinter import messagebox

def celsius_para_fahrenheit():
    try:
        celsius = float(entrada.get().replace(",", "."))
        fahrenheit = celsius * 9 / 5 + 32

        resultado.config(
            text=f"{celsius:.1f} °C = {fahrenheit:.1f} °F"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")

def fahrenheit_para_celsius():
    try:
        fahrenheit = float(entrada.get().replace(",", "."))
        celsius = (fahrenheit - 32) * 5 / 9

        resultado.config(
            text=f"{fahrenheit:.1f} °F = {celsius:.1f} °C"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")

def limpar():
    entrada.delete(0, tk.END)
    resultado.config(text="Resultado:")

janela = tk.Tk()
janela.title("Conversor de temperatura")
janela.geometry("350x220")
janela.resizable(False, False)

tk.Label(janela, text="Celsius ou Fahrenheit:").grid(
    row=0, column=0, padx=10, pady=15
)

entrada = tk.Entry(janela)
entrada.grid(row=0, column=1, padx=10)

botao1 = tk.Button(janela, text="Celsius para Fahrenheit",
                   command=celsius_para_fahrenheit)
botao1.grid(row=1, column=0, columnspan=2, pady=5)

botao2 = tk.Button(janela, text="Fahrenheit para Celsius",
                   command=fahrenheit_para_celsius)
botao2.grid(row=2, column=0, columnspan=2, pady=5)

resultado = tk.Label(janela, text="Resultado:",
                     font=("Arial", 12))
resultado.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(janela, text="Limpar",
          command=limpar).grid(row=4, column=0, columnspan=2)

janela.mainloop()