# calcular peso ideal com formula em base a altura 
# formula = (72,7 * altura) - 58

altura = float(input('Digite sua altura em cm: '))
metros = altura / 100
formula = (72.7 * metros) - 58
print(f'O seu peso ideal é: {formula}')