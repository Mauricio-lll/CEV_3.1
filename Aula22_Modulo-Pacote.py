from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O Dobro é {numeros.dobro(num)} e o triplo é {numeros.triplo(num)}')
