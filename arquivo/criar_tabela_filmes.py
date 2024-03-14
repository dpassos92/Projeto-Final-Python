import sqlite3

#1 ligar à base de dados
conn = sqlite3.connect('stock.db')

#2 criar um cursor
cursor = conn.cursor()

#3 Comando SQL para criar a tabela
#id integer pk
#utilizador text not null unique
#password text not null

criar_tabela_2 = '''
    CREATE TABLE IF NOT EXISTS filmes(
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        realizador TEXT NOT NULL,
        ano INT CHECK (ano >= 1900 AND ano <= 2024),
        genero TEXT NOT NULL,
        imagem_path TEXT
    );
'''

#4 executar o comando sql com o cursor
cursor.execute(criar_tabela_2)

#5 guardar com um commit
conn.commit()

#6 fechar a ligação
conn.close

print('Guardado com sucesso')