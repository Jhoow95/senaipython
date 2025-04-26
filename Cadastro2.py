import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

def atualizar_treeview():
    # Limpar treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Adicionar contatos ordenados por nome
    for id_contato, contato in sorted(contatos.items(), key=lambda item: item[1]['nome']):
        tree.insert("", tk.END, values=(
            id_contato,
            contato['nome'],
            contato['data_nascimento'],
            contato['whatsapp'],
            contato['linkedin'],
            contato['github']
        ))

def adicionar_contato():
    global id_counter
    nome = nome_entry.get().strip()
    data_nasc = data_entry.get().strip()
    whatsapp = whatsapp_entry.get().strip()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    
    if not nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
#    if data_nasc and not validar_data(data_nasc):
#        messagebox.showerror("Erro", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
#        return
    
    contatos[id_counter] = {
        "nome": nome,
        "data_nascimento": data_nasc if data_nasc else "Não informado",
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    id_counter += 1
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")

    limpar_campos()
    atualizar_treeview()

def limpar_campos():
    nome_entry.delete(0, tk.END)
    data_entry.delete(0, tk.END)
    whatsapp_entry.delete(0, tk.END)
    linkedin_entry.delete(0, tk.END)
    github_entry.delete(0, tk.END)

def preencher_campos_selecionados(event):
    item_selecionado = tree.selection()
    
    if item_selecionado:
        valores = tree.item(item_selecionado)['values']
        
        limpar_campos()
        
        nome_entry.insert(0, valores[1])
        data_entry.insert(0, valores[2])
        whatsapp_entry.insert(0, valores[3])
        linkedin_entry.insert(0, valores[4])
        github_entry.insert(0, valores[5])

def remover_contato():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um contato para remover!")
        return
    
    contato_id = tree.item(selected_item)['values'][0]
    
    if messagebox.askyesno("Confirmação", "Tem certeza que deseja remover este contato?"):
        del contatos[contato_id]  # Remove o contato do dicionário usando o ID como chave
        messagebox.showinfo("Sucesso", "Contato removido com sucesso!")
        limpar_campos()
        atualizar_treeview()

def localizar_contato():
    termo_busca = nome_entry.get().strip().lower()  # Pega o termo de busca do campo Nome
    
    if not termo_busca:
        messagebox.showwarning("Aviso", "Digite um nome para buscar!")
        return
    
    # Limpa qualquer seleção anterior
    for item in tree.selection():
        tree.selection_remove(item)
    
    encontrados = False
    
    # Percorre todos os itens na Treeview
    for item in tree.get_children():
        nome = tree.item(item)['values'][1].lower()  # Pega o nome do contato (índice 1)
        
        if termo_busca in nome:
            tree.selection_add(item)  # Seleciona o item encontrado
            tree.focus(item)
            tree.see(item)  # Rola a Treeview até o item
            encontrados = True
    
    if not encontrados:
        messagebox.showinfo("Busca", "Nenhum contato encontrado com esse nome.")
def atualizar_contato():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um contato para atualizar!")
        return
    
    # Pega os dados dos campos do formulário
    novo_nome = nome_entry.get().strip()
    nova_data = data_entry.get().strip()
    novo_whatsapp = whatsapp_entry.get().strip()
    novo_linkedin = linkedin_entry.get().strip()
    novo_github = github_entry.get().strip()
    
    if not novo_nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
    # Obtém o ID do contato selecionado
    contato_id = tree.item(selected_item)['values'][0]
    
    # Atualiza os dados no dicionário de contatos
    contatos[contato_id] = {
        "nome": novo_nome,
        "data_nascimento": nova_data if nova_data else "Não informado",
        "whatsapp": novo_whatsapp if novo_whatsapp else "Não informado",
        "linkedin": novo_linkedin if novo_linkedin else "Não informado",
        "github": novo_github if novo_github else "Não informado"
    }
    
    messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")
    atualizar_treeview()
    limpar_campos()

#CONFIGURAÇÃO INICIAL

root=tk.Tk() #JANELA
root.title("CONTACT SYSTEN")
root.geometry("800x600")

#BASE DE DADOS EM DICIONÁRIO
contatos = {} #DICIONÁRIO ALREY
id_counter = 1

# INTERFACE GRÁFICA
main_frame = tk.LabelFrame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# FRAME DE FORMULÁRIO
form_frame = tk.LabelFrame(main_frame, text="Dados do Contato", padx=10, pady=10)
form_frame.pack(fill=tk.X, pady=(0, 10))

# CAMPOS DO FORMULÁRIO
tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W)
nome_entry = tk.Entry(form_frame, width=40)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Data Nasc. (DD/MM/AAAA):").grid(row=1, column=0, sticky=tk.W)
data_entry = tk.Entry(form_frame, width=40)
data_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="WhatsApp:").grid(row=2, column=0, sticky=tk.W)
whatsapp_entry = tk.Entry(form_frame, width=40)
whatsapp_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="LinkedIn:").grid(row=3, column=0, sticky=tk.W)
linkedin_entry = tk.Entry(form_frame, width=40)
linkedin_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_frame, text="GitHub:").grid(row=4, column=0, sticky=tk.W)
github_entry = tk.Entry(form_frame, width=40)
github_entry.grid(row=4, column=1, padx=5, pady=5)

# FRAME DE BOTÕES
button_frame = tk.LabelFrame(main_frame)
button_frame.pack(fill=tk.X, pady=(0, 10))

tk.Button(button_frame, text="Adicionar",width=15, command=adicionar_contato).grid(row=0,column=0,padx=18)
tk.Button(button_frame, text="Atualizar",width=15, command=atualizar_contato).grid(row=0,column=1,padx=18)
tk.Button(button_frame, text="Excluir",width=15, command=remover_contato).grid(row=0,column=2,padx=18)
tk.Button(button_frame, text="Limpar",width=15, command=limpar_campos).grid(row=0,column=3,padx=18)
tk.Button(button_frame, text="Localizar",width=15, command=localizar_contato).grid(row=0,column=4,padx=18)

# TREEVIEW PARA EXIBIR OS CONTATOS
tree = ttk.Treeview(main_frame, columns=("ID", "Nome", "Nascimento", "WhatsApp", "LinkedIn", "GitHub"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Nascimento", text="Nascimento")
tree.heading("WhatsApp", text="WhatsApp")
tree.heading("LinkedIn", text="LinkedIn")
tree.heading("GitHub", text="GitHub")

tree.column("ID", width=50)
tree.column("Nome", width=150)
tree.column("Nascimento", width=100)
tree.column("WhatsApp", width=120)
tree.column("LinkedIn", width=150)
tree.column("GitHub", width=150)

tree.pack(fill=tk.BOTH, expand=True)

# BARRA DE ROLAGEM
scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# EVENTO DE SELEÇÃO NA TREEVIEW
tree.bind("<<TreeviewSelect>>",preencher_campos_selecionados) 

root.mainloop ()