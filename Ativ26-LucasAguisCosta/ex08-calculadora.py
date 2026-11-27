
import tkinter as tk
from tkinter import messagebox

def ler_numeros():
    try:
        n1 = float(entrada1.get().replace(",", "."))
        n2 = float(entrada2.get().replace(",", "."))
        return n1, n2

    except ValueError:
        messagebox.showerror(
            "Erro", "Digite dois números válidos!"
        )
        return None

def calcular(operacao):
    numeros = ler_numeros()

    if numeros is None:
        return

    n1, n2 = numeros

    if operacao == "+":
        resultado = n1 + n2

    elif operacao == "-":
        resultado = n1 - n2

    elif operacao == "*":
        resultado = n1 * n2

    elif operacao == "/":
        if n2 == 0:
            messagebox.showwarning(
                "Atenção", "Não é possível dividir por zero!"
            )
            return
        resultado = n1 / n2

    elif operacao == "**":
        resultado = n1 ** n2

    texto_resultado.config(
        text=f"Resultado: {resultado}"
    )

    ultima.config(
        text=f"Última conta: {n1} {operacao} {n2} = {resultado}"
    )

def limpar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    texto_resultado.config(text="Resultado:")
    ultima.config(text="Última conta:")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("350x350")
janela.resizable(False, False)

tk.Label(janela, text="Número 1:").pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Número 2:").pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack()

# Frame dos botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=15)

tk.Button(frame_botoes, text="+",
          width=5, command=lambda: calcular("+")).grid(row=0, column=0, padx=3)

tk.Button(frame_botoes, text="-",
          width=5, command=lambda: calcular("-")).grid(row=0, column=1, padx=3)

tk.Button(frame_botoes, text="×",
          width=5, command=lambda: calcular("*")).grid(row=0, column=2, padx=3)

tk.Button(frame_botoes, text="÷",
          width=5, command=lambda: calcular("/")).grid(row=0, column=3, padx=3)

tk.Button(frame_botoes, text="Potência",
          command=lambda: calcular("**")).grid(row=1, column=0, columnspan=4, pady=8)

# Frame do resultado
frame_resultado = tk.Frame(janela)
frame_resultado.pack(pady=10)

texto_resultado = tk.Label(
    frame_resultado,
    text="Resultado:",
    font=("Arial", 14, "bold")
)
texto_resultado.pack()

tk.Button(frame_resultado, text="Limpar",
          command=limpar).pack(pady=5)

ultima = tk.Label(janela, text="Última conta:")
ultima.pack(pady=5)

janela.mainloop()