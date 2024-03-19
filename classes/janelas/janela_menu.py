from tkinter import *
from tkinter import Tk
from classes.janelas.janela_inserir_menu import JanelaInserirMenu
from classes.janelas.janela_pesquisar_menu import JanelaPesquisarMenu
import sqlite3


class JanelaMenu:
    def __init__(self):
        self.janela_menu = Toplevel() #abre nova janela
        self.janela_menu.title('Menu')

        self_texto_menu = Label(self.janela_menu, text='Menu', font='Arial 20')
        self_texto_menu.grid(row=0, column=0, padx=20, pady=20)

        #criar opções
        self_inserir_btn = Button(self.janela_menu, text='Inserir', font='Arial 14', command= JanelaInserirMenu)
        self_inserir_btn.grid(row=1, column=0, pady=20, sticky='NSEW', padx=20)

        self_pesquisar_btn = Button(self.janela_menu, text='Filmes', font='Arial 14', command= JanelaPesquisarMenu)
        self_pesquisar_btn.grid(row=2, column=0, pady=20, sticky='NSEW', padx=20)

        self_logout_btn = Button(self.janela_menu, text='Logout', font='Arial 14', command=self.janela_menu.destroy)
        self_logout_btn.grid(row=3, column=0, pady=20, sticky='NSEW', padx=20)
