aluno1p1 = float(input('aluno1 p1: '))
aluno2p1 = float(input('aluno2 p1: '))
aluno2p2 = float(input('aluno2 p2: '))
erro = 'Aluno 1 não teve acrecimo.'
if aluno1p1 >= 7:
    if aluno2p1 <= 6:
        if aluno2p2 > aluno2p1:
            acrescimo = (aluno2p2 - aluno2p1)/4
            print('O aluno 1 teve %.2f' %acrescimo)
    else:
        print(erro)
else:
    print(erro)