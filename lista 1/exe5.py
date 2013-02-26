preco = float(input('Digite o preço: '))
desconto = float(input('Digite o desconto: '))

desconto = (preco/100) * desconto
print('Desconto: R$',desconto,' .Preço a pagar: ',preco - desconto)