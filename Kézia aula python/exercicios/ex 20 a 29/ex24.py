# Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

FeminiMasculino = input('Digite F para Feminino e M para Masculino: ').upper()
if FeminiMasculino == 'F':
    print('F - Feminino')
else:
    if FeminiMasculino == 'M':
        print('M - Masculino')
    else:
        print('Sexo Inválido')
