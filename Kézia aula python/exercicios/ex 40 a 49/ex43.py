'''
Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:  infantil A = 5 - 7 anos; infantil B = 8-10 anos; juvenil A = 11-13 anos; juvenil B = 14-17 anos; adulto = maiores de 18 anos.
'''

idade = int(input('Digite a idade do nadador: '))
if 5 <= idade <= 7:
    print('Categoria: infantil A')
    if 8 <= idade <= 10:
        print('Categoria: infantil B')
        if 11 <= idade <= 13:
            print('Categoria: juvenil A')
            if 14 <= idade <= 17:
                print('Categoria: juvenil B')
                if idade >= 18:
                    print('Categoria: adulto')
                else:
                    print('Idade inválida')    