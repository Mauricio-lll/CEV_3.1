'''help(print)
print(input.__doc__)'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*= c
    return f
n = int(input('Digite um número: '))
print(f'O Fatorial de {n} é igual a {fatorial(n)}')