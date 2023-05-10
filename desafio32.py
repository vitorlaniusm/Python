from time import sleep
from datetime import date   # Modulo para data
ano = int(input('Digite o Ano: '))
print('Processando!!!')
sleep(3)
if ano == 0:
    ano == date.today().year  # Quando ano for zero ele buscara a data atual.
if (ano % 4 == 0 and ano != 100 == 0) or (ano % 400 == 0):
    # Para saber quando será Ano Bissexto devemos seguir o seguinte princípio: todos os anos múltiplos de 4
    # que também não são múltiplos de 100, com exceção dos múltiplos de 400, deverão ser anos bissextos.
    print('Este é um ano Bissexto!')
else:
    print('Este ano não é bissexto!')

