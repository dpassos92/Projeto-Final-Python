#importações
from tkinter import *
from tkinter import Tk, ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
import os
import customtkinter
from classes.janelas.reconstruir_menu import ReconstruirMenu


class CategoriaFilme:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal

    def abrir_janela_menu(self):

        for widget in self.janela_principal.winfo_children():
            widget.destroy()

        self.janela_principal.title("Sistema de Gestão de Produtos - Filmes")  # Título da janela
        self.janela_principal.iconbitmap("assets/icon/icon.ico")  # Ícone da janela
        self.janela_principal.configure(bg="#f0f0f0")  # Cor de fundo da janela
        self.janela_principal.geometry(self.calcular_posicao())  # Posição da janela no ecrã
        self.janela_principal.state('zoomed')  # Maximizar a janela

        customtkinter.CTkLabel(self.janela_principal, text="Título: ", font=("Arial", 16)).grid(row=0,column=1,padx=10,pady=10,sticky="W")
        nome_produto = customtkinter.CTkEntry(self.janela_principal, font=("Arial", 16))
        nome_produto.grid(row=0, column=2, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_principal, text="Realizador: ", font=("Arial", 16)).grid(row=0, column=3,padx=10, pady=10,sticky="W")
        realizador_produto = customtkinter.CTkEntry(self.janela_principal, font=("Arial", 16))
        realizador_produto.grid(row=0, column=4, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_principal, text="Ano: ", font=("Arial", 16)).grid(row=0, column=5,padx=10, pady=10,sticky="W")
        ano_produto = customtkinter.CTkEntry(self.janela_principal, font=("Arial", 16))
        ano_produto.grid(row=0, column=6, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_principal, text="Género: ", font=("Arial", 16)).grid(row=0, column=7,padx=10, pady=10,sticky="W")
        genero_produto = customtkinter.CTkEntry(self.janela_principal, font=("Arial", 16))
        genero_produto.grid(row=0, column=8, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_principal, text="Sistema de Gestão de Stock - Filmes", font=("Arial", 16)).grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky="NSEW")

        self.style = ttk.Style(self.janela_principal)
        self.treeeview = ttk.Treeview(self.janela_principal, style="mystyle.Treeview",columns=("id", "titulo", "realizador", "ano", "genero", "imagem_path", "quantidade", "preco"), show="headings")
        self.style.theme_use("default")
        self.style.configure("mystyle.Treeview", font='Arial, 14', rowheight=25)

        # Configuração da tabela de exibição dos produtos
        self.treeeview.heading("id", text="Id")
        self.treeeview.heading("titulo", text="Título")
        self.treeeview.heading("realizador", text="Realizador")
        self.treeeview.heading("ano", text="Ano")
        self.treeeview.heading("genero", text="Género")
        self.treeeview.heading("imagem_path", text="Imagem")
        self.treeeview.heading("quantidade", text="Quantidade")
        self.treeeview.heading("preco", text="Preço")
        self.treeeview.column("#0", width=0, stretch=NO)
        self.treeeview.column("id", anchor=CENTER, width=100)
        self.treeeview.column("titulo", anchor=CENTER, width=300)
        self.treeeview.column("realizador", anchor=CENTER, width=200)
        self.treeeview.column("ano", anchor=CENTER, width=200)
        self.treeeview.column("genero", anchor=CENTER, width=200)
        self.treeeview.column("imagem_path", anchor=CENTER, width=200)
        self.treeeview.column("quantidade", anchor=CENTER, width=100)
        self.treeeview.column("preco", anchor=CENTER, width=100)

        self.treeeview.grid(row=3, column=0, columnspan=10, sticky="NSEW")
        self.janela_principal.grid_columnconfigure(0, weight=1)

        self.mostrar_filmes()

        self.treeeview.bind("<Double-1>", self.handle_selecao)

        self.botao_novo_produto = customtkinter.CTkButton(self.janela_principal, text="Novo Produto", font=("Arial", 14),command=self.registar_produto_filme)
        self.botao_novo_produto.grid(row=4, column=0, columnspan=2, sticky="NSEW")

        self.botao_apagar_produto = customtkinter.CTkButton(self.janela_principal, text="Apagar", font=("Arial", 14),command=self.apagar_filme)
        self.botao_apagar_produto.grid(row=4, column=2, columnspan=2, sticky="NSEW")

        self.botao_editar = customtkinter.CTkButton(self.janela_principal, text="Editar", font=("Arial", 14),command=self.editar_filme)
        self.botao_editar.grid(row=4, column=4, columnspan=2, sticky="NSEW")

        self.botao_retroceder = customtkinter.CTkButton(self.janela_principal, text="Retroceder", font=("Arial", 14),command=self.reconstruir_menu)
        self.botao_retroceder.grid(row=4, column=6, columnspan=2, sticky="NSEW")

        self.menu_barra = Menu(self.janela_principal)
        self.janela_principal.configure(menu=self.menu_barra)

        self.menu_ficheiro = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Ficheiro", menu=self.menu_ficheiro)
        self.menu_ficheiro.add_command(label="Novo", command=self.registar_produto_filme)
        self.menu_ficheiro.add_command(label="Retroceder", command=self.reconstruir_menu)
        self.menu_ficheiro.add_command(label="Sair", command=self.janela_principal.destroy)

        nome_produto.bind('<KeyRelease>', lambda e: self.filtrar_titulo_filmes(nome_produto))
        realizador_produto.bind('<KeyRelease>', lambda e: self.filtrar_realizador_filmes(realizador_produto))
        ano_produto.bind('<KeyRelease>', lambda e: self.filtrar_ano_filmes(ano_produto))
        genero_produto.bind('<KeyRelease>', lambda e: self.filtrar_genero_filmes(genero_produto))


    

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

    def apagar_filme(self):
            
            item_selecionado = self.treeeview.selection()[0]
    
            valores_selecionados = self.treeeview.item(item_selecionado)["values"]
    
            conn = sqlite3.connect("stock.db")
            cursor = conn.cursor()
    
            cursor.execute("DELETE FROM filmes WHERE id = ?", (valores_selecionados[0],))
    
            conn.commit()
            conn.close()
    
            self.mostrar_filmes()
    
            messagebox.showinfo("Sucesso", "Produto apagado com sucesso!")

    #verificar que ele não guarda produtos
    def editar_filme(self):

        item_selecionado = self.treeeview.selection()[0]

        valores_selecionados = self.treeeview.item(item_selecionado)["values"]

        self.janela_edicao = customtkinter.CTkToplevel(self.janela_principal)
        self.janela_edicao.title("Editar filme")
        self.janela_edicao.iconbitmap("assets/icon/icon.ico")
        self.janela_edicao.configure(bg="#f0f0f0")
        self.janela_edicao.geometry(self.calcular_posicao(400, 350))

        #estilo_borda = {'borderwidth': 2, 'relief': 'groove'}

        customtkinter.CTkLabel(self.janela_edicao, text="Editar Produto", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=20)

        customtkinter.CTkLabel(self.janela_edicao, text="Titulo:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.nome_filme_editado = customtkinter.CTkEntry(self.janela_edicao, font=("Arial", 12), textvariable=StringVar(value=valores_selecionados[1]))
        self.nome_filme_editado.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_edicao, text="realizador:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.realizador_filme_editado = customtkinter.CTkEntry(self.janela_edicao, font=("Arial", 12), textvariable=StringVar(value=valores_selecionados[2]))
        self.realizador_filme_editado.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_edicao, text="Ano:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.ano_filme_editado = customtkinter.CTkEntry(self.janela_edicao, font=("Arial", 12), textvariable=StringVar(value=valores_selecionados[3]))
        self.ano_filme_editado.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_edicao, text="Género:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.genero_filme_editado = customtkinter.CTkEntry(self.janela_edicao, font=("Arial", 12), textvariable=StringVar(value=valores_selecionados[4]))
        self.genero_filme_editado.grid(row=4, column=1, padx=10, pady=10, sticky="W")
        
        customtkinter.CTkLabel(self.janela_edicao, text="Imagem:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=10, sticky="W")
        self.imagem_filme_editado = customtkinter.CTkEntry(self.janela_edicao, font=("Arial", 12), textvariable=StringVar(value=valores_selecionados[5]))
        self.imagem_filme_editado.grid(row=5, column=1, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_edicao, text="Quantidade:", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=10, sticky="W")
        self.quantidade_filme_editado = customtkinter.CTkEntry(self.janela_edicao, font=("Arial", 12), textvariable=StringVar(value=valores_selecionados[6]))
        self.quantidade_filme_editado.grid(row=6, column=1, padx=10, pady=10, sticky="W")

        customtkinter.CTkLabel(self.janela_edicao, text="Preço:", font=("Arial", 12)).grid(row=7, column=0, padx=10, pady=10, sticky="W")
        self.preco_filme_editado = customtkinter.CTkEntry(self.janela_edicao, font=("Arial", 12), textvariable=StringVar(value=valores_selecionados[7]))
        self.preco_filme_editado.grid(row=7, column=1, padx=10, pady=10, sticky="W")

        def guardar_edicao_filme():
            # Obter os valores dos campos de entrada
            novo_nome_filme = self.nome_filme_editado.get()
            novo_realizador_filme = self.realizador_filme_editado.get()
            novo_ano_filme = self.ano_filme_editado.get()
            novo_genero_filme = self.genero_filme_editado.get()
            novo_imagem_filme = os.path.basename(self.imagem_filme_editado.get())
            novo_quantidade_filme = self.quantidade_filme_editado.get()
            novo_preco_filme = self.preco_filme_editado.get()

            # Verificar se todos os campos foram preenchidos
            if novo_nome_filme and novo_realizador_filme and novo_ano_filme and novo_genero_filme and novo_imagem_filme and novo_quantidade_filme and novo_preco_filme:

                # Conectar à base de dados
                conn = sqlite3.connect("stock.db")
                cursor = conn.cursor()
                
                # Inserir os dados na tabela
                cursor.execute("UPDATE filmes SET realizador = ?, ano = ?, genero = ?, imagem_path = ?, quantidade = ?, preco = ? WHERE id = ?", (novo_realizador_filme, novo_ano_filme, novo_genero_filme, novo_imagem_filme, novo_quantidade_filme, novo_preco_filme, valores_selecionados[0]))

                if novo_nome_filme != valores_selecionados[1]:
                # Verificar se o título já existe na base de dados
                    cursor.execute("SELECT * FROM filmes WHERE titulo = ?", (novo_nome_filme,))
                    if cursor.fetchone():
                        conn.rollback()  # Rollback the transaction
                        conn.close()
                        # Exibir uma mensagem de erro se o título já existir na base de dados
                        messagebox.showerror("Erro", "Este título já existe na base de dados!")
                        return  # Exit the function
                    
                    # Se o novo título não existir, atualizar o título na base de dados
                    cursor.execute("UPDATE filmes SET titulo = ? WHERE id = ?", (novo_nome_filme, valores_selecionados[0]))

                # Confirmar a inserção dos dados
                conn.commit()

                # Fechar a conexão com a base de dados
                conn.close()

                # Update the Treeview with the edited values
                self.treeeview.item(item_selecionado, values=(valores_selecionados[0], novo_nome_filme, novo_realizador_filme, novo_ano_filme, novo_genero_filme, novo_imagem_filme, novo_quantidade_filme, novo_preco_filme))

                self.mostrar_filmes()

                # Exibir uma mensagem de sucesso
                messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
                self.janela_edicao.destroy
            else:
                # Exibir uma mensagem de erro se algum campo estiver vazio
                messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

        self.botao_guardar_produto = customtkinter.CTkButton(self.janela_edicao, text="Guardar Edição", font=("Arial", 12), command=guardar_edicao_filme)
        self.botao_guardar_produto.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

        self.cancelar_edicao = customtkinter.CTkButton(self.janela_edicao, text="Cancelar", font=("Arial", 12), command=self.janela_edicao.destroy)
        self.cancelar_edicao.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

    def registar_produto_filme(self):
        #criar nova janela para registar os produtos
        self.janela_registo_filme = customtkinter.CTkToplevel(self.janela_principal)
        self.janela_registo_filme.title("Registar filme")
        self.janela_principal.iconbitmap("assets/icon/icon.ico")  # Ícone da janela
        self.janela_registo_filme.geometry("700x600")

        self.janela_registo_filme.grab_set()

        customtkinter.CTkLabel(self.janela_registo_filme, text="Sistema de Gestão de Produtos", font=("Arial", 20)).pack(padx=10, pady=10)
        
        self.titulo_filme_entry = customtkinter.CTkEntry(self.janela_registo_filme, placeholder_text="Título:", font=("Arial", 12))
        self.titulo_filme_entry.pack(padx=10, pady=10)

        self.realizador_filme_entry = customtkinter.CTkEntry(self.janela_registo_filme, placeholder_text="Realizador:", font=("Arial", 12))
        self.realizador_filme_entry.pack(padx=10, pady=10)

        self.ano_filme_entry = customtkinter.CTkEntry(self.janela_registo_filme, placeholder_text="Ano:", font=("Arial", 12))
        self.ano_filme_entry.pack(padx=10, pady=10)

        self.genero_filme_entry = customtkinter.CTkEntry(self.janela_registo_filme, placeholder_text="Género:", font=("Arial", 12))
        self.genero_filme_entry.pack(padx=10, pady=10)

        self.imagem_filme_entry = customtkinter.CTkEntry(self.janela_registo_filme, placeholder_text="Imagem:", font=("Arial", 12))
        self.imagem_filme_entry.pack(padx=10, pady=10)

        self.quantidade_filme_entry = customtkinter.CTkEntry(self.janela_registo_filme, placeholder_text="Quantidade:", font=("Arial", 12))
        self.quantidade_filme_entry.pack(padx=10, pady=10)

        self.preco_filme_entry = customtkinter.CTkEntry(self.janela_registo_filme, placeholder_text="Preço:", font=("Arial", 12))
        self.preco_filme_entry.pack(padx=10, pady=10)

        self.botao_gravar_edicao = customtkinter.CTkButton(self.janela_registo_filme, text="Guardar", font=("Arial", 12), command=self.guardar_filme)
        self.botao_gravar_edicao.pack(padx=10, pady=10)

        self.cancelar = customtkinter.CTkButton(self.janela_registo_filme, text="Cancelar", font=("Arial", 12), command=self.janela_registo_filme.destroy)
        self.cancelar.pack(padx=10, pady=10)

    def guardar_filme(self):
    
        # Obter os valores dos campos de entrada
        titulo = self.titulo_filme_entry.get()
        realizador = self.realizador_filme_entry.get()
        ano= self.ano_filme_entry.get()
        genero = self.genero_filme_entry.get()
        imagem = os.path.basename(self.imagem_filme_entry.get())
        quantidade = self.quantidade_filme_entry.get()
        preco = self.preco_filme_entry.get()

        # Verificar se todos os campos foram preenchidos
        if titulo and realizador and ano and genero and imagem and quantidade and preco:

            # Conectar à base de dados
            conn = sqlite3.connect("stock.db")
            cursor = conn.cursor()
            #falta logica de validar titulos repetidos
            # Inserir os dados na tabela
            cursor.execute("INSERT INTO filmes (titulo, realizador, ano, genero, imagem_path, quantidade, preco) VALUES (?, ?, ?, ?, ?, ?, ?)", (titulo, realizador, ano, genero, imagem, quantidade, preco))

            # Confirmar a inserção dos dados
            conn.commit()

            # Fechar a conexão com a base de dados
            conn.close()

            # Limpar os campos de entrada
            self.titulo_filme_entry.delete(0, END)
            self.realizador_filme_entry.delete(0, END)
            self.ano_filme_entry.delete(0, END)
            self.genero_filme_entry.delete(0, END)
            self.imagem_filme_entry.delete(0, END)
            self.quantidade_filme_entry.delete(0, END)
            self.preco_filme_entry.delete(0, END)

            self.mostrar_filmes()

            # Exibir uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Produto guardado com sucesso!")
        else:
            # Exibir uma mensagem de erro se algum campo estiver vazio
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def mostrar_filmes(self):
            
        # Limpar os dados da tabela
        for i in self.treeeview.get_children():
            self.treeeview.delete(i)

        # Conectar à base de dados
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()

        # Obter os dados da tabela
        cursor.execute("SELECT * FROM filmes")
        produtos = cursor.fetchall()

        # Inserir os dados na tabela
        for produto in produtos:
            self.treeeview.insert("", "end", values=produto)

        # Fechar a conexão com a base de dados
        conn.close()


#teste para filtro feito
    def filtrar_titulo_filmes(self, titulo_filme):
        if not titulo_filme.get():
            self.mostrar_filmes()
            return
        
        sql = "SELECT * FROM filmes"
        params = []
        
        if titulo_filme.get():
            sql += " WHERE titulo LIKE ?"
            params.append("%" + titulo_filme.get() + "%")

        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6], produto[7]))        
    
    def filtrar_realizador_filmes(self, realizador_filme):
        if not realizador_filme.get():
            self.mostrar_filmes()
            return
        
        sql = "SELECT * FROM filmes"
        params = []
        
        if realizador_filme.get():
            sql += " WHERE realizador LIKE ?"
            params.append("%" + realizador_filme.get() + "%")

        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6], produto[7]))  

    def filtrar_ano_filmes(self, ano_filme):
        if not ano_filme.get():
            self.mostrar_filmes()
            return
        
        sql = "SELECT * FROM filmes"
        params = []
        
        if ano_filme.get():
            sql += " WHERE ano LIKE ?"
            params.append("%" + ano_filme.get() + "%")

        
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute(sql, tuple(params))
        produtos = cursor.fetchall()

        self.limparDados()

        for produto in produtos:
            self.treeeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6], produto[7]))

    def filtrar_genero_filmes(self, genero_filme):
        if not genero_filme.get():
            self.mostrar_filmes()
            return
        
        sql = "SELECT * FROM filmes"
        params = []
        
        if genero_filme.get():
            sql += " WHERE genero LIKE ?"
            params.append("%" + genero_filme.get() + "%")

        
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


    def reconstruir_menu(self):
        reconstruir_menu_instance = ReconstruirMenu(janela_principal=self.janela_principal)
        reconstruir_menu_instance.reconstruir_menu()

    
    
    def handle_selecao(self, event):
        # Obter o filme_id a partir do item selecionado na treeview
        item_selecionado = self.treeeview.selection()[0]
        filme_id = self.treeeview.item(item_selecionado)['values'][0]
        # Chamar a função exibir_filmes com o filme_id
        self.exibir_filmes(filme_id)

    def exibir_filmes(self, filme_id):
        # Conectar ao banco de dados e obter os detalhes do filme
        conn = sqlite3.connect('stock.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM filmes WHERE id=?", (filme_id,))
        filme = cursor.fetchone()
        conn.close()

        # Criar uma nova janela para exibir os detalhes do filme
        exibir_window = customtkinter.CTkToplevel(self.janela_principal)
        exibir_window.title("Detalhes do filme")

        # Exibir os atributos do filme na janela
        row = 0
        customtkinter.CTkLabel(exibir_window, text="Título:").grid(row=row, column=0, sticky='w')
        customtkinter.CTkLabel(exibir_window, text=filme[1]).grid(row=row, column=1, sticky='w')
        row += 1

        customtkinter.CTkLabel(exibir_window, text="Realizador:").grid(row=row, column=0, sticky='w')
        customtkinter.CTkLabel(exibir_window, text=filme[2]).grid(row=row, column=1, sticky='w')
        row += 1

        customtkinter.CTkLabel(exibir_window, text="Ano:").grid(row=row, column=0, sticky='w')
        customtkinter.CTkLabel(exibir_window, text=filme[3]).grid(row=row, column=1, sticky='w')
        row += 1

        customtkinter.CTkLabel(exibir_window, text="Género:").grid(row=row, column=0, sticky='w')
        customtkinter.CTkLabel(exibir_window, text=filme[4]).grid(row=row, column=1, sticky='w')
        row += 1

    
        customtkinter.CTkLabel(exibir_window, text="Quantidade:").grid(row=row, column=0, sticky='w')
        customtkinter.CTkLabel(exibir_window, text=filme[6]).grid(row=row, column=1, sticky='w')
        row += 1

        customtkinter.CTkLabel(exibir_window, text="Preço:").grid(row=row, column=0, sticky='w')
        customtkinter.CTkLabel(exibir_window, text=filme[7]).grid(row=row, column=1, sticky='w')
        row += 1   

        image_file = filme[5]
        directory_path= "assets\\imagens"
        image_path = os.path.join(directory_path, image_file)
        image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(image)

        customtkinter.CTkLabel(exibir_window, image=tk_image, text=None).grid(row=0, column=2, rowspan= 6, sticky='e')
