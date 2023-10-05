# Exercício 5 - Escreva um programa que encontra quais números são divisíveis por 7 e não são múltiplos de 5, entre 2000 e 3200 (inclusive). Imprima o seu resultado no console em uma única linha separada por vírgulas.


lista_numeros_divisiveis7_não_multiplo5 = []


for dividendo in range(2000,3200+1):
    if dividendo % 7 == 0:
        if dividendo % 5 != 0:
            lista_numeros_divisiveis7_não_multiplo5.append(dividendo)

print(lista_numeros_divisiveis7_não_multiplo5)
