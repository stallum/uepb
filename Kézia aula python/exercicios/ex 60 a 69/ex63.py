'''
faça um programa que receba o valor de uma dívida e mostre uma table com o segueintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo: 
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$ 1.000,00
R$ 1.100,00     100             3                       R$ 366,00
R$ 1.150,00     150             6                       R$ 191,67
'''

valor_divida = input('Digite o valor da dívida: ')

while valor_divida.isalpha() or float(valor_divida) < 0:
    valor_divida = input('Valor inválido, digite um valor de dívida válido: ')
valor_divida = float(valor_divida)

print(f'{"Valor da Dívida":<15} {"Valor dos Juros":<15} {"Quantidade de Parcelas":<25} {"Valor da Parcela":<15}')

parcelas = 1
juros = 0
valor_total = valor_divida + (valor_divida * juros / 100)
valor_parcela = valor_total / parcelas
print(f'R$ {valor_total:,.2f} {juros:<15} {parcelas:<25} R$ {valor_parcela:,.2f}')

parcelas = 3
juros = 10
valor_total = valor_divida + (valor_divida * juros / 100)
valor_parcela = valor_total / parcelas
print(f'R$ {valor_total:,.2f} {juros:<15} {parcelas:<25} R$ {valor_parcela:,.2f}')

parcelas = 6
juros = 15
valor_total = valor_divida + (valor_divida * juros / 100)
valor_parcela = valor_total / parcelas
print(f'R$ {valor_total:,.2f} {juros:<15} {parcelas:<25} R$ {valor_parcela:,.2f}')

#

'''
valor_divida = input('Digite o valor da dívida: ')

while valor_divida.isalpha() or float(valor_divida) < 0:
    valor_divida = input('Valor inválido, digite um valor de dívida válido: ')
valor_divida = float(valor_divida)

parcelas_juros = [(1, 0), (3, 10), (6, 15)]

for parcelas, juros in parcelas_juros:
    valor_total = valor_divida + (valor_divida * juros / 100)
    valor_parcela = valor_total / parcelas
    print(f'R$ {valor_total:,.2f} {'': <5} {juros:<15} {parcelas:<25} R$ {valor_parcela:,.2f}')
'''