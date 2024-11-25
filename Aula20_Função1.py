# () Tupla - [] Lista - {} Dicionário
'''def mostralinha():
    print('-'*30)
mostralinha()
print('CURSO EM VIDEO')
mostralinha()
'''
'''def mensagem(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
mensagem('SISTEMA DE ALUNOS')'''
'''def soma(a,b):
    s = a + b
    print(s)
soma(5, 12)'''
'''def contador(*num):
    #for valor in num:
     #   print(f'{valor} ', end='')
    #print('FIM')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')
contador(2,1,7)
contador(8,0)'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)