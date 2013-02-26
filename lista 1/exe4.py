salario = float(input('Digite o salário: '))
aumento = float(input('Digite o aumento em %: '))

aumento = (salario/100) * aumento
print('Valor do aumento: R$',aumento,'. Novo salário: R$',
      salario + aumento)
