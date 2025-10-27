"""
Exercicio

Exiba os indices da lista 
Maria
Helena
luiz

"""

# lista = ['Maria','helena','Luiz']

# for nome in enumerate(lista): # tambem exibe
#     print(nome, type(nome))


# lista = ['Maria','helena','Luiz']
# indices = range(len(lista))


# for nome in lista:
#     print(nome, type(nome))

lista = ['Maria','helena','Luiz']
indices = range(len(lista))


for indice in indices:
    print(indice, lista[indice], type(lista[indice]))