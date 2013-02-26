peixe = float(input('Informe o peso do peixe: '))
if peixe > 50:
    quilo = peixe - 50
    print('Você passou %5.2fk' %quilo)
    multa = quilo * 4
    print('Multa a ser paga R$%5.2f' %multa)
else:
    print('O peso do peixe não passou de 50k, nada a ser pago.')