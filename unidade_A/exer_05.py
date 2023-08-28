# Exercício 05 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras minúsculas.

# Exercício 04 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras maiúsculas.

def texto_em_minusculo():
    texto = input("Digite seu nome completo ")
    return texto.lower()

print(texto_em_minusculo())