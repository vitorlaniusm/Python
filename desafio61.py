
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('Gerador de Progressão Aritmetica')
print('---------------' * 10)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
while cont <= 10:
    print('{}'.format(termo),end=' -> ')
    termo = termo + r
    cont = cont + 1
print('Finalizado!!!')