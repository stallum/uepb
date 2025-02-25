# ler nome de um vendedor + ler salário fixo + ler valor total vendido no mês. fazer o valor da comissão dele em cima do salário (comissão = 15%)

nomeVendedor = input('Digite o nome do vendedor solicitado: \n')
salarioVendedor = float(input('Digite o salário do vendedor solicitado: \n'))
valorTotal = float(input('Digite o valor total vendido por esse vendedor em R$ (apenas numeros): '))
comissão = valorTotal * (15 / 100)
print(f'o vendedor de nome: {nomeVendedor}, recebe R${salarioVendedor} como salário e receberá R${comissão:.2f} como comissão esse mês, recebendo um total de: R${salarioVendedor + comissão:.2f}.')