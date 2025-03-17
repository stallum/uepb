# Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.
numeroValido = 1
countNumeroP = countNumeroI = countNumeros = somaPares = somaNumeros = numero = 0


while numeroValido > 0:
    numero = input('Digite um número positivo: ')
    while numero.isalpha() and float(numero) < 0:
        numero = input('Número invalido, Digite um número positivo')
    
    numero = float(numero)
    
    if numero == 0:
        numeroValido = 0
    else:
        somaNumeros += numero
        countNumeros += 1

    if numero % 2 == 0:
        countNumeroP += 1 
        somaPares += numero 
    else:
        countNumeroI += 1

countNumeroP = countNumeroP - 1

if countNumeroP > 0:
    mediaPares = somaPares / countNumeroP
else:
    mediaPares = 0

if countNumeros > 0:
    media = somaNumeros / countNumeros
else:
    media = 0

print(f' A quantidade de números pares é: {countNumeroP};\n A quantidade de números impares é: {countNumeroI};\n A Média dos Valores Pares é: {mediaPares:.2f};\n A Média geral dos números lidos é: {media:.2f}.')