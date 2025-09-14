# Menu para editar de bens
from Banco_Dados import bens_patrimoniais as bd


def Atualizar_Bens():
    from main import menu

    print("\n=== Sistema de Atualização de Bens Patrimoniais ===")
    print("\nLista de bens disponíveis:\n")

    for chave, bem in bd.items():
        print(f"Chave: {chave} | Nome: {bem['nome']} | ID: {bem['id']}")

    chave_edicao = input("\nDigite a chave do bem que deseja atualizar:\n")

    if chave_edicao in bd:
        bem = bd[chave_edicao]
        print(f"\nBem selecionado: {chave_edicao}")
        print(f"Nome atual: {bem['nome']}")
        print(f"Tipo atual: {bem['tipo']}")
        print(f"Valor atual: {bem['valor']}")
        print(f"Data de aquisição atual: {bem['data_aquisicao']}")
        print(f"Localização atual: {bem['localizacao']}")
        print(f"Condição atual: {bem['condicao']}")

        print("\nDigite os novos dados (pressione Enter para manter o valor atual):")

        novo_nome = input("Novo nome: ") or bem["nome"]
        novo_tipo = input("Novo tipo: ") or bem["tipo"]

        while True:
            try:
                novo_valor = input("Novo valor: ")
                novo_valor = float(novo_valor) if novo_valor else bem["valor"]
                break
            except ValueError:
                print("Valor inválido. Digite um número.")

        nova_data = input("Nova data de aquisição: ") or bem["data_aquisicao"]
        nova_localizacao = input("Nova localização: ") or bem["localizacao"]
        nova_condicao = input("Nova condição: ") or bem["condicao"]

        bd[chave_edicao] = {
            "id": bem["id"],
            "nome": novo_nome,
            "tipo": novo_tipo,
            "valor": novo_valor,
            "data_aquisicao": nova_data,
            "localizacao": nova_localizacao,
            "condicao": nova_condicao
        }

        print(f"\nBem '{chave_edicao}' atualizado com sucesso!")

    else:
        print("\nChave não encontrada. Verifique e tente novamente.")

    while True:
        print("\nDeseja realizar outra operação?\n"
              "1 - Atualizar outro bem\n"
              "2 - Voltar ao Menu\n"
              "3 - Sair do sistema\n")

        try:
            operacao = int(input("\nEscolha uma opção de 1 à 3:\n"))
        except ValueError:
            continue

        if operacao not in [1, 2, 3]:
            print("\nEscolha inválida. Tente novamente.")
            continue

        match operacao:
            case 1:
                Atualizar_Bens()
            case 2:
                menu()
            case 3:
                print("\nEncerrando o Sistema de Bens Patrimoniais. Até mais!\n")
                exit()



    return