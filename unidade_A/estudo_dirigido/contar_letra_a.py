# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.

texto = input("Escreva um texto: ")

cont = sum(1 for a in texto if a.lower() == 'a')

print(f"Total de letras 'a' que apareceu no texto foi {cont}")


# texto = input("Escreva um texto: ")
# # cont =0
# # for a in texto:
# #     if a.lower() == 'a': 
# #         cont +=1

# print(f"Total de letras 'a' que apareceu no texto foi {cont}")
# outra forma de contar usando uma função
# def contar_caracteres(texto):
#     return texto.count('a')