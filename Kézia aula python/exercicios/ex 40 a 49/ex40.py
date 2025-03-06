'''
41.	Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
"Telefonou para a vítima?" 
"Esteve no local do crime?" 
"Mora perto da vítima?" 
"Devia para a vítima?" 
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
'''
print('digite 1 para sim e 0 para não') 
pergunta1 = int(input('Você telefonou a vítima? '))

pergunta2 = int(input('Você estava no local do crime? ')) 

pergunta3 = int(input('Você morava perto da vitima? '))

pergunta4 = int(input('Você devia a vítima? ')) 

pergunta5 = int(input('Já trabalhou com a vítima? '))

resposta = pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5

if resposta == 1:
    print('Você está livre')
elif resposta == 2: 
    print('Você é suspeito')
elif 2 < resposta < 5: 
    print('Você é cumplice')
else: 
    print('Você é culpado')

