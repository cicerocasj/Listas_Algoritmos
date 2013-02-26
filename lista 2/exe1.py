data = input('Date (dd/mm/yyyy): ')
dia = int(data[0:2])
mes = int(data[3:2])
ano = int(data[6:4])
print(dia)
print(mes)
print(ano)
if(dia > 31 or mes > 12 or ano > 9999):
    print('Data inválido')
if(dia < 31 or mes < 12 or ano < 9999):
    print('Data inválido')

