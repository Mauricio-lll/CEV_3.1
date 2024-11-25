# Aprimore o desafio 93 para que ele funcione com varios jogares, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
time = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    for i in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (123 para parar) '))
    if busca == 123:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)