"""
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
# """
# texto = 'luiz'
# texto. uso de metodos colocando ponto
# numeros = range(0,100,8)

# for numero in numeros:
#     print(numero)



# texto = 'luiz'.__iter__()
# print(texto)

# texto = iter('luiz') # __iter__()
# print(texto)


# texto = iter('luiz') # __iter__()
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

#for letra in texto
texto = 'luiz'# iteravel
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break