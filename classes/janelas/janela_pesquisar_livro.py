from tkinter import *
from tkinter import Tk, Button
import sqlite3


class JanelaPesquisarLivro:
    def __init__(self):
        self.janela_pesquisar_livro= Toplevel()
        self.janela_pesquisar_livro.title('Pesquisar Livro')

        # criar uma label para exibir 'Infomação do livro'
        self.texto_livro_lbl = Label(self.janela_pesquisar_livro, text='Informação Livro', font='Arial 20')
        self.texto_livro_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

        # criar campo para o título do livro
        self.titulo_livro_lbl = Label(self.janela_pesquisar_livro, text='Título', font='Arial 14')
        self.titulo_livro_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.titulo_livro_entry = Entry(self.janela_pesquisar_livro, font='Arial 14')
        self.titulo_livro_entry.grid(row=1, column=1, padx=(0,10), sticky='W')

        # criar campo para o autor do livro
        self.autor_livro_lbl = Label(self.janela_pesquisar_livro, text='Autor', font='Arial 14')
        self.autor_livro_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.autor_livro_entry = Entry(self.janela_pesquisar_livro, font='Arial 14')
        self.autor_livro_entry.grid(row=2, column=1, padx=(0, 10), pady=10, sticky='W')

        # criar capo para o ano do livro
        self.ano_livro_lbl = Label(self.janela_pesquisar_livro, text='Ano', font='Arial 14')
        self.ano_livro_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.ano_livro_entry = Entry(self.janela_pesquisar_livro, font='Arial 14')
        self.ano_livro_entry.grid(row=3, column=1, padx=(0,10), pady=10, sticky='W')
        
        # configuração do botão para pesquisar
        # falta o command
        self.pesquisar_btn = Button(self.janela_pesquisar_livro, text='Pesquisar Livro', font='Arial 14')
        self.pesquisar_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        # configuração do botão para retroceder
        # falta o command
        self.retroceder_btn = Button(self.janela_pesquisar_livro, text='Voltar atrás', font='Arial 10 bold', command=self.janela_pesquisar_livro.destroy)
        self.retroceder_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky='NSEW')