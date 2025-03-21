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

cardapio_display = {
    'Itens': itens,
    'Código': codigos,
    'Preço': preços
}

cardapio_df = pd.DataFrame(cardapio_display)

pedido = 0
total_pedido = 0
quantidade_txt = 'Digite a quantidade que você quer: '

while pedido == 0:
    print(cardapio_df)
    codigo = input('Digite um código presente em nosso cardápio, (ou "0" para finalizar o pedido): ')
    while codigo.isalpha():
        codigo = input('Código inválido, digite um código em nosso cardápio: ')
    
    codigo = int(codigo)

    if codigo == 0:
        pedido += 1

    
    elif codigo < 100 or codigo > 105:
        while int(codigo) < 100 or int(codigo) > 105:
            print('código inválido')
            print(cardapio_df)
            codigo = input('digite um dos códigos presentes no nosso cardápio: ')
        codigo = int(codigo)
            
        if codigo == 100:
            quantidade = input(quantidade_txt)
            while quantidade.isalpha() or int(quantidade) < 0:
                quantidade = input('quantidade inválida, digite uma quantidade válida: ')
            quantidade = int(quantidade)

            nome = 'Cachorro Quente' 
            total = 1.2 * quantidade
            print(f"{nome} ({quantidade}x) - R$ {total:.2f}")
            total_pedido += total

        elif codigo == 101:
            quantidade = input(quantidade_txt)
            while quantidade.isalpha() or int(quantidade) < 0:
                quantidade = input('quantidade inválida, digite uma quantidade válida: ')
            quantidade = int(quantidade)

            nome = 'Bauru Simples'
            total = 1.3 * quantidade
            print(f"{nome} ({quantidade}x) - R$ {total:.2f}")
            total_pedido += total 
                    
        elif codigo == 102:
            quantidade = input(quantidade_txt)
            while quantidade.isalpha() or int(quantidade) < 0:
                quantidade = input('quantidade inválida, digite uma quantidade válida: ')
            quantidade = int(quantidade)

            nome = 'Bauru com ovo'
            total = 1.5 * quantidade
            print(f"{nome} ({quantidade}x) - R$ {total:.2f}")
            total_pedido += total

        elif codigo == 103:
            quantidade = input(quantidade_txt)
            while quantidade.isalpha() or int(quantidade) < 0:
                quantidade = input('quantidade inválida, digite uma quantidade válida: ')
            quantidade = int(quantidade)

            nome = 'Hambúrguer'
            total = 1.2 * quantidade
            print(f"{nome} ({quantidade}x) - R$ {total:.2f}")
            total_pedido += total
                         
        elif codigo == 104:
            quantidade = input(quantidade_txt)
            while quantidade.isalpha() or int(quantidade) < 0:
                quantidade = input('quantidade inválida, digite uma quantidade válida: ')
            quantidade = int(quantidade)

            nome = 'Cheeseburguer'
            total = 1.3 * quantidade
            print(f"{nome} ({quantidade}x) - R$ {total:.2f}")
            total_pedido += total
                            

        elif codigo == 105:
            quantidade = input(quantidade_txt)
            while quantidade.isalpha() or int(quantidade) < 0:
                quantidade = input('quantidade inválida, digite uma quantidade válida: ')
            quantidade = int(quantidade)

            nome = 'Refrigerante'
            total = 1.0 * quantidade
            print(f"{nome} ({quantidade}x) - R$ {total:.2f}")
            total_pedido += total

print(f'\n total geral do pedido: R${total_pedido:.2f}')



#



'''
itens = ['Cachorro Quente', 'Bauru Simple', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
codigos = [100, 101, 102, 103, 104, 105]
preços = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]


cardapio = {
    100: ('Cachorro Quente', 1.20),
    101:  ('Bauru Simples', 1.30),
    102: ('Bauru com Ovo', 1.50),
    103: ('Hambúrguer', 1.20),
    104: ('Cheeseburguer', 1.30),
    105: ('Refrigerante', 1.00)
}

cardapio_display = {
    'Itens': itens,
    'Código': codigos,
    'Preço': preços
}

cardapio_df = pd.DataFrame(cardapio_display)

pedido = 0
total_pedido = 0
itens_pedido = []

print(cardapio_df)
while pedido == 0:
    codigo = input('Digite o código de um produto de nosso cardápio: (ou zero, caso queira terminar o pedido)')
    
    if int(codigo) == 0:
        pedido += 1

    else: 
        while codigo.isalpha() or int(codigo) < 100 or int(codigo) > 105:
            codigo = input('Código fornecido inválido, por favor digite um código válido: ')
        codigo = int(codigo)

        quantidade = input('Digite a quantidade que você quer: ')

        while quantidade.isalpha() or int(quantidade) < 0:
            quantidade = input('Quantidade inválida, por favor digite uma quantidade válida: ')
        quantidade = int(quantidade)

        nome, preco = cardapio[codigo]
        total = quantidade * preco
        total_pedido += total
        itens_pedido.append((nome, quantidade, total))
    print(f"{nome} ({quantidade}x) - R$ {total:.2f}")
print('\n Resumo do Pedido')
for item in itens_pedido:
    nome, quantidade, total = item
    print(f'{nome} ({quantidade}x) - R$ {total:.2f}')
  
print(f"\nTotal geral do pedido: R$ {total_pedido:.2f}")
'''