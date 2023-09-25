
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


# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa 
# retorna no console a área do círculo em m² e o perímetro em m.
# perimetro = 2*pi*raio
#are = pi*raio**2
"""
import math
pi = math.pi
def circulo(raio):
    perimetro = 2*pi*raio
    area = pi*raio**2
    return f"Com base no raio do circulo informado \nO perimeto e {perimetro:.2f} e a area e {area:2f} "

print(circulo(float(input("Digite o raio do circulo em m: "))))
"""
#fim exe 5 circulo area e perimetro

# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês
"""
def horoscopo_chines(ano):
    horoscopo = ["Rato", "Boi", "Tigre", "coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco"]

    ano_inicial_da_primeira_posicao =  1960-12**2 #menor ano da lista informada e depois fatora para diminuir mais 144 anos
    signo = (ano - ano_inicial_da_primeira_posicao)%12

    return f"Posição {signo}, Seu signo chines e {horoscopo[signo].upper()}"

print(horoscopo_chines(int(input("Digite seu ano de Nascimento: "))))
"""
#fim exe 5 signo / horoscopo chines

#Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.  
"""
def num_primo():
    numero = int(input("Digite um numero: "))
    if numero <= 1:
        return f"Não e primo"
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return f"Não e primo"
    return f"Numero {numero} e primo!"
    
print(num_primo())
"""
#fim exe 07 verifcar se num e primo

# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.
"""
def verificar_email():
    email = input("Digite seu email! ")

    if email.count('@') == 1:
        print("Contem 1 '@' ")
        print("Estapa 1 de verificação, passed!")
        if email.count(" ") ==0:
            print("Não contém espaços")
            print("Estapa 2 de verificação, passed!")
            return f"Email: {email}, valido! "
        else:
            print("Email contém espaços, reproved!")
            return f"Email: {email}, Invalido! "
    else:
        print("Email somente 1 '@' , reproved!")
        return f"Email: {email}, Invalido! "

print(verificar_email())
"""
#fim exe 8 verificar email 2 etapas simples

