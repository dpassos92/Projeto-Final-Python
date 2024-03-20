#importações
from tkinter import *
from tkinter import Tk, ttk, messagebox
from classes.janelas.janela_registo import JanelaRegisto
from classes.janelas.janela_login import JanelaLogin
import sqlite3
from classes.janelas.livros import  CategoriaLivro
from classes.janelas.filmes import CategoriaFilme
from classes.janelas.jogos import CategoriaJogo
from classes.janelas.vinyl import CategoriaVinyl

#classe da janela principal
class JanelaPrincipal:
    def __init__(self):

        #criar a janela principal
        self.janela_principal = Tk() #cria a janela
        self.janela_principal.title('Sistema de Gestão de Produtos') #muda o titulo
        self.janela_principal.configure(bg='#f0f0f0') #altera a cor de fundo

        #configuração do texto de boas vindas
        self.boas_vindas_lbl = Label(self.janela_principal, text='Sistema de Gestão de Produtos', font='Arial 20', bg='#f0f0f0', fg='#333333')
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
        JanelaLogin(janela_principal=self)

    
    #definir a posição no ecra
    def calcular_posicao(self, largura_janela=400, altura_janela=300):

        #obter largura e altura do ecrã
        largura_ecra = self.janela_principal.winfo_screenwidth()
        altura_ecra = self.janela_principal.winfo_screenheight()

        #calcular a posição x e y
        x = (largura_ecra // 2) - (largura_janela // 2)
        y = (altura_ecra // 2) - (altura_janela // 2)

        #definir a posição da janela
        return f'{largura_janela}x{altura_janela}+{x}+{y}'


    #Definir a janela de menu após login
    def abrir_janela_menu(self):
        for widget in self.janela_principal.winfo_children():
            widget.destroy()

        self.janela_principal.title("Sistema de Gestão de Produtos")  # Título da janela
        self.janela_principal.iconbitmap("assets/icon/icon.ico")  # Ícone da janela
        self.janela_principal.configure(bg="#f0f0f0")  # Cor de fundo da janela
        self.janela_principal.geometry(self.calcular_posicao())  # Posição da janela no ecrã
        self.janela_principal.state('zoomed')  # Maximizar a janela

        self.janela_principal_livros_btn = Button(self.janela_principal, text='Livros', font='Arial 14', command= self.abrir_janela_livros)
        self.janela_principal_livros_btn.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.janela_principal_filmes_btn = Button(self.janela_principal, text='Filmes', font='Arial 14', command= self.abrir_janela_filmes)
        self.janela_principal_filmes_btn.grid(row=1, column=3, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.janela_principal_jogos_btn = Button(self.janela_principal, text='Filmes', font='Arial 14', command= self.abrir_janela_jogos)
        self.janela_principal_jogos_btn.grid(row=1, column=5, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.janela_principal_vinyl_btn = Button(self.janela_principal, text='Vinyl', font='Arial 14', command= self.abrir_janela_vinyl)
        self.janela_principal_vinyl_btn.grid(row=1, column=7, columnspan=2, padx=20, pady=10, sticky='NSEW')


    def abrir_janela_livros(self):
        categoria_livro = CategoriaLivro(self.janela_principal)  # Criar um objeto da classe CategoriaLivro
        categoria_livro.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal

    def abrir_janela_filmes(self):
        categoria_filme = CategoriaFilme(self.janela_principal)  # Criar um objeto da classe CategoriaFilme
        categoria_filme.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal

    def abrir_janela_jogos(self):
        categoria_jogo = CategoriaJogo(self.janela_principal)  # Criar um objeto da classe CategoriaJogo
        categoria_jogo.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal

    def abrir_janela_vinyl(self):
        categoria_vinyl = CategoriaVinyl(self.janela_principal)  # Criar um objeto da classe CategoriaJogo
        categoria_vinyl.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal


    def reconstruir_interface(self):
        # Limpar a janela
        for widget in self.janela_principal.winfo_children():
            widget.destroy()

        # recrear interface
        self.janela_principal.title("Sistema de Gestão de Produtos")
        self.janela_principal.iconbitmap("assets/icon/icon.ico")
        self.janela_principal.configure(bg="#f0f0f0")
        self.janela_principal.geometry(self.calcular_posicao())
        self.janela_principal.state('zoomed')

        self.janela_principal_livros_btn = Button(self.janela_principal, text='Livros', font='Arial 14', command=self.abrir_janela_livros)
        self.janela_principal_livros_btn.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.janela_principal_filmes_btn = Button(self.janela_principal, text='Filmes', font='Arial 14', command=self.abrir_janela_filmes)
        self.janela_principal_filmes_btn.grid(row=1, column=3, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.janela_principal_jogos_btn = Button(self.janela_principal, text='Filmes', font='Arial 14', command=self.abrir_janela_jogos)
        self.janela_principal_jogos_btn.grid(row=1, column=5, columnspan=2, padx=20, pady=10, sticky='NSEW')

        self.janela_principal_vinyl_btn = Button(self.janela_principal, text='Vinyl', font='Arial 14', command=self.abrir_janela_vinyl)
        self.janela_principal_vinyl_btn.grid(row=1, column=7, columnspan=2, padx=20, pady=10, sticky='NSEW')