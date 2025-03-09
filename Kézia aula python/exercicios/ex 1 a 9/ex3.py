# Programa de calculo de quatro médias

'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média das notas é: {media:.2f}')
'''

#----------------------------------------------------
def notaValida(indice):
    while True:
        nota = float(input(f'Digite a {indice + 1}ª nota: '))
        if nota >= 0 and nota <= 10:
            return nota
        else:
            print('Nota inválida. Digite uma nota entre 0 e 10.')

notas = [notaValida(i) for i in range(4)]
media = sum(notas) / len(notas)
print(notas)
print(f'A média das notas é: {media:.2f}')
#----------------------------------------------------
