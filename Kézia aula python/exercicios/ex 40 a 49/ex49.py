# Faça um programa para calcular a área de N quadriláteros. Formula: Área = base * altura.
N = int(input('Digite a quantidade de quadriláteros: '))
areas = [float(input(f'Digite a base do {i + 1}º quadrilátero: ')) * float(input(f'Digite a altura do {i + 1}º quadrilátero: ')) for i in range(N)]
print(f'Áreas: {areas}.')