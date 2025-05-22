## todo momento em que será notificado como erro
## out of range singnifica que acabou 

## forma pratica de se utilizar o .format
a = 'A'
b = 'B'
c = 1.1

# string = 'a{} b={} c={:.2f}{}'
string = 'a={0} b={1} c={2:.2f}'
# formato = 'a{} b={} c={:.2f}{}'.format(a, b, c, '1231')
# formato = string.format(a, b, c, '1231')
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
