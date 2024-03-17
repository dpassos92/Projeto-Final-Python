from tkinter import *
from tkinter import Tk, Button
import sqlite3


class JanelaInserirVinyl:
    def __init__(self):
        self.janela_inserir_vinyl= Toplevel()
        self.janela_inserir_vinyl.title('Inserir vinyl')

        #criar label informação do vinyl
        self.texto_vinyl_lbl = Label(self.janela_inserir_vinyl, text='Informação do vinyl', font='Arial 20')
        self.texto_vinyl_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)
        
        #criar campo  para o artista do vinyl
        self.artista_vinyl_lbl = Label(self.janela_inserir_vinyl, text='Artista', font='Arial 14')
        self.artista_vinyl_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.artista_vinyl_entry = Entry(self.janela_inserir_vinyl, font= 'Arial 14')
        self.artista_vinyl_entry.grid(row=1, column=1, padx=(0,10),sticky='W')

        #criar campo para editora do vinyl
        self.editora_vinyl_lbl = Label(self.janela_inserir_vinyl, text='Editora', font='Arial 14')
        self.editora_vinyl_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.editora_vinyl_entry = Entry(self.janela_inserir_vinyl, font= 'Arial 14')
        self.editora_vinyl_entry.grid(row=2, column=1, padx=(0,10), sticky='W')

        #criar campo para ano do vinyl
        self.ano_vinyl_lbl = Label(self.janela_inserir_vinyl, text='Ano', font='Arial 14')
        self.ano_vinyl_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.ano_vinyl_entry = Entry(self.janela_inserir_vinyl, font= 'Arial 14')
        self.ano_vinyl_entry.grid(row=3, column=1, padx=(0,10), sticky='W')

        #criar campo para genero do vinyl
        self.genero_vinyl_lbl = Label(self.janela_inserir_vinyl, text='Género', font='Arial 14')
        self.genero_vinyl_lbl.grid(row=4, column=0, padx=(10,0), pady=10, sticky='W')
        self.genero_vinyl_entry = Entry(self.janela_inserir_vinyl, font= 'Arial 14')
        self.genero_vinyl_entry.grid(row=4, column=1, padx=(0,10), sticky='W')

        #criar campo para titulo do vinyl
        self.titulo_vinyl_lbl = Label(self.janela_inserir_vinyl, text='Título', font='Arial 14')
        self.titulo_vinyl_lbl.grid(row=5, column=0, padx=(10,0), pady=10, sticky='W')
        self.titulo_vinyl_entry = Entry(self.janela_inserir_vinyl, font= 'Arial 14')
        self.titulo_vinyl_entry.grid(row=5, column=1, padx=(0,10), sticky='W')

        #configuração do botão de registar
        self.registar_btn = Button(self.janela_inserir_vinyl, text='Registar vinyl', font='Arial 14', command=self.registar_vinyl) #falta command
        self.registar_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.botao_retroceder = Button(self.janela_inserir_vinyl, text='Voltar atrás', font='Arial 10 bold', command= self.janela_inserir_vinyl.destroy)
        self.botao_retroceder.grid(row=8, column=0, columnspan=2, padx=20, pady=20, sticky='NSEW')

    def registar_vinyl(self):
        #pegar nos dados inseridos
        artista_vinyl = self.artista_vinyl_entry.get()
        editora_vinyl = self.editora_vinyl_entry.get()
        ano_vinyl = self.ano_vinyl_entry.get()
        genero_vinyl = self.genero_vinyl_entry.get()
        titulo_vinyl = self.titulo_vinyl_entry.get()

        #ligar à base de dados
        conn= sqlite3.connect('stock.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO vinyls (artista, editora, ano, genero) VALUES(?,?,?,?,?)",
                        (artista_vinyl, editora_vinyl, ano_vinyl, genero_vinyl, titulo_vinyl)) # falta o valor para a imagem
        
        conn.commit()
        conn.close()

        #mensagem de sucesso no registo
        self.mensagem_registo_concluido = Label(self.janela_inserir_vinyl, text='Registo feito com Sucesso', fg='green')
        self.mensagem_registo_concluido.grid(row=6, column=0, columnspan=2)
        self.mensagem_registo_concluido.after(3000, self.janela_inserir_vinyl.destroy)

        #Falta fazer verificação de registos



    


