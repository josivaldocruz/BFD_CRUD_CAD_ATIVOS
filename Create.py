# Menu para criação de bens
# from Read import Consultar_Bens
# from Update import Atualizar_Bens
# from Delete import Baixar_Bens
from Banco_Dados import bens_patrimoniais as bd


def Cadastrar_Bens():

    print("\nBem-vindo ao Sitema de Cadastro de bens\n")

    cadastro = {}

    print("\nDigite os dados para cadastro\n")

    id = 1
    nome = input("\nEscreva o Nome Bem:\n")
    tipo = input("\nEscreva o Tipo do Bem:\n")
    valor = float(input("\nEscreva o Valor do Bem:\n"))
    data_aquisicao = int(input("\nEscreva a Data de Aquisição do Bem:\n"))
    localizacao = input("\nEscreva a Localização Bem:\n")
    condicao = input("\nEscreva a Condição do Bem:\n")


s = bd.values()

print(s)

# for chave, valor in bd.items():
#      print(f"{valor["id"]} - {chave}: {valor["nome"]}")
