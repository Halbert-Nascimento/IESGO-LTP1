# Exerício 2 - Escreva um programa que solicita dois números inteirtos (sendo o primeiro o limite inferior e o segundo o limite superior) e exibe todos os números pares entre esses limites.

limite_inferio = int(input("Digite um num inteiro para limite inferio: "))
limite_superior = int(input("Digite um num inteiro para limite superior: "))

print("Exibe todos os números pares entre esses limites ")
lista_num_par = []

for i in range(limite_inferio+1, limite_superior):
    if i %2 == 0:
        lista_num_par.append(i)

print(lista_num_par)