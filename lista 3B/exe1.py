number = float(input('Digite o numero: '))
x = 1
while number > x:
    if (number / x) / (x + 1) == x + 2:
        break
    else:
        x += 1
print('%d - %d - %d' %(x ,x+1 ,x+2 ))