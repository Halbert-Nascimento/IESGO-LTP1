# Exercício 3 - Escreva um programa que solicita um número inteiro e exibe todos os seus divisores.



dividendo = int(input("\n\nDigite um num inteiro: "))
print("Todos os seus divisores ")
lista_divisor = []
for divisor in range(1,dividendo+1):
    if dividendo %divisor == 0:
        lista_divisor.append(divisor)
print(lista_divisor)