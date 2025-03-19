# Escreva um programa que leia 10 números e informe o maior e menor numero
maxi = None
mini = None

for i in range(1, 11):
    numero = input(f'Digite o {i}º numero: ')
    while numero.isalpha():
        numero = input(f'Termo inválido, Digite um número válido:')
    numero = float(numero)

    if maxi is None or numero > maxi:
        maxi == numero
    if mini is None or numero < mini:
        mini == numero



'''
numero = [float(input(f'Digite o {i + 1}º número: ')) for i in range(10)]
print(f'O maior número é {max(numero)} e o menor número é {min(numero)}')
'''