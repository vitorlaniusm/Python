frase = str(input('Insira uma frase: ')).upper().strip()
print('a quantidades de letras A que aparece é {}'.format(frase.count('A')))
print(' O local da primeira letra A é {}'.format(frase.find('A')+1))
print(' O local da ultima letra A é {}'.format(frase.rfind('A')+1))