# 21.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.

ganho_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = float(input('Quantas horas você trabalha por mês? '))

salario_bruto = ganho_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
total_descontos = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f'Salário bruto: R${salario_bruto:.2f}')
print(f'Imposto de Renda: R${imposto_renda:.2f}')
print(f'INSS: R${inss:.2f}')
print(f'Sindicato: R${sindicato:.2f}')
print(f'Salário líquido: R${salario_liquido:.2f}')

#-------------------------------------------------
'''
def calcular_salario(ganho_hora, horas_trabalhadas):
    descontos = {
        'Imposto de Renda': 0.11,
        'INSS': 0.08,
        'Sindicato': 0.05
    }
    
    salario_bruto = ganho_hora * horas_trabalhadas # define futuramente o valor de salario_bruto
    total_descontos = sum(salario_bruto * taxa for taxa in descontos.values()) # define futuramente o valor de "valores_descontos"
    salario_liquido = salario_bruto - total_descontos # define futuramente o valor de salario_liquido
    
    return salario_bruto, {nome: salario_bruto * taxa for nome, taxa in descontos.items()}, salario_liquido

def main():
    ganho_hora = float(input('Quanto você ganha por hora? '))
    horas_trabalhadas = float(input('Quantas horas você trabalha por mês? '))
    
    salario_bruto, total_descontos, salario_liquido = calcular_salario(ganho_hora, horas_trabalhadas)
    
    print(f'Salário bruto: R${salario_bruto:.2f}')
    for nome, valor in total_descontos.items():
        print(f'{nome}: R${valor:.2f}')
    print(f'Salário líquido: R${salario_liquido:.2f}')

if __name__ == "__main__":
    main()
'''

