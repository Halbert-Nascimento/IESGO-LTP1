# Exercício 03 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console quantas vezes aparece a letra "a", independente de ser maiúscula ou minúscula.


def contar_letra(letra):
    texto = input("Digite seu Nome Completo ").lower()
    return texto.count(letra)

letra_a_contar = 'a'
print("Nome contem ", contar_letra(letra_a_contar), " letras "+ letra_a_contar)