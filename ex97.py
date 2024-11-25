#Faça um programa que tenha uma função chamada escreva() que recebe um texto qualquer como parametro e mostre uma mesagem com tamanha adaptavel
def escreva(msg):
    """
    Escreve uma mensagem em uma caixa de caracteres.

    Args:
        msg (str): A mensagem a ser exibida.
    """

    tamanho = len(msg)
    print('~' * (tamanho + 4))
    print(f'  {msg}  ')
    print('~' * (tamanho + 4))

# Exemplos de uso:
escreva('Olá, Mundo!')
