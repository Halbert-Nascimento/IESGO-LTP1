# file handling(gestao de arquivos)
# quais são as funções basicas para gestao de arquivos?
# ler (read)
# criar (create)
# escrever (write)
# acrescentar (append)
###


imagem = "C:/Users/Halbert Nascimento/OneDrive/Documentos/python/IESGO-LTP1-main/Unidade_B/img.png"

# with open(imagem, "rb") as lista:
#     conteudo = lista.read()


minhas_lista = "C:/Users/Halbert Nascimento/OneDrive/Documentos/python/IESGO-LTP1-main/Unidade_B/minhalista.txt"

# with open(minhas_lista, "rt") as lista:
#     conteudo = lista.readline()
# print(conteudo)

# lista_nome = open(minhas_lista, "r")
# for x in lista_nome:
#     print(x)

"""
lista_nome = open(minhas_lista, "r") #abre arquivo
print(lista_nome.readline())
lista_nome.close() # fecha arquivo
"""

# objetivo: criar um arquivo de texto chamado "meuarquivo.txt" usando o console
"""
nome_do_arquivo = "meuarquivo.txt"
# arquivo = open(nome_do_arquivo, "w")  # abre arquivo e define o nome
with open(nome_do_arquivo, "w") as arquivo:  # abre arquivo e define o nome
    arquivo.write("Este e o conteudo do arquivo! ")

print(f"Seu arquivo {nome_do_arquivo} foi criado com sucesso! ")

arquivo_leitura = open(nome_do_arquivo)
print()
print(arquivo_leitura.read())
"""

nome_do_arquivo = "meu_arquivo.txt"
# arquivo = open(nome_do_arquivo, "w")  # abre arquivo e define o nome
with open(nome_do_arquivo, "w") as arquivo:  # abre arquivo e define o nome
    arquivo.write("Este e o conteudo do arquivo! ")
    arquivo.write("novo conteudo do arquivo! ")

print(f"Seu arquivo {nome_do_arquivo} foi criado com sucesso! ")

arquivo_leitura = open(nome_do_arquivo)
print()
print(arquivo_leitura.read())
