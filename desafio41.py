from datetime import date

nasc = int(input('Digite seu ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('Você nasceu no ano {} sua Categoria é mirim'.format(nasc))
elif idade > 9 and idade <= 14:
    print('Você nasceu no ano {} sua Categoria é Infantil'.format(nasc))
elif idade > 14 and idade <= 19:
    print('Você nasceu no ano {} sua Categoria é junior'.format(nasc))
elif idade > 19 and idade <= 25:
    print('Você nasceu no ano {} sua Categoria é Senior'.format(nasc))
else:
    print('Você nasceu no ano {} sua Categoria é Master'.format(nasc))