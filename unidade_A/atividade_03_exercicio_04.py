# Contador de Palavras:
### Faça um programa que conte quantas palavras há em uma frase inserida pelo usuário.
### Bônus: faça o programa retornar a frase com todas as letras maiúsculas e sem espaços em branco.

#### primeira parte ###
def contar_frase():
    frase = input("Insira uma frase: ")
    frase_partes = frase.split()
    print(f"\nA frase inserida tem {len(frase_partes)} palavras!")
    frase_sem_espaço =  "".join(frase_partes[:])

    ### Bônus: faça o programa retornar a frase com todas as letras maiúsculas e sem espaços em branco.
    return frase_sem_espaço.upper()


print(f"\nFrase inserida sem espaços e maiúsculas! \n{contar_frase()} \n")