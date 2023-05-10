soma = 0  #ACUMULADORES
cont = 0
for c in range(1,501 , 2):
    if c % 3 == 0:
        soma = soma + c # soma =+ c
        cont = cont + 1 # cont =+ 1
print('Dentro os {} valores impares e divisiveis por 3, a soma deles é {}'.format(cont, soma))