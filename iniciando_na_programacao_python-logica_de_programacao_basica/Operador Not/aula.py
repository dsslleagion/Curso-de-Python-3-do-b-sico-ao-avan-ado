# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

senha = input('Senha: ')

if not senha: # é retornado falsy sempre que uma string é avaliada vazia
    print('Você não digitou nada')

    