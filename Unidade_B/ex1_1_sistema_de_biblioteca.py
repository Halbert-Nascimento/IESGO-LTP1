class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "Disponivel"

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
        

logica_de_programaçao = Livro("Lógica de Programação", "Edécio Fernando Iepsen")
entendendo_algoritmos = Livro("Entendendo Algoritmos", "Aditya Y. Bhargava")
o_bom_dinossauro = Livro("O Bom Dinossauro", "Disney")

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

