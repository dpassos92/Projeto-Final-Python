#importações
from tkinter import *
from tkinter import Tk, ttk, messagebox
from classes.janelas.janela_registo import JanelaRegisto
from classes.janelas.janela_login import JanelaLogin
import sqlite3
from classes.janelas.janela_inserir_filme import JanelaInserirFilme

#classe da janela principal
class JanelaPrincipal:
    def __init__(self):

        #criar a janela principal
        self.janela_principal = Tk() #cria a janela
        self.janela_principal.title('Sistema de Gestão de Produtos') #muda o titulo
        self.janela_principal.configure(bg='#f0f0f0') #altera a cor de fundo

        #configuração do texto de boas vindas
        self.boas_vindas_lbl = Label(self.janela_principal, text='Sistema de Gestão de Produtos', font='Arial 20',
                                     bg='#f0f0f0', fg='#333333')
        self.boas_vindas_lbl.grid(row=0, column=1, columnspan=1, pady=20)
        
        #configuração do botão de registo
        self.registar_btn = Button(self.janela_principal, text='Registar', font='Arial 14', command=self.abrir_janela_registo) #falta command
        self.registar_btn.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky='NSEW')

        #configuração do botão de login
        self.login_btn = Button(self.janela_principal, text='Login', font='Arial 14', command=self.abrir_janela_login) #falta command
        self.login_btn.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky='NSEW')

        #configuração do botão de sair
        self.sair_btn = Button(self.janela_principal, text='Sair', font='Arial 14', command=self.janela_principal.destroy)
        self.sair_btn.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky='NSEW')


    def abrir_janela_registo(self):
        JanelaRegisto()

    def abrir_janela_login(self):
        JanelaLogin(janela_principal=self)

    
    #definir a posição no ecra
    def calcular_posicao(self, largura_janela=400, altura_janela=300):

        #obter largura e altura do ecrã
        largura_ecra = self.janela_principal.winfo_screenwidth()
        altura_ecra = self.janela_principal.winfo_screenheight()

        #calcular a posição x e y
        x = (largura_ecra // 2) - (largura_janela // 2)
        y = (altura_ecra // 2) - (altura_janela // 2)

        #definir a posição da janela
        return f'{largura_janela}x{altura_janela}+{x}+{y}'


    #Definir a janela de menu após login
    def abrir_janela_menu(self):
        for widget in self.janela_principal.winfo_children():
            widget.destroy()

        self.janela_principal.title("Sistema de Gestão de Produtos")  # Título da janela
        self.janela_principal.iconbitmap("assets/icon/icon.ico")  # Ícone da janela
        self.janela_principal.configure(bg="#f0f0f0")  # Cor de fundo da janela
        self.janela_principal.geometry(self.calcular_posicao())  # Posição da janela no ecrã
        self.janela_principal.state('zoomed')  # Maximizar a janela

        Label(self.janela_principal, text="Nome do Produto: ", font="Arial 16", fg="#333333", bg="#f0f0f0").grid(row=0,column=2,padx=10,pady=10,sticky="W")
        nome_produto = Entry(self.janela_principal, font="Arial 16")
        nome_produto.grid(row=0, column=3, padx=10, pady=10, sticky="W")

        Label(self.janela_principal, text="Autor: ", font="Arial 16", fg="#333333", bg="#f0f0f0").grid(row=0, column=4,padx=10, pady=10,sticky="W")
        autor_produto = Entry(self.janela_principal, font="Arial 16")
        autor_produto.grid(row=0, column=5, padx=10, pady=10, sticky="W")

        Label(self.janela_principal, text="Ano: ", font="Arial 16", fg="#333333", bg="#f0f0f0").grid(row=0, column=6,padx=10, pady=10,sticky="W")
        ano_produto = Entry(self.janela_principal, font="Arial 16")
        ano_produto.grid(row=0, column=7, padx=10, pady=10, sticky="W")

        Label(self.janela_principal, text="Sistema de Gestão de Stock", font="Arial 16", fg="#333333",
            bg="#f0f0f0").grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky="NSEW")

        self.style = ttk.Style(self.janela_principal)
        self.treeeview = ttk.Treeview(self.janela_principal, style="mystyle.Treeview",columns=("id", "titulo", "autor", "preco", "quantidade"), show="headings")
        self.style.theme_use("default")
        self.style.configure("mystyle.Treeview", font='Arial, 14', rowheight=25)

        # Configuração da tabela de exibição dos produtos
        self.treeeview.heading("id", text="Id")
        self.treeeview.heading("titulo", text="Título")
        self.treeeview.heading("autor", text="Autor")
        self.treeeview.heading("preco", text="Preço")
        self.treeeview.heading("quantidade", text="Quantidade")
        self.treeeview.column("#0", width=0, stretch=NO)
        self.treeeview.column("id", anchor=CENTER, width=100)
        self.treeeview.column("titulo", anchor=CENTER, width=300)
        self.treeeview.column("autor", anchor=CENTER, width=200)
        self.treeeview.column("preco", anchor=CENTER, width=100)
        self.treeeview.column("quantidade", anchor=CENTER, width=100)

        self.treeeview.grid(row=3, column=0, columnspan=10, sticky="NSEW")
        self.janela_principal.grid_columnconfigure(0, weight=1)

        self.mostrar_livros()

        self.treeeview.bind("<Double-1>", self.editar_livro)

        self.botao_novo_produto = Button(self.janela_principal, text="Novo Produto", font="Arial 14",command=self.registar_produto_livro)
        self.botao_novo_produto.grid(row=4, column=0, columnspan=6, sticky="NSEW")

        self.botao_apagar_produto = Button(self.janela_principal, text="Apagar", font="Arial 14",command=self.apagar_livro)
        self.botao_apagar_produto.grid(row=4, column=6, columnspan=5, sticky="NSEW")

        self.menu_barra = Menu(self.janela_principal)
        self.janela_principal.configure(menu=self.menu_barra)

        self.menu_ficheiro = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Ficheiro", menu=self.menu_ficheiro)
        self.menu_ficheiro.add_command(label="Novo", command=self.registar_produto)
        self.menu_ficheiro.add_command(label="Sair", command=self.janela_principal.destroy)

        nome_produto.bind('<KeyRelease>', lambda e: self.filtrar_dados(nome_produto))
        autor_produto.bind('<KeyRelease>', lambda e: self.filtrar_dados(autor_produto))
        ano_produto.bind('<KeyRelease>', lambda e: self.filtrar_dados(ano_produto))


    def apagar_livro(self):
            
            item_selecionado = self.treeeview.selection()[0]
    
            valores_selecionados = self.treeeview.item(item_selecionado)["values"]
    
            conn = sqlite3.connect("stock.db")
            cursor = conn.cursor()
    
            cursor.execute("DELETE FROM stock WHERE id = ?", (valores_selecionados[0],))
    
            conn.commit()
            conn.close()
    
            self.mostrar_livros()
    
            messagebox.showinfo("Sucesso", "Produto apagado com sucesso!")

    def editar_livro(self, event):

        item_selecionado = self.treeeview.selection()[0]

        valores_selecionados = self.treeeview.item(item_selecionado)["values"]

        self.janela_edicao = Toplevel(self.janela_principal)
        self.janela_edicao.title("Editar livro")
        self.janela_edicao.iconbitmap("assets/icon/icon.ico")
        self.janela_edicao.configure(bg="#f0f0f0")
        self.janela_edicao.geometry(self.calcular_posicao(400, 350))

        estilo_borda = {'borderwidth': 2, 'relief': 'groove'}

        Label(self.janela_edicao, text="Editar Produto", font="Arial 20", fg="#333333", bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

        Label(self.janela_edicao, text="Nome do Produto:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.nome_produto_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[1]))
        self.nome_produto_editado.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_edicao, text="Descrição do Produto:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.descricao_produto_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[2]))
        self.descricao_produto_editado.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_edicao, text="Preço do Produto:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.preco_produto_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[3]))
        self.preco_produto_editado.grid(row=3, column=1, padx=10, pady=10, sticky="W")


        def guardar_edicao():
            # Obter os valores dos campos de entrada
            novo_nome = self.nome_produto_editado.get()
            novo_descricao = self.descricao_produto_editado.get()
            novo_preco = self.preco_produto_editado.get()

            # Verificar se todos os campos foram preenchidos
            if novo_nome and novo_descricao and novo_preco:

                # Conectar à base de dados
                conn = sqlite3.connect("stock.db")
                cursor = conn.cursor()

                self.treeeview.item(item_selecionado, values=(valores_selecionados[0], novo_nome, novo_descricao, novo_preco))


                # Inserir os dados na tabela
                cursor.execute("UPDATE stock SET produto = ?, descricao = ?, preco = ? WHERE id = ?", (novo_nome, novo_descricao, novo_preco, valores_selecionados[0]))

                # Confirmar a inserção dos dados
                conn.commit()

                # Fechar a conexão com a base de dados
                conn.close()

                self.mostrar_produtos()

                # Exibir uma mensagem de sucesso
                messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
            else:
                # Exibir uma mensagem de erro se algum campo estiver vazio
                messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

        self.botao_guardar_produto = Button(self.janela_edicao, text="Guardar Edição", font="Arial 12", command=guardar_edicao)
        self.botao_guardar_produto.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

        self.cancelar_edicao = Button(self.janela_edicao, text="Cancelar", font="Arial 12", command=self.janela_edicao.destroy)
        self.cancelar_edicao.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

    def registar_produto_livro(self):
        #criar nova janela para registar os produtos
        self.janela_registo_livro = Toplevel()
        self.janela_registo_livro.title("Registar Livro")
        self.janela_registo_livro.iconbitmap("assets/icon/icon.ico")
        self.janela_registo_livro.configure(bg="#f0f0f0")
        self.janela_registo_livro.geometry(self.calcular_posicao(400, 350))

        estilo_borda = {'borderwidth': 2, 'relief': 'groove'}

        Label(self.janela_registo_livro, text="Sistema de Gestão de Produtos", font="Arial 20", fg="#333333", bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

        Label(self.janela_registo_livro, text="Título:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.titulo_livro_entry = Entry(self.janela_registo_livro, font="Arial 12", **estilo_borda)
        self.titulo_livro_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_livro, text="Autor:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.autor_livro_entry = Entry(self.janela_registo_livro, font="Arial 12", **estilo_borda)
        self.autor_livro_entry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_livro, text="Ano:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.ano_livro_entry = Entry(self.janela_registo_livro, font="Arial 12", **estilo_borda)
        self.ano_livro_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_livro, text="Género:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.genero_livro_entry = Entry(self.janela_registo_livro, font="Arial 12", **estilo_borda)
        self.genero_livro_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_livro, text="Quantidade:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.quantidade_livro_entry = Entry(self.janela_registo_livro, font="Arial 12", **estilo_borda)
        self.quantidade_livro_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_livro, text="Preço:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.preco_livro_entry = Entry(self.janela_registo_livro, font="Arial 12", **estilo_borda)
        self.preco_livro_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        self.botao_gravar_edicao = Button(self.janela_registo_livro, text="Guardar", font="Arial 12", command=self.guardar_livro)
        self.botao_gravar_edicao.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

        self.cancelar = Button(self.janela_registo_livro, text="Cancelar", font="Arial 12", command=self.janela_registo_livro.destroy)
        self.cancelar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")


    def guardar_livro(self):
    
        # Obter os valores dos campos de entrada
        titulo = self.titulo_livro_entry.get()
        autor = self.autor_livro_entry.get()
        ano= self.ano_livro_entry.get()
        genero = self.genero_livro_entry.get()
        quantidade = self.quantidade_livro_entry.get()
        preco = self.preco_livro_entry.get()

        # Verificar se todos os campos foram preenchidos
        if titulo and autor and ano and genero and quantidade and preco:

            # Conectar à base de dados
            conn = sqlite3.connect("stock.db")
            cursor = conn.cursor()

            # Inserir os dados na tabela
            cursor.execute("INSERT INTO livros (titulo, autor, ano, genero, quantidade, preco) VALUES (?, ?, ?, ?, ?, ?)", (titulo, autor, ano, genero, quantidade, preco))

            # Confirmar a inserção dos dados
            conn.commit()

            # Fechar a conexão com a base de dados
            conn.close()

            # Limpar os campos de entrada
            self.titulo_livro_entry.delete(0, END)
            self.autor_livro_entry.delete(0, END)
            self.ano_livro_entry.delete(0, END)
            self.genero_livro_entry.delete(0, END)
            self.quantidade_livro_entry.delete(0, END)
            self.preco_livro_entry.delete(0, END)

            self.mostrar_livros()

            # Exibir uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Produto guardado com sucesso!")
        else:
            # Exibir uma mensagem de erro se algum campo estiver vazio
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def mostrar_livros(self):
            
        # Limpar os dados da tabela
        for i in self.treeeview.get_children():
            self.treeeview.delete(i)

        # Conectar à base de dados
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()

        # Obter os dados da tabela
        cursor.execute("SELECT * FROM livros")
        produtos = cursor.fetchall()

        # Inserir os dados na tabela
        for produto in produtos:
            self.treeeview.insert("", "end", values=produto)

        # Fechar a conexão com a base de dados
        conn.close()

    def filtrar_dados_livros(self, titulo_livro):
        if not titulo_livro.get():
            self.mostrar_livros()
            return
        
        sql = "SELECT * FROM stock"
        params = []
        
        if titulo_livro.get():
            sql += " WHERE produto LIKE ?"
            params.append("%" + titulo_livro.get() + "%")
        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3]))        
        
    def limparDados(self):
        for i in self.treeeview.get_children():
            self.treeeview.delete(i)
    


        
