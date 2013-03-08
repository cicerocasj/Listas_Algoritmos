def exercicio():
    idade,altura = [],[]
    for i in range (1,6):
        idade.append(input('Idade: '))
        altura.append(input('Altura: '))
    print('Ordem recebida:')
    for i in range(0,5):
        print('Idade = %s <=> Altura = %s' %(idade[i],altura[i]))
    print('Invertido' )
    for y in range(0,5):
        print('Altura = %s <=> Idade = %s' %(altura[y],idade[y]))
exercicio()