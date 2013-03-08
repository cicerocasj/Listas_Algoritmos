num = int(input('Número: '))
div = 0
for i in range(1,num+1):
    if num % i == 0:
        div += 1
if div > 2:
    print('Não é primo')
else:
    print('É primo')
