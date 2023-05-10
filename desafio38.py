num = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um numero inteiro: '))

maior = num

if num == num2:
    maior = num
    print('Ambos os numeros digitados são iguais!')
elif num > num2:
    maior = num
    print('O  maior valor entre os numeros digitados é {}'.format(maior))
elif num2 > num:
    maior = num2
    print('O  maior valor entre os numeros digitados é {}'.format(maior))

menor = num2

if num < num2:
    menor = num
    print('O  menor valor entre os numeros digitados é {}'.format(menor))
elif num2 < num:
    menor = num2
    print('O menor valor entre os numeros digitados è {}'.format(menor))


print('--------------' * 9,' Segundo Programa!')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
if n1 > n2:
    print('O primeiro numero é maior que o segundo! ')
elif n2 > n1:
    print('O segundo numero é o maior que o primeiro! ')
else:
    print('Ambos os numeros são iguais! ')
