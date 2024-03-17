#importações
from tkinter import *
from tkinter import Tk
from classes.janelas.janela_registo import JanelaRegisto
from classes.janelas.janela_login import JanelaLogin

#classe da janela principal
class JanelaPrincipal:
    def __init__(self):

        #criar a janela principal
        self.janela_principal = Tk() #cria a janela
        self.janela_principal.title('Sistema de Gestão de Produtos') #muda o titulo
        self.janela_principal.configure(bg='#f0f0f0') #altera a cor de fundo

        #configuração do texto de boas vindas
        self.boas_vindas_lbl = Label(self.janela_principal, text='Sistema de Gestão de Produtos', font='Arial 20',
                                     bg='#f0f0f0', fg='#333333')
        self.boas_vindas_lbl.grid(row=0, column=1, columnspan=1, pady=20)
        
        #configuração do botão de registo
        self.registar_btn = Button(self.janela_principal, text='Registar', font='Arial 14', command=self.abrir_janela_registo) #falta command
        self.registar_btn.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky='NSEW')

        #configuração do botão de login
        self.login_btn = Button(self.janela_principal, text='Login', font='Arial 14', command=self.abrir_janela_login) #falta command
        self.login_btn.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky='NSEW')

        #configuração do botão de sair
        self.sair_btn = Button(self.janela_principal, text='Sair', font='Arial 14', command=self.janela_principal.destroy)
        self.sair_btn.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky='NSEW')


    def abrir_janela_registo(self):
        JanelaRegisto()

    def abrir_janela_login(self):
        JanelaLogin()


        
