velocidade = int(input('qual a velocidade'))
if velocidade > 110:
    print('kkkkkk. Você foi multado')
    valor = velocidade - 110
    print('Você ultrapassou ' + str(valor) + 'km da velocidade permitida')
    print('Multa a ser paga: R$ ' + str(valor * 5) + '. kkkk')
else:
    print('Sua velocidade é de ' + str(velocidade) + 'km. Se deu bem mano!!!')
