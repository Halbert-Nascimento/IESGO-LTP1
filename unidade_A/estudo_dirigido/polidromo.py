# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

def palindromo(texto):
    lista_palavra = []

    for i in range(len(texto)-1, -1, -1):
        char = texto[i]
        lista_palavra.append(char)

    new_palavra = "".join(map(str, lista_palavra))

    if new_palavra == texto:
        return f"\n\tPalavra ({texto}) é um palíndromo.\n"
    else:
        return f"\n\tPalavra ({texto}) não é um palíndromo.\n"


print(palindromo(input("Inserir uma palavra ")))