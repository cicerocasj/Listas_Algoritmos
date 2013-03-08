def exercicio3():
    num,impar,par,todos = [],[],[],[]
    for i in range(1,21):
        num = int(input('Numeros: '))
        todos.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    return print('Todos:\n%s\nImpares:\n%s\nPares:\n%s' %(todos,impar,par))
exercicio3()