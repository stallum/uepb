'''
27.	Faça um programa para validar o login e a senha de um usuário. Caso o usuário informe algum valor inválido informar o erro e pedir novamente os dados. A leitura dos dados deve ser encerrada quando o usuário digitar 3 vezes um valor inválido (login ou senha). Considere o login válido como "kezia" e a senha como "123".
'''
count = 1

login = input('Digite o Login: ').lower()
while count < 3 and login != 'kezia':
    login = input('Login inválido, digite um login válido: ').lower()
    count += 1

senha = input('Digite sua senha: ')
while count < 3 and senha != '123':
    senha = input('Senha inválida, digite sua senha novamente: ')
    count += 1


print(f'ERRO, VOCÊ EXCEDEU AS TENTATIVAS DE LOGIN')