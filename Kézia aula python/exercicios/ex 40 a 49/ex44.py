'''
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7*h) – 58 e para mulheres: (62.1*h) - 44.7 (h = altura)
'''

sexo = input('Digite o sexo da pessoa (M/F): ').upper()
if sexo != 'M' and sexo != 'F':
        print('Sexo inválido.')
else:
    altura = float(input('Digite a altura da pessoa (em centimetros):  '))
    altura = altura / 100
    peso_ideal = 0

    if sexo == 'M': 
        peso_ideal = (72.7 * altura) - 58
        print(f'O peso ideal para um homem com {altura}m de altura é {peso_ideal:.2f}Kg.')
        if peso_ideal < 0:
            print('Altura inválida.')
            if altura < 0:
                print('Altura inválida.')
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f'O peso ideal para uma mulher com {altura}m de altura é {peso_ideal:.2f}Kg.')
        if peso_ideal < 0:
            print('Altura inválida.')
            if altura < 0:
                print('Altura inválida.')    