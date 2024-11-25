# Faça um progama que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo. Cadastrando em uma lista composta
import random

def gerar_jogos(quantidade_jogos):
    """Gera uma lista de jogos para a Mega Sena.

    Args:
        quantidade_jogos: O número de jogos a serem gerados.

    Returns:
        Uma lista de listas, onde cada lista interna representa um jogo com 6 números.
    """

    jogos = []
    for _ in range(quantidade_jogos):
        jogo = set()  # Usamos um conjunto para garantir números únicos
        while len(jogo) < 6:
            jogo.add(random.randint(1, 60))
        jogos.append(list(jogo))  # Convertemos o conjunto para lista
    return jogos

# Solicita a quantidade de jogos ao usuário
quantidade = int(input("Quantos jogos você quer gerar? "))

# Gera os jogos e os exibe
jogos_gerados = gerar_jogos(quantidade)
for i, jogo in enumerate(jogos_gerados):
    print(f"Jogo {i+1}: {jogo}")