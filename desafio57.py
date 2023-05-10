sex = str(input('Digite seu sexo: ')).strip().upper()[0]
while sex not in 'FM':
    sex = str(input('Dados Invalidos, digite novamente seu sexo: ')).strip().upper()[0]
    print('Opção {} valida '.format(sex))
