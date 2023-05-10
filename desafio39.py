from datetime import date

atual = date.today().year
nascimento = int(input('Qual sua o ano de nascimento? '))
idade = atual - nascimento

if idade == 18:
    print(' Este anos o senhor terá que se alistar as forças armadas brasileiras. ')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('O senhor ja passou da epoca de alistamentos a {} anos, o ano de alistamento foi {}'.format(saldo, ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('O senhor ira se alistar apenas no ano de {} daqui a apenas {} anos'.format(ano, saldo))