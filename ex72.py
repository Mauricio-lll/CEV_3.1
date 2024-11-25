#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por externso, de zero até vinte.
# Seu programa devera ler o primeiro número pelo teclado (entre 0 e 20) e mostrar por extenso
numeros_por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
                       "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero = int(input("Digite um número entre 0 e 20: "))

if 0 <= numero <= 20:
    print(f"O número {numero} por extenso é: {numeros_por_extenso[numero]}")
else:
    print("Número inválido. Digite um número entre 0 e 20.")