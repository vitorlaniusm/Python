print('Sequencia de Fibonacci')
n = int(input('Defina um numero para inicial a sequencia: '))

t1 = 0
t2 = 1
print('------------' * 10)
print('{} - {}'.format(t1, t2), end=' - ')

cont = 3    # a contagem ja começa no 3 pois ja possuo o t1 e t2 com numeros iniciais fixos!!!
while cont <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' - ')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('FIM')