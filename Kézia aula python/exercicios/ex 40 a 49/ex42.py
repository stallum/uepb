'''
43.	Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
Até 5 Kg           Acima de 5 Kg 
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

morango = float(input('Digite a quantidade de morangos (em Kg): '))
maca = float(input('Digite a quantidade de maçãs (em Kg): '))
total = 0
if morango <= 5:
    total += morango * 2.50
else:
    total += morango * 2.20
if maca <= 5:
    total += maca * 1.80
else:
    total += maca * 1.50
if morango + maca > 8 or total > 25:
    total *= 0.9
print(f'Valor a ser pago: R$ {total:.2f}')