km = float(input('Digite a distancia percorrida em KM: '))
if km <= 200:
    custo = km * 0.50
    print('Sua viagem custou {:.2f}R$'.format(custo))
else:
    custo = km * 0.45
    print('Sua viagem custou {:.2f}R$'.format(custo))