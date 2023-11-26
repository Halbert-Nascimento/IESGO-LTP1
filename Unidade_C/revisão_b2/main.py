import sqlite3

#faz a conexão com db existente, se não existir cria um novo
connection = sqlite3.connect('revisao.db')
cursor = connection.cursor() # cria curso para conexao com db e passar comandos

#criar tabela usuario se não existir, com colunas id, nome, idade
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')


#inserir dados na tabela
def inserir_dados(nome, idade):
  cursor.execute(
    f"INSERT INTO usuarios(nome, idade) VALUES('{nome}', '{idade}')"
  )
  
  #salva as alterações no banco d dados
  connection.commit()

inserir_dados("Halbert", '30')

#fazer uma consulta d dados * seleciona todas a linhas da tabela usuario
cursor.execute(
  "SELECT * FROM usuarios"
)

#recebe os dados da consulta e salva na variavel  rows
rows = cursor.fetchall()

# varre todas as linhas e ostra no terminal
for row in rows:
  print(row)


#fecha conexao com db
connection.close()