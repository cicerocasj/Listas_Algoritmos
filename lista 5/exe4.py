def exercicio4():
    x = 0
    for i in range(18644,33087):
        if str(2) in str(i) and str(7) not in str(i):
            x +=1
    print('Total de vezes: %s'%x)
exercicio4()