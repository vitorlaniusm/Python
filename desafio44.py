print('''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros''')

print('===================' * 3)

valor = float(input('Iserir o valor do produto: '))

print('===================' * 3)

print('''Opções de Pagamento:
[1] Dinheiro/ Cheque:
[2] Cartão:
[3] 2x Cartão: 
[4] 3x ou mais no Cartão:''')

print('===================' * 3)

op = int(input('Escolha sua opção de pagamento: '))

um = valor - (valor * 10 / 100)
dois = valor - (valor * 5 / 100)
tres = valor
quatro  = valor +  (valor * 20 / 100)

if op == 1:
    print('O valor a ser pago em dinheiro ou cheque com desonto de 10% será {}'.format(um))
elif op == 2:
    print('O valor no cartão tem 5% de desconto, ficando {}'.format(dois))
elif op == 3:
    print('O valor em até 2x sem juros fica {}'.format(tres))
elif op == 4:
    print('O valor em 3x ou mais terá juros de 20% ficando {}'.format(quatro))
else:
    print('Opção de pagamento invalida!')