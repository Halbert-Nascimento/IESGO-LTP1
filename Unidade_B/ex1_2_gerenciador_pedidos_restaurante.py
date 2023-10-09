def mostra_cardapio(menu):
    print("Cardapio: ")#quebra linha, orgamização
    for cardapio, valor in menu.items():
        print(f"\t{cardapio}: R$ {valor} ")

itens_menu ={
    "hamburguer": 15.00, "batata frita": 12.00, "refrigerante": 3.50, "cerveja": 10.50, "caldo": 10.00, "torresmo": 2.50, "suco": 8.00
    } 

pedidos = {} 
 #dic para itens do novo pedido

def fazer_pedido():
    numero_pedido = input("\nDigite o numero (identificação do pedido): ")
    itens_pedidos = {}
    mostra_cardapio(itens_menu)

    while True:
        item = input("Digite o pedido: ")
        if(item in itens_menu):
            itens_pedidos[item] = int(input(f"Quantos {item}? "))
            pedidos[numero_pedido] = itens_pedidos
            if input("\nDigite 'f' para finalizar o pedido, ou tecle qualquer para continuar: ").lower() != "f":
                continue
            else:
                break
        else:
            print(f"\n\t'{item}' não consta no Cardapio! ")
            print(f"\tDigite igual nome no cardapio... \n")
            mostra_cardapio(itens_menu)

def alterar_remover_pedido(numero_pedido):
    opcao = input(" _'alterar' ou 'remover' um pedido? ").lower()
    if  opcao == "remover":
        comanda = pedidos[numero_pedido]
        for item_lista_for in comanda:
            print(f"Produto: {item_lista_for} ")
        print("\n Qual item deseja remover? ")       
        item_remover = input("Digite o nome: ")
        del comanda[item_remover]
        pedidos[numero_pedido] = comanda

    elif opcao == "alterar":
        comanda = pedidos[numero_pedido]
        for item_lista_for in comanda:
            print(f"Produto: {item_lista_for} ")
        print("\n Qual item deseja Alterar? ")       
        item_alterar = input("Digite o nome: ")
        alterar_quantidade = int(input("Digite quantidade desse produto: "))


        comanda[item_alterar] = alterar_quantidade
        pedidos[numero_pedido] = comanda



fazer_pedido()

while input("\n\tFazer um novo pedido? 'sim' , 'não' ").lower() == "sim":
    print(f"Comandas: {pedidos.keys()}, digite a proxima comanda. ")
    fazer_pedido()
    

alterar_remover_pedido(input(f"\n {pedidos.keys()}\nQual comanda deseja modificar? "))

print(pedidos,"\n")
# print(pedidos.values())
# print(f"Comandas: {pedidos.keys()}\n")

for comanda, pedido in pedidos.items():
    print(f"Comanda {comanda}: pedido{pedido}")
    total_a_pagar = 0
    for produto, quantidade in pedido.items():
        valor_produto = itens_menu[produto]
        parcial_conta = valor_produto * quantidade
        total_a_pagar += parcial_conta
    print(f"\tComanda {comanda}: total a pagar: R${total_a_pagar}\n")

