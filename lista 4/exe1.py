def exercicio1():
    num = []
    for i in range(1,11):
        num.append(int(input('Numero: ')))
    num.sort()
    return print('Menor = %d\nMaior = %d' %(num[0],num[9]))
exercicio1()
