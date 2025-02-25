# Celsius => Farenheit
# C = (F - 32) * 5/9 <-> F = (C * 9/5) + 32

C = float(input('Digite a temperatura em Farenheit: '))
F = (C * 9/5) + 32
print(f'A temperatura em Farenheit é {F:.2f} arredondado a 2 casas decimais')
print(f'A temperatura em Farenheit é {F} exatos')