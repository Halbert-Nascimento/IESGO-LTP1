#Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.

def input_numero(mensagem,tipo): #tipo na chamada da função pode escolher em ser do tipo int ou float
   while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Favor, Digite a entrada corretamente! \n")

def e_primo(num):
    if num < 2:
        return f"\nNão e primo!"
    else:
        for i in range(2, num):        
            if num % i == 0:
                return f"\nNão e primo! "
        return f"\n\tE primo!"

print(e_primo(num = input_numero("Digite um numero ",int)))