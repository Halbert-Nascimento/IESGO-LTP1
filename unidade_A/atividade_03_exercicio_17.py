# Calculadora de impostos:
### Crie um programa que permita ao usuário inserir o valor de uma compra e, em seguida, exiba o valor total da compra após adicionar o imposto.
### Bônus: permita que o usuário insira o valor do imposto a ser adicionado.

def compras():
    # valor_imposto = 10
    valor_compra = float(input("\nDigite o valor da compra: "))
    valor_imposto = float(input("Digite a taxa de imposto, somente numeros: "))
    valor_total = valor_compra + valor_compra*(valor_imposto/100)
    print(f"\nValor da compra {valor_compra:.2f}$ valor do imposto {valor_imposto}%")
    print(f"\n\t\tValor total compra mais imposto: R$ {valor_total:.2f}\n")

compras()