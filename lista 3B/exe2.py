com,pag = int(input('Valor compra: ')),int(input('Valor pago: '))
tro,ret = pag - com, {}
if tro%50 ==0:
    ret['R$50'] = int(tro/50)
else:
    ret['R$50'] = int(tro/50)
    tro = tro % 50
    if tro%20 ==0:
        ret['R$20'] = int(tro/20)
    else:
        ret['R$20'] = int(tro/20)
        tro = tro % 20
        if tro%10 ==0:
            ret['R$10'] = int(tro/10)
        else:
            ret['R$10'] = int(tro/10)
            tro = tro % 10
            if tro%5 ==0:
                ret['R$5']= int(tro/5)
            else:
                ret['R$5']= int(tro/5)
                tro = tro%5
                if tro%2==0:
                    ret['R$2']= int(tro/2)
                else:
                    ret['R$2']=int(tro/2)
                    ret['R$1']=tro%2
print(ret)