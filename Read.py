# Menu de consulta de bens
from Create import Cadastrar_Bens
from Update import Atualizar_Bens
from Delete import Baixar_Bens
from Banco_Dados import bens_patrimoniais as bd


def Consultar_Bens():
    print("\nSegue o inventário dos bens:\n")

    for chave, valor in bd.items():
        print(f"{valor["id"]} - {chave}: {valor["nome"]}")


    
    while True:
        print("\nQuais Operações deseja realizar no sistema:\n" \
        "1 - Cadastrar Bens\n"
        "2 - Atualizar Bens\n"
        "3 - Baixar Bens\n"
        "4 - Visualizar Bens Detalhados\n"
        "5 - Voltar ao Menu Principal\n")

        try:
            operacao = int(input("\nEscolha uma opção do menu de 1 à 5:\n"))
        except (NameError, ValueError):
            continue

        if operacao == 5:
            break
        if operacao not in [1, 2, 3, 4, 5]:
            print("\nSó é permitido a escolha de uma das opção do menu de 1 à 5:")
            continue

        match operacao:
            case 1:
                resultado = Cadastrar_Bens()
            case 2:
                resultado = Atualizar_Bens()
            case 3:
                resultado = Baixar_Bens()
            case 4:
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

        return
