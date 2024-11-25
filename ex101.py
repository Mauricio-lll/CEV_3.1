# Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
#Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições
def voto(ano):
  """Verifica a situação eleitoral de uma pessoa com base no ano de nascimento.

  Args:
      ano (int): Ano de nascimento da pessoa.

  Returns:
      str: Retorna 'NEGADO', 'OPCIONAL' ou 'OBRIGATÓRIO' de acordo com a idade.
  """

  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade < 16:
    return 'NEGADO'
  elif 16 <= idade < 18 or idade > 70:
    return 'OPCIONAL'
  else:
    return 'OBRIGATÓRIO'

# Exemplo de uso:
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))