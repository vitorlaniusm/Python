from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pess in range(1, 8):

    ano = int(input('Qual o ano que a {}° pessoa nasceu? '.format(pess)))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1

print(' {} pessoas são maiores de idade'.format(totalmaior))
print(' {} pessoas são menores de idade'.format(totalmenor))













