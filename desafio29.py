velocidade = float(input('Velocidade do Veiculo: '))
if velocidade > 80:
    print('Velocidade de 80km/h excedida! Você foi multado! ')
    multa = (velocidade - 80) * 7
    print('Sua multa tem o valor de {:.2f}'.format(multa))
else:
    print('Velocidade dentro do limite!')

print('--=--' * 20)
print('Tenha um bom dia!!!')
print('--=--' * 20)