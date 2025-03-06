# 31.	Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.  
num_dia = int(input('Digite um número de 1 a 7: '))
if num_dia == 1:
    print('Domingo')
else:
    if num_dia == 2:
            print('Segunda')
    else:
            if num_dia == 3:
                print('Terça')
            else:
                if num_dia == 4:
                    print('Quarta')
                else:
                    if num_dia == 5:
                        print('Quinta')
                    else:
                        if num_dia == 6:
                            print('Sexta')
                        else:
                            if num_dia == 7:
                                print('Sábado')
                            else:
                                print('Valor inválido')