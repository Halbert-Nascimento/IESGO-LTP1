# Exercício 17 - Escreva um programa que solicita ao usuário inserir uma palavra e retorna se a palavra é um palíndromo ou não.


def palindromo(palavra):
    lista_palavra = []

    for i in range(len(palavra)-1, -1, -1):
        char = palavra[i]
        lista_palavra.append(char)

    new_palavra = "".join(map(str, lista_palavra))

    if new_palavra == palavra:
        return f"\n\tPalavra ({palavra}) é um palíndromo.\n"
    else:
        return f"\n\tPalavra ({palavra}) não é um palíndromo.\n"


print(palindromo(input("Inserir uma palavra ")))