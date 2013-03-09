def exercicio5():
    v1,v2,v3 = [],[],[]
    for i in range (0,10):
        v1.append(input('Lista 1: '))
        v2.append(input('Lista 2: '))
        v3.append(v1[i])
        v3.append(v2[i])
    print('Lista 1 = %s'%v1)
    print(v2)
    print(v3)
exercicio5()