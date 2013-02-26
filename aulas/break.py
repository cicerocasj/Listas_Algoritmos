soma = 0
i = 0
while True:
    x = int(input('Digite (0 sai): '))
    if x == 0:
        break
    soma = soma + x
    i = i + 1
print('media = %5.2f' %(soma/i))
