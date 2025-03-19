'''
27.	Faça um programa para validar o login e a senha de um usuário. Caso o usuário informe algum valor inválido informar o erro e pedir novamente os dados. A leitura dos dados deve ser encerrada quando o usuário digitar 3 vezes um valor inválido (login ou senha). Considere o login válido como "kezia" e a senha como "123".
'''
login = input('Digite o Login: ').lower()
while login != 'kezia':
    login = input('Login inválido, digite um login válido: ').lower()

senha = input('Digite sua senha: ')
while senha != '123':
    senha = input('Senha inválida, digite sua senha novamente: ')