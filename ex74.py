# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menos e o maior valor que estão na tupla
import random

# Gera 5 números aleatórios entre 1 e 100 e coloca em uma tupla
numeros = tuple(random.randint(1, 100) for _ in range(5))

# Imprime a tupla
print("Números gerados:", numeros)

# Encontra o menor e o maior valor
menor_valor = min(numeros)
maior_valor = max(numeros)

# Imprime o menor e o maior valor
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)