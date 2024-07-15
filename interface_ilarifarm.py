from tkinter import * 
master = Tk() 
master.geometry("300x400") 
master.title('--ILARI FARM--')
master['bg'] = '#4EE8C4'

def Cadastro_cliente():
	janela = Toplevel(master)
	janela.geometry('300x400')
	janela['bg'] = '#4EE8C4'
	
	#titulo
	janela.texto = Label(janela, text = 'Cadastro dos clientes', foreground = 'white')
	janela.texto['font'] = ("Courier New", "17")
	janela.texto['bg'] = '#4EE8C4'
	janela.texto.pack()
	
	#Criação do Entry código
	janela.codigo_texto = Label(janela, text = 'Código', foreground='white')
	janela.codigo_texto.place(x=189, y=18)
	janela.codigo_texto['font'] = ("Courier New", "12")
	janela.codigo_texto['bg'] = '#4EE8C4'
	janela.codigo_texto.pack(pady=20)
	
	janela.codigo = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.codigo['font'] = ("Times New Roman TUR", "10")
	janela.codigo.pack()
	
	#Criação do Entry nome
	janela.nome_texto = Label(janela, text = 'Nome', foreground='white')
	janela.nome_texto.place(x=189, y=18)
	janela.nome_texto['font'] = ("Courier New", "12")
	janela.nome_texto['bg'] = '#4EE8C4'
	janela.nome_texto.pack(pady=20)
	
	janela.nome = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.nome['font'] = ("Times New Roman TUR", "10")
	janela.nome.pack()
	
	#Criação do Entry Endereço
	janela.endereco_texto = Label(janela, text = 'Endereço', foreground='white')
	janela.endereco_texto.place(x=189, y=18)
	janela.endereco_texto['font'] = ("Courier New", "12")
	janela.endereco_texto['bg'] = '#4EE8C4'
	janela.endereco_texto.pack(pady=20)
	
	janela.endereco = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.endereco['font'] = ("Times New Roman TUR", "10")
	janela.endereco.pack()
	
	#Criação do Entry Telefone
	janela.telefone_texto = Label(janela, text = 'Telefone', foreground='white')
	janela.telefone_texto.place(x=189, y=18)
	janela.telefone_texto['font'] = ("Courier New", "12")
	janela.telefone_texto['bg'] = '#4EE8C4'
	janela.telefone_texto.pack(pady=20)
	
	janela.telefone = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.telefone['font'] = ("Times New Roman TUR", "10")
	janela.telefone.pack()
		
	#Botão para cadastrar
	janela.bot_cadastro = Button(janela, text = 'Cadastrar', width = 32, height=0, borderwidth=2, relief="ridge", bg = 'white')
	janela.bot_cadastro['font'] = ("Times New Roman TUR", "10")
	janela.bot_cadastro.pack(pady = 40)

	
#criação do catálogo
def Catalogo():
	janela = Toplevel(master)
	janela.geometry('1000x1000')
	janela['bg'] = '#4EE8C4'
	
	#titulo
	janela.texto = Label(janela, text = 'Catálogo', foreground = 'white')
	janela.texto['font'] = ("Courier New", "19")
	janela.texto['bg'] = '#4EE8C4'
	janela.texto.pack()
	
	#Criação dos produtos
	janela.nome_produto = Label(janela, text = 'Produto 1', foreground='white')
	janela.nome_produto['font'] = ("Courier New", "12")
	janela.nome_produto['bg'] = '#4EE8C4'
	janela.nome_produto.pack(side = LEFT)
	
	#Criação do label código
	janela.codigo_texto = Label(janela, text = 'Código', foreground='white')
	janela.codigo_texto.place(x=189, y=18)
	janela.codigo_texto['font'] = ("Courier New", "12")
	janela.codigo_texto['bg'] = '#4EE8C4'
	janela.codigo_texto.pack(pady=20)
	
	#Criação do label descrição
	janela.descricao_texto = Label(janela, text = 'Descrição', foreground='white')
	janela.descricao_texto['font'] = ("Courier New", "12")
	janela.descricao_texto['bg'] = '#4EE8C4'
	janela.descricao_texto.pack(pady=20)
	
	

	
def Cadastro_produto():
	janela = Toplevel(master)
	janela.geometry('300x400')
	janela['bg'] = '#4EE8C4'
	
	#titulo
	janela.texto = Label(janela, text = 'Cadastro do Produto', foreground = 'white')
	janela.texto['font'] = ("Courier New", "19")
	janela.texto['bg'] = '#4EE8C4'
	janela.texto.pack()
	
	
	#Criação do Entry código
	janela.codigo_texto = Label(janela, text = 'Código', foreground='white')
	janela.codigo_texto.place(x=189, y=18)
	janela.codigo_texto['font'] = ("Courier New", "12")
	janela.codigo_texto['bg'] = '#4EE8C4'
	janela.codigo_texto.pack(pady=20)
	
	janela.codigo = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.codigo['font'] = ("Times New Roman TUR", "10")
	janela.codigo.pack()
	
	#Criação do Entry nome
	janela.nome_texto = Label(janela, text = 'Nome', foreground= 'white')
	janela.nome_texto['font'] = ("Courier New", "12")
	janela.nome_texto['bg'] = '#4EE8C4'
	janela.nome_texto.pack(pady=20)
	
	janela.nome = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.nome['font'] = ("Times New Roman TUR", "10")
	janela.nome.pack()
	
	
	#Criação do Entry descrição
	janela.descricao_texto = Label(janela, text = 'Descrição', foreground='white')
	janela.descricao_texto['font'] = ("Courier New", "12")
	janela.descricao_texto['bg'] = '#4EE8C4'
	janela.descricao_texto.pack(pady=20)
	
	janela.descricao = Entry(janela, width = 41, borderwidth=2, relief="ridge")
	janela.nome['font'] = ("Times New Roman TUR", "10")
	janela.descricao.pack()
	
	#Botão para cadastrar
	janela.bot_cadastro = Button(janela, text = 'Cadastrar', width = 32, height=0, borderwidth=2, relief="ridge", bg = 'white')
	janela.bot_cadastro['font'] = ("Times New Roman TUR", "10")
	janela.bot_cadastro.pack(pady = 40)

	
def Altera():
	janela = Toplevel(master)
	janela.geometry('300x400')
	janela['bg'] = '#4EE8C4'
	
	janela.titulo = Label(janela, text = 'Alterar', foreground = 'white')
	janela.titulo['font'] = ("Courier New", "19")
	janela.titulo['bg'] = '#4EE8C4'
	janela.titulo.pack()
	

	#Criação do Entry código
	janela.codigo_texto = Label(janela, text = 'Código', foreground = 'white')
	janela.codigo_texto['bg'] = '#4EE8C4'
	janela.codigo_texto['font'] = ("Courier New", "12")
	janela.codigo_texto.pack(pady = 20)
	
	janela.codigo = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.codigo['font'] = ("Times New Roman TUR", "10")
	janela.codigo.pack()
	
	#Criação da Combo box
	janela.alteracao_texto = Label(janela, text = 'Campo para alteração', foreground = 'white')
	janela.alteracao_texto['bg'] = '#4EE8C4'
	janela.alteracao_texto['font'] = ("Courier New", "12")
	janela.alteracao_texto.pack(pady = 20)
	'''
	janela.alteracao = Combobox(janela)
	janela.alteracao.pack()
	'''
	#Criação do botão Alterar
	janela.bot_alterar = Button(janela, text = 'Alterar', width = 32, height=0, borderwidth=2, relief="ridge", bg = 'white')
	janela.bot_alterar['font'] = ("Times New Roman TUR", "10")
	janela.bot_alterar.pack(pady = 40)
	

def Exclui():
	janela = Toplevel(master)
	janela.geometry('300x400')
	janela['bg'] = '#4EE8C4'
	
	#titulo
	janela.texto = Label(janela, text = 'Excluir', foreground = 'white')
	janela.texto['font'] = ("Courier New", "19")
	janela.texto['bg'] = '#4EE8C4'
	janela.texto.pack()
	
	#Criação do Entry código
	janela.codigo_texto = Label(janela, text = 'Código', foreground ='white')
	janela.codigo_texto['bg'] = '#4EE8C4'
	janela.codigo_texto['font'] = ("Courier New", "12")
	janela.codigo_texto.pack(pady = 20)

	janela.codigo = Entry(janela, width = 35, borderwidth=2, relief="ridge")
	janela.codigo['font'] = ("Times New Roman TUR", "10")
	janela.codigo.pack()
	
	#Criação do botão Excluir
	janela.bot_excluir = Button(janela, text = 'Excluir', width = 32, height=0, borderwidth=2, relief="ridge", bg = 'white')
	janela.bot_excluir['font'] = ("Times New Roman TUR", "10")
	janela.bot_excluir.pack(pady = 80)
	
#side = posicao; pady = espaçamento de cima e de baixo
#Criação do menu
# criação do container 1


#Adicionando o título
titulo = Label(master,text ="Ilari Farm", foreground = 'white')
titulo['font'] = ("Courier New", "30")
titulo['bg'] = '#4EE8C4'
titulo.pack()

#Botão Catálogo
catalogo = Button(master,text='Catálogo', width=32, command = Catalogo, height=0, borderwidth=2, relief="ridge", bg = 'white')
catalogo['font'] = ("Times New Roman TUR", "10")
catalogo.place(x=91, y=45)
catalogo.pack(pady = 9) 

#Botão cadastrar Cliente
cadastrar_cliente = Button(master, text = 'Cadastrar Cliente', width = 32, height=0, borderwidth=2, relief="ridge", bg = 'white', command = Cadastro_cliente)
cadastrar_cliente.place(x = 116, y = 12)
cadastrar_cliente['font'] = ("Times New Roman TUR", "10")
cadastrar_cliente.pack()

#entrada do codigo do funcionário
func = Label(text="Acesso dos funcionários:", foreground = 'white')
func['font'] = ("Courier New", "12")
func['bg'] = '#4EE8C4'
func.pack(pady = 30)

#Botão Cadastrar Produto
cadastrar_produto = Button(master,text = 'Cadastrar Produto', width = 32, command = Cadastro_produto, height=0, borderwidth=2, relief="ridge", bg = 'white')
cadastrar_produto.place(x=159, y=168)
cadastrar_produto['font'] = ("Times New Roman TUR", "10")
cadastrar_produto.pack()

#Botão alterar
alterar = Button(master, text ="Alterar", width=32, command = Altera, height=0, borderwidth=2, relief="ridge", bg = 'white')
alterar['font'] = ("Times New Roman TUR", "10")
alterar.pack(pady = 4)

#Botão excluir
excluir = Button(master, text="Excluir", width = 32, command = Exclui, height=0, borderwidth=2, relief="ridge", bg = 'white')
excluir['font'] = ("Times New Roman TUR", "10")
excluir.pack(pady = 2)

#criando caixa de texto
codigo = Label(master,text = 'Código', foreground='white')
codigo['font'] = ("Courier New", "12")
codigo['bg'] = '#4EE8C4'
codigo.pack(pady = 10)
escreve_codigo = Entry(width = 35, borderwidth=2, relief="ridge")
escreve_codigo['font'] = ("Times New Roman TUR", "10")
escreve_codigo.pack()

master.mainloop()
