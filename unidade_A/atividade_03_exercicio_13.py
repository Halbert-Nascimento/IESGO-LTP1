# Par ou ímpar:
### Crie um jogo simples em que o computador escolhe um número aleatório e o usuário tenta adivinhar se o número é par ou ímpar.
### Bônus: permita que o usuário jogue contra outro usuário humano.

import random
import time

def escolha_do_computador():
    num_aleatorio = random.randint(1,100)
    if num_aleatorio%2 == 0:
        return True
    else:
        return False
escolha_adversario = input("Digite \n\t1. para jogar contra o computador \n\tou qualquer tecla para jogar contra um Humano! \t\t")
if escolha_adversario == "1":
    print("Foi gerado um numero aleatorio, e voce precisa advinhar se ele e par ou impar. ")
    while True:
        escolha_usuario = int(input("Digite: \n1. IMPAR \n2. PAR \t"))
        if escolha_usuario < 1 or escolha_usuario > 2:
            print("\n\t Escolha as opções entre 1 e 2 \n")
            time.sleep(1)
            continue
        if escolha_usuario == 2 and escolha_do_computador():
            print("\tVOCE acertou!!! e PAR! \n")
            break
        elif escolha_usuario ==1 and not escolha_do_computador():
            print("\tVOCE acertou!!! e IMPAR! \n")
            break
        else:
            print("\t\tVocê Errou, tente novamente!")
else:
        numero_jogador1 = int(input("Jogador 1 digite um numero a sua escolha para o adversario tentar advinha se e par ou impar: "))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        while True:
            escolha_usuario = int(input("Jogador 2 tente advinhar: \n1. IMPAR \n2. PAR \t"))
            if escolha_usuario < 1 or escolha_usuario > 2:
                print("\n\t Escolha as opções entre 1 e 2 \n")
                time.sleep(1)
                continue
            if escolha_usuario == 2 and numero_jogador1%2 ==0:
                print("\tVOCE acertou!!! e PAR! \n")
                break
            elif escolha_usuario ==1 and not numero_jogador1%2 ==0:
                print("\tVOCE acertou!!! e IMPAR! \n")
                break
            else:
                print("\t\tVocê Errou, tente novamente!")