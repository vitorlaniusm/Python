salario  = float(input('anexe o salario do funcionario '))
porcentagem = float(input('anexe a porcentagem de aumento '))
print('o salario é de {} e o aumento foi de {}%'.format(salario, porcentagem))
aumento = salario * porcentagem / 100
total = aumento + salario
print('o aumento do funcionario foi de RS{:.2f} dando num total de RS{:.2f} '.format(aumento, total))