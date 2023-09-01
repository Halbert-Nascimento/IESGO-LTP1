#Conversor de Temperatura:
### Crie um conversor de temperatura que permita ao usuário converter entre Celsius e Fahrenheit.
### Bônus: permita que o usuário especifique o número de casas decimais que deseja exibir.

print("\nConversor de temperatura!\n")
opcao = int(input("Digite: \n1: celsius - fahrenheit \n2: fahrenheit - celsius "))
if opcao >= 1 or opcao <= 2:
    temp = float(input("Informe uma valor a temperatura: "))

    ### Bônus: permita que o usuário especifique o número de casas decimais que deseja exibir.
    casas_decimais = int(input("Exibir a temp com quantas casas decimais? "))
    formato = "{:.%df}"%casas_decimais
    """
        # "{}" é uma string de formatação em Python. As chaves {} são espaços reservados onde os valores serão inseridos.
        # ":." dentro das chaves é uma parte do formato que diz como o número deve ser formatado. O : indica que estamos configurando a formatação, e o . indica que estamos lidando com as casas decimais.

        # "%df" fora das chaves é uma string de formatação que contém %d, que é um marcador de posição para um número inteiro (casas_decimais é um número inteiro que o usuário forneceu), e f é apenas um caractere literal que usamos para indicar que estamos formatando um número de ponto flutuante.

        # Portanto, a linha "formato = "{:.%df}" % casas_decimais" está criando uma string de formatação que irá formatar um número float com um número específico de casas decimais. O % casas_decimais insere o valor de casas_decimais na string de formatação.
    """

    if opcao == 1:
        temperatura = (temp * 1.8)+32
        print(f"Temperatura {formato.format(temperatura)}ºF fahrenheit \n")
    else:
      temperatura = (temp - 32 )/ 1.8
      print(f"Temperatura {formato.format(temperatura)}ºC celsius\n")
    

else:
    print("\nOpção invalida! \n")
