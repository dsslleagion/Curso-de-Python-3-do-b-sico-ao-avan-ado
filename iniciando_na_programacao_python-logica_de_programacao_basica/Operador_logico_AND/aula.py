"""
Operadores logicos
AND (e) or (ou) not (não)
and - todas as condições precisam ser
verdadeiras.
Se qualquer valor for considerado falso,
a expressao inteira será avaliada naquele valor
São considerados falso(que você já viu)
0 0.0 '' Falsy
tambem existe o tipo none que é
usado para representar um não valor

"""

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')



# senha_permitida='123456'

# print(entrada)
# #if TRUE
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')


# #avaliação de curto circuito
# print(True and True and True)
# print(True and False and True)

# print(bool(''))# false
# print(bool(' '))# True
# print(bool('qualquer coisa digitada'))# True
# print(bool(0))# zero considera como false
# print(bool(1))# true


#OR

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')



# senha_permitida='123456'

# print(entrada)
# #if TRUE
# if (entrada == 'E' or entrada=='e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')


# senha = input('Senha: ') or 'Sem senha'



# Operador Lógico "not"
#Usado para inverter expressões
# not True = False
# not False = True

# senha = input('senha: ')

# if not senha:
#     print('Você não digitou nada')
# else:
#     print('Senha incorreta. ')

print(not False)

print(not True)