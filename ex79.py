# Crie um programa onde o usuário possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o número ja exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores unicos digitados, em ordem crescente
numeros = []

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    if numero not in numeros:
        numeros.append(numero)

# Ordenando a lista
numeros.sort()

print("Números únicos digitados em ordem crescente:")
print(numeros)