# Crie um programa que tenha uma tupla com varias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
palavras = ('TETO', 'PATRULHA', 'PEDIATRA', 'ANELAR', 'GAFANHOTO')
vogais = 'AEIOU'

for palavra in palavras:
    print(f'Palavra: {palavra}')
    print('Vogais:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print()