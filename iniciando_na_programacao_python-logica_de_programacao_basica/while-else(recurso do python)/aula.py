"""

while/else

"""

string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == '':
       break 

    # break
    print(letra)
    i += 1
else:
    print('O else foi executado')
print('esta fora')