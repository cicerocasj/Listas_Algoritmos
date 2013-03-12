i,primo,res,num = 2,[],0,int(input('Numero: '))
while res != 1:
    if num % i == 0:
        res = num / i
        num = res
        primo.append(i)
    else:
        i += 1
print(primo)