# Calculadora de Idade:
### Crie um programa que recebe o ano de nascimento do usuário e calcula a idade atual.
### Bônus: faça o programa retornar o signo do usuário de acordo com o mês e dia do seu nascimento.
def signo(dia, mes):
    if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):# Áries: 21 de março a 19 de abril
        return "Áries"
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):# Touro: 20 de abril a 20 de maio
        return "Touro"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6): # Gêmeos: 21 de maio a 20 de junho
        return "Gêmeos"
    elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):# Câncer: 21 de junho a 22 de julho
        return "Câncer"
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):# Leão: 23 de julho a 22 de agosto
        return "Leão"
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9): # Virgem: 23 de agosto a 22 de setembro
        return "Virgem"
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):# Libra: 23 de setembro a 22 de outubro
        return "Libra"
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):# Escorpião: 23 de outubro a 21 de novembro
        return "Escorpião"
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):# Sagitário: 22 de novembro a 21 de dezembro
        return "Sagitário"
    elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):# Capricórnio: 22 de dezembro a 19 de janeiro
        return "Capricórnio"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):# Aquário: 20 de janeiro a 18 de fevereiro
        return "Aquário"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):# Peixes: 19 de fevereiro a 20 de março
        return "Peixes"

ano_atual = 2023
dia_nascimento = int(input("Digite o DIA de nascimento: "))
mes_nascimento = int(input("Digite MÊS de nascimento: 'NUMERAL' "))
ano_nascimento = int(input("Digite seu ANO de nascimento com 4 digitos: "))

idade = ano_atual - ano_nascimento
print(f"\nSua idade atual e: {idade} signo de {signo(dia_nascimento, mes_nascimento)}\n")
