# 11.	Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.
# formula: J = C * i * t

deposito = float(input('Digite o valor do depósito: '))
taxa = 1 + (0.7 / 100)
print(f'O valor com rendimento após um mês é: R${deposito * taxa:.2f}')