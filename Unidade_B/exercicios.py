"""
#ex1_1_sistema_de_biblioteca
class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.status = "Disponivel"
        self.id = id

    def __str__(self):
        return(f"\tTitulo: {self.titulo} \n\tAutor: {self.autor} \n\tStatus: {self.status}\n")


class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestador = []

    def __str__(self):
        return f"\nMembro: {self.nome} \nLivros emprestados: {len(self.livros_emprestador)}"

class Biblioteca:
    def __init__(self):    
        self.livros = {}
        self.membros = {}

    def __str__(self):
        return f"\n{len(self.livros)} livros cadastrados na biblioteca! \n{len(self.membros)} membros cadastrados na biblioteca! "

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro
        #Adiciona um livro ao dicionário de livros.

    def registrar_membro(self, membro): 
         self.membros[membro.nome] = membro
        #Adiciona um membro ao dicionário de membros.

    def emprestar_livro(self, titulo_livro, nome_membro): 
        #Empresta um livro para um membro se o livro estiver disponível.
        biblioteca_livro = self.livros.get(titulo_livro)
        biblioteca_membro = self.membros.get(nome_membro)

        if biblioteca_livro.status == "Disponivel":
            biblioteca_membro.livros_emprestador.append(biblioteca_livro)
            biblioteca_livro.status = "Emprestado!"
            print(f" {biblioteca_membro.nome} pegou Livro {biblioteca_livro.titulo} EMPRESTADO! \n")
        else:
            print(f"Livro: {biblioteca_livro.titulo}, indisponivel!")                     
        

    def retornar_livro(self, titulo_livro, nome_membro): 
        #Retorna um livro que estava emprestado.
        biblioteca_livro = self.livros.get(titulo_livro)
        biblioteca_membro = self.membros.get(nome_membro)

        if biblioteca_livro.status != "Disponivel":
             biblioteca_membro.livros_emprestador.remove(biblioteca_livro)
             biblioteca_livro.status = "Disponivel"
             print(f"\n Livro {biblioteca_livro.titulo} devolvido! \n Status atualizado!")
             print(f" Livro {biblioteca_livro.titulo} - Status {biblioteca_livro.status}!")
        else:
            print(f"Livro: {biblioteca_livro.status}, não se encontrava emprestado! \n")

    def remover_membro(self, nome_membro):
        membro_removido = self.membros.pop(nome_membro)
        return f"Membro removido: {membro_removido.nome}"
        
    def remover_livro(self, titulo_livro):
        livro_removido = self.livros.pop(titulo_livro)
        return f"Livro removido: {livro_removido.titulo}"
    
    def mostra_membros(self):
        print("\nMembros cadastrados:")
        for membro in self.membros:
            print("\t",membro)

    def mostra_livros(self):
        print("\nLivros cadastrados:")
        for livros in self.livros:
            print("\t",livros)
        

logica_de_programaçao = Livro("Lógica de Programação", "Edécio Fernando Iepsen", "001")
entendendo_algoritmos = Livro("Entendendo Algoritmos", "Aditya Y. Bhargava", "002")
o_bom_dinossauro = Livro("O Bom Dinossauro", "Disney", "003")

halbert = Membro("Halbert Nascimento")
murilo = Membro("Murilo Nascimento")
iesgo_biblioteca = Biblioteca()


iesgo_biblioteca.adicionar_livro(logica_de_programaçao)
iesgo_biblioteca.adicionar_livro(entendendo_algoritmos)
iesgo_biblioteca.adicionar_livro(o_bom_dinossauro)

iesgo_biblioteca.registrar_membro(halbert)
iesgo_biblioteca.registrar_membro(murilo)

iesgo_biblioteca.emprestar_livro("O Bom Dinossauro", "Murilo Nascimento")
iesgo_biblioteca.emprestar_livro("Lógica de Programação", "Halbert Nascimento")
iesgo_biblioteca.emprestar_livro("Entendendo Algoritmos", "Halbert Nascimento")

#printa info dos objetos
print(halbert)
print(iesgo_biblioteca)


print("\n Situação dos livros:")
print(logica_de_programaçao)
print(entendendo_algoritmos)
print(o_bom_dinossauro)

iesgo_biblioteca.retornar_livro("O Bom Dinossauro", "Murilo Nascimento")
iesgo_biblioteca.retornar_livro("Lógica de Programação", "Halbert Nascimento")
iesgo_biblioteca.retornar_livro("Entendendo Algoritmos", "Halbert Nascimento")

print("\n Situação dos livros:")
print(logica_de_programaçao)
print(entendendo_algoritmos)
print(o_bom_dinossauro)



print(iesgo_biblioteca.remover_membro("Halbert Nascimento"))
print(iesgo_biblioteca.remover_livro("O Bom Dinossauro"))

iesgo_biblioteca.mostra_membros()
iesgo_biblioteca.mostra_livros()


"""

"""
#ex1_2_gerenciador_pedidos_restaurante
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


"""
"""
#ex1_3_sis_gerenciamento_zoo

class Animal:
    def __init__(self, nome, especie, idade, dieta, id):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = ""
        self.id = id
        
    def __str__(self):
        return (f"\nEspecie: {self.especie} \nNome: {self.nome} \nIdade: {self.idade} \nDieta: {self.dieta}")

    def descricao(self):
        return (f"\n{self.especie} {self.nome}, tem {self.idade} anos e é {self.dieta}")
    # Leo é um Leão de 5 anos que é Carnívoro").

class Zoologico:
    def __init__(self):
        self.animais = {}
        self.animais_lista = []


    def __str__(self):
        return (f"\nO zoologico tem {len(self.animais_lista)} animais sobre nossos cuidados! ")

    def adicionar_animal(self, animal):# para adicionar um novo animal ao zoológico.
        self.animais_lista.append(animal)
        # self.animais.append(animal)
        # print("")


    def remover_animal(self, nome): #para remover um animal do zoológico usando seu nome.
        print(f"{nome.especie} {nome.nome} morreu...\n")
        self.animais_lista.remove(nome)
        

    def listar_animais(self): #para listar todos os animais no zoológico e suas informações.
        print("Animais No Zoologio:")
        for for_animal in self.animais_lista:
            print("\t",for_animal.descricao())


leao_billy = Animal("Billy", "Leão", "4", "Carnivoro", "001")
leao_wendy = Animal("Wendy", "Leão", "3.5", "Carnivoro", "002")
vaca_maru = Animal("Maru", "Vaca", "3", "Herbívoro", "003")
porco_jose = Animal("José", "Porco", "7", "Onívoro", "004")
# print(leao_billy.descricao())

brasilia_zoo = Zoologico()
brasilia_zoo.adicionar_animal(leao_billy)
brasilia_zoo.adicionar_animal(leao_wendy)
brasilia_zoo.adicionar_animal(vaca_maru)
brasilia_zoo.adicionar_animal(porco_jose)

brasilia_zoo.listar_animais()

brasilia_zoo.remover_animal(porco_jose)
brasilia_zoo.listar_animais()


print(brasilia_zoo)
"""

"""
#ex1_4_plataforma_jogo_azar
class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, id_unico):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id_unico = id_unico

    def __str__(self):
        return f"Nome: {self.nome} \nCategoria: {self.categoria} \nTaxa de Entrada: R${self.taxa_entrada:.2f} \nID: {self.id_unico}\n"
    
class Platafoma:
    def __init__(self):
        self.jogos = []

    def __str__(self):
        return f"A plataforma consta com {len(self.jogos)} jogos cadastrados! \n"

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def remover_jogo(self, id):
        for jogo in self.jogos:
            if jogo.id_unico == id:
                self.jogos.remove(jogo)
                return f"Jogo ID: {id} = '{jogo.nome}' removido com sucesso!"
        return f"Jogo ID: {id}, Não encontrado! "

    def listar_jogos(self):
        print("\nA plataforma tem os seguintes Jogos cadastrados! ")
        for jogo in self.jogos:
            print(jogo)


caca_niqueis = Jogo("Caça-níqueis da Sorte", "Caça-níqueis", 5.00, "001")
roleta = Jogo("Roleta Premium", "Mesa de Jogo", 10.00, "002")
poker_online = Jogo("Poker Texas Hold'em", "Mesa de Jogo", 20.00, "003")
blackjack = Jogo("Blackjack VIP", "Mesa de Jogo", 15.00, "004")
bingo_online = Jogo("Bingo da Sorte", "Bingo", 8.00, "005")

# print(roleta)

jogando_mais = Platafoma()
jogando_mais.adicionar_jogo(caca_niqueis)
jogando_mais.adicionar_jogo(roleta)
jogando_mais.adicionar_jogo(poker_online)
jogando_mais.adicionar_jogo(blackjack)
jogando_mais.adicionar_jogo(bingo_online)

print(jogando_mais)

jogando_mais.listar_jogos()

print(jogando_mais.remover_jogo(caca_niqueis.id_unico))
print(jogando_mais.remover_jogo("004"))
print(jogando_mais.remover_jogo("0010"))

jogando_mais.listar_jogos()

"""

"""
#ex1_5_Sis_gerenciamento_estudante

class Estudante:
    def __init__(self,nome, idade, nota, id_unico):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id_unico = id_unico

    def __str__(self):
        return f"\tNome: {self.nome}  \n\tIdade: {self.idade} \n\tNota: {self.nota:.1f} \n\tID: {self.id_unico}\n"
    
    def alterar_nota(self, nova_nota): #modifica a nota do estudante.
        self.nota = nova_nota

class Turma_Estudantes:
    def __init__(self):
        self.estudantes = []

    def __str__(self) -> str:
        return f"A turma contém {len(self.estudantes)} alunos! \n"

    def adicionar_estudante(self, estudante): #adiciona um estudante à turma.
        self.estudantes.append(estudante)
    
    def remover_estudante(self, id): #remove um estudante usando sua ID.
        for aluno in self.estudantes:
            if aluno.id_unico == id:
                self.estudantes.remove(aluno)
                return F"Id: {id}, '{aluno.nome}' removido da turma! "
        return f"ID: {id}, não encontrada na turma! "
        

    def media_da_turma(self): #calcula e retorna a média das notas dos estudantes.
        nota_media = 0
        nota_parcial = 0
        divisor_media = 0
        for aluno in self.estudantes:
            divisor_media +=1
            nota_parcial += aluno.nota
        nota_media = nota_parcial/divisor_media
        return (f"A media de notas dos {divisor_media} alunos é: {nota_media:.1f}")

    def melhor_estudante(self): #retorna o estudante com a maior nota.
        maior_nota = self.estudantes[0]
        for aluno in self.estudantes[1::]:
            if aluno.nota > maior_nota.nota:
                maior_nota = aluno
        return f"Aluno: {maior_nota.nome}, tem a maior nota da turma: NOTA: {maior_nota.nota:.1f} \n{maior_nota}"        

    def informacoes(self, estudante): #imprime informações básicas sobre o estudante.
        return f"Informações do estudante: \n{estudante}"
    
    

joao = Estudante("João", 19, 7.9,"001")
halbert = Estudante("Halbert", 30, 9,"002")
murilo = Estudante("Murilo", 16, 9.1,"003")
luiz = Estudante("Luiz", 20, 8,"004")

ltp1 = Turma_Estudantes()

ltp1.adicionar_estudante(joao)
ltp1.adicionar_estudante(halbert)
ltp1.adicionar_estudante(murilo)
ltp1.adicionar_estudante(luiz)

print(ltp1.media_da_turma())
print(ltp1.melhor_estudante())
print(ltp1.remover_estudante("001"))


print(ltp1.media_da_turma())
print(ltp1.informacoes(luiz))
halbert.alterar_nota(10)
print(ltp1.informacoes(halbert))
print(ltp1.melhor_estudante())

"""