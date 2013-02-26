a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))
error = 'Não formou um Triângulo'
if b - c < a < b - c:
    resultado = error
elif a - c < b < a + c:
    resultado = error
elif a - b < c < a + b:
    resultado = error
elif (a + b)  <= c or \
                (a + c) <= b or \
                (b + c) <= a:
    resultado = error
elif a == b and c == a:
    resultado = 'Triângulo Equilátero'
elif a == b > c and a != c or \
                        a == c and a != b or \
                        c == b and c != a:
    resultado = 'Triângulo Isóceles'
elif a != b and a != c and b != c:
    resultado = 'Triângulo Escaleno'
print(resultado)

