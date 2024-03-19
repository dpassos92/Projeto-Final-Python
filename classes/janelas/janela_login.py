#importações
from tkinter import *
from tkinter import Tk, messagebox
import sqlite3
import hashlib


#Criar a classe para a janela de registo
class JanelaLogin:
    def __init__(self, janela_principal=None):

        #criar a janela principal
        self.janela_principal =  janela_principal
        self.janela_login = Toplevel() #cria a janela
        self.janela_login.title('Registo de utilizadores') #muda o titulo
        self.janela_login.configure(bg='#f0f0f0') #altera a cor de fundo
        self.janela_login.geometry(self.calcular_posicao()) # Posição da janela no ecrã

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
        self.registar_btn = Button(self.janela_login, text='Entrar', font='Arial 14', command=self.verificar_login)
        self.registar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

    def verificar_login(self):
        utilizador = self.nome_utilizador_entry.get()
        password = self.nome_password_entry.get()

        #ligação à base de dados
        self.conn = sqlite3.connect('stock.db')
        self.cursor = self.conn.cursor()
        
    
         # Executa uma consulta SQL para selecionar a password da tabela utilizadores onde o utilizador corresponde ao fornecido como argumento
        self.cursor.execute("SELECT password FROM utilizadores WHERE utilizador=?", (utilizador,))
         # Obtém a primeira linha do resultado da consulta
        match = self.cursor.fetchone()
        self.conn.close()

         # Verifica se a linha existe (ou seja, se o utilizador existe)
        if match:
            # Extrai a password armazenada na linha
            db_password = match[0]
            # Divide a password armazenada em duas partes: o salt e o hash da password
            salt, hash_pass = db_password.split(':')
            # Calcula o hash da password fornecida usando o mesmo salt e compara com o hash armazenado na base de dados
            input_hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 100000).hex()
            if input_hashed_password == hash_pass:
                messagebox.showinfo("Login", "Login bem-sucedido!")
                self.janela_login.destroy() # Fecha a janela de login após sucesso
                if self.janela_principal:
                    self.janela_principal.abrir_janela_menu() # Abre a janela de menu
                else:
                    messagebox.showerror("Erro", "Password incorreta.")
            else:
                messagebox.showerror("Erro", "Utilizador não encontrado.")
    
    #definir a posição no ecra
    def calcular_posicao(self):
        #definir largura e altura da janela
        largura_janela = 450
        altura_janela = 300

        #obter largura e altura do ecrã
        largura_ecra = self.janela_login.winfo_screenwidth()
        altura_ecra = self.janela_login.winfo_screenheight()

        #calcular a posição x e y
        x = (largura_ecra // 2) - (largura_janela // 2)
        y = (altura_ecra // 2) - (altura_janela // 2)

        #definir a posição da janela
        return f'{largura_janela}x{altura_janela}+{x}+{y}'
        
