# Calculadora de Fatorial:
### Crie uma calculadora que permita ao usuário calcular o fatorial de qualquer número.
### Bônus: faça o programa retornar um erro se o usuário inserir um número negativo.

def fatorioal(fatorar):
    if fatorar <0:
        return f"ERROR... numero negativo...."
    num_fatorado = fatorar
    while fatorar > 1:
        num_fatorado = num_fatorado *(fatorar-1)
        fatorar -=1
    return num_fatorado
                     
num = int(input("Digite um numero! "))

print(f"O fatorial de {num} e: {fatorioal(num)}")