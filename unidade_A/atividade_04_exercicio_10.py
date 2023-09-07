# Exercício 10 - Escreva um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna um dicionário que contém (i, i*i) para cada número inteiro positivo i menor ou igual a n. Use o dicionário para imprimir o quadrado de cada número inteiro positivo menor ou igual a n.

def dicionario():
    dic_n = {}
    while True:
        try:
            numero_inserido = int(input("Inserir um número inteiro positivo para n "))
            if numero_inserido > 0:
                break
            else:
                print("Por favor, insira um número inteiro positivo válido.\n")
        except ValueError: #se o usuario digitar uma letra o codigo não quebra, volta para o inicio e pede para digitar novamente
            print("Por favor, insira um número inteiro positivo válido.\n")

    for i in range(1, numero_inserido+1):
        dic_n[i] = i*i

    for mostrar in dic_n:
        print(f"{mostrar} : {dic_n[mostrar]}")



dicionario()