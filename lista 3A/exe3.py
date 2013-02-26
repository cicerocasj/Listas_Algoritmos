a = 80000
b = 200000
x = 0
while a <= b:
    a = int(a * 1.03)
    b = int(b * 1.015)
    x += 1
print('Precisa de %d' %x)