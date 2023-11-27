import sqlite3



def criar_tabela():
  #conecta ao db
  connection = sqlite3.connect("revisao2.db")
  cursor = connection.cursor()

  #cria a tabela usuarios
  cursor.execute( '''
  CREATE TABLE IF NOT EXISTS usuarios(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 email TEXT NOT NULL,
                 idade INTEGER NOT NULL
  )
''')
  connection.commit() # salva a alteração do db
  connection.close() # fecha a conexao com o db


def visualizar_lista():
  connection = sqlite3.connect('revisao2.db')
  cursor = connection.cursor()

  cursor.execute("SELECT * FROM usuarios")
  linhas = cursor.fetchall()
  print("\nLista de usuarios: ")
  print("\t ID - \tNome - \tEmail - \tIdade")
  for linha in linhas:
    print('\t',linha)
  connection.close()


def visualizar_lista_formatada():
  connection = sqlite3.connect('revisao2.db')
  cursor = connection.cursor()

  curso.execute('SELECT * FROM usuarios')
  linhas = cursor.fetchall()
  print("Lista Formatada: ")

  for coluna in linhas:
    print(
      f'''\t ID: {coluna[0]} - Usuario: {coluna[1]}'''
    )
    
  connection.close()


def adicionar_usuario():
  nome = input("Digite nome: ")
  email = input("Digite Email: ")
  idade = int(input("Digite a idade: "))

  connection = sqlite3.connect('revisao2.db')
  cursor = connection.cursor()

  cursor.execute(f'''
  INSERT INTO usuarios(nome, email, idade) VALUES('{nome}', '{email}', '{idade}')
''')
  connection.commit()
  connection.close()
  print(f"\nUsuario {nome} adicionado com sucesso! \n ")


def deletar_dados():
  connection = sqlite3.connect('revisao2.db')
  cursor = connection.cursor()
  visualizar_lista_formatada()
  id = int(input("Digite o id a ser deletado: "))

  cursor.execute(f'DELETE FROM usuarios WHERE id = {id}')
  connection.commit()
  connection.close()
  print("Usuario excluido com sucesso! ")

##################### FIM funções ##################


criar_tabela()
# adicionar_usuario()
# deletar_dados()
# visualizar_lista()

####### MENU ############

print("\n\tMenu opções ")

while True:
  opc = int(input('''
     opc   ----    acão
      1    ----  Adicionar Usuario
      2    ----  Deletar Usuario
      3    ----  Visualisar Lista de usuarios
      4    ----  Sair
      5    ----  Visualisar Formatado
            Digite a opção desejada: '''
  ))
  
  if opc == 4:
    break
  elif opc == 1:
    adicionar_usuario()
  elif opc == 2:
    deletar_dados()
  elif opc == 3:
    visualizar_lista()
  elif opc == 5:
    visualizar_lista_formatada()
  else:
    print("Opção invalida! Verifique opção desejada...")
    continue
