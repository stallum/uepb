# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

prod1 = float(input('Digite o preço do primeiro produto: '))
prod2 = float(input('Digite o preço do segundo produto: '))
prod3 = float(input('Digite o preço do terceiro produto: '))
melhor = min(prod1, prod2, prod3)
print(f'O produto mais barato é o que custa R${melhor:.2f}')