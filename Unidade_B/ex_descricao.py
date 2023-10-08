"""
Exercício 1.5: Sistema de Gerenciamento de Estudantes

Contexto:
Você está construindo um software para gerenciar estudantes em uma escola. Cada estudante tem um nome, idade, nota e um ID único. A escola deseja realizar várias operações com esses estudantes, como adicionar uma nota a um estudante, calcular a média da turma e encontrar o estudante com a maior nota.

Objetivo:
Crie uma classe para representar um estudante e uma classe para representar uma turma de estudantes. Use métodos dentro dessas classes para executar as operações necessárias.

Requisitos:

Crie uma classe chamada Estudante com os seguintes atributos:

nome
idade
nota
id
Crie uma classe chamada Turma com o seguinte atributo:

estudantes: uma lista para armazenar objetos da classe Estudante.
Adicione os seguintes métodos à classe Turma:

adicionar_estudante(self, estudante): adiciona um estudante à turma.
remover_estudante(self, id): remove um estudante usando sua ID.
media_da_turma(self): calcula e retorna a média das notas dos estudantes.
melhor_estudante(self): retorna o estudante com a maior nota.
Desafio:
Adicione os seguintes métodos à classe Estudante:

alterar_nota(self, nova_nota): modifica a nota do estudante.
informacoes(self): imprime informações básicas sobre o estudante.

"""
