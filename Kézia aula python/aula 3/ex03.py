contMasc = contFemi = 0
n = 10
for i in range(n):
    FeminiMasculino = input('Digite F para Feminino e M para Masculino: ').upper()
    if FeminiMasculino == 'F':
        contFemi += 1
    else:
        if FeminiMasculino == 'M':
            contMasc += 1
        else:
            print('Sexo Inválido')

print(f'As pessoas de sexo masculino: {contMasc} \n As pessoas do sexo feminino são: {contFemi}')