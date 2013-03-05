v = []
v.append(float (input('Valor: ')))
v.append(float(input('Valor: ')))
v.sort()
dividendo = v[1]
divisor = v[0]
while dividendo % divisor > 0:
    resto = dividendo % divisor
    dividendo = divisor
    divisor = resto
print('%.f MDC'%divisor)

