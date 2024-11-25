# Faça um programa que tenha uma função notas() que pode receber varias notas de alnos e vai retornar um dicionario com as seguintes informações:
# - Quantidade de notas;
# - Maior nota;
# - Menor nota;
# - Média da turma;
# - A situação (opcional)
# Adicione também as docstrings da função
def notas(*n, sit=False):
  """
  Função para analisar notas e retornar um dicionário com várias informações.

  Args:
    *n (int): Uma ou mais notas dos alunos.
    sit (bool, optional): Indica se deve ou não calcular a situação da turma. Defaults to False.

  Returns:
    dict: Um dicionário com as seguintes informações:
      - quantidade: Quantidade de notas.
      - maior: Maior nota.
      - menor: Menor nota.
      - média: Média das notas.
      - situação: Situação da turma (opcional).
  """

  dados = dict()
  dados['quantidade'] = len(n)
  dados['maior'] = max(n)
  dados['menor'] = min(n)
  dados['média'] = sum(n) / len(n)
  if sit:
    if dados['média'] >= 7:
      dados['situação'] = 'BOA'
    elif dados['média'] >= 5:
      dados['situação'] = 'RAZOÁVEL'
    else:
      dados['situário'] = 'RUIM'
  return dados

# Exemplo de uso:
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
