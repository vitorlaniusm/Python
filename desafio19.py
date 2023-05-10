import random
n1 = str(input('nome do aluno: '))
n2 = str(input('nome do aluno: '))
n3 = str(input('nume do aluno: '))
n4 = str(input('nome do aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))