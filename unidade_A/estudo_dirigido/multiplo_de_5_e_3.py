# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário


def input_numero(mensagem,tipo): #tipo na chamada da função pode escolher em ser do tipo int ou float
   while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Favor, Digite a entrada corretamente! \n")

def multiplo_de_5_e_3(dividendo):

    if dividendo % 5 == 0 and dividendo % 3 ==0:
        return True
    else:
        return False
    
num = input_numero("Digite um numero ",int)
print(f"{num} e multiplo de 5 e de 3: {multiplo_de_5_e_3(num)}")