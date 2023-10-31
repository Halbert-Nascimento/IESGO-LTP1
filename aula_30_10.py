# tipos de agrupamentos de dados
"""
dicionario
lista
tupla
string
"""
"""
import array as ar
# importa um array com nome de ar

# obj = ar.array(typecode[, initializer])
obj = ar.array('i', [1, 2, 3])
print(type(obj), obj)

obj2 = ar.array('u', 'Yesgo')
print(type(obj2), obj2)
obj2[0] = "I"
print(obj2)

obj3 = ar.array('d', [1.233, 2.234, 3.345])
print(type(obj3), obj3)
print(type(obj3), obj3[1:])
"""


import array as arr
meu_array = arr.array('i')

for indice in range(5):
    num = int(input("Digite um numero "))
    meu_array.append(num)

print(meu_array)

soma = 0
for somar in meu_array:
    soma += somar
print(soma)

# outra forma de somar mais simples
print("A soma do array e: ", sum(meu_array))

print("Menor valor do array: ", min(meu_array))
print("Maior valor do array: ", max(meu_array))


# remover o ultimo elemento do array, pop por padrao ele remove o ultimo elemento
print(meu_array)
ultimo = meu_array.pop()
print(meu_array)
print(ultimo)
meu_array.reverse()
print(meu_array)
