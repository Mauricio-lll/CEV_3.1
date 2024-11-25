# Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: nome do jogador e quantos gols marcou;
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
def ficha(nome='<desconhecido>', gols=0):
  """Cria uma ficha de jogador.

  Args:
    nome (str, optional): Nome do jogador. Defaults to '<desconhecido>'.
    gols (int, optional): Número de gols marcados. Defaults to 0.
  """
  print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# Exemplos de uso:
ficha(nome='Diego')
ficha(gols=10)
ficha(nome='Ronaldo', gols=91)
ficha()