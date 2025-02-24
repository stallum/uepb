a = float(input('Digite o valor de a: '))
if a == 0:
    print('Isso não é uma equacção de segundo grau')
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    delta = b ** 2 - (4 * a * c)
    
    if delta < 0: 
        print ('Essa raiz é dos imaginários.')
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'as duas raizes da equação {a}x² + {b}x + {c} é: {raiz}.')
    else:
        x1 = -b + delta ** 0,5 /(2 * a)
        x2 = -b - delta ** 0,5 / (2 * a)
        print(f'as duas raizes da equação {a}x² + {b}x + {c} são: {x1} e {x2}.')
