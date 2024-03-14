from tkinter import *
from tkinter import Tk, Button

class JanelaInserirMenu:
    def __init__(self):
        self.janela_inserir_menu = Tk()
        self.janela_inserir_menu.title('Menu inserir')

        self.botao_retroceder = Button(self.janela_inserir_menu, text='Voltar atrás', font='Arial 10 bold')
        self.botao_retroceder.grid(row=1, column=0, padx=20, pady=20, sticky='e')

        self.texto_menu_inserir = Label(self.janela_inserir_menu, text='Escolha a categoria que quer inserir', font='Arial 20')
        self.texto_menu_inserir.grid(row=2, column=0, padx=20, pady=20)

        self.botao_filmes = Button(self.janela_inserir_menu, text='Filmes', font='Arial 14')
        self.botao_filmes.grid(row=4, column=0, padx=20, pady=20, sticky='NSEW')

        self.botao_livros = Button(self.janela_inserir_menu, text='Livros', font='Arial 14')
        self.botao_livros.grid(row=5, column=0, padx=20, pady=20, sticky='NSEW')

        self.botao_jogos = Button(self.janela_inserir_menu, text='Jogos', font='Arial 14')
        self.botao_jogos.grid(row=6, column=0, padx=20, pady=20, sticky='NSEW')

        self.botao_vinyl = Button(self.janela_inserir_menu, text='Vinyl', font='Arial 14')
        self.botao_vinyl.grid(row=7, column=0, padx=20, pady=20, sticky='NSEW')


    def iniciar(self):
        self.janela_inserir_menu.mainloop()

menu_inserir = JanelaInserirMenu()
menu_inserir.iniciar()

