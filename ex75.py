#Desenvolva um programa que leia quarto valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9;
# B) Em que posição foi digitado o valor 3;
# C) Quais foram os números pares;

numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')))

print(f'Você digitou os valores: {numeros}')

# A) Quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

# B) Em que posição foi digitado o valor 3
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

# C) Quais foram os números pares
print('Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')