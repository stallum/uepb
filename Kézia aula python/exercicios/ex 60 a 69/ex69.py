'''
26.	Faça um programa que receba um número e verifique se ele é ou não triangular.  OBS: um número é triangular quando é resultado do produto de 3 números consecutivos. Exemplo: o número 24 é triangular, pois, 24 = 2 * 3 * 4.
'''
a, b, c = 1, 2, 3
numero = input('Digite um número inteiro: ')
while numero.isalpha() or type(numero) == float:
    numero = input('Detectado número invalido, digite um número inteiro: ')
numero = int(numero)

is_triangular = False
while a * b * c <= numero and is_triangular == False:
    if a * b * c == numero:
        is_triangular = True
    else:
        a += 1
        b += 1
        c += 1

if is_triangular == True:
    print(f'O número {numero} é triangular.')
else: 
    print(f'O número {numero} não é triangular.')