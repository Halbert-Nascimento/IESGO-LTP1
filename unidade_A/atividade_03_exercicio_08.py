# Jogo de Adivinhação:
###Implemente um jogo simples em que o computador escolhe um número aleatório e o usuário tenta adivinhar o número.
### Bônus: faça o computador informar se o número inserido pelo usuário é maior ou menor que o número escolhido pelo computador.


import random
min = 0
max = 100
tentativa = 1
escolha_computador = random.randint(min,max)

print(f"Jogo de advinhação \nTente adivinha numero {min} a {max}")

while True:
    escolha_usuario = int(input(f"{tentativa}º Tentativa : "))
    if(escolha_usuario == escolha_computador):
        print(f"\nParabens!!! \nVocê acertou na {tentativa}º tentativa ")
        print(f"Numero escolhido pelo computador era: {escolha_computador}")
        print("Jogo Finalizado!")
        break
    elif escolha_usuario > escolha_computador:
        print("Errou... \n dica... e Menor!\n")
    else:
        print("Errou... \n dica... e Maior!\n")
    tentativa +=1