# Faça um programa  que leia nome e media de um aluno, guardando tambem a situação em um dicionário.
# No final, mostre o conteudo da estrutura na tela
alunos = {}

while True:
    nome = str(input('Nome: '))
    media = float(input(f'Média de {nome}: '))

    if media >= 7:
        situacao = 'Aprovado(a)'
    else:
        situacao = 'Reprovado(a)'

    alunos[nome] = [media, situacao]

    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('-=' * 30)
print('BOLETIM')
print('-=' * 30)

for aluno, dados in alunos.items():
    print(f'{aluno:<10} {dados[0]:>8.1f} {dados[1]}')