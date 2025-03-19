# Pedir dois números e imprima o maior deles

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
else:
    print(f'O número {num2} é maior que o número {num1}')

#

'''
def numeroValido(indice):
    while True:
        try:
            num = float(input(f'Digite o {indice + 1}º numero: '))
            return num 

        except ValueError: 
            print('isso não é um número válido!')

numero = [numeroValido(i) for i in range(2)]
soma = sum(numero)
print(f'A soma desses dois números é: {soma:.2f}')
'''