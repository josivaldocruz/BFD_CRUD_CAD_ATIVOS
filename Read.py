# Menu de consulta de bens
from Banco_Dados import bens_patrimoniais as bd


def Consultar_Bens():
    from main import menu

    print("\nSegue o inventário dos bens:\n")

    for chave, valor in bd.items():
        print(f"{valor["id"]} - {chave}: {valor["nome"]}")


    
    while True:
        print("\nQuais Operações deseja realizar no sistema:\n" \
        "1 - Visualizar Bens Detalhados\n"
        "2 - Voltar ao Menu\n"
        "3 - Sair do sistema\n")

        try:
            operacao = int(input("\nEscolha uma opção do menu de 1 à 3:\n"))
        except (NameError, ValueError):
            continue

        if operacao not in [1, 2, 3]:
            print("\nSó é permitido a escolha de uma das opção do menu de 1 à 3:")
            continue

        match operacao:
            case 1:
                print("\n=== Detalhes dos Bens ===\n")
                for chave, valor in bd.items():
                    print(f"Chave: {chave}\n"
                          f"ID: {valor['id']}\n"
                          f"Nome: {valor['nome']}\n"
                          f"Tipo: {valor['tipo']}\n"
                          f"Valor: {valor['valor']}\n"
                          f"Data de Aquisição: {valor['data_aquisicao']}\n"
                          f"Localização: {valor['localizacao']}\n"
                          f"Condição: {valor['condicao']}\n"
                          "-----------------------------")
            case 2:
                menu()
            case 3:
                print("\nEncerrando o Sistema de Bens Patrimoniais. Até mais!\n")
                exit()
                


    return
