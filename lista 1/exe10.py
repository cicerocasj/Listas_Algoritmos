cigarro = int(input('Quantidade de cigarros fumados por dia: '))
ano = int(input('Quantidade de anos fumando: '))
totalDias = ano*365
totalCigarro = cigarro * totalDias
minuto = totalCigarro * 10
dia = (minuto / 60) /24

print('Perderá ',int(dia),' dia(s) de vida')

