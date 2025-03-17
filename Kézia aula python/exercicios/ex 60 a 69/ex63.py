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
import pandas as pd
taxaJuros = 0
dividas = []
parcelas_list = []
taxasJuros = []

num = int(input('digite um número inteiro positivo que representará a quantidade de dividas que você quer registrar: '))

for i in range(1, num + 1):
    divida = input('Digite o valor da dívida adquirida: ')

    while divida.isalpha() or float(divida) < 0: 
        divida = float(input('Valor inválido, digite m valor numérico positivo: '))
    divida = int(divida)
    dividas.append(divida)

for i in range(1, num + 1):
    parcelas = input('Digite a quantidade de meses em que você dividirá sua dívida: \n (Saiba que serão aplicados juros apartir de uma divisão de 3 meses.)\n')

    while parcelas.isalpha() or int(parcelas) <= 0:
        parcelas = int(input('Valor inválido, digite um valor inteiro positivo.'))

    parcelas = int(parcelas)
    parcelas_list.append(parcelas)

for i in range(len(parcelas_list)):
    if parcelas_list[i] <= 2:
        taxaJuros = 0
    else:
        if parcelas_list[i] <= 5:
            taxaJuros = 0.1
        else:
            if parcelas_list[i] >= 6:
                taxaJuros = 0.15
            else:
                print('Quantidade de meses inserida é invalida')
    taxasJuros.append(taxaJuros)

valoresFinais = []
valoresJuros = []
valoresParcelas = []

for i in range(num):
    valorJuros = dividas[i] * taxasJuros[i]
    valorFinal = dividas[i] + valorJuros
    valorParcela = valorFinal / parcelas_list[i]

    valoresJuros.append(valorJuros)
    valoresFinais.append(valorFinal)
    valoresParcelas.append(valorParcela)

tabela = {
    'Valor da Dívida': valoresFinais,
    'Valor dos Juros': valoresJuros,
    'Quantidade de Parcelas': parcelas_list,
    'Valor da Parcela': valoresParcelas
}

tabela_df = pd.DataFrame (tabela)
print(tabela_df)