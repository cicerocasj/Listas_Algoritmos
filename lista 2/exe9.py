metro = float(input('Metros: '))
latas = metro % 54
if latas == 0:
    latas = int(metro / 54)
else:
    latas = int(metro / 54) + 1
print('Total de latas a comprar %d. Preço a ser pago: R$%.2f'%(latas,latas * 80))