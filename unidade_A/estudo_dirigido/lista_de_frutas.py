# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. 
#O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de 
#frutas que o usuário deseja comprar.


lista_de_compas = []

while True:    
    print("Lista de compras")
    print(f"Itens da lista\n {lista_de_compas}")
    
    produto = input("Digite o produto a adcionar ou 'sair' para finalizar: ")
    if produto.lower() == "sair":
        print(f"\n\nLista fechada! ")
        print(f"A lista contém {len(lista_de_compas)} produtos: \n{lista_de_compas}")
        break
    else:
        lista_de_compas.append(produto)