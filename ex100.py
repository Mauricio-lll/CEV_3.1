# Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 numeros e vai colocalos dentro da lista.
# A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
from random import randint

def sorteia(lista):
    """Sorteia 5 números e adiciona à lista.

    Args:
        lista: A lista onde os números serão armazenados.
    """
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('PRONTO!')

def somaPar(lista):
    """Calcula a soma dos valores pares em uma lista.

    Args:
        lista: A lista de números.

    Returns:
        A soma dos números pares.
    """
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

# Programa principal
numeros = []
sorteia(numeros)
somaPar(numeros)