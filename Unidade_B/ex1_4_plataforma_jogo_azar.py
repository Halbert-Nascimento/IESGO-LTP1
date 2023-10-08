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
