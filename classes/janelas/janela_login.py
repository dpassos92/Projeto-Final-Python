#importações
from tkinter import *
from tkinter import Tk
import sqlite3
import hashlib
import os
from classes.janelas.janela_menu import  JanelaMenu

#Criar a classe para a janela de registo
class JanelaLogin:
    def __init__(self):

        #criar a janela principal
        self.janela_login = Toplevel() #cria a janela
        self.janela_login.title('Registo de utilizadores') #muda o titulo
        self.janela_login.configure(bg='#f0f0f0') #altera a cor de fundo

        #criar label login
        self.login_lbl = Label(self.janela_login, text='Login', font='Arial 20', fg='#333333', bg='#f0f0f0')
        self.login_lbl.grid(row=0, column=0, columnspan=2, pady=20, sticky='NSEW')

        #criar campo utilizador
        self.nome_utilizador_lbl = Label(self.janela_login, text='Utilizador', font='Arial 14 bold')
        self.nome_utilizador_lbl.grid(row=1, column=0, sticky='e', pady=20)
        self.nome_utilizador_entry = Entry(self.janela_login, font='Arial 14 bold', bg='#f0f0f0')
        self.nome_utilizador_entry.grid(row=1, column=1, pady=10)

        #criar campo password
        self.nome_password_lbl = Label(self.janela_login, text='Password', font='Arial 14 bold')
        self.nome_password_lbl.grid(row=2, column=0, sticky='e', pady=20)
        self.nome_password_entry = Entry(self.janela_login, font='Arial 14 bold', bg='#f0f0f0', show='*')
        self.nome_password_entry.grid(row=2, column=1, pady=10)

        #configuração do botão de sair
        self.sair_btn = Button(self.janela_login, text='Sair', font='Arial 14', command=self.janela_login.destroy)
        self.sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        #configuração do bptão de registar
        self.registar_btn = Button(self.janela_login, text='Entrar', font='Arial 14', command=self.login_utilizador) #falta command
        self.registar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

    def login_utilizador(self):
        utilizador = self.nome_utilizador_entry.get()
        password = self.nome_password_entry.get()
        validar_credentials = DatabaseLogin().verificar_login(utilizador, password)


        if validar_credentials:
            # Mensagem de login bem sucedido
            self.mensagem_registo_concluido = Label(self.janela_login, text='Login feito com Sucesso', fg='green')
            self.mensagem_registo_concluido.grid(row=3, column=0, columnspan=2)
            self.mensagem_registo_concluido.after(3000, self.mensagem_registo_concluido.destroy)
            self.abrir_janela_menu()
            

        else:
            # Mensagem de login inválido
            self.mensagem_erro = Label(self.janela_login, text='Credenciais inválidas', fg='red')
            self.mensagem_erro.grid(row=3, column=0, columnspan=2)
            self.mensagem_erro.after(3000, self.mensagem_erro.destroy)
    
    def abrir_janela_menu(self):
            self.janela_login.withdraw()
            JanelaMenu()



class DatabaseLogin():
    def __init__(self):
        self.conn = sqlite3.connect('stock.db')
        self.cursor = self.conn.cursor()
        
    def verificar_login(self, utilizador, password):
         # Executa uma consulta SQL para selecionar a password da tabela utilizadores onde o utilizador corresponde ao fornecido como argumento
         self.cursor.execute("SELECT password FROM utilizadores WHERE utilizador=?", (utilizador,))
         # Obtém a primeira linha do resultado da consulta
         match = self.cursor.fetchone()

         # Verifica se a linha existe (ou seja, se o utilizador existe)
         if match:
            # Extrai a password armazenada na linha
            db_password = match[0]
            # Divide a password armazenada em duas partes: o salt e o hash da password
            salt, hash_pass = db_password.split(':')
            # Calcula o hash da password fornecida usando o mesmo salt e compara com o hash armazenado na base de dados
            input_hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 100000).hex()
            if input_hashed_password == hash_pass:
                # Se os hashes coincidirem, retorna True (autenticação bem-sucedida)
                return True

         # Retorna False se o utilizador não existir ou se as passwords não coincidirem
         return False
    
    def __del__(self):
        # Fecha a ligação com a base de dados
        self.conn.close()

