# Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados;
# b) A lista de valores, ordenada de forma decrescente;
# c) Se o valor 5 foi digitado e esta ou não na lista
numeros = []

while True:
    num = int(input("Digite um número (ou 0 para parar): "))
    if num == 0:
        break
    numeros.append(num)

# a) Quantidade de números digitados
quantidade_numeros = len(numeros)
print(f"Você digitou {quantidade_numeros} números.")

# b) Lista ordenada de forma decrescente
numeros.sort(reverse=True)
print("Lista ordenada de forma decrescente:", numeros)

# c) Verificar se o número 5 está na lista
if 5 in numeros:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")