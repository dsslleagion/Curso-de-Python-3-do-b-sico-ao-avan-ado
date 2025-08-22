"""
Listas em Python
TIpo list - Mutavel

suporta varios valores de qualquer tipo 
Conhecimentos reutilizaveis - indices e fatiamento
Métodos Uteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
criar, let, alterar, apagar = lista[i](crud)
"""

# append - adiciona 
# pop - remove
# del - deleta 


# lista = [1,2,3,4,5]
# print(lista)

# lista.pop(3)
# print(lista)

# lista = [10,20,30,40,50]
# lista[2] = 300
# del lista[2] # deletou o indice 
# print(lista)
# print(lista[2])


# lista = [10,20,30,40,50]
# lista[2] = 300
# del lista[2] # deletou o indice 
# print(lista)



# para deletar ou modificar a lista, deve se mexer apenas no final dela

#adicionar
lista = [10,20,30,40,50]
lista.append(60) 
lista.pop() 
lista.append(70) 
lista.append("BBB")
lista.pop() # pega o ultimo item da lista e executa
lista.append(90) 
ultimo_valor = lista.pop()
ultimo_valor = lista.pop(3)
print(lista, 'Removido', ultimo_valor)

