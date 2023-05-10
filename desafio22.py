nome = str(input('insira o nome')).strip()
print('seu nome maiuscule é {}: '.format(nome.upper()))
print('seu nome maiuscule é: {}'.format(nome.lower()))
print('a quantidade de letras do seu nome é: {} '.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

