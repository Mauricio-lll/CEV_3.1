# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado.
# No final, mostre a matriz na tela com a formatação completa e correta
matriz = []

# Lendo os valores para a matriz
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}, {j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Imprimindo a matriz formatada
for linha in matriz:
    for elemento in linha:
        print(f"[{elemento:^4}]", end="")
    print()