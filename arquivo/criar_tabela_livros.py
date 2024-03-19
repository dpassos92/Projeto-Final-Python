import sqlite3

#1 ligar à base de dados
conn = sqlite3.connect('stock.db')

#2 criar um cursor
cursor = conn.cursor()

#3 Comando SQL para criar a tabela
#id integer pk
#utilizador text not null unique
#password text not null

criar_tabela_3 = '''
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT NOT NULL,
        ano INT CHECK (ano >= 1900 AND ano <= 2024),
        genero TEXT NOT NULL,
        imagem_path TEXT
    );
'''

#4 executar o comando sql com o cursor
cursor.execute(criar_tabela_3)

#5 guardar com um commit
conn.commit()

#6 fechar a ligação
conn.close

print('Guardado com sucesso')

alterar_tabela_livros_2 = '''
    ALTER TABLE livros
    ADD COLUMN autor TEXT NOT NULL;
'''

# 4. Executar o comando SQL
cursor.execute(alterar_tabela_livros_2)

# 5. Salvar as alterações com commit
conn.commit()

# 6. Fechar a conexão
conn.close()

print('Atributo "autor" adicionado à tabela "livros" com sucesso.')


# Eliminar dados para adicionar atributos "quantidade" e "preço" como NOT NULL
eliminar_dados = '''
    DELETE FROM livros;
'''

cursor.execute(eliminar_dados)
conn.commit()
print('Eliminado com sucesso')


# Adicionar quantidade
alterar_tabela_livros_3 = '''
    ALTER TABLE livros
    ADD COLUMN quantidade INT NOT NULL;
'''

cursor.execute(alterar_tabela_livros_3)
conn.commit()
print('Atributo "quantidade" adicionado à tabela "livros" com sucesso.')

# Adicionar preço
alterar_tabela_livros_4 = '''
    ALTER TABLE livros
    ADD COLUMN preco DECIMAL(10, 2) NOT NULL;
'''

cursor.execute(alterar_tabela_livros_4)
conn.commit()
conn.close
print('Atributo "preço" adicionado à tabela "livros" com sucesso.')
