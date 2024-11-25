# Crie um programa que tenha uma função leiaint(), que vai funcionar de forma semelhante a função input() do Python. Só que fazendo a validação para aceitar apenas numeros
def leiaInt(msg):
  """Lê um número inteiro do usuário com validação.

  Args:
    msg (str): A mensagem a ser exibida para o usuário.

  Returns:
    int: O número inteiro digitado pelo usuário.
  """

  while True:
    try:
      n = int(input(msg))
    except ValueError:
      print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    else:
      return n

# Exemplo de uso:
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')