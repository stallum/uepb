# 12.	A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
valorProduto = float(input('Digite o valor do produto: '))
parcelas = float(input('Digite a quantidade de parcelas: '))

if parcelas == 2: 
    valorParcela = valorProduto / parcelas
    print(f'O valor de cada parcela é de R$ {valorParcela:.2f}')
elif parcelas == 3:
    valorParcela = valorProduto / parcelas
    print(f'O valor de cada parcela é de R$ {valorParcela:.2f}')
elif parcelas == 4:
    valorParcela = valorProduto / parcelas
    print(f'O valor de cada parcela é de R$ {valorParcela:.2f}')
elif parcelas == 5:
    valorParcela = valorProduto / parcelas
    print(f'O valor de cada parcela é de R$ {valorParcela:.2f}')
elif parcelas == 1:
    print(f'O valor de cada parcela é de R$ {valorProduto:.2f}')
elif parcelas == 0:
    print(f'O valor de cada parcela é de R$ {valorProduto:.2f}')
else:
    print('Número de parcelas inválido!')