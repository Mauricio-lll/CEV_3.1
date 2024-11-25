# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade e um arquivo de texto simples.
# O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas;
from modulo_pessoa import Pessoa

def cadastrar_pessoa(nome, idade, arquivo):
    with open(arquivo, 'a') as arquivo:
        pessoa = Pessoa(nome, idade)
        arquivo.write(str(pessoa) + '\n')
        print(f"Pessoa {nome} cadastrada com sucesso!")

def listar_pessoas(arquivo):
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(', ')  # Separa nome e idade
            pessoa = Pessoa(nome, int(idade))
            print(pessoa)

def menu():
    arquivo = 'pessoas.txt'  # Nome do arquivo para salvar as pessoas
    while True:
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas cadastradas")
        print("3 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            cadastrar_pessoa(nome, idade, arquivo)
        elif opcao == '2':
            listar_pessoas(arquivo)
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()