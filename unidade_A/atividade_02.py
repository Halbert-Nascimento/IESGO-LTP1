### Desafio... Jogo de advinhação
### 1. O computador vai "pensar" em um número entre 0 e 10. O jogador vai tentar advinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

def jogo_advinhacao():
    numero_sorteado = random.randint(0,10)

    tentativas = 1
    acertou = False
    print("Desafio... Jogo de advinhação, tente acerta o numero de 0 a 10 ")
    while acertou != True:
        palpite = int(input(f"Tentativa {tentativas}: "))
        if palpite == numero_sorteado:
            acertou = True
            print(f"\n\t\t Parabens! voce acertou na tentativa  n {tentativas} \n\n")
        else:
            print(f"\nVoce errou, tente novamente! \n")
            tentativas +=1
    
jogo_advinhacao()

def jokenpo():
    opcoes_do_jogo = ['pedra', 'papel', 'tesoura']
    selecao_do_computador = random.choice(opcoes_do_jogo)
    selecao_do_usuario = opcoes_do_jogo[int(input("Escolha entre pedra, papel ou tesoura: \n 1. pedra \n 2. papel \n 3. tesoura \n"))-1]
    print(f'O computador escolheu {selecao_do_computador}.')
    print(f'O usuário escolheu {selecao_do_usuario}.')

    if selecao_do_usuario == selecao_do_computador:
        print('Empate!')
    elif selecao_do_usuario == 'pedra' and selecao_do_computador == 'tesoura':
        print('Você ganhou!')
    elif selecao_do_usuario == 'papel' and selecao_do_computador == 'pedra':
        print('Você ganhou!')
    elif selecao_do_usuario == 'tesoura' and selecao_do_computador == 'papel':
        print('\nVocê ganhou!\n\n')
    else:
        print('\nVocê perdeu!\n\n')
    
    if input('\nDeseja gogar novamente? s= sim n= nao ').lower() == 's':
        jokenpo()

jokenpo()