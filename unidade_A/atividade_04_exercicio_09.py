# Exercício 9 - Escreva um programa que solicita ao usuário as dimensões de um retângulo e o programa retorna o perímetro e a área do retângulo.

def perimetro_area_retangulo():
    print("Vamos calcular perímetro e a área do retângulo\n")

    altura = float(input("Digite altura do retângulo: "))
    comprimento = float(input("Digite comprimento do retângulo: "))

    perimetro_retangulo = 2 * (altura+comprimento)
    area_retangulo = altura*comprimento

    return f" O perimetro do retângulo e: {perimetro_retangulo},\n A área do retângulo e: {area_retangulo} "

print(perimetro_area_retangulo())