# Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. no final mostre:
# A- Quantas pessoas foram cadastradas;
# b- Uma listagem com as pessoas mais pesadas;
# c- Uma listagem com as pessoas mais leves;
pessoas = []
dados = []

while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input('Peso: '))
    dados.append([nome, peso])
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print('=' * 30)
print('As pessoas mais pesadas são:')
maior = 0
for p in pessoas:
    if p[0][1] > maior:
        maior = p[0][1]
for p in pessoas:
    if p[0][1] == maior:
        print(f'\t{p[0][0]} com {p[0][1]}Kg')
print('=' * 30)
print('As pessoas mais leves são:')
menor = pessoas[0][0][1]
for p in pessoas:
    if p[0][1] < menor:
        menor = p[0][1]
for p in pessoas:
    if p[0][1] == menor:
        print(f'\t{p[0][0]} com {p[0][1]}Kg')