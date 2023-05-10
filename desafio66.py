soma = 0
cont = 0
while True:
    n = int(input('Digite um numero:(Parar digite 999)'))
    if n == 999:
        break # realiza a quebra (Finalização do comando)
    soma = soma + n
    cont = cont + 1


print(f'A quantidade de numeros digitados foi: {cont}')
print(f'A soma de todos os numeros digitados excluindo o numero de saida é: {soma}')