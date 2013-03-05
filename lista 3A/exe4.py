def fib(valor):
    if valor < 2:
        return valor
    else:
        return fib(valor-1) + fib(valor-2)

print(fib(int(input('Valor: '))))
