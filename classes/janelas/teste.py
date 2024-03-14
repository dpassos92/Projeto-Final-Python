from tkinter import Tk, Button

class JanelaMenu:
    def __init__(self):
        self.janela_menu = Tk()
        self.janela_menu.title('Menu')
        self.janela_menu.geometry('400x300')

class JanelaInserirMenu:
    def __init__(self):
        self.janela_inserir_menu = Tk()
        self.janela_inserir_menu.title('Menu inserir')

        self.botao_retroceder = Button(self.janela_inserir_menu, text='Voltar atrás', font='Arial 14', command=self.voltar_menu)
        self.botao_retroceder.grid(row=1, column=0, padx=20, pady=20)

    def voltar_menu(self):
        self.janela_inserir_menu.withdraw()  # Oculta a janela atual
        self.exibir_janela_menu()  # Exibe a janela JanelaMenu

    def exibir_janela_menu(self):
        janela_menu = JanelaMenu()  # Cria uma nova instância da classe JanelaMenu
        janela_menu.janela_menu.mainloop()  # Exibe a janela JanelaMenu

    def iniciar(self):
        self.janela_inserir_menu.mainloop()

# Criar uma instância da classe JanelaInserirMenu e iniciar a interface gráfica
menu_inserir = JanelaInserirMenu()
menu_inserir.iniciar()
