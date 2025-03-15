import tkinter as tk
from tkinter import messagebox
from unittest import result

def Somar():
    numA = float(entryNum1.get())
    numB = float(entryNum2.get())
    resultado = numA + numB
    messagebox.showinfo("Adição",f"A soma de {numA} e {numB} é {resultado}")

janelaConta = tk.Tk()
janelaConta.title("Minha Calculadora")
janelaConta.geometry("800x600")

labelNum1 =tk.Label(janelaConta,text="Primeiro Número")
labelNum1.pack(padx=5,pady=5)
entryNum1 = tk.Entry(janelaConta)
entryNum1.pack(padx=5,pady=5)

labelNum2 =tk.Label(janelaConta,text="Segundo Número")
labelNum2.pack(padx=5,pady=5)
entryNum2 = tk.Entry(janelaConta)
entryNum2.pack(padx=5,pady=5)

buttonAdicao = tk.Button(janelaConta,text="Adição", command=Somar)
buttonAdicao.pack(padx=5,pady=5)

buttonSubtracao = tk.Button(janelaConta,text="Subtração")
buttonSubtracao.pack(padx=5,pady=5)

buttonMult = tk.Button(janelaConta,text="Multipliacação")
buttonMult.pack(padx=5,pady=5)

buttonDivisao = tk.Button(janelaConta,text="Divisão")
buttonDivisao.pack(padx=5,pady=5)

janelaConta.mainloop()