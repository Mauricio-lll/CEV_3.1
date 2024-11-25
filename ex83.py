# Crie um programa onde o usuário digitre uma expressão qualquer que use parenteses.
# O aplicativo deverá analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta
def validar_parenteses(expressao):
  """Valida se os parênteses em uma expressão estão balanceados.

  Args:
    expressao: A expressão a ser verificada.

  Returns:
    True se a expressão estiver válida, False caso contrário.
  """

  pilha = []
  for caractere in expressao:
    if caractere == '(':
      pilha.append(caractere)
    elif caractere == ')':
      if not pilha:
        return False
      pilha.pop()

  return not   pilha

# Exemplo de uso:
expressao = input("Digite a expressão: ")
if validar_parenteses(expressao):
  print("A expressão está válida.")
else:
  print("A expressão está inválida.")