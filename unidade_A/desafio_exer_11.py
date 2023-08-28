# ####################################################################################
# ------------------------------------------------------------------------------------
# -----------------------------DESAFIO DE ARTE ASCII----------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ####################################################################################

# # Crie um programa Python que permita ao usuário criar sua própria arte ASCII no console. Siga as instruções abaixo:

# # Solicite ao usuário que insira um caractere (por exemplo, "*", "@", "#", etc.) que será usado para criar o padrão de arte. Solicite ao usuário que insira um número inteiro positivo que represente a altura do padrão de arte. Use o caractere fornecido pelo usuário e crie um padrão de arte que tenha a forma de um triângulo retângulo. O triângulo deve ter a altura especificada pelo usuário. Imprima o padrão de arte no console. Cada linha do triângulo deve conter um número crescente de caracteres, começando com 1 na primeira linha e aumentando em 1 em cada linha subsequente.

# # DICA: Use métodos de string para criar e formatar o padrão de arte e lembre-se de que podemos fazer operações matemáticas com strings em Python, como multiplicação e adição.


caracter = input("Insira um caractere (por exemplo, *, @, #, etc.) ")
altura_arte = input("Insira um número inteiro positivo ")
if int(altura_arte) > 0:
    print(f"Iniciando forma, triângulo retângulo com '{caracter}' com {altura_arte} de altura \n")

    for linhas in range(1, int(altura_arte)+1):
        print(caracter*linhas)
    print("\nArte finalizada! \n")
else:
    print("\nValor inserido não e válido para aplicação! \n")
