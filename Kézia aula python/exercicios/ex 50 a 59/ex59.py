# Faça um programa qu peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.	
# 0 a 25: jovem, 26 a 60: adulto, maior que 60: idoso

contador = 0 
somador_idade = 0

num = int(input('Digite o número de pessoas: '))
for i in range(1, num):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    somador_idade += idade
    contador += 1

media = somador_idade / contador

if media <= 25:
    print('Turma jovem.')
else:
    if media <= 60:
        print('Turma adulta.')
    else:
        print('Turma idosa.')


#

'''
idades = []
num = int(input('Digite o número de pessoas: '))
for i in range(1, num):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    idades.append(idade)

media = sum(idades) / len(idades)
if media <= 25:
    print('Turma jovem.')
else:
    if media <= 60:
        print('Turma adulta.')
    else:
        print('Turma idosa.')
'''