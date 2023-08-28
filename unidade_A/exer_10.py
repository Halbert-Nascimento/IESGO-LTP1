# Exercício 10 - Crie uma aplicação que solicita ao usuário que digite um texto e retorne a quantidade de caracteres que o texto possui.

def quantidade_caracter(texto):
    texto_sem_espaca = texto.lower().replace(' ', '')
    return len(texto_sem_espaca)
 
    
print("Esse texto possui ",quantidade_caracter(input("Digite texto ")), " caracter's")
