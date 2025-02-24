#---------------------------------------------------------
# verificação de número positivo

num = int(input('Digite um número inteiro: '))

if num > 0:
    print('Esse número é positivo.')

elif num == 0:
    print('Esse número é neutro')

else:
    print('Esse número é negativo')


#---------------------------------------------------------
# verificação de par ou impar

nume = int(input('Digite um número: '))

if nume == 0:
    print('Esse número é neutro.')

elif nume % 2 == 0:
    print('Esse número é par')

else: 
    print('Esse número é impar')


#---------------------------------------------------------
# Equação de segundo grau

import math

def bahskara(): 
    b = float(input('Digite o valor de b'))
    c = float(input('Digite o valor de c'))


a = float(input('Digite o valor de a'))
if a == 0:
    print('Isso não é uma equacção de segundo grau')
else:
    bahskara()
    
 
