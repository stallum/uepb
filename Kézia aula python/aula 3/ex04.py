# um programa que receba um x como entrada e devolva uma aproximação do arco tangente de x
x = float(input('Digite um número real: '))
result = 0
termos = 50
for i in range(termos):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
    result += term

aproximation = result
print(f'A aproximação de arctan({x}) com 50 termos: {aproximation:.2f}')

expoente = 1
sinal = 1
arctan = 0
x = float(input('Digite um número real: '))
for i in range(50):
    arctan += sinal * ((x**expoente)/expoente)
    expoente += 2
    sinal *= -1 
print('Kezia')
print(f'arctan de {x} é: {arctan}')