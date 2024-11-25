''''# () Tupla - [] Lista - {} Dicionário
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

#Usando Range:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

#Usando direto:
for comida in lanche:
   print(f'Eu vou comer {comida}')

#Usando Enumerate
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Usando sorted: para ordenar
print(sorted(lanche))

print('Comi pra caramba!')'''
# EXEMPLO 2
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #A ordem aqui afeta por tuplas serem estruturas compostas
print(c)
print(c.index(8)) #Mostra a posição do número que escolhe

