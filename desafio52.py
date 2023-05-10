n = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
if tot == 2:
    print(' {} é numero primo'.format(n))
else:
    print(' O numero {} não é primo'.format(n))
