salario = float(input('Insira o salario do funcionario: '))
if salario <= 1250.00:
    aumento = salario * 15 / 100
    print('Seu aumento foi de {:.2f}R$ seu salario é de {:.2f}'.format(aumento, aumento + salario))
if salario > 1250.00:
    aumento = salario * 10 /100
    print('Seu aumento foi de {:.2f}R$ e seu salario total é de {:.2f}'.format(aumento, aumento + salario))
