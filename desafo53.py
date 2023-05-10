frase = str(input('Digite um frase: ')).strip().upper()
p = frase.split()
junto = ''.join(p) # comando para juntar a frase sem espaço ou inserir simbolos nu lugar dos espaços.
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += junto[letra] # += soma das variaveis / junto[letra] é a variavel junto sendo verificada pelo FOR.
if inverso == junto:
    print('Esta frase é um palindromo!')
else:
    print('Esta frase não é um palindromo!')



''' Sem usar o for é possivel fazer usando o metodo de fatiamento deixando mais simples '''

frase = str(input('Digite um frase: ')).strip().upper()
p = frase.split()
junto = ''.join(p) # comando para juntar a frase sem espaço ou inserir simbolos nu lugar dos espaços.
inverso = junto[::-1] # Metodo de fatiamento! O -1 faz ler de traz para frente!
if inverso == junto:
    print('Esta frase é um palindromo!')
else:
    print('Esta frase não é um palindromo!')
