# Exercício 18 -  Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). 
# Peça ao usuário para adivinhar o número e, em seguida, diga a eles se eles adivinharam, se o número é menor que o seu palpite ou se número é maior que o seu palpite.

# Extras:

# 1. Continue o jogo até que o usuário digite "sair".
# 2. Acompanhe quantas tentativas o usuário fez e, quando o jogo terminar, imprima este número.



import random
min = 1
max = 9
tentativa = 1
total_jogos = 0
total_erros = 0
total_acertos = 0
total_tentativas = 0
escolha_computador = random.randint(min,max)

print(f"Jogo de advinhação \nTente adivinha numero {min} a {max}")
print("\tO jogo Continuara ate que digite sair! \n")


while True:
    escolha_usuario = input(f"Partida {total_jogos+1}, {tentativa}º Tentativa : ")
    if escolha_usuario.lower() == 'sair':
        print("\n\t\t    RESUMO DO JOGO!")
        print(f"\t\tTotal de partidas: \t{total_jogos}")
        print(f"\t\tTotal de acertos: \t{total_acertos}")
        print(f"\t\tTotaal de erros: \t{total_erros}")
        print(f"\t\tTotal de tentativas: \t{total_tentativas}\n")
        break

    if(int(escolha_usuario) == escolha_computador):
        print(f"\nParabens!!! \nVocê acertou na {tentativa}º tentativa ")
        print(f"Numero escolhido pelo computador era: {escolha_computador}")
        print("\n\tJogo REINICIADO!\n")
        print("\tDigite 'sair' a qualquer momento para finalizar!\n")
        escolha_computador = random.randint(min,max)
        total_acertos +=1
        total_jogos +=1
        tentativa = 1
        continue
    elif int(escolha_usuario) > escolha_computador:
        print("Errou... \n dica... e Menor!\n")
        total_erros +=1
    else:
        print("Errou... \n dica... e Maior!\n")
        total_erros +=1
    tentativa +=1
    total_tentativas +=1
