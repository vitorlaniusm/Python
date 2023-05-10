#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('Valor de Saque: R$')) #Valor do saque
total = saque # Total do saque
ced = 50 # valor da maior cedula a ser retirada
totced = 0 #contador de cedulas
while True:
    if total >= ced: # se o total for maior que 50
        total = total - ced # vai tirar 50 do total
        totced = totced + 1 # e somar um no contator de cedulas
    else:
        if totced > 0: # se o total for maior que zero ele mostra a mensagem
            print(f'O total de cedulas de R${ced} foi {totced}')
        if ced == 50: # quando ele não poder mais tirar 50 ele transforma ced em 20 e assim por diante ate chegar a 0.
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0

        if total == 0: # chegando a zero ele quebra o cod e finaliza.
            break
print('Volte Sempre')

