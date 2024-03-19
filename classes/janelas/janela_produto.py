import tkinter as tk
import sqlite3

# Função para exibir os dados dos filmes
def exibir_filmes():
    # Conectar ao banco de dados
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()

    # Executar uma consulta SQL para obter todos os filmes
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()

    # Criar uma nova janela para exibir os dados
    exibir_window = tk.Tk()
    exibir_window.title("Filmes")

    # Criar e posicionar rótulos e atributos dos filmes usando o método grid
    row = 0
    for filme in filmes:
        tk.Label(exibir_window, text="Título:").grid(row=row, column=0, sticky='w')
        tk.Label(exibir_window, text=filme[1]).grid(row=row, column=1, sticky='w')
        row += 1

        tk.Label(exibir_window, text="Realizador:").grid(row=row, column=0, sticky='w')
        tk.Label(exibir_window, text=filme[2]).grid(row=row, column=1, sticky='w')
        row += 1

        tk.Label(exibir_window, text="Ano:").grid(row=row, column=0, sticky='w')
        tk.Label(exibir_window, text=str(filme[3])).grid(row=row, column=1, sticky='w')
        row += 1

        tk.Label(exibir_window, text="Género:").grid(row=row, column=0, sticky='w')
        tk.Label(exibir_window, text=filme[4]).grid(row=row, column=1, sticky='w')
        row += 1

        tk.Label(exibir_window, text="Caminho da Imagem:").grid(row=0, column=2, sticky='w')
        tk.Label(exibir_window, text=filme[5]).grid(row=row, column=2, sticky='w')
        row += 1

        # Adicionar um espaço entre os filmes
        tk.Label(exibir_window, text="").grid(row=row)
        row += 1

    # Fechar a conexão com o banco de dados
    conn.close()

    # Iniciar o loop principal da janela de exibição dos filmes
    exibir_window.mainloop()

# Chamar a função para exibir os filmes ao iniciar o programa
exibir_filmes()
