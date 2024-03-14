#importações
from tkinter import *
from tkinter import Tk
import sqlite3
import hashlib
import os

#Criar a classe para a janela de registo
class JanelaRegisto:
    def __init__(self):

        #criar a janela principal
        self.janela_registo = Toplevel() #cria a janela
        self.janela_registo.title('Registo de utilizadores') #muda o titulo
        self.janela_registo.configure(bg='#f0f0f0') #altera a cor de fundo

        #criar label registo
        self.registo_lbl = Label(self.janela_registo, text='Registo', font='Arial 20', fg='#333333', bg='#f0f0f0')
        self.registo_lbl.grid(row=0, column=0, columnspan=2, pady=20, sticky='NSEW')

        #criar campo utilizador
        self.nome_utilizador_lbl = Label(self.janela_registo, text='Utilizador', font='Arial 14 bold')
        self.nome_utilizador_lbl.grid(row=1, column=0, sticky='e', pady=20)
        self.nome_utilizador_entry = Entry(self.janela_registo, font='Arial 14 bold', bg='#f0f0f0')
        self.nome_utilizador_entry.grid(row=1, column=1, pady=10)

        #criar campo password
        self.nome_password_lbl = Label(self.janela_registo, text='Password', font='Arial 14 bold')
        self.nome_password_lbl.grid(row=2, column=0, sticky='e', pady=20)
        self.nome_password_entry = Entry(self.janela_registo, font='Arial 14 bold', bg='#f0f0f0', show='*')
        self.nome_password_entry.grid(row=2, column=1, pady=10)

        #configuração do botão de sair
        self.sair_btn = Button(self.janela_registo, text='Sair', font='Arial 14', command=self.janela_registo.destroy)
        self.sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        #configuração do bptão de registar
        self.registar_btn = Button(self.janela_registo, text='Registar', font='Arial 14', command=self.registar_utilizador) #falta command
        self.registar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

    def registar_utilizador(self):
        #pegar nos dados inseridos
        dados_utilizador = self.nome_utilizador_entry.get()
        password_utilizador = self.nome_password_entry.get()

        #gerar valor do salt
        salt = os.urandom(16)

        #gerar o hash sha-256
        password_hash = hashlib.pbkdf2_hmac('sha256', password_utilizador.encode('UTF-8'), salt, 100000)

        #converter salt e password hashada para hexadecimal
        salt_hex = salt.hex()
        password_hash_hex = password_hash.hex()

        #valor a ser gravada
        password_a_gravar = f'{salt_hex}:{password_hash_hex}'


        #ligar à base de dados
        conn = sqlite3.connect('stock.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO utilizadores (utilizador, password) VALUES (?, ?)', (dados_utilizador, password_a_gravar)
        )
        conn.commit()
        conn.close()

        #mensagem de sucesso no registo
        self.mensagem_registo_concluido = Label(self.janela_registo, text='Registo feito com Sucesso', fg='green')
        self.mensagem_registo_concluido.grid(row=3, column=0, columnspan=2)
        self.mensagem_registo_concluido.after(3000, self.janela_registo.destroy)

