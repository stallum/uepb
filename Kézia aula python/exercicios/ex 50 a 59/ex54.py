# Faça um programa que receba o número real x como entrada e devolva uma aproximação do arco tangente de x (em radianos) através da série: arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + x^9/9 - x^11/11 + ... considere a aproximação para 50 termos.
x = float(input('Digite um número real: '))
result = 0
for i in range(51):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
    result += term

aproximation = result
print(f'A aproximação de arctan({x}) com 50 termos: {aproximation:.2f}')