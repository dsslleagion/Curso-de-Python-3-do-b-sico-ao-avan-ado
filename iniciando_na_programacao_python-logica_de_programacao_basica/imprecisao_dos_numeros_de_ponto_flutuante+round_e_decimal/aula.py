"""
Imprecisão do ponto flutuante em Python
Double-precision floating-point format IEEE 754 é o formato usado internamente pelo Python para representar números de ponto flutuante. Devido à forma como esses números são armazenados na memória do computador, algumas operações aritméticas podem resultar em imprecisões aparentes.

"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)  # Saída: 0.7999999999999999
print(f'{numero_3:.2f}')
print(round(numero_3, 3))  # Arredondar para 3 casas decimais
