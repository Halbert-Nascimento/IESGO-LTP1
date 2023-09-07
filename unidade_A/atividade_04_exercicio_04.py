# Exercício 4 - Escreva um programa que solicita um número inteiro e exibe todos os seus divisores primos.

def numero_primo(numero):
    if numero == 1 or numero == 0:
        return False
    
    for divisor in range(2,numero):
        if numero% divisor == 0:
            return False
        # break
    return True



dividendo = int(input("\n\nDigite um num inteiro: "))
print("Exibe todos os seus divisores primos ")
lista_divisor_primos = []
for divisor in range(1,dividendo):
    if dividendo %divisor == 0:
        if(numero_primo(divisor)):
            lista_divisor_primos.append(divisor)
print(lista_divisor_primos)





