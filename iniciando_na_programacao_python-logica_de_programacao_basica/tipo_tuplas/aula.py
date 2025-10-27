"""
Tipo tupla - uma lista imutavel
"""

nomes_tupla_form1 = 'Maria', 'João', 'Ana'
print(nomes_tupla_form1)
print(type(nomes_tupla_form1))

nomes_tupla_form2 = ('Maria', 'João', 'Ana')
print(nomes_tupla_form2)
print(type(nomes_tupla_form2))

nomes_tupla_form3 = ['Maria', 'João', 'Ana']
nomes_tupla_form3 = tuple(nomes_tupla_form3)
print(nomes_tupla_form3)
print(type(nomes_tupla_form3))

# _,_,nome, *resto = ['Maria','', 'João', '3', '4',' 5', '6']
# print(nome)

# nomes = 'Maria', 'João', 'Ana'
# nomes[1] = 'outro'
# _, _,nome, *resto = nomes
# print(nome)
# print(nomes)


# nomes = 'Maria', 'João', 'Ana'
# nomes[1] = 'outro'
# print(nomes)