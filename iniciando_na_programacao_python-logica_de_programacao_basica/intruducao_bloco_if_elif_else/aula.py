# if / elif      /else 
# se /se nao se  /se nao
# condicionais\

#condicionais simples
entrada = input('voce que "entrar" ou "sair"?')
if entrada == 'entrar':
 print("Bem vindo")
else:
 print("Logue novamente")


#condicionais compostas
entrada = input('voce que "entrar" ou "sair"?')
if entrada == 'entrar':
 print("Bem vindo")
elif entrada == 'sair':
 print("Logue novamente") 
else:
 print('não houve caracter digitado')

 entrada = input('voce que "entrar" ou "sair"?')
if entrada == 'entrar':
 print("Bem vindo")
# elif entrada == 'sair':
#  print("Logue novamente") 
# else:
#  print('não houve caracter digitado')

entrada = input('voce que "entrar" ou "sair"?')
if entrada == 'entrar':
 print("Bem vindo")
# elif entrada == 'sair':
#  print("Logue novamente") 
else:
 print('não houve caracter digitado')

# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')