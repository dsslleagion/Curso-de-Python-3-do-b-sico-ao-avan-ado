"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = int(input("Digite um numero inteiro: "))

# if numero.isdigit():
#     entrada_int = int(numero)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar == True:
#         par_impar_texto = 'par'

#     print(f'o numero {entrada_int} é {par_impar_texto}')
# else:
#     print('você digitou um número não inteiro')


try:
    entrada_int = int(numero)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar == True:
        par_impar_texto = 'par'

    print(f'o numero {entrada_int} é {par_impar_texto}')
except:
    print('você digitou um número não inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite a hora em numeros inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else: 
        print('Não conheco essa hora')

except: 
    print('Por favor, digite numeros inteiros')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome:')
tamanho_nome = len(nome)

if tamanho_nome > 1  :
    if tamanho_nome <= 4:
        print('seu nome é muito pequeno')
    elif tamanho_nome >= 5 and tamanho_nome <= 6 :
        print("seu nome é normal")
    else:
        print('Seu nome é muito grande')
else:
    print("Digite mais de uma letra")