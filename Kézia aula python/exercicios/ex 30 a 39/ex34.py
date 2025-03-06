'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: 
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; 
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuáro e encerre o programa; 
'''

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
if a == 0:
    print('A equação não é do segundo grau')
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('A equação não possui raízes reais')
    else:
        if delta == 0:
            x = -b / (2 * a)
            print(f'O delta dessa equação é {delta} e a raiz da equação é {x}')
        else:
         x1 = (-b + delta ** 0.5) / (2 * a)
         x2 = (-b - delta ** 0.5) / (2 * a)
         print(f'As raízes da equação são {x1} e {x2}')
