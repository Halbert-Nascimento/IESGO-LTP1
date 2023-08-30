#Gerador de Senhas:
### Crie um gerador de senhas que gera senhas aleatórias com base no comprimento especificado pelo usuário.
# Dica: use a biblioteca random do Python para gerar números aleatórios.
### Bônus: permita que o usuário especifique quantas letras, números e caracteres especiais a senha deve conter.

import random
"""
#primeira parte
def gerador_senha():
    num_letras = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z")

    tamanho_senha = int(input("\nQual o tamanho de senha que deseja gerar? " ))
    contador = 0
    senha = ""
    while contador < tamanho_senha:
        contador +=1
        gerador = random.choice(num_letras)
        senha += gerador
    
    print(f"Senha {tamanho_senha} digitos gerada: {senha} \n")

gerador_senha()

"""

########## Segunda parte - desafio ###############

letras = ("a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z")

numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

carac_especiais = ("!", "@", "#", "$", "%", "&", "*", "_", "-", "+", "=", "?")

print("\nGerador de senha! " )
qtn_letras = int(input("\nQuantas letras deseja na senha?  " ))
qtn_numero = int(input("\nQuantos Numeros? " ))
qtn_caracteres = int(input("\nQuantos caracteres especiais? " ))
tamanho_senha = qtn_caracteres+qtn_letras+qtn_numero

contador_loop = 0
cont_letras = 0
cont_num = 0
cont_caracter = 0
senha = ""

while contador_loop < tamanho_senha:    
    
    if(cont_letras < qtn_letras):
        gerador = random.choice(letras)
        senha += gerador
        cont_letras +=1
        contador_loop +=1

    if cont_num < qtn_numero:
        gerador = random.choice(numeros)
        senha += gerador
        cont_num +=1
        contador_loop +=1

    if cont_caracter < qtn_caracteres:
        gerador = random.choice(carac_especiais)
        senha += gerador
        cont_caracter +=1
        contador_loop +=1

    

print(f"Senha {tamanho_senha} digitos gerada: {senha} \n")

