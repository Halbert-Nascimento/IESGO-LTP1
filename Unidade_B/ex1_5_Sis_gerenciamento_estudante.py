
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