n = str(input('Digite um nome completo: ')).strip()
nome = n.split()
print('primeiro nome do usuario é {}'.format(nome[0]))
print('O ultimo nome do usuario é {}'.format(nome[len(nome)-1]))