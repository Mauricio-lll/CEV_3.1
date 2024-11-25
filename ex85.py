# crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# No final mostre os valores pares e impares em ordem crescente
numeros = []
pares = []
impares = []

for i in range(7):
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()

print("Todos os números:", numeros)
print("Números pares em ordem crescente:", pares)
print("Números ímpares em ordem crescente:", impares)