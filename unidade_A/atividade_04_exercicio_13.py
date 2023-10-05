# Exercício 13 - Crie um programa que entrega a raiz quadrada de um número inteiro positivo n com uma precisão de 0.001.


import math

def entrada_numero(mensagem,tipo): #tipo na chamada da função pode escolher em ser do tipo int ou float
    while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Favor, Digite a entrada corretamente! \n")



numero = entrada_numero("Digite um numero inteiro ",int)
while numero < 0:
    numero = entrada_numero("Digite um numero inteiro positivo",int)



raiz_quadrada = math.sqrt(numero)
print(f"Raiz quadra de {numero} = {raiz_quadrada:.3f}")


