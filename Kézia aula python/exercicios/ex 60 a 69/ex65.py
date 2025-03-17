"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
a)	Média do salário da população;
b)	Média do número de filhos;
c)	Maior salário;
d)	Percentual de pessoas com salário até R$250,00.
Desenvolver um programa para calcular e escrever o que foi pedido nos itens a, b, c e d. O final da leitura de dados se dará com a entrada de um salário negativo.
"""
maxSalario = 0
salarioValido = 0
numFilhos = 0
salario = 0
contadorFamilias = 0
contadorSalario250 = 0


while salarioValido >= 0:
    salarioValido = input('Digite qual a renda salarial da família: ')

    while salarioValido.isalpha():
        salarioValido = input('Esse valor é inválido, digite um valor válido para salário: ')
    salarioValido = float(salarioValido)
    
    if salarioValido < 0:
        break

    salario += salarioValido

    if salarioValido > maxSalario:
        maxSalario = salarioValido

    if salarioValido <= 250:
        contadorSalario250 += 1

    countFilhos = input('Digite quantos filhos têm a família: ')

    while countFilhos.isalpha() and int(countFilhos) < 0:
        countFilhos = input('o valor inserido é invalido, insira um valor válido para número de filhos')
    countFilhos = int(countFilhos)

    numFilhos += countFilhos

    contadorFamilias += 1

mediaSalario = salario / contadorFamilias
mediaNumFilhos = numFilhos / contadorFamilias
percentMenor250 = (contadorSalario250 / contadorFamilias) * 100

print(
    f' a média dos salários das famílias dessa cidade é: {mediaSalario:.2f}\n a média dos filhos das famílias dessa cidade é: {mediaNumFilhos}\n o maior salário dessa cidade é: {maxSalario:.2f} o percentual de famílias com salário até R$250,00 é {percentMenor250:.2f}%'
)

