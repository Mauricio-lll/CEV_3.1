# Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()
# Faça um programa que importe esse modulo e use algumas dessas funções
from uteis import aula22

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é {aula22.metade(preco)}')
print(f'O dobro de {preco} é {aula22.dobro(preco)}')
print(f'Aumentando 10%, temos {aula22.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos {aula22.diminuir(preco, 13)}')