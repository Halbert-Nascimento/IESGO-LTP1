# Exercício 12 - Escreva um programa que contenha uma função com o seu nome que solicita ao usuário inserir um texto e retorna o número de letras que o texto contém que também compõem o seu nome.

def halbert(texto):
    texto = texto.lower()
    contador_letras = 0
    # modo 1
    for char in texto:
        if char == 'h' or char == 'a'or char == 'l'or char == 'b'or char == 'e'or char == 'r'or char == 't':
            contador_letras +=1

    # modo 2
    nome = 'halbert'
    contador_letras_modo2 = 0
    for char in texto:
        comparar = char
        for char2 in nome:
            if comparar == char2:
                contador_letras_modo2 +=1



    return contador_letras_modo2

texto = input("Inserir texto para analise: ")
print(halbert(texto))