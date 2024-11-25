from logging import exception

try:
    a = int(input('Numerado: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Tivemos um problema. O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')