# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês

"""
def horoscopo_chines(ano):
    horoscopo = ["Cachorro", "Porgo", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Cobra", "Cavalo", "Cabra", "Macaco","Galo"]

    inicio = 1934-12**2    
    posi_sig = 0
    while inicio < ano:
        posi_sig +=1
        inicio +=1
        if posi_sig == 12:
            posi_sig = 0        
    print(f"posição signo {posi_sig} \nSeu signo chines e {horoscopo[posi_sig]}")
ano_nascimento = int(input("Digite o ano de nascimento: "))
horoscopo_chines(ano_nascimento)
"""
#Refatorado

def horoscopo_chines(ano):
    horoscopo = ["Cachorro", "Porgo", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Cobra", "Cavalo", "Cabra", "Macaco","Galo"]

    inicio = 1934-12**2 #reduz mais 144 anos
    sigino = (ano-inicio)%12 
    return f"\nposição signo {sigino} \nSeu signo chines e {horoscopo[sigino]}\n"

print(horoscopo_chines(int(input("Digite o ano de nascimento: "))))