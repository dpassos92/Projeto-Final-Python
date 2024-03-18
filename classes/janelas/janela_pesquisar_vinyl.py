from tkinter import *
from tkinter import Tk, Button
import sqlite3


class JanelaPesquisarVinyl:
    def __init__(self):
        self.janela_pesquisar_vinyl= Toplevel()
        self.janela_pesquisar_vinyl.title('Pesquisar Vinyl')

        # criar uma label para exibir 'Infomação do vinyl'
        self.texto_vinyl_lbl = Label(self.janela_pesquisar_vinyl, text='Informação Vinyl', font='Arial 20')
        self.texto_vinyl_lbl.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

        # criar campo para o título do vinyl
        self.titulo_vinyl_lbl = Label(self.janela_pesquisar_vinyl, text='Título', font='Arial 14')
        self.titulo_vinyl_lbl.grid(row=1, column=0, padx=(10,0), pady=10, sticky='W')
        self.titulo_vinyl_entry = Entry(self.janela_pesquisar_vinyl, font='Arial 14')
        self.titulo_vinyl_entry.grid(row=1, column=1, padx=(0,10), sticky='W')

        # criar campo para o artista do vinyl
        self.artista_vinyl_lbl = Label(self.janela_pesquisar_vinyl, text='Artista', font='Arial 14')
        self.artista_vinyl_lbl.grid(row=2, column=0, padx=(10,0), pady=10, sticky='W')
        self.artista_vinyl_entry = Entry(self.janela_pesquisar_vinyl, font='Arial 14')
        self.artista_vinyl_entry.grid(row=2, column=1, padx=(0, 10), pady=10, sticky='W')

        # criar capo para o ano do vinyl
        self.ano_vinyl_lbl = Label(self.janela_pesquisar_vinyl, text='Ano', font='Arial 14')
        self.ano_vinyl_lbl.grid(row=3, column=0, padx=(10,0), pady=10, sticky='W')
        self.ano_vinyl_entry = Entry(self.janela_pesquisar_vinyl, font='Arial 14')
        self.ano_vinyl_entry.grid(row=3, column=1, padx=(0,10), pady=10, sticky='W')
        
        # configuração do botão para pesquisar
        # falta o command
        self.pesquisar_btn = Button(self.janela_pesquisar_vinyl, text='Pesquisar Vinyl', font='Arial 14')
        self.pesquisar_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        # configuração do botão para retroceder
        # falta o command
        self.retroceder_btn = Button(self.janela_pesquisar_vinyl, text='Voltar atrás', font='Arial 10 bold', command=self.janela_pesquisar_vinyl.destroy)
        self.retroceder_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky='NSEW')