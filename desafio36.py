#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input('Valor do Imovel: '))
salario = float(input('Salario do Comprador: '))
ano = int(input('quantos anos de pagamento: '))
prest = (vcasa / (ano * 12))
juros = vcasa * 0.0087
if prest <= salario * 30 / 100:
    print('Valor de pagamento de {:.2f} mensal é o valor maximo aprovado. '.format(prest + juros))
else:
    print('Valor de {:.2f} acima dos 30% do salario mensal permitido.'.format(prest + juros))


