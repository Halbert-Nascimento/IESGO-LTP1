# Gerador de Cartão de Crédito:
### Crie um gerador de cartão de crédito que gere números de cartão de crédito válidos para a empresa de cartão de crédito especificada.
### Bônus: gere um número de cartão de crédito válido aleatoriamente para cada uma das empresas de cartão de crédito suportadas pelo seu aplicativo.
import random


def prefixo_identificação_emitente(opcao):
    visa = "423564"
    master_card = "564365"
    american_Express = "346934"
    elo = "636368"
    hipercard = "636368"
    if opcao == 1:
        return visa
    elif opcao == 2:
        return master_card
    elif opcao == 3:
        return american_Express
    elif opcao == 4:
        return elo
    elif opcao == 5:
        return hipercard
    
def gerador_de_cv():
    return f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
 

def gerador_de_cartao(nome_cliente, numero_conta, bandeira):
    bandeira = prefixo_identificação_emitente(bandeira)
    cartao_decredito = bandeira+numero_conta
    cvv = gerador_de_cv()
    return f"\n{nome_cliente} o numero do seu novo cartão de credito e: {cartao_decredito} cv: {cvv}\n"




nome_cliente = input("Digite seu nome: ")

while True:
    numero_conta = input(f"{nome_cliente} Digite numero para sua conta com 10 digitos (apenas numeros): ")
    if numero_conta.isdigit() and len(numero_conta) == 10:
        break
    else:
        print("Número de conta inválido. Certifique-se de inserir exatamente 10 numeros.\n")

print(f"\n1: Visa. \n2: Marter Card. \n3: American Express. \n4: Elo. \n5: hipercard ")
while True:
    bandeira = int(input(f"\n{nome_cliente} entre com numero da bandeira desejada! "))
    if bandeira > 0 and bandeira < 6:
        break
    else:
        print("Opção Invalida, digite novamente! ")

print(gerador_de_cartao(nome_cliente, numero_conta, bandeira))


#a parte: gerar numeros para conta do cliente
# def gerar_numero_conta_cliente():
#     cont = 0
#     gerador_num_conta = ""
#     conta = ""
#     while True:
#         if cont < 10:
#             gerador_num_conta = random.randint(0,9)
#             conta += str(gerador_num_conta)
#         else:
#             print(f"Numero conta cliente gerado: {conta}")
#             return conta
#             break
#         cont +=1
    