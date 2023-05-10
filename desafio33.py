n1 = int(input('Insira um numero: '))
n2 = int(input('Insira um numero: '))
n3 = int(input('Insira um numero: '))
menor = n1
if (n2 <= n1 and n3):
    menor = n2
if (n3 <= n2 and n3):
    menor = n3
print('O numero {} é o menor numero entre os digitados!'.format(menor))
maior = n1
if (n2 >= n1 and n3):
    maior = n2
if (n3 >= n1 and n2):
    maior = n3
print('O numero {} é o maior entre os digitados!'.format(maior))