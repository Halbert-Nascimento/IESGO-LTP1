# Exercício 06 - Crie uma aplicação que solicite ao usuário digitar o seu nome e sobrenome e imprima no console o nome com todas as letras maiúsculas e o sobrenome com todas as letras minúsculas sem espaços entre o nome e o sobrenome e sem alterar a variável original.

def formatar_nome_sobrenome():
    nome = input("Digite seu nome completo ")
    partes_nome = nome.split( )
    primeiro_nome = partes_nome[0]
    sobrenome = " ".join(partes_nome[1:])

    return primeiro_nome.upper() +" "+ sobrenome.lower()

print(formatar_nome_sobrenome())