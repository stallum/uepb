#29.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: salários até R$ 280,00 (incluindo): aumento de 20% salários entre R$ 280,00 e R$ 700,00: aumento de 15% salários entre R$ 700,00 e R$ 1500,00: aumento de 10% salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela: o salário antes do reajuste; o percentual de aumento aplicado; o valor do aumento; o novo salário, após o aumento. 

salario = float(input('Digite aqui o salário do colaborador: '))
if salario <= 280:
    aumento = 20
    novo_salario = salario + (salario * 0.20)
else:
    if salario > 280 and salario <= 700:
        aumento = 15
        novo_salario = salario + (salario * 0.15)
    else:
        if salario > 700 and salario <= 1500:
            aumento = 10
            novo_salario = salario + (salario * 0.10)
        else:
            if salario > 1500:
                aumento = 5
                novo_salario = salario + (salario * 0.05)
            else:
                print('Valor inválido')

print(f'O salário antes do reajuste era de: R${salario}')
print(f'O percentual de aumento aplicado foi de: {aumento}%')
print(f'O valor do aumento foi de: R${novo_salario - salario}')
print(f'O novo salário, após o aumento, é de: R${novo_salario}')