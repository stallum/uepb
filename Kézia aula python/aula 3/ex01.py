soma = 0
n = 20
for i in range(n):
    num = int(input('Digite um número: '))
    soma = soma + num

media = soma / n
print(f'A média é: {media}')