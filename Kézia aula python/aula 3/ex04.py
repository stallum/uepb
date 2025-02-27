# um programa que receba um x como entrada e devolva uma aproximação do arco tangente de x
x = float(input('Digite um número real: '))
result = 0
for i in range(0, 51, 2):
    term = ((-1)) ** i * (x ** (2 * i + 1)) / (2 * i + 1)
    result += term

aproximation = result
print(f'A aproximação de arctan({x}) com 50 termos: {aproximation:.2f}')