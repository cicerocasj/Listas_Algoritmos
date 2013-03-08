compra = int(input('Valor compra: '))
pago = int(input('Valor pago: '))
troco = pago - compra
retorno = {}
if troco%50 ==0:
    retorno['R$50'] = int(troco/50)
else:
    retorno['R$50'] = int(troco/50)
    troco = troco % 50
    if troco%20 ==0:
        retorno['R$20'] = int(troco/20)
    else:
        retorno['R$20'] = int(troco/20)
        troco = troco % 20
        if troco%10 ==0:
            retorno['R$10'] = int(troco/10)
        else:
            retorno['R$10'] = int(troco/10)
            troco = troco % 10
            if troco%5 ==0:
                retorno['R$5']= int(troco/5)
            else:
                retorno['R$5']= int(troco/5)
                troco = troco%5
                if troco%2==0:
                    retorno['R$2']= int(troco/2)
                else:
                    retorno['R$2']=int(troco/2)
                    retorno['R$1']=troco%2
print(retorno)
