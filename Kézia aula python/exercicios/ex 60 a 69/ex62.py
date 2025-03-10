# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
temp = []
num = int(input('Digite o número de temperaturas: '))
for i in range(1, num):
    temp.append(float(input(f'Digite a {i}ª temperatura: ')))

print(f'Menor temperatura: {min(temp)}')
print(f'Maior temperatura: {max(temp)}')
print(f'Média das temperaturas: {sum(temp) / len(temp)}')