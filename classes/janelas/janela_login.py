#importações
from tkinter import *
from tkinter import Tk, messagebox
import sqlite3
import hashlib
import customtkinter


#Criar a classe para a janela de registo
class JanelaLogin:
    def __init__(self, janela_principal=None):

        #criar a janela principal
        self.janela_login = customtkinter.CTkToplevel()
        self.janela_login.geometry('500X300') # Posição da janela no ecrã

        #criar label login
        self.login_lbl = customtkinter.CTkLabel(self.janela_login, text='Login')
        self.login_lbl.pack(padx=10, pady=10)

        #criar campo utilizador    
        self.nome_utilizador_entry = customtkinter.CTkEntry(self.janela_login, placeholder_text='Utilizador')
        self.nome_utilizador_entry.pack(padx=10, pady=10)

        #criar campo password
        self.nome_password_entry = customtkinter.CTkEntry(self.janela_login, placeholder_text='Password')
        self.nome_password_entry.pack(padx=10, pady=10)

        #configuração do bptão de registar
        self.registar_btn = customtkinter.CTkButton(self.janela_login, text='Entrar', command=self.verificar_login)
        self.registar_btn.pack(padx=10, pady=10)

        #configuração do botão de sair
        self.sair_btn = customtkinter.CTkButton(self.janela_login, text='Sair', command=self.janela_login.destroy)
        self.sair_btn.pack(padx=10, pady=10)

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
    
    
# função para definir a posição no ecra
"""def calcular_posicao(self):
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
    return f'{largura_janela}x{altura_janela}+{x}+{y}'"""
        
