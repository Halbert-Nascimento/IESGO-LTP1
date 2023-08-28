# Exercício 09 - Crie uma aplicação que solicita ao usuário que digite um texto e imprima no console o texto digitado pelo usuário sem nenhuma vogal.

def apagar_vogais():
    frase = input("Digite uma palavra ")
    return frase.lower().replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

print(apagar_vogais())