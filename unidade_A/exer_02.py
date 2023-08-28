# Exercício 02 - Crie uma aplicação que solicite ao usuário digitar uma palavra e imprima no console a quantidade de caracteres que a palavra possui.

def quantidade_caracter_palavra():
    texto = input("Digite uma palavra ")
    return len(texto)

print("Palavra digitada em " , quantidade_caracter_palavra(), " caracteres")


# segunda forma convertendo para string

def quantidade_caracter_palavra():
    texto = input("Digite uma palavra ")
    return len(texto)

print("Palavra digitada em " + str( quantidade_caracter_palavra())+ " caracteres")