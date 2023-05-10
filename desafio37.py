num = int(input('Digite um numero inteiro para converção: '))
op = int(input('''Digite:
[1] para binario:
[2] para octal: 
[3] para hexadecimal: '''))

# Metodo format(value, format_spec) converte diretamente
# format_spec possui um listagem de formatações diverças as letras representam o tipo de formatação
# especifica b = binario / o = octal / x = hexadecimal entre outros.


if op == 1:
    print('O numero convertido em binario é {}'.format(format(num, 'b')))
elif op == 2:
    print('O numero convertido em octal é {}'.format(format(num, 'o')))
elif op == 3:
    print('O numero convertido em Hexadecimal é {}'.format(format(num, 'x')))
else:
    print('Opção incorreta tente novamente!')

