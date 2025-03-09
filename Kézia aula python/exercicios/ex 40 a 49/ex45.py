#calcular média de 30 alunos e verificar se está aprovado, reprova ou em recuperação.

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
