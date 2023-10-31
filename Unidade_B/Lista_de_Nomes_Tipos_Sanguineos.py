"""
Crie um programa Python que ofereça as seguintes funcionalidades:
a. Adicionar um novo nome e tipo sanguíneo à lista.
b. Visualizar a lista atual de nomes e tipos sanguíneos.
c. Salvar a lista em um arquivo de texto chamado "lista_tipos_sanguineos.txt".
"""

lista_pessoas = []
nome_tipo_sanguineo = {}
nome_arquivo = "lista_tipos_sanguineos.txt"


def adicionar_nome_e_tipo_sanguineo():
    nome = input("Digite o Nome da pessoa: ")
    tipo_sanguineo = input(f"Digite o tipo sanguíneo de {nome}: ")
    pessoa = {
        "Nome": nome,
        "Tipo Sanguíneo": tipo_sanguineo
    }
    lista_pessoas.append(pessoa)
    print(f"Dados de {pessoa} armazenado com sucesso! ")


def visualizar_lista():
    if not lista_pessoas:
        print("A lista esta vazia! ")
    else:
        print("Lista de nome e tipagem sanguínea")
        for pessoa in lista_pessoas:
            print(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}")
    print()


def salvar_dados():
    with open(nome_arquivo, "w") as arquivo:
        for pessoa in lista_pessoas:
            arquivo.write(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}\n")
        print("Arquivo Gerado com sucesso! ")
    print()


def carregar_dados():
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(", ")
                nome = dados[0].split(": ")[1]
                tipo_sanguineo = dados[1].split(": ")[1]
                pessoa = {
                    "Nome": nome,
                    "Tipo Sanguíneo": tipo_sanguineo
                }
                lista_pessoas.append(pessoa)
            print("Dados carregado com sucesso! \n")

    except FileNotFoundError:
        print(
            f"Erro! \nO arquivo {nome_arquivo} não foi encontrado! \nContate o adm do sistema. \n")


carregar_dados()

while True:
    print("\nOpções: ")
    print("1. Adicionar um novo nome e tipo sanguíneo à lista: ")
    print("2. Visualizar a lista atual de nomes e tipos sanguíneos: ")
    print("3. Salvar a lista em um arquivo de texto: ")
    print("4. Finalizar: ")

    opc = input()
    if opc == "1":
        adicionar_nome_e_tipo_sanguineo()
    elif opc == "2":
        visualizar_lista()
    elif opc == "3":
        salvar_dados()
    elif opc == "4":
        break
    else:
        print("Opção invalida! ")
