# Exercício 04 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras maiúsculas.

def texto_em_maiusculo():
    texto = input("Digite seu nome completo ")
    return texto.upper()

print(texto_em_maiusculo())