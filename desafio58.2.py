from random import randint
comp = randint(0, 10)
cont = 0
right = False
while not acertou:
    n = int(input('Tente advinhar em que numero estou pensando ente 0 a 10: '))
    cont = cont + 1
    if n == comp:
        right = True
    else:
        if n > comp:
            print('Voce errou tente um numero menor! ')
        elif n < comp:
            print('Voce errou tente um numero maior! ')
print('Parabens voce acertou em {} tentativas'.format(cont))


