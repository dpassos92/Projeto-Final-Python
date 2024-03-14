from tkinter import *
from tkinter import Tk

class JanelaMenu:
    def __init__(self):
        self.janela_menu = Tk()
        self.janela_menu.title('Menu')

        self_texto_menu = Label(self.janela_menu, text='Menu', font='Arial 20')
        self_texto_menu.grid(row=0, column=0, padx=20, pady=20)

        #criar opções
        self_inserir_btn = Button(self.janela_menu, text='Inserir', font='Arial 14', command=self.abrir_menu_inserir) #falta inserir o command para ir para o menu de escolher a categora a inserir
        self_inserir_btn.grid(row=1, column=0, pady=20, sticky='NSEW', padx=20)

        self_pesquisar_btn = Button(self.janela_menu, text='Pesquisar(editar ou remover)', font='Arial 14', command=self.abrir_menu_pesquisar)
        self_pesquisar_btn.grid(row=2, column=0, pady=20, sticky='NSEW', padx=20)

        self_logout_btn = Button(self.janela_menu, text='Logout', font='Arial 14', command=self.janela_menu.destroy)
        self_logout_btn.grid(row=3, column=0, pady=20, sticky='NSEW', padx=20)


    def iniciar(self):
        self.janela_menu.mainloop()

    def abrir_menu_inserir(self):
        from janela_inserir_menu import JanelaInserirMenu
        janela_inserir = JanelaInserirMenu()
        janela_inserir.iniciar()

    def abrir_menu_pesquisar(self):
        from janela_pesquisar_menu import JanelaPesquisarMenu
        janela_inserir_pesquisa = JanelaPesquisarMenu()
        janela_inserir_pesquisa.iniciar()

# Criar uma instância da classe JanelaMenu e iniciar a interface gráfica
menu = JanelaMenu()
menu.iniciar()
