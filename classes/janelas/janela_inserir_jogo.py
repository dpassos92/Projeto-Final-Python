from tkinter import *
from tkinter import Tk, Button
import sqlite3


class JanelaInserirJogo:
    def __init__(self):
        self.janela_inserir_jogo= Toplevel()
        self.janela_inserir_jogo.title('Inserir jogo')

        #criar label informação do jogo
        self.texto_jogo_lbl = Label(self.janela_inserir_jogo, text='Informação do jogo', font='Arial 20')
        self.texto_jogo_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)
        
        #criar campo  para o título do jogo
        self.titulo_jogo_lbl = Label(self.janela_inserir_jogo, text='Título', font='Arial 14')
        self.titulo_jogo_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.titulo_jogo_entry = Entry(self.janela_inserir_jogo, font= 'Arial 14')
        self.titulo_jogo_entry.grid(row=1, column=1, padx=(0,10),sticky='W')

        #criar campo para plataforma do jogo
        self.plataforma_jogo_lbl = Label(self.janela_inserir_jogo, text='Plataforma', font='Arial 14')
        self.plataforma_jogo_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.plataforma_jogo_entry = Entry(self.janela_inserir_jogo, font= 'Arial 14')
        self.plataforma_jogo_entry.grid(row=2, column=1, padx=(0,10), sticky='W')

        #criar campo para ano do jogo
        self.ano_jogo_lbl = Label(self.janela_inserir_jogo, text='Ano', font='Arial 14')
        self.ano_jogo_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.ano_jogo_entry = Entry(self.janela_inserir_jogo, font= 'Arial 14')
        self.ano_jogo_entry.grid(row=3, column=1, padx=(0,10), sticky='W')

        #criar campo para genero do jogo
        self.genero_jogo_lbl = Label(self.janela_inserir_jogo, text='Género', font='Arial 14')
        self.genero_jogo_lbl.grid(row=4, column=0, padx=(10,0), pady=10, sticky='W')
        self.genero_jogo_entry = Entry(self.janela_inserir_jogo, font= 'Arial 14')
        self.genero_jogo_entry.grid(row=4, column=1, padx=(0,10), sticky='W')

        #configuração do botão de registar
        self.registar_btn = Button(self.janela_inserir_jogo, text='Registar jogo', font='Arial 14', command=self.registar_jogo) #falta command
        self.registar_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.botao_retroceder = Button(self.janela_inserir_jogo, text='Voltar atrás', font='Arial 10 bold', command= self.janela_inserir_jogo.destroy)
        self.botao_retroceder.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

    def registar_jogo(self):
        #pegar nos dados inseridos
        titulo_jogo = self.titulo_jogo_entry.get()
        plataforma_jogo = self.plataforma_jogo_entry.get()
        ano_jogo = self.ano_jogo_entry.get()
        genero_jogo = self.genero_jogo_entry.get()

        #ligar à base de dados
        conn= sqlite3.connect('stock.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO jogos (titulo, plataforma, ano, genero) VALUES(?,?,?,?)",
                        (titulo_jogo, plataforma_jogo, ano_jogo, genero_jogo)) # falta o valor para a imagem
        
        conn.commit()
        conn.close()

        #mensagem de sucesso no registo
        self.mensagem_registo_concluido = Label(self.janela_inserir_jogo, text='Registo feito com Sucesso', fg='green')
        self.mensagem_registo_concluido.grid(row=5, column=0, columnspan=2)
        self.mensagem_registo_concluido.after(3000, self.janela_inserir_jogo.destroy)

        #Falta fazer verificação de registos



    


