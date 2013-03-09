def exercicio():
    idade,altura,soma,alunos = [],[],0,0
    for i in range (0,30):
        idade.append(int(input('Idade: ')))
        altura.append(int(input('Altura: ')))
        soma += altura[i]
    media = soma/30
    for i in range(0,30):
        if idade[i] > 13 and altura[i]< media:
            alunos += 1
    print('Media = %s\nAlunos = %s '%(media,alunos))
exercicio()