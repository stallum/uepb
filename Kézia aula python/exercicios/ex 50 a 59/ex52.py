# faça um programa para: ler um valor x qualquer; calcular Y = (x+1) + (x+2) + (x+3) + ... + (x+100); imprimir o valor de Y.
X = float(input('Digite o valor de X: '))
Y = 0
for i in range(1, 101):
    Y += X + i
print(f'O valor de Y é igual a {Y}.')