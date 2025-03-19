# cada espectador de um cinema respondeu a um questionário no qual constava sua idadee a sua opnião em relação ao filme: ótimo - 3, bom - 2, regular - 1. faça um programa que leia a idade e a opnião de 15 espectadores, calcule  e imprima: a média das idades das pessoas que responderam ótimo; a quantidade de pessoas que responderam regular; a porcentagem de pessoas que responderam bom, entre todos os espectadores analisados.

soma_idades = 0
quantidade_avaliacao_otimo = 0
quantidade_avaliação_regular = 0
quantidade_avaliacao_bom = 0
numero_avaliantes = 0

for i in range(0, 3, 1):

    idade = int(input("Qual a sua idade?"))
    
    print("1 - Regular")
    print("2 - Bom")
    print("3 - Ótimo")

    avaliacao = int(input("Qual sua avaliação do filme: "))

    
    if avaliacao == 3:
        soma_idades = soma_idades + idade
        quantidade_avaliacao_otimo += 1
    elif avaliacao == 1:
        quantidade_avaliação_regular += 1
    elif avaliacao == 2:
        quantidade_avaliacao_bom += 1 
    
    numero_avaliantes += 1
        


print(f"A média da idade das pessoas que acharam o filme ótimo foi: {soma_idades / quantidade_avaliacao_otimo}")
print(f'A quantidade de pessoas que responderam regular é: {quantidade_avaliação_regular}')
print(f'A porcentagem de pessoas que responderam bom é: {(quantidade_avaliacao_bom / numero_avaliantes) * 100:.2f}%')


#

'''
ages = []
opinions = []
for i in range(5):
    age = int(input('Digite a idade: '))
    opinion = int(input('Digite a opinião (ótimo = 3, bom = 2, regular = 1): '))
    ages.append(age)
    opinions.append(opinion)

average_age = sum([age for age in ages if opinions[ages.index(age)] == 3]) / opinions.count(3)
regular = opinions.count(1)
bom = opinions.count(2)
percentage_bom = (bom / 5) * 100
print(f'A média das idades das pessoas que responderam ótimo é: {average_age:.2f}')
print(f'A quantidade de pessoas que responderam regular é: {regular}')
print(f'A porcentagem de pessoas que responderam bom é: {percentage_bom:.2f}%')
'''