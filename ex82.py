# Crie um progama que vai ler varios numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteudo das tres listas geradas
numeros = []
pares = []
impares = []

while True:
    num = int(input("Digite um número (ou 0 para parar): "))
    if num == 0:
        break
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista de todos os números:", numeros)
print("Lista de números pares:", pares)
print("Lista de números ímpares:", impares)