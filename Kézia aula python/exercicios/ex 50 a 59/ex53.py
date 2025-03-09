# Fazer um programa que calcule e escreva a soma dos 50 primeros termos da seguinte série:  1000/1 + 997/2 + 994/3 + 991/4 + ... + 7/50 
soma = 0
for i in range(1, 51):
    soma += 1000 - 3 * (i - 1) / i
print(f'A soma dos 50 primeiros termos da série é igual a {soma}.')