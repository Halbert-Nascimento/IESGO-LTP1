#Calculadora de IMC (Índice de Massa Corporal):
### Crie uma calculadora que permite ao usuário calcular seu IMC com base em seu peso e altura.
### Bônus: responda se o usuário está acima, abaixo ou dentro do peso ideal.

def calcular_imc():
    nome = input("Informe seu nome: ")
    peso = float(input(f"{nome} infome seu peso: "))
    altura = float(input(f"{nome} infome sua altura: "))
    # sexo = input(f"{nome} Qual seu sexo? masculino = 'M' feminino = 'F': ").lower()

    imc = peso/(altura*altura)

    print(f"{nome} seu imc e: {imc:.2f}")
    if imc < 18.5:
        print("Voce esta abaixo do peso ideal \n")
    elif imc >= 18.5 and imc <= 24.9:
        print("Voce esta com peso ideal \n")
    elif imc >= 25 and 29.9:
        print("Voce esta acima do peso ideal \n")
    elif imc >=30 and imc <= 34.9:
        print("Obesidade grau 1 \n")
    elif imc >= 35 and imc <=39.9:
        print("Obesidade grau 2 \n")
    else:
        print("Obesidade grau 3 \n")


calcular_imc()