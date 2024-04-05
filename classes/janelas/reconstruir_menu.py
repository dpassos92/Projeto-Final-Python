#importações
from tkinter import *
from tkinter import Tk, ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
import customtkinter    

class ReconstruirMenu:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal

    def reconstruir_menu(self):
        for widget in self.janela_principal.winfo_children():
            widget.destroy()

        self.janela_principal.title("Sistema de Gestão de Produtos")  # Título da janela
        #self.janela_principal.iconbitmap("assets/icon/icon.ico")  # Ícone da janela
        self.janela_principal.geometry("600x500")  # Posição da janela no ecrã
        self.janela_principal.state('zoomed')  # Maximizar a janela~

        self.janela_principal.grab_set()

        customtkinter.CTkLabel(self.janela_principal, text="Escolha a categoria de produto: ", font=("Arial", 18)).pack(padx=10, pady=10)

        self.janela_principal_livros_btn = customtkinter.CTkButton(self.janela_principal, text='Livros', command= self.abrir_janela_livros)
        self.janela_principal_livros_btn.pack(padx=10, pady=10)

        self.janela_principal_filmes_btn = customtkinter.CTkButton(self.janela_principal, text='Filmes', command= self.abrir_janela_filmes)
        self.janela_principal_filmes_btn.pack(padx=10, pady=10)

        self.janela_principal_jogos_btn = customtkinter.CTkButton(self.janela_principal, text='Jogos', command= self.abrir_janela_jogos)
        self.janela_principal_jogos_btn.pack(padx=10, pady=10)

        self.janela_principal_vinyl_btn = customtkinter.CTkButton(self.janela_principal, text='Vinyl', command= self.abrir_janela_vinyl)
        self.janela_principal_vinyl_btn.pack(padx=10, pady=10)

    def abrir_janela_livros(self):
        from classes.janelas.livros import CategoriaLivro
        categoria_livro = CategoriaLivro(self.janela_principal)  # Criar um objeto da classe CategoriaLivro
        categoria_livro.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal

    def abrir_janela_filmes(self):
        from classes.janelas.filmes import CategoriaFilme
        categoria_filme = CategoriaFilme(self.janela_principal)  # Criar um objeto da classe CategoriaFilme
        categoria_filme.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal

    def abrir_janela_jogos(self):
        from classes.janelas.jogos import CategoriaJogo
        categoria_jogo = CategoriaJogo(self.janela_principal)  # Criar um objeto da classe CategoriaJogo
        categoria_jogo.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal

    def abrir_janela_vinyl(self):
        from classes.janelas.vinyl import CategoriaVinyl
        categoria_vinyl = CategoriaVinyl(self.janela_principal)  # Criar um objeto da classe CategoriaJogo
        categoria_vinyl.abrir_janela_menu()  # Chamar o método abrir_janela_menu() neste objeto, na janela principal'''

    