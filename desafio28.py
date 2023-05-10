from random import randint
from time import sleep
computador = randint(0, 5) #Computador randomiza um numero de 0 a 5
print('Escolha um numero de 0 a 5')
jogador = int(input(' e tente adivinha em qual estou pensando: '))

print('PROCESSANDO...')
sleep(4)

if jogador == computador:
     print('Parabens seu merda voce acertou!!O numero que pensei foi {} ...'.format(computador))
else:
     print('Seu bosta voce errou!! O numero que pensei foi {} ...'.format(computador))
