while True:
    try:
        nota = input('Informe a nota: ')
        validar = int(nota)
        res = 1
    except ValueError:
        res = 0

    if res == 1:
        print('Nota válida')
        break
    else:
        print('Nota Inválida')
