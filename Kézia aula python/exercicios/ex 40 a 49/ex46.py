# Escreva um programa que leia 10 números e informe o maior e menor numero
numeros = [float(input(f'Digite o {i + 1}º número: ')) for i in range(10)]
print(f'O maior número é {max(numeros)} e o menor número é {min(numeros)}')

