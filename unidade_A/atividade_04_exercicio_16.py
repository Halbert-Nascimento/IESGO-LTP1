# Exercício 16 - Considere a seguinte lista: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] ----> e escreva um programa que imprime todos os elementos da lista que são menores que 5.


lista_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""
#primeira parte
# for verificar_menor_q5 in lista_a:
# 	if verificar_menor_q5 < 5:
# 		print("\t",verificar_menor_q5)

##Segunda parte extra nova lista

lista_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista_menoq5 =[]

for verificar_menor_q5 in lista_a:
	if verificar_menor_q5 < 5:
		lista_menoq5.append(verificar_menor_q5)

print(lista_menoq5)
"""
### extra fazer em uma linha

# new_list = list(filter(lambda verificar_menor: verificar_menor < 5, lista_a))
# print(new_list)

print(list(filter(lambda verificar_menor: verificar_menor < 5, lista_a)))