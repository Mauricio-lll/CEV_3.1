# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
# Guarde esses resultados em um dicionario.
# No final, coloque esse dicionario em order, sabendo que o vencedor tirou o maior numero no dado
import random

jogadores = {}

for i in range(1, 5):
    nome = input(f"Digite o nome do jogador {i}: ")
    dado = random.randint(1, 6)
    jogadores[nome] = dado

print("\nResultados:")
for jogador, valor in sorted(jogadores.items(), key=lambda item: item[1], reverse=True):
    print(f"{jogador}: {valor}")

vencedor = max(jogadores, key=jogadores.get)
print(f"\nO vencedor é {vencedor} com {jogadores[vencedor]} pontos!")