ano = int(input('Informe o ano: '))
if (ano % 4) == 0 and (ano % 100)!=0 or (ano % 400)==0:
    print('Esse é um ano bissexto')
else:
    print('Não um ano bissexto')