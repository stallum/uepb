# ler 3 números inteiros positivos e usar em uma formula.

A = int(input('Escreva um número inteiro e positivo aqui: '))
if A < 0: 
    print('esse número é invalido! DIGITE UM NÚMERO INTEIRO E POSITIVO.')
else: 
    B = int(input('Escreva outro número inteiro e positivo aqui: '))
if B < 0:
    print('esse número é invalido! DIGITE UM NÚMERO INTEIRO E POSITIVO.')
else:
    C = int(input('Escreva outro número inteiro e positivo aqui: '))
if C < 0:
    print('esse número é invalido! DIGITE UM NÚMERO INTEIRO E POSITIVO.')
else:
    R = (A + B) ** 2
    S = (B + C) ** 2
    D = (R + S) / 2
    print(f'O resultado do calculo é: {D}')