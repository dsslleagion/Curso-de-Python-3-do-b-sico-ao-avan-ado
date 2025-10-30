"""
Exercicio
Exiba os indices da lista
0 Maria 
1 Helena
2 Luiz
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append('João')

# lista_enumerada = enumerate(lista)
# print(lista_enumerada)
# print(next(lista_enumerada))

# for i in lista_enumerada:
#     print(i)

# print(lista_enumerada,"Zerado")

# for i in lista_enumerada:
#     print(i)

# for i in enumerate(lista):
#     print(i)

# for i in enumerate(lista):
#     print(i)

# for i in enumerate(lista):
#     print(i)

# for i in enumerate(lista):
#     print(i)

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# for i in enumerate(lista):
#     indice, nome = i
#     print(indice,nome)

for indice, nome in enumerate(lista):
    print(indice,nome)

for tupla_enumerada in enumerate(lista):
    print('---')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
