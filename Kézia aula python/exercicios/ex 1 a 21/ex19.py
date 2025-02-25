# faça um programa que calcula o tempo para passar um arquivo com o tamanho do arquivo e a velocidade da internet
# formula: v = arq * t (v * arq = t)

arq = float(input('Digite aqui o tamanho do arquivo que você quer transferir (Apenas números em KBs): '))
velocidade = float(input('Digite aqui a velocidade da sua internet (Apenas números KB/s )'))
tempo = (arq / velocidade) / 60

print(f'Os arquivos serão enviados em: {tempo} minutos')