# Exercício 20 - Crie um programa que solicita ao usuário inserir uma string longa contendo várias palavras. Em seguida, o programa deve imprimir:
# 1. uma string contendo apenas as palavras que começam com uma letra maiúscula.
# 2. uma string contendo apenas as palavras que terminam com uma vogal.
# 3. uma string contendo apenas as palavras que têm mais de 5 letras.
# 4. uma string contendo o inverso de cada palavra na string original. (Nota: não use a função reverse() do Python, faça isso manualmente!)

def palavra_maiuscula(texto): # 1. uma string contendo apenas as palavras que começam com uma letra maiúscula.
    letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    

    texto_lista = texto.split()
    new_lista_maiuscula =[]

    # for i in texto_lista:
    #     for n in letras_maiusculas:
    #         if i[0] == n:
    #             new_lista_maiuscula.append(i)

    for primeira_letra_maius in texto_lista:
        if primeira_letra_maius.istitle():
            new_lista_maiuscula.append(primeira_letra_maius)
    string = ", ".join(map(str, new_lista_maiuscula))
    print(f"Palavtas inicio maiusculo: {string}")

def termina_vogal(texto): # 2. uma string contendo apenas as palavras que terminam com uma vogal.
    texto_lista = texto.split()
    new_lista_vogal =[]
    vogais = ['a', 'e', 'i', 'o', 'u']

    for terminavogal in texto_lista:
        for vogal in vogais:
            so_tem_uma_letra = len(terminavogal)
            if so_tem_uma_letra > 1:
                if terminavogal[-1].lower() == vogal and terminavogal[-2].lower() != vogal:
                    new_lista_vogal.append(terminavogal)
            elif terminavogal[-1].lower() == vogal:
                new_lista_vogal.append(terminavogal)

    string = ", ".join(map(str, new_lista_vogal))
    print(f"list termina com vogais: {string}")

def palavra_maior5(texto): # 3. uma string contendo apenas as palavras que têm mais de 5 letras.
    texto_lista = texto.split()
    new_lista_maior =[]

    for palavra in texto_lista:
        tamanho = len(palavra)
        if tamanho > 5:
            new_lista_maior.append(palavra)
    string = ", ".join(map(str, new_lista_maior))
    print(f"list termina palavras maior que 5: {string}")



string = input("Insira uma string longa contendo várias palavras ")
palavra_maiuscula(string)
termina_vogal(string)
palavra_maior5(string)