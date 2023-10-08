def mostra_cardapio(menu):
    print("Cardapio: ")#quebra linha, orgamização
    for cardapio, valor in menu.items():
        print(f"\t{cardapio}: R$ {valor} ")

itens_menu ={
    "hamburguer": 5.50, "batata frita": 2.00, "refrigerante": 1.50, "cerveja": 10.5, "caldo": 12.0
    } 

pedidos = {} 
 #dic para itens do novo pedido

def fazer_pedido():
    numero_pedido = input("Digite o numero (identificação do pedido): ")
    itens_pedidos = {}
    mostra_cardapio(itens_menu)

    while True:
        item = input("Digite o pedido: ")
        if(item in itens_menu):
            itens_pedidos[item] = int(input(f"Quantos {item}? "))
            pedidos[numero_pedido] = itens_pedidos
            if input("Digite 'f' para finalizar o pedido, ou tecle qualquer para continuar: ").lower() != "f":
                continue
            else:
                break
        else:
            print(f"\n\t'{item}' não consta no Cardapio! ")
            print(f"\tDigite igual nome no cardapio... \n")
            mostra_cardapio(itens_menu)


fazer_pedido()
while input("Fazer um novo pedido? 'sim' , 'não' ").lower() == "sim":
    fazer_pedido()

print(pedidos,"\n")

# print(pedidos.values())
print(f"Comandas: {pedidos.keys()}\n")

for comanda, pedido in pedidos.items():
    print(f"Comanda {comanda}: pedido{pedido}")
    total_a_pagar = 0
    for produto, quantidade in pedido.items():
        valor_produto = itens_menu[produto]
        parcial_conta = valor_produto * quantidade
        total_a_pagar += parcial_conta
    print(f"\tComanda {comanda}: total a pagar: R${total_a_pagar}\n")

    ##### teste
    # for comanda, pedido in pedidos.items():
    # total_a_pagar = 0
    # for produto, quantidade in pedido.item():
    #     valor_produto = itens_menu[produto]
    #     parcial_conta = valor_produto * quantidade
    #     total_a_pagar +=parcial_conta
    # print(f"Comanda {comanda}: total Conta: R${total_a_pagar}")