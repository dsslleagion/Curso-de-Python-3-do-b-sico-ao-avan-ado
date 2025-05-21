#f-strings
'''
tudo envolvendo
'''


nome = "Dionisio Samuel"
altura = 1.75
peso=91
imc = peso/altura**2

# utilizando :.2f é simbolizar quantas casas decimais serão exibidas
# no exemplo dentro da formatação f""  {altura:.2f}
linha_1 = f"{nome} tem {altura:.2f} de altura"
# tambem é possivel colocar , em numero decimal ou float acrescentando ,
#linha_1 = f"{nome} tem {altura:,.2f} de altura"
linha_2 = f"{peso}, peso, quilos e seu IMC é,"
linha_3 = f"{imc:.2f}"
print(linha_1)
print(linha_2)
print(linha_3)