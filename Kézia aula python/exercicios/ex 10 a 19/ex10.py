# 10.	Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

cotacao = float(input('Digite a cotação do dólar: '))
dolar = float(input('Digite a quantidade de dólares disponíveis: '))
real = cotacao * dolar
print(f'O valor em reais é: R${real:.2f}')
print(f'O valor em reais é: R${real}')