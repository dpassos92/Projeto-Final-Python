from tkinter import *
from tkinter import Tk, Button
from classes.janelas.janela_pesquisar_filme import JanelaPesquisarFilme
from classes.janelas.janela_pesquisar_jogo import JanelaPesquisarJogo

class JanelaPesquisarMenu:
    def __init__(self):
        self.janela_pesquisar_menu= Toplevel()
        self.janela_pesquisar_menu.title('Menu pesquisar')

        self.botao_retroceder = Button(self.janela_pesquisar_menu, text='Voltar atrás', font='Arial 10 bold', command= self.janela_pesquisar_menu.destroy)
        self.botao_retroceder.grid(row=1, column=0, padx=20, pady=20, sticky='e')

        self.texto_menu_inserir = Label(self.janela_pesquisar_menu, text='Escolha a categoria que quer pesquisar', font='Arial 20')
        self.texto_menu_inserir.grid(row=2, column=0, padx=20, pady=20)

        self.botao_filmes = Button(self.janela_pesquisar_menu, text='Filmes', font='Arial 14', command = JanelaPesquisarFilme)
        self.botao_filmes.grid(row=4, column=0, padx=20, pady=20, sticky='NSEW')

        self.botao_livros = Button(self.janela_pesquisar_menu, text='Livros', font='Arial 14')
        self.botao_livros.grid(row=5, column=0, padx=20, pady=20, sticky='NSEW')

        self.botao_jogos = Button(self.janela_pesquisar_menu, text='Jogos', font='Arial 14', command = JanelaPesquisarJogo)
        self.botao_jogos.grid(row=6, column=0, padx=20, pady=20, sticky='NSEW')

        self.botao_vinyl = Button(self.janela_pesquisar_menu, text='Vinyl', font='Arial 14')
        self.botao_vinyl.grid(row=7, column=0, padx=20, pady=20, sticky='NSEW')


