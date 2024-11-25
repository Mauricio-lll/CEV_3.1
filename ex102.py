# Crie um programa que tenha uma função fatorial() que receba dois parametros:
# O primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico(opcional) indicando se será mostrado ou não na tela o processo de calculo fatoria
def fatorial(num, show=False):
  """Calcula o fatorial de um número e opcionalmente mostra o processo.

  Args:
    num (int): O número para calcular o fatorial.
    show (bool, optional): Se True, mostra o processo de cálculo. Defaults to False.
  """

  f = 1
  for c in range(num, 0, -1):
    if show:
      print(c, end='')
      if c > 1:
        print(' x ', end='')
      else:
        print(' = ', end='')
    f *= c
  return f

# Exemplo de uso:
num = int(input('Digite um número: '))
show = str(input('Mostrar o cálculo? (S/N) ')).upper()
print(fatorial(num, show == 'S'))