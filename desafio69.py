#: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 ano
m = f = mt = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade < 20 and sexo == 'F':
        f += 1
    if idade >= 18:
        m += 1
    if sexo == 'M':
        mt += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Numero total de pessoas registradas com mais de 18 anos foi {m}')
print(f'A quantidade de homens cadastrados foi de {mt}')
print(f'Um total de {f} mulheres possuem menos de 20 anos')