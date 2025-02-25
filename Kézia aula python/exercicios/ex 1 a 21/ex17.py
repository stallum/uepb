# Peça dois números inteiros + um numero real. Calcule o produto do primeiro com a metade do segundo (1º * (2º/2)), a soma do triplo do primero com o terceiro (1º * 3 + 3º) e o terceiro elevado ao cubo (3º³ {math.pow 3º, 3} {3º ** 3})

primeiro = int(input('Digite um número inteiro: '))
segundo = int(input('Digite outro número inteiro: '))
terceiro = float(input('Digite um número real: '))

print(f'O produto do primeiro com a metade do segundo {primeiro * (segundo / 2)}')
print(f'A soma do triplo do primeiro com o terceiro {primeiro * 3 + terceiro}')
print(f'O terceiro elevado ao cubo {terceiro ** 3:.2f}')