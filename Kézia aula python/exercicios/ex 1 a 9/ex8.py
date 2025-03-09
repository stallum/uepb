# Farenheit => celcius
# C = (F - 32) * 5/9

F = float(input('Digite a temperatura em Farenheit: '))
C = (F - 32) * 5/9
print(f'A temperatura em Celcius é {C:.2f} arredondado a 2 casas decimais')