valorHora = int(input('Quanto você ganha por hora: '))
numHora = int(input('Quantas horas você trabalhar por mês: '))
bruto = valorHora * numHora
imposto = (bruto/100) * 11
inss = (bruto/100) * 8
sindicato = (bruto/100) * 5
print('Imposto= %.2f' %imposto)
print('Inss= %.2f' %inss)
print('Sindicato= %.2f' %sindicato)
print('Salário Bruto = R$%.2f' %bruto)
liquido = bruto - (imposto + inss + sindicato)
print('Salário Líquido = R$%.2f' %liquido)