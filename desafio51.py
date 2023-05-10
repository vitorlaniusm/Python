#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = pt + (10 - 1 ) * r
for c in range(pt, d + r, r):
    print(c, end=' -> ')
print('FIM')
