# Escreva um programa que imprima os N termos de uma Progressão Aritmética conforme a fórmula a seguir. O usuário deverá fornecer o valor de: n (numero de termos), r (razão) e a1 (primeiro termo).
# # An = A1 + (n - 1) * r
n = int(input('Digite o número de termos: '))
r = int(input('Digite a razão: '))
a1 = int(input('Digite o primeiro termo: '))
for n in range (1, n + 1):
    an = a1 + (n - 1) * r
print(an)