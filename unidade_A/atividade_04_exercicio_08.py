# Exercício 8 - Escreva um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna a soma de todos os números inteiros positivos entre 1 e n que são divisíveis por 3 ou 5.


def somar_numeros_rangen(numero):
    soma_n = 0
    for n in range(1, numero+1):
        if n % 3 == 0 or n % 5 == 0:
            soma_n +=n

    return soma_n

while True:
    numero = int(input("\n\tInsere um número inteiro positivo "))
    if numero > 0:
        print(f"Soma dos números inteiros positivos entre 1 e {numero} que são divisíveis por 3 ou 5 e: {somar_numeros_rangen(numero)}")
        break

