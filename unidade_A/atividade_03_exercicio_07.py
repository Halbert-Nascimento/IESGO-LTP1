#Analisador de String:
### Faça um programa que analise uma string inserida pelo usuário e conte quantas letras maiúsculas, minúsculas, dígitos e caracteres especiais ela contém.
### Bônus: faça o programa retornar quantas palavras há na string.

def analisador_string():
    texto = input("Digite uma palavra ou frase: ")
    # letras_maisculas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    # letras_minusculas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    digitos = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    caracteres_especiais = ("@", "#", "$", "%", "&", "!", "?", "*")

    cont_maiusculas = 0
    cont_minusculas = 0
    cont_digitos = 0
    cont_caracteres_especiais = 0
    cont_espaços = 0

    for char in texto:
        if char.isupper():
            cont_maiusculas += 1

        elif char.islower():
            cont_minusculas += 1

        elif char in digitos:
            cont_digitos +=1

        elif char in caracteres_especiais:
            cont_caracteres_especiais +=1
        else:
            cont_espaços +=1            

    print(f"\nO texto inserido contem {cont_maiusculas} letras MAIÚSCULAS")
    print(f"\nO texto inserido contem {cont_minusculas} letras minúsculas")
    print(f"\nO texto inserido contem {cont_digitos} letras DIGITOS")
    print(f"\nO texto inserido contem {cont_caracteres_especiais} letras CARACTER ESPECIAIS")
    print(f"\nO texto inserido contem {cont_espaços} ESPAÇOS")
    textosplit = texto.split()
    
    return f"O texto digitado tem {len(textosplit)} palavras"

print(analisador_string())