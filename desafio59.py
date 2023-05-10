from time import sleep
n = int(input('Digite um Valor: '))
n2 = int(input('Digite um valor: '))
select = 0
while select != 5:
    print('''Escolha uma opção a baixo: '
    '[1] Somar'
    '[2] Multiplicar'
    '[3] Maior'
    '[4] Novos Numeros'
    '[5] Sair do Programa''')
    select = int(input('Digite sua Opção: '))
    print('Processando!')
    sleep(1)
    if select == 1:
        addition = n + n2
        print('{} + {} = {}'.format(n, n2, addition))
    elif select == 2:
        mult = n * n2
        print('{} x {} = {}'.format(n, n2, mult))
    elif select == 3:
        if n > n2:
            bigger = n
        else:
            bigger = n2
            print('O maior numero entre os escolhido é {}'.format(bigger))
    elif select == 4:
        n = int(input('Digite um Valor: '))
        n2 = int(input('Digite um valor: '))
    elif select == 5:
        print('Saindo do sistema')
    else:
        print('Digite uma opção valida!')
    print('--------------' * 4)
    sleep(2.5)
print('Fim do programa!!!')

