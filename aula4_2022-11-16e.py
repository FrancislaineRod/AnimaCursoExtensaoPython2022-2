import aula4_2022_11_16c as bd

def consulta_pessoas_grupos_e_mostra(cursor):
    sql = "SELECT pessoa_id, grupo_id FROM pessoas_grupos"  # confirmando quais são os grupos que estão disponíveis
    cursor.execute(sql)
    pessoas_grupos = cursor.fetchall()

    print("Tabela pessoas_grupo")
    for pessoa_grupo in pessoas_grupos:
        print(pessoa_grupo)

con, cur = bd.conectar()

# 1o passo: Consultar a tabela grupos
sql = "SELECT grupo_id, nome FROM grupos" # confirmando quais são os grupos que estão disponíveis
cur.execute(sql)

# Mostra todos do grupo_pessoa
grupos = cur.fetchall() 
for grupo in grupos:
    print(grupo)

# 2o passo: Consultar a tabela pessoas_grupo
consulta_pessoas_grupos_e_mostra(cur)

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")
pessoa_id = 12
grupo_id = input("Tecle 1 - para grupo Sociedade da Justiça da América, 2 - Liga da Justiça, 3 - Tropa dos Lanternas Verdes, 4 - Esquadrão Suicida: ")

#Consulta aqui a tabela grupos e exibe na tela, pedindo para o usuário digitar o grupo_id

#Jason Momoa
#Aquaman
  
#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)

#Insert pessoas_grupos
sql = f"INSERT or REPLACE INTO pessoas_grupos (pessoa_id,  grupo_id) VALUES ('{pessoa_id}', '{grupo_id}')"
cur.execute(sql)

# Confirmar o INSERT com commit() e fechar o banco

con.commit()

# Precisa selecionar novamente

consulta_pessoas_grupos_e_mostra(cur)
  
con.close()