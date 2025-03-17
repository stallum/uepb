# Uma grande firma deseja saber qual é o empregado mais recente e qual é o mais antigo. Desenvolver um programa para ler um número indeterminado de informações contendo o número do empregado e o número de meses de trabalho deste empregado e imprimir o mais recente e o mais antigo. Obs.: A última informação contém os dois números iguais a zero. Não existem dois empregados admitidos no mesmo mês.

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