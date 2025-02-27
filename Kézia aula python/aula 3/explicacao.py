'''for i in range(5):
    print('Olá, mundo')

# range(inicio, fim, i/d)
for i in range(1, 6):
    num = i
    print(num)'''

# criar uma sequência de repetição que print numeros impares
#forma 1
for i in range(1, 51, 2):
    num = i
    print(num)

#forma 2
for i in range(1, 50):
    if i % 2 != 0:
        print(i)