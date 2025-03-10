# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qaualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5: 5 X 1 = 5, 5 X 2 = 10, ..., 5 X 10 = 50
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')