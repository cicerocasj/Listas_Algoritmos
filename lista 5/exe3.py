def exercicio3():
    x = 0
    for i in range(1067,3627):
        if i%2==0 and i%7==0:
            x+=1
    print('Total = %s'%x)
exercicio3()