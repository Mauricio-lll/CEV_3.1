# Aprimore o desafio anterior, mostrando no final:
# a- A soma de todos os valores pares digitados;
# b- A soma dos valores da terceira coluna;
# c- O maior valor da segunda linha:
matriz = []
soma_pares = 0
soma_terceira_coluna = 0

# Lendo os valores para a matriz
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}, {j}]: "))
        linha.append(valor)
        if valor % 2 == 0:
            soma_pares += valor
        if j == 2:
            soma_terceira_coluna += valor
    matriz.append(linha)

# Imprimindo a matriz formatada
print("Matriz:")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:^5}", end="")
    print()

# Encontrando o maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

print(f"A soma dos valores pares é: {soma_pares}")
print(f"A soma dos valores da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {maior_segunda_linha}")