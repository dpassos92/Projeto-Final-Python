#importações
from tkinter import *
from tkinter import Tk
import sqlite3
import hashlib
import os
import customtkinter

#Criar a classe para a janela de registo
class JanelaRegisto:
    def __init__(self, janela_principal=None):

        #criar a janela principal
        self.janela_principal =  janela_principal
        self.janela_registo = customtkinter.CTkToplevel() #cria a janela
        self.janela_registo.title("Sistema de Gestão de Produtos")
        self.janela_registo.iconbitmap("assets/icon/icon.ico")  # Ícone da janela
        self.janela_registo.geometry('500x300')

        self.janela_registo.grab_set()

        #criar label registo
        self.registo_lbl = customtkinter.CTkLabel(self.janela_registo, text='Registo', font=("Arial bold", 14))
        self.registo_lbl.pack(padx=10, pady=10)

        #criar campo utilizador
        self.nome_utilizador_entry = customtkinter.CTkEntry(self.janela_registo, placeholder_text='Utilizador')
        self.nome_utilizador_entry.pack(padx=10, pady=10)

        #criar campo password
        self.nome_password_entry = customtkinter.CTkEntry(self.janela_registo, placeholder_text='Password', show='*')
        self.nome_password_entry.pack(padx=10, pady=10)

        #configuração do botão de registar
        self.registar_btn = customtkinter.CTkButton(self.janela_registo, text='Registar', command=self.registar_utilizador)
        self.registar_btn.pack(padx=10, pady=10)

        #configuração do botão de sair
        self.sair_btn = customtkinter.CTkButton(self.janela_registo, text='Sair', command=self.janela_registo.destroy)
        self.sair_btn.pack(padx=10, pady=10)
        
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

        cursor.execute("SELECT utilizador FROM utilizadores WHERE utilizador=?", (dados_utilizador,))
         # Obtém a primeira linha do resultado da consulta
        match = cursor.fetchone()

        if match:
            self.mensagem_registo_concluido = customtkinter.CTkLabel(self.janela_registo, text='Registo já existe...')
            self.mensagem_registo_concluido.pack(padx=10, pady=10)
            self.mensagem_registo_concluido.after(3000, self.mensagem_registo_concluido.destroy)
        else:
            cursor.execute(
                'INSERT INTO utilizadores (utilizador, password) VALUES (?, ?)', (dados_utilizador, password_a_gravar)
            )
            conn.commit()
            conn.close()
            
            #mensagem de sucesso no registo
            self.mensagem_registo_concluido = customtkinter.CTkLabel(self.janela_registo, text='Registo feito com Sucesso')
            self.mensagem_registo_concluido.pack(padx=10, pady=10)
            self.mensagem_registo_concluido.after(3000, self.janela_registo.destroy)
