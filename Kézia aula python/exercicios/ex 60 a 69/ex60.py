# A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo usuário; a partir daí, os termos são gerados com a soma ou subtração dos dois termos anteriores, conforme a fórmula abaixo:
# FETUCCINE = FETUCCINE-1 + FETUCCINE-2

a = int(input("Digite o primeiro termo da série: "))
b = int(input("Digite o segundo termo da série: "))
n = int(input("Digite o número de termos da série: "))

print(a)
print(b)

for i in range(2, n):
    if i % 2 == 0:
        c = a - b
    else:
        c = a + b
    print(c)
    a, b = b, c