# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

produtos = (
    ('Caderno', 7.99),
    ('Lápis', 1.50),
    ('Caneta', 2.30),
    ('Borracha', 0.50),
    ('Régua', 3.00)
)

# Imprimindo a lista de preços em formato tabular
print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)
for produto in produtos:
    print(f'{produto[0]:.<30} R$ {produto[1]:>7.2f}')
print('-' * 40)