"""
intrudução ao desempacotamento
"""

# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome1)

# nome1, nome2, nome3 =  ['Maria', 'Helena', 'Luiz']
# print(nome1)

# nome1, nome2 =  ['Maria', 'Helena', 'Luiz'] # erro de desempacotamento
# print(nome1)

# nome1, nome2, nome3, nome4 =  ['Maria', 'Helena', 'Luiz'] # erro tambem   
# print(nome1)

# nome1, *resto =  ['Maria', 'Helena', 'Luiz', 'João', 'Ana']
# print(nome1)
# print(resto)


# nome1, *_ =  ['Maria', 'Helena', 'Luiz', 'João', 'Ana']
# print(nome1)
# print(_)

_,_,nome1, *_ =  ['Maria', 'Helena', 'Luiz', 'João', 'Ana']
print(nome1)
print(_)