number = int(input('Insira o numero que deseja converter: '))
opcao = int(input('------Escolha uma opção para conversao:----------\n 1. Para converter para Hexadecimal: \n 2. Para converter para Octal: \n 3. Para converter para Binário: \n '))

hexa = hex(number)
octa = oct(number)
bina = bin(number)

if opcao == 1:
    print(hexa)
elif opcao == 2:
    print (octa)
elif opcao == 3:
    print (bina)
else:
    print("Opção não reconhecida, favor escolher uma válida")
