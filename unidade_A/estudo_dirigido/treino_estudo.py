
# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário
"""
def e_multiplo_de_5(numero):
    return True if numero %5 ==0 else False

if e_multiplo_de_5(int(input("Digite um Numero "))):
    print("E multiplo de 5")
else:
    print("Não e multiplo! ")

"""
# fim exe 01 multiplo de 5

# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário
"""
def multiplo_de_5_e_3(numero):
    if numero % 5 == 0 and numero%3 ==0:
        print (f"Numero {numero} e primo de 5 e 3")
    elif numero % 5 == 0:
        print (f"Numero {numero} e primo de 5 mas não e de 3")
    elif numero % 3 == 0:
        print (f"Numero {numero} e primo de 3  mas não e de 5")
    else:
        print (f"Numero {numero} NÂO e primo nem de 5 nem de 3")

multiplo_de_5_e_3(int(input("Digite um numero ")))
"""
#fim exe 2 primo de 5 e 3

# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.
"""
def e_polindromo(palavra):
    #return f"{palavra} e uma palavra Palíndomo! " if palavra == palavra[::-1] else f"Não e uma palavra Palindroma! "
    if palavra == palavra[::-1]:
        return f"{palavra} e uma palavra Palíndomo! "
    else:
        return f"Não e uma palavra Palindroma! "

print(e_polindromo(input("Digite uma palavra para verificar ")))
"""
#fim exe 3 palavras polidromas são iguais a originais lidas de tras para frente

# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. 
#O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de 
#frutas que o usuário deseja comprar.
"""
import time
lista_compra = []
informativo = "Digite nome da fruta para ADC a lista ou 'sair' para finalizar! "
produto = input(f"Lista de compras:\n {informativo}")

while produto.lower() != "sair":
    lista_compra.append(produto)
    print("...")
    time.sleep(1)
    print("Itens adicionado a lista! ")
    print(f"Lista atualizada: \n{lista_compra}\n")
    produto = input(informativo)

print(f"Lista finalizada! \n Itens: {lista_compra}")
"""
#fim exe 4 lista de frutas / compras
