hour = int(input('coloque a hora: '))
mins = int(input('coloque os minutos: '))
dur = int(input('coleque o tempo de duração: '))

hora = hour + (dur // 60)       # // divisão inteira
minutos = mins + (dur % 60)
hora += minutos // 60           # x = x + valor (no caso minutos // 60)
minutos = minutos % 60          # Resto do minutos limitando a o valor de 60
hora = hora % 24                # Resto do horas limitando a o valor de 24

print('{}:{}'.format(hora, minutos))