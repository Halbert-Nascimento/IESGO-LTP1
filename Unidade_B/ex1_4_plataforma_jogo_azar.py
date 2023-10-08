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


tetris = Jogo("Tetris", "Quebra-cabeça", 2, "001")
flyff = Jogo("Flyff", "RPG", 20, "002")
f1 = Jogo("F1", "Corrida", 6, "003")

# print(flyff)

jogando_mais = Platafoma()
jogando_mais.adicionar_jogo(tetris)
jogando_mais.adicionar_jogo(flyff)
jogando_mais.adicionar_jogo(f1)

print(jogando_mais)

jogando_mais.listar_jogos()

print(jogando_mais.remover_jogo(tetris.id_unico))
print(jogando_mais.remover_jogo("0003"))

jogando_mais.listar_jogos()
