# Programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que quatro;
# - A mensagem "Você está em recuperação", se a média for maior ou igual a quatro e
# menor do que sete.
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
def notaN(indice):
    while True:
        nota = float(input(f'Digite a {indice + 1}ª nota: '))
        if nota >= 0 and nota <= 10:
            return nota
        else:
            print('Nota inválida. Digite uma nota entre 0 e 10.')

notas = [notaN(i) for i in range(2)]
media = sum(notas) / len(notas)
'''
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

#


if media == 10:
    print(f'A média das notas é: {media:.2f}')
    print('Aprovado com Distinção')
else:
    if media >= 7:
        print(f'A média das notas é: {media:.2f}')
        print('Aprovado')
    else:
        if media >= 4 and media < 7 :
            print(f'A média das notas é: {media:.2f}')
            print('Você está em recuperação')
            
        else:
            if media < 4 and media >= 0:
                print(f'A média das notas é: {media:.2f}')
                print('Reprovado')    
            else:
                print('Erro, nota inválida')
