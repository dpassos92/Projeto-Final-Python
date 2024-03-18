import sqlite3

#1 ligar à base de dados
conn = sqlite3.connect('stock.db')

#2 criar um cursor
cursor = conn.cursor()

#3 Comando SQL para criar a tabela
#id integer pk
#utilizador text not null unique
#password text not null

eliminar_tabela = '''DROP TABLE  IF EXISTS vinyl;'''

#4 executar o comando sql com o cursor
cursor.execute(eliminar_tabela)

#5 guardar com um commit
conn.commit()

#6 fechar a ligação
conn.close

print('Guardado com sucesso')