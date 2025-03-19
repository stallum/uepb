# Faça um program para smar os números pares posistivos menores que 1000

somatorio = 0
for i in range(1, 1000):
    if i % 2 == 0:
        somatorio += i

#
'''
somatorio = sum([i for i in range(1, 1000) if i % 2 == 0])
'''

print(f'A soma dos números pares positivos menores que 1000 é {somatorio}.')