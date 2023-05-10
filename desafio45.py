import random

print('''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.''')

print(''' Escolha entre as opções: 
[1] PEDRA
[2] PAPEL
[3] TESOURA''')

n = int(input('Digite sua opção: '))

list = ['PEDRA', 'PAPEL', 'TESOURA']
op = random.randint(0, 2)

if n == 1:
     print('O computador escolhe {}'.format(list[op]))
     if op == 2:
         print('You win!')
     elif op == 0:
         print('Empate!')
     elif op == 1:
         print('Voce Perdeu!')
elif n == 2:
    print('O computador escolhe {}'.format(list[op]))
    if op == 0:
        print('You win!')
    elif op == 1:
        print('Empate!')
    elif op == 2:
        print('Voce Perdeu!')
elif n == 3:
     print('O computador escolhe {}'.format(list[op]))
     if op == 1:
         print('You win!')
     elif op == 2:
         print('Empate!')
     elif op == 0:
         print('Voce Perdeu!')
