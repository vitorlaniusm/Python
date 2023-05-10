primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1    # Contador!!!
total = 0   # vazio para receber o a nova informação!!!
mais = 10   # A operação começa com 10 termos fixos!!!
print('-------------' * 10)
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA!!!')
    print('-------------' * 10)
    mais = int(input('Quantos termos a mais voce quer mostrar: '))
print('FIM DO PROCESSO!!!')