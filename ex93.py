# crie um programa para gerenciar o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
jogador = {}
partidas = []

nome = str(input('Nome do jogador: '))
tot_partidas = int(input(f'Quantas partidas {nome} jogou? '))

for p in range(0, tot_partidas):
    gols = int(input(f'Quantos gols na partida {p+1}? '))
    partidas.append(gols)

jogador['nome'] = nome
jogador['gols'] = partidas
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {tot_partidas} partidas.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-=' * 30)