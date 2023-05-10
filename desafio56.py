#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

# variaveis vazias para receberem dados
maioridade = 0
somaage = 0
media = 0
homem = ''
mulher = 0
for p in range(0, 4):
    print('-------------------------------------------------')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [m/f]: ')).strip().upper()
    somaage += age
    media = somaage / 4

#Verificação do Homem mais velho:
    if p == 1 and sex == 'M':
        maioridade = age
        homem = name
    if age > maioridade and sex == 'M':
        maioridade = age
        homem = name
    if sex == 'F' and age < 20:
        mulher = mulher + 1


print('O nome da pessoa mais velha é {} com {} anos'.format(homem, maioridade))

print('temos {} mulher(es) com menos de 20 anos'.format(mulher))
# media de idade do grupo:

print('A media de Idade dos Selecionados é {}'.format(media))






