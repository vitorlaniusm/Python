#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = totmil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Digite a Carta: '))
    valor = float(input('Digite o Valor: '))
    cont += 1
    soma = total + valor
    if valor > 1000.00:
        total = totmil + 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    resp = ' '
    while resp not in 'YN':
        resp = str(input('Quer Continuar? [Y/N]: ')).strip().upper()[0]
    if resp == 'N':
         break
print(f' O valor total gasto em suas compra foi de {total:.2f} reais!')
print(f' Apenas {totmil:.2f} produtos estão custando acima dos 1000,00 Reais!')
print(f' O produto mais barato é {barato}!')