# Escreva um programa que calcula o fatorial de um dado número N. Se N for negativo, exiba uma mensagem de erro.
numero = int(input('Digite um número inteiro: '))
if numero < 0:
    print('Número inválido. Digite um número positivo.')
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f'O fatorial de {numero} é {fatorial}.')