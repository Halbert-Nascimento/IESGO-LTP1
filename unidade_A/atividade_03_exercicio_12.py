# Jogo da Velha:
### Crie um jogo da velha para dois jogadores que permite aos usuários inserir o local onde desejam inserir seu símbolo (X ou O) e mantenha uma contagem das vitórias de cada jogador.
### Bônus: permita que o usuário jogue contra o computador.
import random
def interface_jogo():
    print("Interface do jogo!")
    print(f"\n\t1 | 2 | 3 \n\t--------- \n\t4 | 5 | 6 \n\t--------- \n\t7 | 8 | 9 \n\t")
    print("Para jogar digite o numero correspondente a posição desejada! \n")

interface_jogo()
print("Inicio de jogo ")
escolha_simbolov = input("X ou O? \n Jogador 1 digite x para selecionar X ou qualquer tecla para O ").upper()
if escolha_simbolov == 'X':
    opcao_jogar1 = "X"
    opcao_jogar2 = "O"
else:
    opcao_jogar1 = "O"
    opcao_jogar2 = "X"
    
print(f"Voce escolheu {opcao_jogar1}")

primeiro_jogador = random.randint(0,1)