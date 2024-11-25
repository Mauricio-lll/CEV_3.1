# Faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros.
# O programa tem que analitar todos os valores e dizer qual deles é o maior
def maior(* num):
  """
  Encontra o maior valor entre vários números.

  Args:
    *num: Uma tupla contendo os números a serem comparados.

  Returns:
    O maior valor encontrado.
  """

  maior = 0
  cont = 0
  print('Analisando os valores ', end='')
  for valor in num:
    print(f'{valor} ', end='')
    if cont == 0:
      maior = valor
    else:
      if valor > maior:
        maior = valor
    cont += 1
  print(f'Foram informados {cont} valores ao todo.')
  print(f'O maior valor informado foi {maior}')

# Exemplos de uso:
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)