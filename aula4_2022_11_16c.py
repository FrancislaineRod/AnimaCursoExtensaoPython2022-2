#1° passo: importar a biblioteca sqlite3
import sqlite3

#PASSOS 2 e 3 VIRARÃO funçao conectar()
def conectar():
  #2° passo: vamos estabelecer uma conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #3° passo: criar um objeto do tipo cursor
  cursor = conexao.cursor()
  
  return conexao, cursor