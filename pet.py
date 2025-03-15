import tkinter 
from tkinter import messagebox

def gravarPet():
    nomeTutor = entryNometutor.get()
    nomePet = entryNomePet.get()
    messagebox.showinfo("Atenção",f" Pet:  {nomePet}  \nTutor: {nomeTutor}")



janela = tkinter.Tk ("Cadastro de Cliente")
janela.geometry("800x600")
janela.title("Cadastro de Pet")

labelNometutor = tkinter.Label(janela,text = "Nome do Tutor")
labelNometutor.pack(padx=5, pady=5)
entryNometutor = tkinter.Entry(janela,width=100)
entryNometutor.pack(padx=5,pady=5)

labelNomePet= tkinter.Label(janela,text = "Nome do Pet")
labelNomePet.pack(padx=5, pady=5)
entryNomePet = tkinter.Entry(janela,width=100)
entryNomePet.pack(padx=5,pady=5)

buttonGravar = tkinter.Button (janela,text = "Gravar", width=100,command=gravarPet )
buttonGravar.pack(padx=5, pady=100)

janela.mainloop()
