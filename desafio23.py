num = int(input('insira um numero'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade igual {}'.format(u))
print('dezena igual {}'.format(d))
print('centena igual {}'.format(c))
print('milhar igual {}'.format(m))