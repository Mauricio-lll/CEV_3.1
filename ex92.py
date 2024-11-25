# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-se (com idade) em um dicionario.
# Se por acaso a CTPS for diferente de zero, o dicionario receberá também o ano de contratação e salario.
# Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar
from datetime import date

funcionarios = {}

while True:
    nome = str(input('Nome: '))
    ano_nascimento = int(input('Ano de nascimento: '))
    ctps = int(input('Carteira de Trabalho (0 não tem): '))

    idade = date.today().year - ano_nascimento
    dados = {'idade': idade}

    if ctps != 0:
        ano_contratacao = int(input('Ano de contratação: '))
        salario = float(input('Salário: R$ '))
        dados.update({'ctps': ctps, 'contratacao': ano_contratacao, 'salario': salario})
        if idade >= 35 and ano_contratacao >= 20:
            aposentadoria = idade + (35 - idade) + 20 - ano_contratacao
            dados['aposentadoria'] = aposentadoria

    funcionarios[nome] = dados

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print('    REGISTRO DE FUNCIONÁRIOS    ')
print('-=' * 30)

for pessoa, informacoes in funcionarios.items():
    print(f'NOME: {pessoa}')
    for k, v in informacoes.items():
        print(f'  - {k} tem o valor {v}')
    print('-=' * 20)