# Menu para deletar bens

from Banco_Dados import bens_patrimoniais as bd

def Baixar_Bens():
    from main import menu

    print("\n=== Sistema de Baixa de Bens Patrimoniais ===")
    print("\nLista de bens disponíveis:\n")

    # Exibe todos os bens cadastrados
    for chave, bem in bd.items():
        print(f"Chave: {chave} | Nome: {bem['nome']} | Localização: {bem['localizacao']}")

    chave_baixa = input("\nDigite a chave do bem que deseja dar baixa:\n")

    if chave_baixa in bd:
        confirmacao = input(f"\nTem certeza que deseja excluir o bem '{chave_baixa}'? (s/n): ").lower()
        if confirmacao == 's':
            del bd[chave_baixa]
            print(f"\nBem '{chave_baixa}' removido com sucesso!")
        else:
            print("\nOperação cancelada.")
    else:
        print("\nChave não encontrada. Verifique e tente novamente.")

    while True:
        print("\nDeseja realizar outra operação?\n"
              "1 - Baixar outro bem\n"
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
                Baixar_Bens()
            case 2:
                menu()
            case 3:
                print("\nEncerrando o Sistema de Bens Patrimoniais. Até mais!\n")
                exit()







    return