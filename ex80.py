# Crie um programa onde o usuario possa digitar cinco valores numericos e cadastr-os em uma lista, já na posição correta de inserção. SEM USAR O SORT.
# No final, mostre a lista ordenada na tela
lista = []

for i in range(5):
    num = int(input("Digite um número: "))
    # Encontrar a posição correta para inserir o número
    pos = 0
    while pos < len(lista) and lista[pos] < num:
        pos += 1
    # Inserir o número na posição correta
    lista.insert(pos, num)

print("Lista ordenada:", lista)