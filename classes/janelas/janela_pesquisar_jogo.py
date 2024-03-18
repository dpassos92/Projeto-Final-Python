from tkinter import *
from tkinter import Tk, Button
import sqlite3


class JanelaPesquisarJogo:
    def __init__(self):
        self.janela_pesquisar_jogo= Toplevel()
        self.janela_pesquisar_jogo.title('Pesquisar Jogo')

        # criar uma label para exibir 'Infomação do jogo'
        self.janela_pesquisar_jogo_lbl = Label(self.janela_pesquisar_jogo, text='Informação Jogo', font='Arial 20')
        self.janela_pesquisar_jogo_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

        # criar campo para o título do jogo
        self.janela_pesquisar_jogo_lbl = Label(self.janela_pesquisar_jogo, text='Título', font='Arial 14')
        self.janela_pesquisar_jogo_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.janela_pesquisar_jogo_entry = Entry(self.janela_pesquisar_jogo, font='Arial 14')
        self.janela_pesquisar_jogo_entry.grid(row=1, column=1, padx=(0,10), sticky='W')

        # criar campo para a plataform do jogo
        self.janela_pesquisar_jogo_lbl = Label(self.janela_pesquisar_jogo, text='Plataforma', font='Arial 14')
        self.janela_pesquisar_jogo_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.janela_pesquisar_jogo_entry = Entry(self.janela_pesquisar_jogo, font='Arial 14')
        self.janela_pesquisar_jogo_entry.grid(row=2, column=1, padx=(0, 10), pady=10, sticky='W')

        # criar capo para o ano do jogo
        self.janela_pesquisar_jogo_lbl = Label(self.janela_pesquisar_jogo, text='Ano', font='Arial 14')
        self.janela_pesquisar_jogo_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.janela_pesquisar_jogo_entry = Entry(self.janela_pesquisar_jogo, font='Arial 14')
        self.janela_pesquisar_jogo_entry.grid(row=3, column=1, padx=(0,10), pady=10, sticky='W')
        
        # configuração do botão para pesquisar
        # falta o command
        self.pesquisar_btn = Button(self.janela_pesquisar_jogo, text='Pesquisar Jogo', font='Arial 14')
        self.pesquisar_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        # configuração do botão para retroceder
        # falta o command
        self.retroceder_btn = Button(self.janela_pesquisar_jogo, text='Voltar atrás', font='Arial 10 bold', command=self.janela_pesquisar_jogo.destroy)
        self.retroceder_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky='NSEW')