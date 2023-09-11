# Exercício 19 - Crie um jogo da velha para ser jogado por dois jogadores no terminal. Esse jogo deve ser capaz de imprimir o tabuleiro, solicitar ao jogador 1 que insira a sua jogada, solicitar ao jogador 2 que insira a sua jogada e verificar se o jogo terminou e quem ganhou.

import random
import time

def input_numero(mensagem,tipo): #tipo na chamada da função pode escolher em ser do tipo int ou float
   while True:
        try:
            num = tipo(input(mensagem+" "))
            if not isinstance(posicao_jogo[num], int):
                interface_jogo()
                print("\t\tJogada invalida!")
                continue
            return num
        except ValueError:
            print("Favor, Digite a entrada corretamente! \n")


def interface_jogo():
    print("Interface do jogo!")
    # print(f"\n\t1 | 2 | 3 \1\t--------- \n\t4 | 5 | 6 \n\t--------- \n\t7 | 8 | 9 \n\t")
    print(f"\n\t{posicao_jogo[1]} | {posicao_jogo[2]} | {posicao_jogo[3]} \n\t--------- \n\t{posicao_jogo[4]} | {posicao_jogo[5]} | {posicao_jogo[6]} \n\t--------- \n\t{posicao_jogo[7]} | {posicao_jogo[8]} | {posicao_jogo[9]} \n\t")
    print("Para jogar digite o numero correspondente a posição desejada! \n")

# interface_jogo()

print("Inicio. \nJogo da velha!\n")
# escolha_simbolov = input("X ou O? \n Jogador 1 digite x para selecionar X ou qualquer tecla para O: ").upper()
# if escolha_simbolov == 'X':
#     opcao_jogar1 = "X"
#     opcao_jogar2 = "O"
# else:
#     opcao_jogar1 = "O"
#     opcao_jogar2 = "X"
    
# print(f"\nJogador 1 escolheu {opcao_jogar1}\n")
xor0 = ('X', 'O')
print("iniciando sorteio.")
time.sleep(0.5)
print("iniciando sorteio..")
time.sleep(0.5)
print("iniciando sorteio...")
time.sleep(1)
comeca_por = random.choice(xor0)
print(f"\n\tJogador do '{comeca_por}' começa! \n")

jogador1_simbolo = comeca_por
if jogador1_simbolo == 'X':
    jogador2_simbolo = 'O'
else:
    jogador2_simbolo = 'X'

posicao_jogo = [0,1,2,3,4,5,6,7,8,9]
interface_jogo()
def marcar_jogo(local, simbolo):
    posicao_jogo[local] = simbolo
    print(f"\n\t{posicao_jogo[1]} | {posicao_jogo[2]} | {posicao_jogo[3]} \n\t--------- \n\t{posicao_jogo[4]} | {posicao_jogo[5]} | {posicao_jogo[6]} \n\t--------- \n\t{posicao_jogo[7]} | {posicao_jogo[8]} | {posicao_jogo[9]} \n\t")
def validar_jogo_tem_ganhador():
    if posicao_jogo[1] == posicao_jogo [2] and posicao_jogo[1] == posicao_jogo[3]:
        print(f"Jogador {posicao_jogo[1]} Venceu! \n")
        return True
    elif posicao_jogo[1] == posicao_jogo [4] and posicao_jogo[1] == posicao_jogo[7]:
        print(f"Jogador {posicao_jogo[1]} Venceu! \n")
        return True
    elif posicao_jogo[1] == posicao_jogo [5] and posicao_jogo[1] == posicao_jogo[9]:
        print(f"Jogador {posicao_jogo[1]} Venceu! \n")
        return True
    elif posicao_jogo[7] == posicao_jogo [5] and posicao_jogo[7] == posicao_jogo[3]:
        print(f"Jogador {posicao_jogo[7]} Venceu! \n")
        return True
    elif posicao_jogo[2] == posicao_jogo [5] and posicao_jogo[2] == posicao_jogo[8]:
        print(f"Jogador {posicao_jogo[2]} Venceu! \n")
        return True
    elif posicao_jogo[3] == posicao_jogo [6] and posicao_jogo[3] == posicao_jogo[9]:
        print(f"Jogador {posicao_jogo[3]} Venceu! \n")
        return True
    elif posicao_jogo[4] == posicao_jogo [5] and posicao_jogo[4] == posicao_jogo[6]:
        print(f"Jogador {posicao_jogo[4]} Venceu! \n")
        return True
    elif posicao_jogo[7] == posicao_jogo [8] and posicao_jogo[7] == posicao_jogo[9]:
        print(f"Jogador {posicao_jogo[7]} Venceu! \n")
        return True
    elif all(not isinstance(posicao_jogo[i], int) for i in range(1, 10)):
    # Verifica se nenhum dos valores em posicao_jogo[1] até posicao_jogo[9] é um número inteiro se não for ele executa.
        print(f"\n\t\tEMPATE! \n")
        return True
    else:
        return False
        

while True:
    jogador1 = input_numero("Jogardor 1: \nDigite a posição desejada! ",int)
    marcar_jogo(jogador1, jogador1_simbolo)
    if validar_jogo_tem_ganhador():
        break
    jogador2 = input_numero("Jogardor 2: \nDigite a posição desejada! ",int)
    marcar_jogo(jogador2, jogador2_simbolo)
    if validar_jogo_tem_ganhador():
        break