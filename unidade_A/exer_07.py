# Exercício 07 - Crie uma aplicação em que o usuário digite o seu nome e sobrenome de uma só vez e armazene o nome em uma variável 'nome_usuário' e o sobrenome em uma variável 'sobrenome_usuario'. 
# Em seguida, crie uma variável 'nome_completo' que armazene o nome completo do usuário com todas as letras maiúsculas e 
# imprima no console o nome completo do usuário com todas as letras minúsculas. 
# Além disso, crie outra variável chamada 'tamanho_nome_completo' que armazene o tamanho do nome completo do usuário e imprima no console o tamanho do nome completo do usuário.

def formatar_nome_sobrenome(nome):
    # nome = input("Digite seu nome completo ")
    partes_nome = nome.split( )
    nome_usuário = partes_nome[0]
    sobrenome_usuario = " ".join(partes_nome[1:])
    nome_completo = nome.upper()
    tamanho_nome_completo = len(nome)
    
    print("Nome: "+nome_completo.lower())
    print("tem ",tamanho_nome_completo, " caracteres ")


    

formatar_nome_sobrenome(input("Digite seu nome completo "))