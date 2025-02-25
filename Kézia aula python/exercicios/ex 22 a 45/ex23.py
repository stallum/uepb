# pedir um valor e mostre na tela se o valor é positivo ou negativo. 

num = float(input('Digite um número: '))
if num > 0:
    print(f'O número {num} é positivo.')
else:
    if num == 0:
        print(f'O número {num} é neutro.')
    else:
        print(f'O número {num} é negativo.')