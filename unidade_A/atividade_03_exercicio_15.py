# Gerador de Sim ou Não:
### Crie um programa que permita ao usuário inserir uma pergunta e, em seguida, exiba uma resposta aleatória de sim ou não.
### Bônus: adicione a opção talvez ao gerador de respostas.

import random
resposta = ["Sim","Não","Talvez"]

pergunta = input("Faça Sua pergunta! ")

print(f"{pergunta} {random.choice(resposta)}")

#comentario para fazer passo a passo do gi