from random import randint
from time import sleep
num = randint(0, 10)
cont = 0
n = int(input('Em qual numero entre 0 e 10 estou pensando? '))
print('------------------------')
while n != num:
    cont += 1
    sleep(0.5)
    if n < num:
        n = int(input('Você errou tente outro numero maior! '))
        print('------------------------')
    if n > num:
        n = int(input('Você errou tente outro numero menor! '))
        print('------------------------')
    if n == num:
        print('Parabens você adivinhou após {} tentativas'.format(cont))

