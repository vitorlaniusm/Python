d = int(input('dias alugados '))
km = float(input('km rodado com o veiculo '))
valor = (km * 0.15) + (d * 60.00)
print('O total a ser pago é de R${:.2f} '.format(valor))

