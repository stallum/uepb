'''
Você foi contratado para escrever um algoritmo que calcule quantos pontos fez um time num campeonato de futebol. Para os que não conhecem futebol uma vitória vale três pontos, um empate vale 1 ponto e a derrota não vale ponto. A entrada será composta por pares de números indicando o resultado de cada jogo. O primeiro número sempre corresponde ao total de gols que o time fez no jogo. A leitura dos dados será finalizada quando for fornecido um número de gols negativo.
'''
pontos = 0
gols_time = 0
gols_adversario = 0
calculo_campeonato = 0

while calculo_campeonato == 0:
    gols_time = input('Digite quantos gols o time fez (Ou um número negativo para sair do programa): ')
    
    if int(gols_time) < 0:
        calculo_campeonato += 1

    else: 
        while gols_time.isalpha():
            gols_time = input('A quantidade fornecida é invalida, digite um número de gols válido: ')
        gols_time = int(gols_time)

        gols_adversario = input('Digite a quantidade de gols do adversário: ')
        while gols_adversario.isalpha():
            gols_adversario = input('A quantidade fornecida é invalida, digite um número de gols válido: ')
        gols_adversario = int(gols_adversario)

        if gols_time > gols_adversario:
            pontos += 3
        else: 
            if gols_time == gols_adversario:
                pontos += 1

print(f'O time fez um total de {pontos} pontos no campeonato.')