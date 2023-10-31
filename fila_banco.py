"""
Questão: Gerenciamento de Fila de Banco com Prioridade

Você foi designado para criar um programa em Python que simula a gestão de uma fila de banco do tipo FIFO (First-In, First-Out) com a capacidade de lidar com clientes prioritários de acordo com a lei. Sua tarefa é criar um programa que permita adicionar clientes à fila, atender o próximo cliente e visualizar a fila.

A fila funciona da seguinte maneira:

Quando um cliente chega ao banco, ele pode ou não ter prioridade por lei. Os clientes com prioridade por lei devem ser atendidos imediatamente e, portanto, pulam para a frente da fila.
Os clientes que não têm prioridade por lei são adicionados ao final da fila.
O atendimento é realizado no estilo FIFO, ou seja, o próximo cliente na fila é atendido.
Os clientes podem escolher sair do banco a qualquer momento.
Aqui está um resumo das funcionalidades que o programa deve ter:

Adicionar cliente à fila:

Solicita ao usuário o nome do cliente.
Pergunta se o cliente tem prioridade por lei (S para Sim, N para Não).
Se o cliente tiver prioridade, ele é adicionado à frente da fila. Caso contrário, é adicionado ao final da fila.
Atender próximo cliente:

Remove o próximo cliente da fila e informa que ele está sendo atendido.
Visualizar fila:

Exibe a fila atual, mostrando os nomes dos clientes na ordem em que estão na fila.
Sair do programa:

Encerra o programa.
Lembre-se de que você precisa criar uma classe Cliente para representar as pessoas na fila. A lista fila deve conter objetos dessa classe para acompanhar os clientes e suas prioridades.

Ao criar o programa, certifique-se de tratar erros e situações em que a fila está vazia.

Siga as diretrizes acima para criar um programa Python que simule a gestão de uma fila de banco com clientes prioritários. Certifique-se de que o programa funcione corretamente e permita que os usuários interajam com a fila, adicionando clientes, atendendo-os e visualizando a fila.
"""
import array as ar
# fila = ar.array('u')


class cliente():
    def __init__(self):
        # self.fila = ar.array('s') fazer com array
        self.fila = []

    def adicionar_cliente_fila(self):
        nome = input("Nome Cliente: ")
        prioritario = input("Cliente Prioritario? 'S' / 'N': ").lower()
        if prioritario == 's':
            self.fila.insert(0, nome)
        else:
            self.fila.append(nome)

    def atender_cliente(self):
        atendido = self.fila.pop(0)

        print(f"\nCliente {atendido.upper()} atendido! \n")
        self.visualizar_fila()

    def visualizar_fila(self):
        print("Clientes para serem atendidos! ")
        position = 1
        for cliente in self.fila:
            print(f"\t {position}. {cliente}")
            position+=1

    def remover_da_fila_cliente(self):
        self.visualizar_fila()
        remover = int(input("Qual deseja remover da fila? Digite numeração: "))
        removido = self.fila.pop(remover-1)
        print(f"\nCliente {removido}  foi removido da fila! \n")
        



Banco = cliente()

while True:
    print("\n" +
          "1. Adicionar cliente à fila: \n" +
          "2. Atender próximo cliente: \n" +
          "3. Visualizar fila: \n" +
          "4. Remover Cliente da fila: \n" +
          "5. Sair do programa: \n"
          )

    opcao = input("\t Digite o numero correspondente: ")
    if opcao == '1':
        Banco.adicionar_cliente_fila()

    elif opcao == '2':
        Banco.atender_cliente()

    elif opcao == '3':
        Banco.visualizar_fila()
    elif opcao == '4':
        Banco.remover_da_fila_cliente()
    elif opcao == '5':
        break
    else:
        print("\n\tOpção Invalida!\n")
