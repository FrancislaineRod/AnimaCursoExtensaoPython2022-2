#1° passo: importar a biblioteca sqlite3
import sqlite3

#2° passo: vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3° passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4° passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas(pessoa_id,nome,nome_civil,tipo)VALUES (12,'The Flash','Barry Allen','Herói(na)')"

#5° passo: executar o comando SQL
cursor.execute(sql)

#6° passo: confirmar o INSERT com o commit() e fechar o banco
conexao.commit()
conexao.close()