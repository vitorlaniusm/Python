media = n = soma = 0 # posso colocar todos juntos pois todos contem 0.
cont = maior = menor = 0
resp = 'S'

while resp in 'Ss':
    n = int(input('Digite um numero para a operação: '))
    cont = cont + 1
    soma = soma + n
    if cont == 1:  # se apenas um numero foi digitado ele define que este é o maior e o menor numero!
        maior = n
        menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    print('-------------' * 10)
    print('Processando...')
    print('-------------' * 10)
    resp = str(input("Digite deseja continuar? [S/N] ")).strip().upper()[0]

media = soma / cont
print('A soma dos valores deu {}, e o valor medio dos numeros digitados é {:.2f} '.format(soma, media))
print('O maior numero entre os digitados é {}, e o menor foi {}'.format(maior, menor))