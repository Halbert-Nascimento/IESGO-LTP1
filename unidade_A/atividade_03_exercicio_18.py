# Menu interativo
### Crie um aplicativo que exibe um menu interativo no console do usuário. Nesse menu, o usuário pode escolher entre as seguintes opções:
## 1. Calcular a sua idade em meses
## 2. Calcular a sua idade em dias
## 3. Calcular a sua idade em horas
## 4. Calcular a sua idade em minutos
## 5. Calcular a sua idade em segundos
## 6. Sair do programa

### Bônus: permita que o usuário insira a data atual e a data de seu nascimento.
import time
def menu():
    menu = "\n1. Calcular a sua idade em meses \n2. Calcular a sua idade em dias \n3. Calcular a sua idade em horas \n4. Calcular a sua idade em minutos \n5. Calcular a sua idade em segundos \n\t6. Sair do programa\n"
    ano_nascimento = int(input("Digite o ANO de seu nascimento xxxx: "))
    # mes_nascimento = 4 #int(input("Digite o MÊS de seu nascimento x: "))
    # dia_nascimento = 2 #int(input("Digite o DIA de seu nascimento x: "))

    ano_atual = int(input("Digite o ANO atual xxxx: "))
    # mes_atual = 9 #int(input("Digite o MÊS atual x: "))
    # dia_atual = 7 #int(input("Digite o DIA atual x: "))

    idade = ano_atual - ano_nascimento
    meses_idade = idade*12
    dias_idade = idade*365.25 #valor para levar em consideração os anos bissextos.
    horas_idade = dias_idade*24
    minutos_idade = horas_idade*60
    segundos_idade = minutos_idade*60

    while True:
        opcao_menu = int(input(f"{menu} \tDigite a opção desejada: "))
        if opcao_menu == 6:
            break
        elif opcao_menu == 1:
            print(f"\n\tVoce tem {meses_idade} meses de idade")
            time.sleep(1.2)
        elif opcao_menu == 2:
            print(f"\n\tVoce tem {dias_idade} dias de idade")
            time.sleep(1.2)
        elif opcao_menu == 3:
            print(f"\n\tVoce tem {horas_idade} horas de idade")
            time.sleep(1.2)
        elif opcao_menu == 4:
            print(f"\n\tVoce tem {minutos_idade} minutos de idade")
            time.sleep(1.2)
        elif opcao_menu == 5:
            print(f"\n\tVoce tem {segundos_idade} segundos de idade")
            time.sleep(1.2)
            



menu()