'''
import requests

'''


#-------------------------------------------------------------------------------------
# Calculadora de cotação

valorDolar = float(input('Digite o valor em US$ que você quer fazer o câmbio: '))
cotacao = float(input('Digite a cotação do dolar hoje: '))
valorTotal = valorDolar * cotacao
print(f'O valor que você tem para cotação é: {valorTotal:.2f}')

#-------------------------------------------------------------------------------------
#Calculadora de Investimento

C = float(input('Coloque o valor do capital investido: '))
i = float(input('Digite a taxa em porcentagem que você usará?: ps.: não use o símbolo de %: '))  / 100
t = int(input('Digite o tempo que você investirá em meses: '))
J =  C * i * t
valorFinal = C + J 

if t > 1: 
    print(f'O que você terá no final dos {t} meses é: {valorFinal}')
else :
    print(f'O que você terá no final dos {t} mês é: {valorFinal}')

#-------------------------------------------------------------------------------------

a = float(input())
b = float(input())

a, b = b, a 
print(f'a = {a} b = {b}')

#-------------------------------------------------------------------------------------
# calcular area de um circulo
import math 
r = float(input('Coloque um valor de raio de circulo: '))
areaCirculo = math.pi * math.pow(r, 2)
print(f'Essa é a area do circulo: {areaCirculo:.2f}')
print(f'Essa é a area do circulo: {areaCirculo}')