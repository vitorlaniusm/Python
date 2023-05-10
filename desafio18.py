import math
a = float(input('Digite o angulo a ser calculado: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('o seno {:.2f} , cosseno {:.2f} e a tangente {:.2f}'.format(seno, cosseno, tangente))
