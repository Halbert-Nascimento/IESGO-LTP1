# Exercício 15 - Crie um programa em que o usuário deve responder no terminal quantos números de Fibonacci ele deseja ver. Em seguida, o programa deve imprimir os números de Fibonacci na tela em uma lista separada por vírgulas.
def input_numero(mensagem,tipo): #tipo na chamada da função pode escolher em ser do tipo int ou float
   while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Favor, Digite a entrada corretamente! \n")

def fibonacci(qt_fibi):
    lista_fibonacci = [0,1]

    if qt_fibi < 2:
        return lista_fibonacci[0]
    
    sequencia =2
    while sequencia < qt_fibi:
        sequencia +=1
        fibi = lista_fibonacci[-2] + lista_fibonacci[-1]
        lista_fibonacci.append(fibi)
    # return lista_fibonacci
    return ", ".join(map(str, lista_fibonacci))

# num = input_numero("Quantos números de Fibonacci ele deseja ver? ",int)
print(fibonacci(input_numero("Quantos números de Fibonacci ele deseja ver? ",int)))