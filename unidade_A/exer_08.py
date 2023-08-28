# Exercício 08 - Crie um programa que solicite apresenta um menu de opções no Console e solicite ao usuário que digite a opção desejada. Em seguida, crie uma função para cada opção do menu que execute a ação solicitada pelo usuário. O menu deve conter as seguintes opções:

# 1. Conte o número total de palavras digitadas.
# 2. Conte o número de vogais na palavra digitada (ignore maiúsculas/minúsculas, ou seja, "Python" e "python" devem ser contadas como iguais).
# 3. Substitua todas as ocorrências da palavra "Python" por "Java".
# 4. Converta todas as letras da string para minúsculas.
# 5. Crie uma lista com todas as palavras únicas encontradas na string (ignorando maiúsculas/minúsculas).
# 6. Imprima as palavras na string em ordem alfabética.

def menu_selecionado(opcao_selecionada):
    if opcao_selecionada >= 1 or opcao_selecionada <=6:
        texto = input("\nDigite a palavra ou frase: ")

        if opcao_selecionada == 1:
            print("opção selecionada:  1")
            print(cont_total_palavra(texto),"\n")

        elif opcao_selecionada == 2:
            print("opção selecionada:  2")
            print(cont_vogais_palavra(texto),"\n")
            
        elif opcao_selecionada == 3:
            print("opção selecionada:  3")
            print(substituir_palavra_dotexto(texto), "\n")
        elif opcao_selecionada == 4:
            print("opção selecionada:  4")
            print(format_texto_minusculo(texto), "\n")
        elif opcao_selecionada == 5:
            print("opção selecionada:  5")
            print(lista_palavras_unicas(texto))
        elif opcao_selecionada == 6:
            print("opção selecionada:  6")
            print(ordem_alfabetica(texto))
    else:
        print("opção Invalida! \nCodigo finalizado!")

def cont_total_palavra(texto): #opção 1 do menu, contar quantidade de palavras
    quantidade_de_palavras = texto.split();
    if len(quantidade_de_palavras)> 1:
        return f"O texto Digitado contém {len(quantidade_de_palavras)} palavras "
    else:
        return f"{len(quantidade_de_palavras)} palavra Digitada "
    
def cont_vogais_palavra(texto): #opção 2 do menu, contar vogais
    quantidade_devogais = texto.count('a')+texto.count('e')+texto.count('i')+texto.count('o')+texto.count('u')
    if quantidade_devogais > 1:
        return f"Texto Digitado contem {quantidade_devogais} vogais"
    else:
        return f"Texto Digitado contem {quantidade_devogais} vogal"
    
def substituir_palavra_dotexto(texto): #opção 3 do menu, Substituapalavra Python por Java.
    texto_trocado_palavras = texto.lower().replace('python', 'java')
    return f"Novo texto: \n {texto_trocado_palavras}"


def format_texto_minusculo(texto): #opção 4 do menu, converter string em minusculas
    return texto.lower()

def lista_palavras_unicas(texto): # opção 5 do menu, Crie uma lista com todas as palavras únicas encontradas na string (ignorando maiúsculas/minúsculas).
    texto = texto.lower().split()
    palavras_unicas = list(set(texto))
    return f"Lista com as palavras unicas: \n   {palavras_unicas}"

def ordem_alfabetica(texto):
    lista_palavras = texto.split()
    lista_palavras = sorted(lista_palavras)
    return f"Palavras em ordem alfabetica: \n{lista_palavras}"


def opcoes_menu(): # menu com opções, 
    #texto do menu salvo em variaveis
    opc_1 = "1. Conte o número total de palavras digitadas."
    opc_2 = "2. Conte o número de vogais na palavra digitada."
    opc_3 = "3. Substitua todas as ocorrências da palavra Python por Java."
    opc_4 = "4. Converta todas as letras da string para minúsculas."
    opc_5 = "5. Crie uma lista com todas as palavras únicas encontradas na string (ignorando maiúsculas/minúsculas)."
    opc_6 = "6. Imprima as palavras na string em ordem alfabética."
    print("MENU OPÇÕES: ")
    print(f" {opc_1}\n {opc_2}\n {opc_3}\n {opc_4}\n {opc_5}\n {opc_6}") # exibe menu 
    opcao_selecionada = input("Digite a opção desejada: ")
    menu_selecionado(int(opcao_selecionada)) #passa como parametro a opção que foi selecionado do menu


opcoes_menu()