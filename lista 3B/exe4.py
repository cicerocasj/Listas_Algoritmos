i = 2
num = int(input('Numero: '))
primo = []
res=0
while res != 1:
    if num % i == 0:
        print(i)
        res = num / i
        num = res
        primo.append(i)
    else:
        i += 1
print(primo)
