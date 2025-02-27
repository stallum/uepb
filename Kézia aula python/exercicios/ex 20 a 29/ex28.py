# 28.	Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('Em que turno você estuda?')
horario = input('Digite: \n M para Matutino\n V para Vespertino \n N para Noturno\n ').upper()
if horario == 'M':
    print('M - Matutino')
else:
    if horario == 'V':
        print('V - Vespertino')
    else:
        if horario == 'N':
            print('N - Noturno')
        else:
            print('Valor Inválido')