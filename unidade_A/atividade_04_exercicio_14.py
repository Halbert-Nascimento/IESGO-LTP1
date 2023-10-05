# Exercício 14 - Crie um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna se o número é par ou ímpar.


def input_numero(mensagem,tipo): #tipo na chamada da função pode escolher em ser do tipo int ou float
    while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Favor, Digite a entrada corretamente! \n")

def par_ou_impar(num):

    if num % 2 == 0:
        return f"O numero {num} e par!\n"
    else:
        return f"O numero {num} e impar!!\n"


numero = input_numero("Digite um número inteiro positivo", int)
while numero <0:
    numero = input_numero("Digite um número inteiro positivo", int)

print(par_ou_impar(numero))