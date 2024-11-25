# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final, mostre o boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente
alunos = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno = [nome, [nota1, nota2], media]
    alunos.append(aluno)

    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('-=' * 30)
print('BOLETIM')
print('-=' * 30)

for i, a in enumerate(alunos):
    print(f'{i+1:<4} {a[0]:<10} {a[2]:>8.1f}')

while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno? (123 para parar): '))
    if mostrar_notas == 123:
        break
    if mostrar_notas < 1 or mostrar_notas > len(alunos):
        print('Aluno não encontrado.')
    else:
        aluno = alunos[mostrar_notas - 1]
        print(f'Notas de {aluno[0]}: {aluno[1]}')