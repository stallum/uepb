'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
par ou ímpar; 
positivo ou negativo; 
inteiro ou decimal. 

'''

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada: (apenas o sinal, ex.: "+", "-") ')
if operacao == '+':
    resultado = numero1 + numero2
    print(f'O resultado da soma é {resultado}')
    if resultado % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
    if resultado >= 0:
        print('Número positivo')
    else:
        print('Número negativo')
    if resultado == int(resultado):
        print('Número inteiro')
    else:
        print('Número decimal')
elif operacao == '-':
    resultado = numero1 - numero2
    print(f'O resultado da subtração é {resultado}')
    if resultado % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
    if resultado >= 0:
        print('Número positivo')
    else:
        print('Número negativo')
    if resultado == int(resultado):
        print('Número inteiro')
    else:
        print('Número decimal')
elif operacao == '*':
    resultado = numero1 * numero2
    print(f'O resultado da multiplicação é {resultado}')
    if resultado % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
    if resultado >= 0:
        print('Número positivo')
    else:
        print('Número negativo')
    if resultado == int(resultado):
        print('Número inteiro')
    else:
        print('Número decimal')
elif operacao == '/':
    resultado = numero1 / numero2
    print(f'O resultado da divisão é {resultado}')
    if resultado % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
    if resultado >= 0:
        print('Número positivo')
    else:
        print('Número negativo')
    if resultado == int(resultado):
        print('Número inteiro')
    else:
        print('Número decimal')
else:
    print('Operação inválida')