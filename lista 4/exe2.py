def exercicio2():
    compra = int(input('Valor compra: '))
    pago = int(input('Valor pago: '))
    troco = pago - compra
    retorno = []
    if troco%50 ==0:
        for i in range(1,int(troco/50)+1):
            retorno.append(50)
    else:
        for i in range(1,int(troco/50)+1):
            retorno.append(50)
        troco = troco % 50
        if troco%20 ==0:
            for i in range(1,int(troco/20)+1):
                retorno.append(20)
        else:
            for i in range(1,int(troco/20)+1):
                retorno.append(20)
            troco = troco % 20
            if troco%10 ==0:
                for i in range(1,int(troco/10)+1):
                    retorno.append(10)
            else:
                for i in range(1,int(troco/10)+1):
                    retorno.append(10)
                troco = troco % 10
                if troco%5 ==0:
                    for i in range(1,int(troco/5)+1):
                        retorno.append(5)
                else:
                    for i in range(1,int(troco/5)+1):
                        retorno.append(5)
                    troco = troco%5
                    if troco%2==0:
                        for i in range(1,int(troco/2)+1):
                            retorno.append(2)
                    else:
                        for i in range(1,int(troco/2)+1):
                            retorno.append(2)
                        retorno.append(troco%2)
    n50,n20,n10,n5,n2,n1 = int(retorno.count(50)),int(retorno.count(20)),int(retorno.count(10)),int(retorno.count(5)),int(retorno.count(2)), int(retorno.count(1))
    return print('R$50 = %d \nR$20 = %d \nR$10 = %d \nR$5 = %d \nR$2 = %d \nR$1 = %d ' %(n50,n20,n10,n5,n2,n1))
exercicio2()