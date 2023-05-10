n = 0
cont = 0
soma = 0
n = int(input('Digite quantos numeros quiser para finalizar digite 999: '))
while n != 999:
    soma = (soma + n)
    cont = cont + 1
    n = int(input('Digite quantos numeros quiser para finalizar digite 999: '))
print('Voce digitou {} numeros, o total somado foi {} '.format(cont, soma))
