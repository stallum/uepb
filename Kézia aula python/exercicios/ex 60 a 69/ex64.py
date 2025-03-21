# Uma grande firma deseja saber qual é o empregado mais recente e qual é o mais antigo. Desenvolver um programa para ler um número indeterminado de informações contendo o número do empregado e o número de meses de trabalho deste empregado e imprimir o mais recente e o mais antigo. Obs.: A última informação contém os dois números iguais a zero. Não existem dois empregados admitidos no mesmo mês.

mais_recente_id = None
mais_antigo_id = None
mais_recente_meses = None
mais_antigo_meses = None
continuar_prog = 0

while continuar_prog == 0:
    print('Para finalizar o programa coloque id = 0 e meses de trabalho = 0')
    id_empregado = input('Digite o ID do empregado: ')
    while id_empregado.isalpha() or int(id_empregado) < 0:
        id_empregado = input('Id Inválido, Digite um Id válido: ')
    id_empregado = int(id_empregado)

    meses_trabalho = input('Digite a quantos meses esse empregado trabalha: ')
    while meses_trabalho.isalpha() or int(meses_trabalho) < 0:
        meses_trabalho = input('Quantidade de Meses inválidas, digite uma quantidade de meses válida: ')
    meses_trabalho = int(meses_trabalho)

    if mais_recente_id == None and mais_antigo_id == None:
        mais_recente_id = id_empregado
        mais_antigo_id = id_empregado
        mais_recente_meses = meses_trabalho
        mais_antigo_meses = meses_trabalho
    
    else: 
        if id_empregado == 0 and meses_trabalho == 0:
            continuar_prog += 1 
        else:
            if meses_trabalho == mais_recente_meses or meses_trabalho == mais_antigo_meses:
                print('Erro, nenhum trabalhador foi admitido no mesmo mês que outro.')
                while meses_trabalho == mais_recente_meses or meses_trabalho == mais_antigo_meses:
                    meses_trabalho = input('Digite a quantos meses que esse empregado trabalha: ')
                    while int(meses_trabalho) < 0 or meses_trabalho.isalpha():
                        meses_trabalho = input('Quantidade de Meses inválidas, digite uma quantidade de meses válida: ')
                    meses_trabalho = int(meses_trabalho)
            else:
                if id_empregado == mais_antigo_id or id_empregado == mais_recente_id:
                     print('Erro, nenhum trabalhador tem mesmo id que outro')
                while id_empregado == mais_recente_id or id_empregado == mais_antigo_id:
                    id_empregado = input('Digite a quantos meses que esse empregado trabalha: ')
                    while int(id_empregado) < 0 or id_empregado.isalpha():
                        id_empregado = input('Id inválid, digite um id válido (um id válido é um numero inteiro maior que 0): ')
                    id_empregado = int(id_empregado)
                else: 
                    if mais_recente_meses < meses_trabalho:
                        mais_recente_meses = meses_trabalho
                        mais_recente_id = id_empregado
                    else:
                        if mais_antigo_meses > meses_trabalho:
                            mais_antigo_meses = meses_trabalho
                            mais_antigo_id = id_empregado

if mais_recente_id is not None and mais_antigo_id is not None:
    print(f'Empregado mais recente: {mais_recente_id} com: {mais_recente_meses} meses de trabalho')
    print(f'Empregado mais antigo: {mais_antigo_id} com: {mais_antigo_meses} meses de trabalho')
else:
    print('Nenhum funcionário foi regristrado')



#


'''
funcionarios = []
continuar_prog = 0

while continuar_prog == 0:
    id_empregado = int(input("Id do empregado: "))
    meses_trabalho = int(input("Número de meses de trabalho: "))
    
    if id_empregado == 0 and meses_trabalho == 0:
        continuar_prog += 1
    
    funcionarios.append((id_empregado, meses_trabalho))

if funcionarios:
    mais_recente = min(funcionarios, key=lambda x: x[1])
    mais_antigo = max(funcionarios, key=lambda x: x[1])
    
    print(f"Empregado mais recente: {mais_recente[0]} com {mais_recente[1]} meses de trabalho")
    print(f"Empregado mais antigo: {mais_antigo[0]} com {mais_antigo[1]} meses de trabalho")
else:
    print("Nenhum funcionário foi registrado.")
'''