# programa de calculo de salario com horas trabalhadas + ganho por hora
valorHora = float(input('Digite o valor da hora trabalhada: '))
horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
salario = valorHora * horasTrabalhadas
print(f'O salário a ser recebido é R${salario:.2f} arredondado a 2 casas decimais')