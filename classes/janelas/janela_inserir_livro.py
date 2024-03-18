from tkinter import *
from tkinter import Tk, Button
import sqlite3


class JanelaInserirLivro:
    def __init__(self):
        self.janela_inserir_livro= Toplevel()
        self.janela_inserir_livro.title('Inserir livro')

        #criar label informação do livro
        self.texto_livro_lbl = Label(self.janela_inserir_livro, text='Informação do livro', font='Arial 20')
        self.texto_livro_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)
        
        #criar campo  para o título do livro
        self.titulo_livro_lbl = Label(self.janela_inserir_livro, text='Título', font='Arial 14')
        self.titulo_livro_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.titulo_livro_entry = Entry(self.janela_inserir_livro, font= 'Arial 14')
        self.titulo_livro_entry.grid(row=1, column=1, padx=(0,10),sticky='W')

        #criar campo para autor do livro
        self.autor_livro_lbl = Label(self.janela_inserir_livro, text='Autor', font='Arial 14')
        self.autor_livro_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.autor_livro_entry = Entry(self.janela_inserir_livro, font= 'Arial 14')
        self.autor_livro_entry.grid(row=2, column=1, padx=(0,10), sticky='W')

        #criar campo para ano do livro
        self.ano_livro_lbl = Label(self.janela_inserir_livro, text='Ano', font='Arial 14')
        self.ano_livro_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.ano_livro_entry = Entry(self.janela_inserir_livro, font= 'Arial 14')
        self.ano_livro_entry.grid(row=3, column=1, padx=(0,10), sticky='W')

        #criar campo para genero do livro
        self.genero_livro_lbl = Label(self.janela_inserir_livro, text='Género', font='Arial 14')
        self.genero_livro_lbl.grid(row=4, column=0, padx=(10,0), pady=10, sticky='W')
        self.genero_livro_entry = Entry(self.janela_inserir_livro, font= 'Arial 14')
        self.genero_livro_entry.grid(row=4, column=1, padx=(0,10), sticky='W')

        #configuração do botão de registar
        self.registar_btn = Button(self.janela_inserir_livro, text='Registar livro', font='Arial 14', command=self.registar_livro) #falta command
        self.registar_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.botao_retroceder = Button(self.janela_inserir_livro, text='Voltar atrás', font='Arial 10 bold', command= self.janela_inserir_livro.destroy)
        self.botao_retroceder.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky='NSEW')

    def registar_livro(self):
        #pegar nos dados inseridos
        titulo_livro = self.titulo_livro_entry.get()
        autor_livro = self.autor_livro_entry.get()
        ano_livro = self.ano_livro_entry.get()
        genero_livro = self.genero_livro_entry.get()

        #ligar à base de dados
        conn= sqlite3.connect('stock.db')
        cursor = conn.cursor()

        # Verificar se o título do livro já existe na tabela
        cursor.execute("SELECT * FROM livros WHERE titulo=?", (titulo_livro,))
        livro_existente = cursor.fetchone()

        if livro_existente:
            # Se o livro já existir, exibir mensagem e não realizar a inserção novamente
            self.mensagem_registo_concluido = Label(self.janela_inserir_livro, text="Erro, este livro já está registado.", fg='red')
            self.mensagem_registo_concluido.grid(row=5, column=0, columnspan=2)
            self.mensagem_registo_concluido.after(3000, self.mensagem_registo_concluido.destroy)
        else:
            # Inserir o livro apenas se não existir na tabela
            cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES (?,?,?,?)",
                            (titulo_livro, autor_livro, ano_livro, genero_livro))
            conn.commit()
            conn.close()

            # mensagem de sucesso no registo
            self.mensagem_registo_concluido = Label(self.janela_inserir_livro, text='Registo feito com Sucesso', fg='green')
            self.mensagem_registo_concluido.grid(row=5, column=0, columnspan=2)
            self.mensagem_registo_concluido.after(3000, self.janela_inserir_livro.destroy)



    


