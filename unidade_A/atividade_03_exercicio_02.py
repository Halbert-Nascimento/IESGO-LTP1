#Conversor de Moeda:
###Desenvolva um aplicativo que converte uma quantidade de uma moeda para outra, utilizando taxas de câmbio predefinidas.
### Bônus: faça o programa solicitar ao usuário a moeda de origem e a moeda de destino e a taxa de câmbio.

#Não finalizado, em andamento

#######
#obs: fazer com que ao selecionar o numero da moeda, tambem seleciona a abreveatura da moeda para que possa aparecer nas mensagens mais intuitivas
#######

def menu():
    BRL = "BRL - Real Brasileiro"
    USD = "USD - Dólar Americano"
    EUR = "EUR - Euro"
    GBP = "GBP - Libra Esterlina (Libra Britânica)"
    JPY = "JPY - Iene Japonês"
    CHF = "CHF - Franco Suíço"
    CAD = "CAD - Dólar Canadense"
    AUD = "AUD - Dólar Australiano"
    print("\nCONVERSOR DE MOEDAS")
    print("Digite o numero correspodente da moeda que deseja fazer a conversão : ")
    print("\n 1: "+ BRL +"\n 2: "+ USD +"\n 3: "+ EUR +"\n 4: "+ GBP +"\n 5: "+ JPY +"\n 6: "+ CHF +"\n 7: "+ CAD +"\n 8: "+ AUD +"\n")
    opcao_moeda_1 = int(input("_____"))
    montante_moeda_1 = float(input("Qual o valor deseja converter? "))
    print("\nPara qual moeda deseja converter? \nDigite o numero correspodente: ")
    print("\n 1: "+ BRL +"\n 2: "+ USD +"\n 3: "+ EUR +"\n 4: "+ GBP +"\n 5: "+ JPY +"\n 6: "+ CHF +"\n 7: "+ CAD +"\n 8: "+ AUD +"\n")
    opcao_moeda_2 = int(input("____"))

    print(f"O montante ja convertido e: {conversor_moedas(opcao_moeda_1, opcao_moeda_2-1, montante_moeda_1):.2f} ")

def conversor_moedas(moeda_principal, moeda_2, montante):
    taxa_conversao = float
    if moeda_principal == 1:
        taxa_conversao = taxa_moeda_brl(moeda_2)
    elif moeda_principal == 2:
        taxa_conversao = taxa_moeda_usd(moeda_2)
    elif moeda_principal == 3:
        taxa_conversao = taxa_moeda_eur(moeda_2)
    elif moeda_principal == 4:
        taxa_conversao = taxa_moeda_gbp(moeda_2)
    elif moeda_principal == 5:
        taxa_conversao = taxa_moeda_jpy(moeda_2)
    elif moeda_principal == 6:
        taxa_conversao = taxa_moeda_chf(moeda_2)
    elif moeda_principal == 7:
        taxa_conversao = taxa_moeda_cad(moeda_2)
    elif moeda_principal == 8:
        taxa_conversao = taxa_moeda_aud(moeda_2)
    else:
        print("opção invalida!")
    return montante*taxa_conversao





def taxa_moeda_brl(opcao):
    taxa_brl = [
        1,          #brl_brl =
        0.2058,     # brl_usd =
        0.1894,     # brl_eur = 
        0.1630,     # brl_gbp = 
        30.02,      # brl_jpy = 
        0.1809,     # brl_chf = 
        0.2793,     # brl_cad = 
        0.3178      # brl_aud = 
    ]
    """
    brl_brl = 1
    brl_usd = 0.2058
    brl_eur = 0.1894
    brl_gbp = 0.1630
    brl_jpy = 30.02
    brl_chf = 0.1809
    brl_cad = 0.2793
    brl_aud = 0.3178
    """
    return taxa_brl[opcao]
#parei aqui, 

def taxa_moeda_usd():
    usd_usd = 1
    usd_brl = 4.85
    usd_eur = 0.9199
    usd_gbp = 0.7918
    usd_jpy = 145.81
    usd_chf = 0.8784
    usd_cad = 0.3554
    usd_aud = 0.6788

def taxa_moeda_eur():
    eur_eur = 1
    eur_brl = 5.2861
    eur_usd = 1.0872
    eur_gbp = 0.7609
    eur_jpy = 158.51
    eur_chf = 0.9557
    eur_cad = 1.4745
    eur_aud = 1.6789

def taxa_moeda_gbp():
    gbp_gbp = 1
    gbp_brl = 6.1387
    gbp_usd = 1.2645
    gbp_eur = 1.1621
    gbp_jpy = 184.44
    gbp_chf = 1.1107
    gbp_cad = 1.7134
    gbp_aud = 1.9510

def taxa_moeda_jpy():
    jpy_jpy = 1
    jpy_brl = 0.0332
    jpy_usd = 0.6854
    jpy_eur = 0.6300
    jpy_gbp = 0.5420
    jpy_chf = 0.6022
    jpy_cad = 0.9290
    jpy_aud = 1.0578

def taxa_moeda_chf():
    chf_chf = 1
    chf_brl = 5.5304
    chf_usd = 1.1384
    chf_eur = 1.0464
    chf_gbp = 0.9003
    chf_jpy = 166.06
    chf_cad = 1.5426
    chf_aud = 1.7568

def taxa_moeda_cad():
    cad_cad = 1
    cad_brl = 3.5800
    cad_usd = 0.7379
    cad_eur = 0.6783
    cad_gbp = 0.5836
    cad_jpy = 107.65
    cad_chf = 0.6482
    cad_aud = 1.1389

def taxa_moeda_aud():
    aud_aud = 1
    aud_brl = 3.1476
    aud_usd = 0.6480
    aud_eur = 0.5956
    aud_gbp = 0.5125
    aud_jpy = 94.54
    aud_chf = 0.5692
    aud_cad = 0.8782


# def conversao_moeda():
 

    

#     print(f" 2 brl => brl = {2 *brl_brl}")

#     print(f" 2 brl => usd = {2 *brl_usd}")
#     print(f" 2 usd => brl = {2 *usd_brl}")

#     print(f" 2 brl => eur = {2 *brl_eur}")
#     print(f" 2 eur => brl = {2 *eur_brl}")

#     print(f" 2 eur => usd = {2 *eur_usd}")
#     print(f" 2 usd => eur = {2 *usd_eur}")


#     # qtn_real = float(input("Quantidade que deseja converter? "))
# conversao_moeda()

menu()