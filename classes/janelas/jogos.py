#importações
from tkinter import *
from tkinter import Tk, ttk, messagebox
from classes.janelas.janela_registo import JanelaRegisto
from classes.janelas.janela_login import JanelaLogin
import sqlite3


class CategoriaJogo:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal

    def abrir_janela_menu(self):


        for widget in self.janela_principal.winfo_children():
            widget.destroy()

        self.janela_principal.title("Sistema de Gestão de Produtos")  # Título da janela
        self.janela_principal.iconbitmap("assets/icon/icon.ico")  # Ícone da janela
        self.janela_principal.configure(bg="#f0f0f0")  # Cor de fundo da janela
        self.janela_principal.geometry(self.calcular_posicao())  # Posição da janela no ecrã
        self.janela_principal.state('zoomed')  # Maximizar a janela

        Label(self.janela_principal, text="Título: ", font="Arial 16", fg="#333333", bg="#f0f0f0").grid(row=0,column=1,padx=10,pady=10,sticky="W")
        nome_produto = Entry(self.janela_principal, font="Arial 16")
        nome_produto.grid(row=0, column=2, padx=10, pady=10, sticky="W")

        Label(self.janela_principal, text="Plataforma: ", font="Arial 16", fg="#333333", bg="#f0f0f0").grid(row=0, column=3,padx=10, pady=10,sticky="W")
        plataforma_produto = Entry(self.janela_principal, font="Arial 16")
        plataforma_produto.grid(row=0, column=4, padx=10, pady=10, sticky="W")

        Label(self.janela_principal, text="Ano: ", font="Arial 16", fg="#333333", bg="#f0f0f0").grid(row=0, column=5,padx=10, pady=10,sticky="W")
        ano_produto = Entry(self.janela_principal, font="Arial 16")
        ano_produto.grid(row=0, column=6, padx=10, pady=10, sticky="W")

        Label(self.janela_principal, text="Género: ", font="Arial 16", fg="#333333", bg="#f0f0f0").grid(row=0, column=7,padx=10, pady=10,sticky="W")
        genero_produto = Entry(self.janela_principal, font="Arial 16")
        genero_produto.grid(row=0, column=8, padx=10, pady=10, sticky="W")

        Label(self.janela_principal, text="Sistema de Gestão de Stock", font="Arial 16", fg="#333333",
            bg="#f0f0f0").grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky="NSEW")

        self.style = ttk.Style(self.janela_principal)
        self.treeeview = ttk.Treeview(self.janela_principal, style="mystyle.Treeview",columns=("id", "titulo", "plataforma", "ano", "genero", "imagem_path", "quantidade", "preco"), show="headings")
        self.style.theme_use("default")
        self.style.configure("mystyle.Treeview", font='Arial, 14', rowheight=25)

        # Configuração da tabela de exibição dos produtos
        self.treeeview.heading("id", text="Id")
        self.treeeview.heading("titulo", text="Título")
        self.treeeview.heading("plataforma", text="Plataforma")
        self.treeeview.heading("ano", text="Ano")
        self.treeeview.heading("genero", text="Género")
        self.treeeview.heading("imagem_path", text="Imagem")
        self.treeeview.heading("quantidade", text="Quantidade")
        self.treeeview.heading("preco", text="Preço")
        self.treeeview.column("#0", width=0, stretch=NO)
        self.treeeview.column("id", anchor=CENTER, width=100)
        self.treeeview.column("titulo", anchor=CENTER, width=300)
        self.treeeview.column("plataforma", anchor=CENTER, width=200)
        self.treeeview.column("ano", anchor=CENTER, width=200)
        self.treeeview.column("genero", anchor=CENTER, width=200)
        self.treeeview.column("imagem_path", anchor=CENTER, width=200)
        self.treeeview.column("quantidade", anchor=CENTER, width=100)
        self.treeeview.column("preco", anchor=CENTER, width=100)

        self.treeeview.grid(row=3, column=0, columnspan=10, sticky="NSEW")
        self.janela_principal.grid_columnconfigure(0, weight=1)

        self.mostrar_jogos()

        self.treeeview.bind("<Double-1>", self.editar_jogo)

        self.botao_novo_produto = Button(self.janela_principal, text="Novo Produto", font="Arial 14",command=self.registar_produto_jogo)
        self.botao_novo_produto.grid(row=4, column=0, columnspan=6, sticky="NSEW")

        self.botao_apagar_produto = Button(self.janela_principal, text="Apagar", font="Arial 14",command=self.apagar_jogo)
        self.botao_apagar_produto.grid(row=4, column=6, columnspan=5, sticky="NSEW")

        self.menu_barra = Menu(self.janela_principal)
        self.janela_principal.configure(menu=self.menu_barra)

        self.menu_ficheiro = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Ficheiro", menu=self.menu_ficheiro)
        self.menu_ficheiro.add_command(label="Novo", command=self.registar_produto_jogo)
        self.menu_ficheiro.add_command(label="Sair", command=self.janela_principal.destroy)

        nome_produto.bind('<KeyRelease>', lambda e: self.filtrar_titulo_jogos(nome_produto))
        plataforma_produto.bind('<KeyRelease>', lambda e: self.filtrar_plataforma_jogos(plataforma_produto))
        ano_produto.bind('<KeyRelease>', lambda e: self.filtrar_ano_jogos(ano_produto))
        genero_produto.bind('<KeyRelease>', lambda e: self.filtrar_genero_jogos(genero_produto))


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

    def apagar_jogo(self):
            
            item_selecionado = self.treeeview.selection()[0]
    
            valores_selecionados = self.treeeview.item(item_selecionado)["values"]
    
            conn = sqlite3.connect("stock.db")
            cursor = conn.cursor()
    
            cursor.execute("DELETE FROM jogos WHERE id = ?", (valores_selecionados[0],))
    
            conn.commit()
            conn.close()
    
            self.mostrar_jogos()
    
            messagebox.showinfo("Sucesso", "Produto apagado com sucesso!")

    #verificar que ele não guarda produtos
    def editar_jogo(self, event):

        item_selecionado = self.treeeview.selection()[0]

        valores_selecionados = self.treeeview.item(item_selecionado)["values"]

        self.janela_edicao = Toplevel(self.janela_principal)
        self.janela_edicao.title("Editar jogo")
        self.janela_edicao.iconbitmap("assets/icon/icon.ico")
        self.janela_edicao.configure(bg="#f0f0f0")
        self.janela_edicao.geometry(self.calcular_posicao(400, 350))

        estilo_borda = {'borderwidth': 2, 'relief': 'groove'}

        Label(self.janela_edicao, text="Editar Produto", font="Arial 20", fg="#333333", bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

        Label(self.janela_edicao, text="Titulo:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.nome_jogo_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[1]))
        self.nome_jogo_editado.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_edicao, text="plataforma:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.plataforma_jogo_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[2]))
        self.plataforma_jogo_editado.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_edicao, text="Ano:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.ano_jogo_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[3]))
        self.ano_jogo_editado.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_edicao, text="Género:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.genero_jogo_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[4]))
        self.genero_jogo_editado.grid(row=4, column=1, padx=10, pady=10, sticky="W")
        
        Label(self.janela_edicao, text="Imagem:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        self.imagem_jogo_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[5]))
        self.imagem_jogo_editado.grid(row=5, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_edicao, text="Quantidade:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=6, column=0, padx=10, pady=10, sticky="W")
        self.quantidade_jogo_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[6]))
        self.quantidade_jogo_editado.grid(row=6, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_edicao, text="Preço:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=7, column=0, padx=10, pady=10, sticky="W")
        self.preco_jogo_editado = Entry(self.janela_edicao, font="Arial 12", **estilo_borda, textvariable=StringVar(value=valores_selecionados[7]))
        self.preco_jogo_editado.grid(row=7, column=1, padx=10, pady=10, sticky="W")

        def guardar_edicao_jogo():
            # Obter os valores dos campos de entrada
            novo_nome_jogo = self.nome_jogo_editado.get()
            novo_plataforma_jogo = self.plataforma_jogo_editado.get()
            novo_ano_jogo = self.ano_jogo_editado.get()
            novo_genero_jogo = self.genero_jogo_editado.get()
            novo_imagem_jogo = self.imagem_jogo_editado.get()
            novo_quantidade_jogo = self.quantidade_jogo_editado.get()
            novo_preco_jogo = self.preco_jogo_editado.get()

            # Verificar se todos os campos foram preenchidos
            if novo_nome_jogo and novo_plataforma_jogo and novo_ano_jogo and novo_genero_jogo and novo_imagem_jogo and novo_quantidade_jogo and novo_preco_jogo:

                # Conectar à base de dados
                conn = sqlite3.connect("stock.db")
                cursor = conn.cursor()

                # Verificar se o título já existe na base de dados
                cursor.execute("SELECT * FROM jogos WHERE titulo = ?", (novo_nome_jogo,))
                if cursor.fetchone():
                    conn.close()
                    # Exibir uma mensagem de erro se o título já existir na base de dados
                    messagebox.showerror("Erro", "Este título já existe na base de dados!")
                else:
                    self.treeeview.item(item_selecionado, values=(valores_selecionados[0], novo_nome_jogo, novo_plataforma_jogo, novo_ano_jogo, novo_genero_jogo, novo_imagem_jogo, novo_quantidade_jogo, novo_preco_jogo))

                
                    # Inserir os dados na tabela
                    cursor.execute("UPDATE jogos SET titulo = ?, plataforma = ?, ano = ?, genero = ?, imagem_path = ?, quantidade = ?, preco = ? WHERE id = ?", (novo_nome_jogo, novo_plataforma_jogo, novo_ano_jogo, novo_genero_jogo, novo_imagem_jogo, novo_quantidade_jogo, novo_preco_jogo, valores_selecionados[0]))


                    # Confirmar a inserção dos dados
                    conn.commit()

                    # Fechar a conexão com a base de dados
                    conn.close()

                    self.mostrar_jogos()

                    # Exibir uma mensagem de sucesso
                    messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
            else:
                # Exibir uma mensagem de erro se algum campo estiver vazio
                messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

        self.botao_guardar_produto = Button(self.janela_edicao, text="Guardar Edição", font="Arial 12", command=guardar_edicao_jogo)
        self.botao_guardar_produto.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

        self.cancelar_edicao = Button(self.janela_edicao, text="Cancelar", font="Arial 12", command=self.janela_edicao.destroy)
        self.cancelar_edicao.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

    def registar_produto_jogo(self):
        #criar nova janela para registar os produtos
        self.janela_registo_jogo = Toplevel()
        self.janela_registo_jogo.title("Registar jogo")
        self.janela_registo_jogo.iconbitmap("assets/icon/icon.ico")
        self.janela_registo_jogo.configure(bg="#f0f0f0")
        self.janela_registo_jogo.geometry(self.calcular_posicao(400, 350))

        estilo_borda = {'borderwidth': 2, 'relief': 'groove'}

        Label(self.janela_registo_jogo, text="Sistema de Gestão de Produtos", font="Arial 20", fg="#333333", bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

        Label(self.janela_registo_jogo, text="Título:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.titulo_jogo_entry = Entry(self.janela_registo_jogo, font="Arial 12", **estilo_borda)
        self.titulo_jogo_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_jogo, text="plataforma:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.plataforma_jogo_entry = Entry(self.janela_registo_jogo, font="Arial 12", **estilo_borda)
        self.plataforma_jogo_entry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_jogo, text="Ano:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.ano_jogo_entry = Entry(self.janela_registo_jogo, font="Arial 12", **estilo_borda)
        self.ano_jogo_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_jogo, text="Género:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.genero_jogo_entry = Entry(self.janela_registo_jogo, font="Arial 12", **estilo_borda)
        self.genero_jogo_entry.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_jogo, text="Imagem:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        self.imagem_jogo_entry = Entry(self.janela_registo_jogo, font="Arial 12", **estilo_borda)
        self.imagem_jogo_entry.grid(row=5, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_jogo, text="Quantidade:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=6, column=0, padx=10, pady=10, sticky="W")
        self.quantidade_jogo_entry = Entry(self.janela_registo_jogo, font="Arial 12", **estilo_borda)
        self.quantidade_jogo_entry.grid(row=6, column=1, padx=10, pady=10, sticky="W")

        Label(self.janela_registo_jogo, text="Preço:", font="Arial 12", fg="Black", bg="#f0f0f0").grid(row=7, column=0, padx=10, pady=10, sticky="W")
        self.preco_jogo_entry = Entry(self.janela_registo_jogo, font="Arial 12", **estilo_borda)
        self.preco_jogo_entry.grid(row=7, column=1, padx=10, pady=10, sticky="W")

        self.botao_gravar_edicao = Button(self.janela_registo_jogo, text="Guardar", font="Arial 12", command=self.guardar_jogo)
        self.botao_gravar_edicao.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

        self.cancelar = Button(self.janela_registo_jogo, text="Cancelar", font="Arial 12", command=self.janela_registo_jogo.destroy)
        self.cancelar.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

    def guardar_jogo(self):
    
        # Obter os valores dos campos de entrada
        titulo = self.titulo_jogo_entry.get()
        plataforma = self.plataforma_jogo_entry.get()
        ano= self.ano_jogo_entry.get()
        genero = self.genero_jogo_entry.get()
        imagem = self.imagem_jogo_entry.get()
        quantidade = self.quantidade_jogo_entry.get()
        preco = self.preco_jogo_entry.get()

        # Verificar se todos os campos foram preenchidos
        if titulo and plataforma and ano and genero and imagem and quantidade and preco:

            # Conectar à base de dados
            conn = sqlite3.connect("stock.db")
            cursor = conn.cursor()

            # Inserir os dados na tabela
            cursor.execute("INSERT INTO jogos (titulo, plataforma, ano, genero, imagem_path, quantidade, preco) VALUES (?, ?, ?, ?, ?, ?, ?)", (titulo, plataforma, ano, genero, imagem, quantidade, preco))

            # Confirmar a inserção dos dados
            conn.commit()

            # Fechar a conexão com a base de dados
            conn.close()

            # Limpar os campos de entrada
            self.titulo_jogo_entry.delete(0, END)
            self.plataforma_jogo_entry.delete(0, END)
            self.ano_jogo_entry.delete(0, END)
            self.genero_jogo_entry.delete(0, END)
            self.imagem_jogo_entry.delete(0, END)
            self.quantidade_jogo_entry.delete(0, END)
            self.preco_jogo_entry.delete(0, END)

            self.mostrar_jogos()

            # Exibir uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Produto guardado com sucesso!")
        else:
            # Exibir uma mensagem de erro se algum campo estiver vazio
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def mostrar_jogos(self):
            
        # Limpar os dados da tabela
        for i in self.treeeview.get_children():
            self.treeeview.delete(i)

        # Conectar à base de dados
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()

        # Obter os dados da tabela
        cursor.execute("SELECT * FROM jogos")
        produtos = cursor.fetchall()

        # Inserir os dados na tabela
        for produto in produtos:
            self.treeeview.insert("", "end", values=produto)

        # Fechar a conexão com a base de dados
        conn.close()


#teste para filtro feito
    def filtrar_titulo_jogos(self, titulo_jogo):
        if not titulo_jogo.get():
            self.mostrar_jogos()
            return
        
        sql = "SELECT * FROM jogos"
        params = []
        
        if titulo_jogo.get():
            sql += " WHERE titulo LIKE ?"
            params.append("%" + titulo_jogo.get() + "%")

        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6], produto[7]))        
    
    def filtrar_plataforma_jogos(self, plataforma_jogo):
        if not plataforma_jogo.get():
            self.mostrar_jogos()
            return
        
        sql = "SELECT * FROM jogos"
        params = []
        
        if plataforma_jogo.get():
            sql += " WHERE plataforma LIKE ?"
            params.append("%" + plataforma_jogo.get() + "%")

        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6], produto[7]))  

    def filtrar_ano_jogos(self, ano_jogo):
        if not ano_jogo.get():
            self.mostrar_jogos()
            return
        
        sql = "SELECT * FROM jogos"
        params = []
        
        if ano_jogo.get():
            sql += " WHERE ano LIKE ?"
            params.append("%" + ano_jogo.get() + "%")

        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6], produto[7]))

    def filtrar_genero_jogos(self, genero_jogo):
        if not genero_jogo.get():
            self.mostrar_jogos()
            return
        
        sql = "SELECT * FROM jogos"
        params = []
        
        if genero_jogo.get():
            sql += " WHERE genero LIKE ?"
            params.append("%" + genero_jogo.get() + "%")

        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6], produto[7]))

    def limparDados(self):
        for i in self.treeeview.get_children():
            self.treeeview.delete(i)
