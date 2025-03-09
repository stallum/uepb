# 13.	Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
# valorVenda = custo * percent

def percentVal():
    while True:
        try:
            percent = float(input(' use apenas o numero sem ser dividido por 100 \n exemplo: 30 para 30%/0.3 \n Digite um valor percentual que será adicionado ao produto: '))
            percent = percent/100
            return percent
        except ValueError:
            print('Isso não é um número válido')

custo = float(input(f'Digite o valor de custo do produto a ser vendido: '))
if custo <= 0:
    print('Esse não é um valor válido!')
else: 
    valorVenda = custo * (1 + percentVal())
    print(f'O valor do produto final em cima do custo do produto e o percentual informado deve ser: {valorVenda}')