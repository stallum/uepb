'''
30.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 
Desconto do IR: 
Salário Bruto até 900 (inclusive) - isento 
Salário Bruto até 1500 (inclusive) - desconto de 5% 
Salário Bruto até 2500 (inclusive) - desconto de 10% 
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00  
(-) INSS (10%)                  : R$  110,00
(-) FGTS (11%)                  : R$  121,00
(-) Sindical (3%)               : R$   33,00
(-) Total de descontos          : R$  165,00
(-) Salário Liquido             : R$  935,00
'''

valor_hora = float(input('Digite aqui o valor da sua hora de trabalho: '))
horas_trabalhadas = float(input('Digite aqui a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 0.05
elif salario_bruto <= 2500:
    ir = 0.10
else:
    ir = 0.20

ir_valor = salario_bruto * ir
inss_valor = salario_bruto * 0.08
sindicato_valor = salario_bruto * 0.05

total_descontos = ir_valor + inss_valor + sindicato_valor
salario_liquido = salario_bruto - total_descontos

if salario_bruto < 0:
    print('Valor inválido')
else:
    print(f'Salário bruto: R${salario_bruto:.2f}')
    print(f'(-) IR ({ir * 100:.0f}%): R${ir_valor:.2f}')
    print(f'(-) INSS (8%): R${inss_valor:.2f}')
    print(f'(-) Sindicato (5%): R${sindicato_valor:.2f}')
    print(f'Total de descontos: R${total_descontos:.2f}')
    print(f'Salário líquido: R${salario_liquido:.2f}')

# 

'''
def calcular_salario(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas # define futuramente o valor de salario_bruto

    if salario_bruto <= 900:
        ir = 0 / 100
    else:
        if salario_bruto <= 1500:
            ir = 5 / 100
        else:
            if salario_bruto <= 2500:
                ir = 10 / 100
            else:
                if salario_bruto > 2500:
                    ir = 20 / 100
    descontos = {
        'Imposto de Renda': ir,
        'INSS': 0.08,
        'Sindicato': 0.05
    }
    
    total_descontos = sum(salario_bruto * taxa for taxa in descontos.values()) # define futuramente o valor de "valores_descontos"
    salario_liquido = salario_bruto - total_descontos # define futuramente o valor de salario_liquido
    
    return salario_bruto, {nome: salario_bruto * taxa for nome, taxa in descontos.items()}, salario_liquido

def main():
    valor_hora = float(input('Digite aqui o valor da sua hora de trabalho: '))
    horas_trabalhadas = float(input('Digite aqui a quantidade de horas trabalhadas no mês: '))
    
    salario_bruto, total_descontos, salario_liquido = calcular_salario(valor_hora, horas_trabalhadas)
    
    if salario_bruto < 0:
        print('Valor inválido')
    else:
        print(f'Salário bruto: R${salario_bruto:.2f}')
        for nome, valor in total_descontos.items():
            print(f'{nome}: R${valor:.2f}')
        print(f'Salário líquido: R${salario_liquido:.2f}')


if __name__ == "__main__":
    main()
'''

