#Lista de Tarefas:
### Desenvolva um aplicativo de lista de tarefas que permita ao usuário adicionar, marcar como concluída e remover tarefas.
### Bônus: armazene a lista de tarefas em um arquivo e carregue-a quando o aplicativo for iniciado.

import time
lista_tarefas = []
# with open("lista_tarefas.txt", "w") as lista_tarefas_txt:
#     lista_tarefas_txt.write("lista_tarefass")


while True:
    print("\nMenu opções: ")
    print("1: Adicionar item. \n2: Remover item. \n3: Finalizar/salvar \n4: Mostra itens da lista")

    selecao_item = int(input("digite o numero correspondente: "))

    if selecao_item == 1:
        lista_tarefas.append(input("\nDigite o item a adc na lista: ").lower())
    elif selecao_item == 2:
        print(f"Itens da lista: \n{lista_tarefas}")
        lista_tarefas.remove(input("\nQual item da lista deseja remover? ").lower())
        time.sleep(1)
        print("item removido! ")
        time.sleep(1)
    elif selecao_item == 3:
        print(f"\nItens da lista: \n{lista_tarefas}")
        print("\nSalvando... \n")
        time.sleep(3)
        print("Lista Salva! ")
        break
    elif selecao_item == 4:
        print(f"\nItens da lista: \n{lista_tarefas}\n")
        time.sleep(4)

    else:
        print("\n\nOpção invalida! \nDigite novamente! \n\n")
        time.sleep(2)
        


