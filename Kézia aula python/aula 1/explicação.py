print('Hello World')
print(3)
print(4.9)
print(3 + 4j )
print(type(3 + 4j))
print(type(4.9))

msg = "Alô Mundo"
idade = 4
altura = 1.8

print(msg)

nota1 = float(input('Digite aqui sua primeira nota: '))
nota2 = float(input('Digite aqui sua segunda nota:  '))
media = (nota1 + nota2)/2

print(f'a média de suas notas é {media:.2f}')


entrada = input()
print('o nome informado foi:', entrada)
print('o nome informado foi:'+ entrada) # o + significa além de somar contatenar

try: 
    nota1 = float(input('Digite aqui sua primeira nota: '))
    nota2 = float(input('Digite aqui sua segunda nota:  '))
    media = (nota1 + nota2)/2

    print(f'a média de suas notas é {media:.2f}')
except ValueError: 
    print('Isso não é um número, por favor escreva um número')


"{0:b}".format(37)
