media = 0
somamedia = 0
homem = 0
maisvelho = 0
mulher = 0

for p in range(0, 3):

    print('---------------------------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()

    media = media + idade
    somamedia = media / 3

    if sex == 'M' and p == 1:
        maisvelho = idade
        homem = nome
    if sex == 'M' and idade > maisvelho:
        maisvelho = idade
        homem = nome
    if sex == 'F' and idade < 20:
        mulher = mulher + 1








print('A idade media dos envlvidos é {}'.format(somamedia))
print('O homem mais velho é o {}!'.format(homem))
print('  {} mulheres possuem menos de 20 anos'.format(mulher))

