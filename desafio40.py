n1 = float(input('Nota do grau A: '))
n2 = float(input('Nota do grau B: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Aluno Reprovado nota {}'.format(m))
elif m >= 5.0 and m <= 6.9:
    print('Aluno em Recuperação nota {}'.format(m))
else:
    print('Aluno Aprovadonota {}'.format(m))