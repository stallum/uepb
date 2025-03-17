"""
O cardápio de uma lanchonete é o seguinte: 

Especificação 	     Código 	 Preço
Cachorro Quente 	  100     	R$ 1,20
Bauru Simples         101     	R$ 1,30
Bauru com ovo         102     	R$ 1,50
Hambúrguer            103     	R$ 1,20
Cheeseburguer         104     	R$ 1,30
Refrigerante          105     	R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado. 
"""
import pandas as pd
itens = ['Cachorro Quente', 'Bauru Simple', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
codigos = [100, 101, 102, 103, 104, 105]
preços = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
itens_escolhidos = []

cardapio = {
    'Itens': itens,
    'Código': codigos,
    'Preço': preços
}
cardapio_df = pd.DataFrame(cardapio)

pedido = 0

while pedido == 0:
    print(f'{cardapio_df}\n caso queira terminar o pedido digite "0"')
    
    codigo = input('digite o código do item que você quer: ')

    while codigo.isalpha() or int(codigo) > 106 and int(codigo) < 100 and int(codigo) != 0 or codigo == type(float):
        codigo = input('código inválido, digite um do códigos presentes no cardápio: ')
    codigo = int(codigo)

    if codigo > 0:    
        if codigo == 100:
            id = 0
        if codigo == 101:
            id = 1
        if codigo == 102:
            id = 2
        if codigo == 103:
            id = 3
        if codigo == 104:
            id = 4
        if codigo == 105:
            id = 5

        quantidade = input('digite a quantidade que você quer do item: ')
        
        while quantidade.isalpha() or int(quantidade) < 0:
            quantidade = input('Você digitou uma quantidade inválida, Digite uma quantidade válida: ')
        quantidade = int(quantidade)

    else: 
        pedido += 1
        
        
pedido_feito = {
    'Item Escolhido': 
}