# crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
# Mostre:
# a- Quantas pessoas foram cadastradas;
# b- A media de idade do grupo;
# c- Uma lista com todas as mulheres;
# d- Uma lista com todas as pessoas com idade acima da média
pessoas = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()[0]
        if sexo in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa.copy())

    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')

soma_idade = 0
for p in pessoas:
    soma_idade += p['idade']
media_idade = soma_idade / len(pessoas)
print(f'A média de idade é de {media_idade:.2f} anos.')

print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=', ')
print()

print('As pessoas com idade acima da média são: ')
for p in pessoas:
    if p['idade'] > media_idade:
        print(f'{p["nome"]} ({p["idade"]} anos)')