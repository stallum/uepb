#calcular média de 30 alunos e verificar se está aprovado, reprova ou em recuperação.

for i in range(4):
    soma_notas = 0
    for j in range(3):
        nota = float(input(f'Digite a {j + 1}ª nota: '))
        if nota < 0 or nota > 10:
            print('Nota inválida. Digite uma nota entre 0 e 10.')
            nota = float(input(f'Digite a {j + 1}ª nota: '))
        soma_notas += nota

    media = soma_notas / 3
    if media >= 7:
        print('Aprovado')
    elif 5 <= media < 7:
        print('Recuperação')
    else:
        print('Reprovado')

#

'''
for i in range(4):
    def notaValida(indice):
        while True:
            nota = float(input(f'Digite a {indice + 1}ª nota: '))
            if nota >= 0 and nota <= 10:
                return nota
            else:
                print('Nota inválida. Digite uma nota entre 0 e 10.')


    notas = [notaValida(i) for i in range(3)]
    media = sum(notas) / len(notas)
    if media >= 7:
        print('Aprovado')
    elif media < 7 and media >= 5:
        print('Recuperação')
    else:
        print('Reprovado')
'''