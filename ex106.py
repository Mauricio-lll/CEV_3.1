# Faça um mini-sistema que utilize o interactive Help do Python.
# O Usuario vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar "FIM" o programa irá encerrar.
# Usar cores
def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg)
    print('\033[m~' * tam)
    print(f'\033[{cor}m  {msg:^>{tam}}  \033[m')
    print('~' * tam)

# Cores (Você pode personalizar)
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[1;47m'}

comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 2)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    titulo(f'Acessando o manual do comando {comando}', 1)
    ajuda(comando)
    print('\033[m')