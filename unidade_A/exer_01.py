# Exercício 01 - Crie uma função que solicite ao usuário digitar uma palavra e substitua as vogais por "*" e a execute numa aplucação que solicite uma palavra ao usuário e imprima o resultado no console, independentemente do usuário digitar a palavra em maiúscula ou minúscula.

def substituir_vogais():
    frase = input("Digite uma palavra ")
    return frase.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')

print(substituir_vogais())