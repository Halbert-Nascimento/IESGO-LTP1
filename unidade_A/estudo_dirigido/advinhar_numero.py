# Exercício 9: Usando o método random(), crie um programa que solicita ao 
#usuário que adivinhe um número inteiro entre 1 e 10. Se o usuário digitar um número 
#menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário 
#digitar um número válido, verifique se o número que o usuário digitou é igual ao número 
#gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". 
#Caso contrário, imprima "Você errou!".

import random

numero_aleatorio = random.randint(1, 10)

while True:
    advinhar_numero = int(input("Insina um numero de 1 a 10 "))
    if advinhar_numero < 1 or advinhar_numero > 10:
        print("\n\tInsira um numero Valido! ")
        continue
    else:
        if advinhar_numero == numero_aleatorio:
            print("\n\t Você acertou!")
            break
        else:
            print("\n\t Você errou! ")