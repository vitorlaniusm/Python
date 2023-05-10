while True:
    n = int(input('Digite um numero para verificar sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c * n}')
print('Fim do programa o numero digitado é negativo!')

