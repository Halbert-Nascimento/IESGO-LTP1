import sqlite3



  
def create_table():
  connection = sqlite3.connect('biblioteca.db')
  cursor = connection.cursor()

  cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS livros(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      autor TEXT NOT NULL,
      ano_publicacao INTEGER  NOT NULL)
    '''
  )
  connection.commit()
  connection.close()
########## Fim  função criar tabela #############

def cadastrar_livros():
  connection = sqlite3.connect('biblioteca.db')
  cursor = connection.cursor()

  in_titulo = input("Digite o titulo do livro: ")
  in_autor = input(f"Digite o autor do livro {in_titulo}: ")
  in_ano_publicacao = int(input(f"Digite o ano de publicação do livro {in_titulo}: "))

  cursor.execute(
    f'''
    INSERT INTO livros(titulo, autor, ano_publicacao) VALUES('{in_titulo}', '{in_autor}', '{in_ano_publicacao}')
    '''
  )
  connection.commit()
  connection.close()
  print(f"\n\tLivro {in_titulo} foi salvo...")
########### fim função salva livro ##############


def remover_livro():
  connection = sqlite3.connect('biblioteca.db')
  cursor = connection.cursor()
  visualizar_livros()

  id_remover = int(input("\tDigite o ID do livro que deseja remover: "))
  
  cursor.execute(
    f'''
    DELETE FROM livros WHERE id = {id_remover}
    '''
  )
  connection.commit()
  connection.close()
  print("\n\t Livro removido com sucesso!")
  ################ fim da função remover livros ##################


def visualizar_livros():
  connection = sqlite3.connect('biblioteca.db')
  cursor =connection.cursor()

  cursor.execute('SELECT * FROM livros ')
  linhas = cursor.fetchall()
  print('DB Livros: ')
  for coluna in linhas:
    print(
      f''' ID: {coluna[0]} - Titulo: {coluna[1]} \t ----   \t @autor: {coluna[2]}'''
    )

  connection.close()
  ####### fim função visuaizar livros ##################

create_table()

while True:
  print("\n\tMenu Opções")

  opcao = int(input(
    '''
      1 - cadastrar livros
      2 - remover livro
      3 - visualizar livros
      4 - Sair
      \tDigite a opção desejada: '''
  ))
  if(opcao == 4):
    break
  elif opcao ==1:
    cadastrar_livros()
  elif opcao ==2:
    remover_livro()
  elif opcao ==3:
    visualizar_livros()
  else:
    print("Opção invalida! ")
