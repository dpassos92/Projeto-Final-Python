from tkinter import *
from tkinter import Tk, Button, messagebox
import sqlite3


class JanelaInserirFilme:
    def __init__(self):
        self.janela_inserir_filme= Toplevel()
        self.janela_inserir_filme.title('Inserir Filme')

        #criar label informação do filme
        self.texto_filme_lbl = Label(self.janela_inserir_filme, text='Informação do Filme', font='Arial 20')
        self.texto_filme_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)
        
        #criar campo  para o título do filme
        self.titulo_filme_lbl = Label(self.janela_inserir_filme, text='Título', font='Arial 14')
        self.titulo_filme_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.titulo_filme_entry = Entry(self.janela_inserir_filme, font= 'Arial 14')
        self.titulo_filme_entry.grid(row=1, column=1, padx=(0,10),sticky='W')

        #criar campo para realizador do filme
        self.realizador_filme_lbl = Label(self.janela_inserir_filme, text='Realizador', font='Arial 14')
        self.realizador_filme_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.realizador_filme_entry = Entry(self.janela_inserir_filme, font= 'Arial 14')
        self.realizador_filme_entry.grid(row=2, column=1, padx=(0,10), sticky='W')

        #criar campo para ano do filme
        self.ano_filme_lbl = Label(self.janela_inserir_filme, text='Ano', font='Arial 14')
        self.ano_filme_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.ano_filme_entry = Entry(self.janela_inserir_filme, font= 'Arial 14')
        self.ano_filme_entry.grid(row=3, column=1, padx=(0,10), sticky='W')

        #criar campo para genero do filme
        self.genero_filme_lbl = Label(self.janela_inserir_filme, text='Género', font='Arial 14')
        self.genero_filme_lbl.grid(row=4, column=0, padx=(10,0), pady=10, sticky='W')
        self.genero_filme_entry = Entry(self.janela_inserir_filme, font= 'Arial 14')
        self.genero_filme_entry.grid(row=4, column=1, padx=(0,10), sticky='W')

        #configuração do botão de registar
        self.registar_btn = Button(self.janela_inserir_filme, text='Registar Filme', font='Arial 14', command=self.registar_filme) #falta command
        self.registar_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.botao_retroceder = Button(self.janela_inserir_filme, text='Voltar atrás', font='Arial 10 bold', command= self.janela_inserir_filme.destroy)
        self.botao_retroceder.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky='NSEW')

    def registar_filme(self):
        #pegar nos dados inseridos
        titulo_filme = self.titulo_filme_entry.get()
        realizador_filme = self.realizador_filme_entry.get()
        ano_filme = self.ano_filme_entry.get()
        genero_filme = self.genero_filme_entry.get()

        #ligar à base de dados
        conn= sqlite3.connect('stock.db')
        cursor = conn.cursor()

        # Verificar se o título do filme já existe na tabela
        cursor.execute("SELECT * FROM filmes WHERE titulo=?", (titulo_filme,))
        filme_existente = cursor.fetchone()

        if filme_existente:
            # Se o filme já existir, exibir mensagem e não realizar a inserção novamente
            self.mensagem_registo_concluido = Label(self.janela_inserir_filme, text="Erro, este filme já está registado.", fg='red')
            self.mensagem_registo_concluido.grid(row=5, column=0, columnspan=2)
            self.mensagem_registo_concluido.after(3000, self.mensagem_registo_concluido.destroy)
        else:
            # Inserir o filme apenas se não existir na tabela
            cursor.execute("INSERT INTO filmes (titulo, realizador, ano, genero) VALUES (?,?,?,?)",
                            (titulo_filme, realizador_filme, ano_filme, genero_filme))
            conn.commit()
            conn.close()

            # mensagem de sucesso no registo
            self.mensagem_registo_concluido = Label(self.janela_inserir_filme, text='Registo feito com Sucesso', fg='green')
            self.mensagem_registo_concluido.grid(row=5, column=0, columnspan=2)
            self.mensagem_registo_concluido.after(3000, self.janela_inserir_filme.destroy)
            



    


