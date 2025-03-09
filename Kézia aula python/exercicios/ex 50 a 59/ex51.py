# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
N = int(input('Digite o valor de N: '))
H = 1
for i in range(2, N + 1):
    H += 1 / i
print(f'O valor de H com {N} termos é igual a {H}.')