# 20.	Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

A = float(input('Digite um número pra A: '))
B = float(input('Digite um número pra B: '))

A, B = B, A
print(f'Agora A é {A} e B é {B}')