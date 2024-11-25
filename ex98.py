# Faça um programa que tenha uma função chamada contador() que receba três parametros: inicio, fim e passo. E realize a contagem.
# Seu programa tem que realizr tres contagens atraves da função criada.
# a- De 1 até 10, de 1 em 1;
# b- De 10 até 0, de 2 em 2;
# c- Uma contagem personalizada
def contador(i, f, p):
    """
    Realiza uma contagem personalizada.

    Args:
        i (int): Valor inicial da contagem.
        f (int): Valor final da contagem.
        p (int): Passo da contagem.
    """

    print('=' * 20)
    if p < 0:
        while i >= f:
            print(f'{i}', end=' ')
            i += p
    else:
        while i <= f:
            print(f'{i}', end=' ')
            i += p
    print()

# Exemplos de uso:
contador(1, 10, 1)
contador(10, 0, -2)

# Contagem personalizada
inicio = int(input('Início: '))
fim = int(input('Fim:     '))
passo = int(input('Passo:   '))
contador(inicio, fim, passo)