# Exercício 11 - Escreva um programa em que o usuário insere o valor do raio de uma esfera em m e o programa retorna o volume da esfera em litros.
import math #importa a bibliotema matematica para poder usar a função pi

def volume_da_esfera():
    raio_esfera = float(input("Insira o valor do raio de uma esfera em m "))

    volume = (4/3)*math.pi*(raio_esfera**3) # Calcula o volume da esfera usando a fórmula

    volume_litros = volume * 1000  # 1 metro cúbico = 1000 litros
    
    return f"O volume da esfera é aproximadamente {volume_litros:.2f} litros."


print(volume_da_esfera())