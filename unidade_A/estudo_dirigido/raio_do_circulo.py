# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa 
# retorna no console a área do círculo em m² e o perímetro em m.


import math #importa a bibliotema matematica para poder usar a função pi

def volume_da_esfera():
    raio_esfera = float(input("Insira o valor do raio de uma circulo em m "))

    perimetro = 2*math.pi*raio_esfera # Calcula o volume da esfera usando a fórmula

    area_circulo_m = math.pi*raio_esfera
    
    return f"A área do círculo em m²: {area_circulo_m:.2f} e o perímetro {perimetro}."


print(volume_da_esfera())