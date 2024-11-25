# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lista = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: '))
    lista.append(numero)

# Encontrando o maior valor e sua posição
maior = max(lista)
posicao_maior = lista.index(maior)

# Encontrando o menor valor e sua posição
menor = min(lista)
posicao_menor = lista.index(menor)

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} na posição {posicao_maior}')
print(f'O menor valor digitado foi {menor} na posição {posicao_menor}')
