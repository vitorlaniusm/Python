from random import randint
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(1, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()[0]
    if tipo == 'P' and total % 2 == 0:
        print('--------------' * 10)
        print(f'DEU PAR! Voce venceu o numero foi {total}!')
        v += 1
    elif tipo == 'I' and total % 2 == 1:
        print('--------------' * 10)
        print(f'DEU IMPAR! Voce Venceu o numero foi {total}!')
        v += 1
    else:
        print('--------------' * 10)
        print(f'GAME OVER! O numero era {total}')
        print('--------------' * 10)
        break
print(f'Voce venceu {v} vezes')
