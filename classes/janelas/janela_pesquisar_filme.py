from tkinter import *
from tkinter import Tk, Button
import sqlite3


class JanelaPesquisarFilme:
    def __init__(self):
        self.janela_pesquisar_filme= Toplevel()
        self.janela_pesquisar_filme.title('Pesquisar Filme')

        # criar uma label para exibir 'Infomação do filme'
        self.texto_filme_lbl = Label(self.janela_pesquisar_filme, text='Informação Filme', font='Arial 20')
        self.texto_filme_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

        # criar campo para o título do filme
        self.titulo_filme_lbl = Label(self.janela_pesquisar_filme, text='Título', font='Arial 14')
        self.titulo_filme_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.titulo_filme_entry = Entry(self.janela_pesquisar_filme, font='Arial 14')
        self.titulo_filme_entry.grid(row=1, column=1, padx=(0,10), sticky='W')

        # criar campo para o realizador do filme
        self.realizador_filme_lbl = Label(self.janela_pesquisar_filme, text='Realizador', font='Arial 14')
        self.realizador_filme_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.realizador_filme_entry = Entry(self.janela_pesquisar_filme, font='Arial 14')
        self.realizador_filme_entry.grid(row=2, column=1, padx=(0, 10), pady=10, sticky='W')

        # criar capo para o ano do filme
        self.ano_filme_lbl = Label(self.janela_pesquisar_filme, text='Ano', font='Arial 14')
        self.ano_filme_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.ano_filme_entry = Entry(self.janela_pesquisar_filme, font='Arial 14')
        self.ano_filme_entry.grid(row=3, column=1, padx=(0,10), pady=10, sticky='W')
        
        # configuração do botão para pesquisar
        # falta o command
        self.pesquisar_btn = Button(self.janela_pesquisar_filme, text='Pesquisar Filme', font='Arial 14')
        self.pesquisar_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        # configuração do botão para retroceder
        # falta o command
        self.retroceder_btn = Button(self.janela_pesquisar_filme, text='Voltar atrás', font='Arial 10 bold', command=self.janela_pesquisar_filme.destroy)
        self.retroceder_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky='NSEW')


    def pesquisar_livro(self):
        # pegar nos dados inseridos
        # titulo_filme = self
        pass