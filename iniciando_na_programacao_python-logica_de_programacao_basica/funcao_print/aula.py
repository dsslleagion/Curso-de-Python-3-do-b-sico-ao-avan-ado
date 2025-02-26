# função de exibição que recebe argumentos 
print(12, "olá", 1213123)
# exemplo citados 3 argumentos
# Saida: 12 olá 1213123
# por padrão o print coloca espaço entre os argumentos para a sua exibição

print(12, "olá", 1213123)
print(12, "olá", 1213123)
#saida
#12 olá 1213123
#12 olá 1213123
# por padrão as funções print ja  possuem quebra de linha 

# a função sep(separador) personaliza os espaços entre os argumentos basta apenas colocar sep="conteudo do espaço"
print(12, "olá", sep="-")
print(12, "olá", sep='-')
#saida
#12-olá
#12-olá


# agora a função end(final) é a personalização do final do print 
print(12, "olá", end="-")
#saida
#12 olá-
# \r\n quebra de linha e espaço
print(12, "olá",sep="-", end="\r\n")
#saida
#12 olá-12-olá

print(12, "olá",sep="-", end="\n")
#saida 
# (espaço)
#12-olá

# \r\n quebra de linha e espaço
print(12, "olá",sep="-", end="##\n")
#saida
#12-olá##

# \r\n quebra de linha e espaço
print(12, "olá",sep="-", end="\n##")
#saida
#12-ol�
# ##

# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')