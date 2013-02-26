dias = (((int(input('Valor de dias: ')) * 24 ) * 60) *60)
horas = ((int(input('Valor de horas: ')) * 60) *60)
minutos = int(input('Valor de minutos: ')) * 60
segundos = int(input('Valor de segundos: '))
print('Total em Segundos: ', dias + horas + minutos + segundos)