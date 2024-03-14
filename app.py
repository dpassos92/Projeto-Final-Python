#importação
from classes.janelas.janela_principal import JanelaPrincipal

#função main
def main():
    janela = JanelaPrincipal()
    janela.janela_principal.mainloop()

#roda função main se o arquivo for executado
if __name__ == '__main__':
    main()
