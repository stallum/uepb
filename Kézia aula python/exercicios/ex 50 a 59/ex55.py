# faça um programa que mostre os n termos da série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m imprima no final a soma da série.
n = int(input('Digite um número inteiro: '))
m = int(input('Digite um número inteiro: '))
s = 0
for i in range(1, n+1):
    s += i/m
    m += 2
print(f'A soma da série é: {s:.2f}')