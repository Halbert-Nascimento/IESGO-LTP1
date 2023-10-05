# Pedra, Papel e Tesoura:
### Crie um jogo simples de pedra, papel e tesoura em que o computador escolhe aleatoriamente uma das três opções e o usuário tenta vencer o computador escolhendo sua própria opção.
### Bônus: dê ao usuário a opção de jogar com outro jogador humano.
import random



def vencedor(jogador, computador):

    if jogador == "pedra" and computador == "tesoura":
        return "o vencendor e: JOGADOR"
    elif jogador == "papel" and computador == "pedra":
        return "o vencendor e: JOGADOR"
    elif jogador == "tesoura" and computador == "papel":
        return "o vencendor e: JOGADOR"
    elif jogador == "pedra" and computador == "pedra" or jogador == "papel" and computador == "papel" or jogador == "tesoura" and computador == "tesoura":
        return "resultado: EMPATE"
    else:
        return "o vencendor e: COMPUTADOR"

pedra_papel_tesoura = ("pedra", "papel", "tesoura")
print(f"Jogo de {pedra_papel_tesoura}")
print("Adiversario computador!\n")
computador = random.choice(pedra_papel_tesoura)

while True:
    jogador = input(f"Digite sua escolha: {pedra_papel_tesoura}? ").lower()
    if jogador == "pedra" or jogador == "papel" or jogador == "tesoura":
        break
    else:
        print("Insersão invalida! \nDigite novamente!\n")
    



print(f"\n\tJogador escolheu {jogador.upper()} e computador escolheu {computador.upper()}, {vencedor(jogador, computador)}\n")


