def exercicio():
    mes = ['1 - Janeiro','2 - Fevereiro','3 - Março','4 - Abril','5 - Maio','6 - Junho',
           '7 - Julho','8 - Agosto','9 - Setembro','10 - Outubro','11 - Novembro','12 - Dezembro']
    temp,soma,total = [],0,[]
    for i in range (0,4):
        temp.append(int(input('Temperatura M.: ')))
        soma += temp[i]
    media = soma/4
    print('Media = %s\n'%media)
    for i in range(0,4):
        if temp[i]> media:
            total.append(mes[i])
            print('%s <=> Temperatura = %s'%(mes[i],temp[i]))

            #for i in range(0,len(total)):
        #print('Mes = %s'%total[i])

exercicio()
