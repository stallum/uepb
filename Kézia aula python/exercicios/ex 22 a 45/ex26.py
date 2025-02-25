# Faça um Programa que leia três números e mostre o maior deles. 
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite mais um número: '))

max = max(num1, num2, num3)
print(f'O maior número é {max}')
