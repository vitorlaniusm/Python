num = int(input('Digite um numero inteiro para converção: '))
op = int(input('''Digite:
[1] para binario:
[2] para octal: 
[3] para hexadecimal: '''))

if op == 1:
    print('O numero convertido em binario é {}'.format(bin(num)[2:]))
elif op == 2:
    print('O numero convertido em octal é {}'.format(oct(num)[2:]))
elif op == 3:
    print('O numero convertido em Hexadecimal é {}'.format(hex(num)[2:]))
else:
    print('Opção incorreta tente novamente!')
