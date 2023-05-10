print('------- * 10')
print('Analisando')
print('------- * 10')
r1 = float(input('Digite uma medida de uma reta: '))
r2 = float(input('Digite uma medida de uma reta: '))
r3 = float(input('Digite uma medida de uma reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Estas retas podem formar um triangulo')
else:
    print('Estas retas não podem format um triangulo')