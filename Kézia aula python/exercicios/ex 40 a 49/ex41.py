'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
Álcool: 
até 20 litros, desconto de 3% por litro 
acima de 20 litros, desconto de 5% por litro 
Gasolina: 
até 20 litros, desconto de 4% por litro 
acima de 20 litros, desconto de 6% por litro.
Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
'''

litros = float(input('Digite o número de litros vendidos: '))
combustivel = input('Digite o tipo de combustível (A - álcool, G - gasolina): ')
if combustivel == 'A':
    if litros <= 20:
        valor = litros * 1.90 * 0.97
    else:
        valor = litros * 1.90 * 0.95
elif combustivel == 'G':
    if litros <= 20:
        valor = litros * 2.50 * 0.96
    else:
        valor = litros * 2.50 * 0.94

print(f'Valor a ser pago: R$ {valor:.2f}')
