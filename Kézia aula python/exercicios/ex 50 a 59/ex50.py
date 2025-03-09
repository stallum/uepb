# Faça um programa para calcular um valor A elevado a um valor B. Não usar A ** B.
A = float(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
numero = A
for i in range(B - 1):
    A *= A
print(f'O número {numero} elevado a {B} é igual a {A}.')