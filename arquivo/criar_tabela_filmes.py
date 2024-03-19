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
        titulo TEXT NOT NULL UNIQUE,
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


# Eliminar dados para adicionar atributos "quantidade" e "preço" como NOT NULL
eliminar_dados = '''
    DELETE FROM filmes;
'''

cursor.execute(eliminar_dados)
conn.commit()
print('Eliminado com sucesso')


# Adicionar quantidade
alterar_tabela_filmes_2 = '''
    ALTER TABLE filmes
    ADD COLUMN quantidade INT NOT NULL;
'''

cursor.execute(alterar_tabela_filmes_2)
conn.commit()
print('Atributo "quantidade" adicionado à tabela "filmes" com sucesso.')

# Adicionar preço
alterar_tabela_filmes_3 = '''
    ALTER TABLE filmes
    ADD COLUMN preco DECIMAL(10, 2) NOT NULL;
'''

cursor.execute(alterar_tabela_filmes_3)
conn.commit()
conn.close
print('Atributo "preço" adicionado à tabela "filmes" com sucesso.')