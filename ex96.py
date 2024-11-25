#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangula (largura e comprimento)
# Mostre a área do terreno
def area(largura, comprimento):
  """
  Calcula a área de um terreno retangular.

  Args:
    largura: A largura do terreno em metros.
    comprimento: O comprimento do terreno em metros.

  Returns:
    A área do terreno em metros quadrados.
  """

  area = largura * comprimento
  print(f'A área do terreno é de {area}m².')

# Exemplo de uso da função
largura_terreno = float(input('Digite a largura do terreno em metros: '))
comprimento_terreno = float(input('Digite o comprimento do terreno em metros: '))

area(largura_terreno, comprimento_terreno)