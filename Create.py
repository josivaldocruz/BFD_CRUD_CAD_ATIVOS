# Menu para criação de bens
# from Read import Consultar_Bens
# from Update import Atualizar_Bens
# from Delete import Baixar_Bens

from Banco_Dados import bens_patrimoniais as bd


def Cadastrar_Bens():
    from main import menu

    print("\nBem-vindo ao Sitema de Cadastro de bens")
    print("\nDigite os dados para cadastro\n")

    novoid = (list(bd.values())[-1]["id"]) + 1

    nome = input("\nEscreva o Nome Bem:\n")
    tipo = input("\nEscreva o Tipo do Bem:\n")

    while True:
        try:
            valor = float(input("\nEscreva o valor do Bem:\n"))  
        except ValueError:
            print("Valor inválido! digite o preço correto.")
            continue

        data_aquisicao = input("\nEscreva a data de aquisição do Bem (DD/MM/AAAA):\n")
        localizacao = input("\nEscreva a localização Bem:\n")
        condicao = input("\nEscreva a condição do Bem:\n")

        novo_ativo = {
            "id": novoid,
            "nome": nome,
            "tipo": tipo,
            "valor": valor,
            "data_aquisicao": data_aquisicao,
            "localizacao": localizacao,
            "condicao": condicao
        }

        nova_chave = f"{nome}_{novoid}"
        bd[nova_chave] = novo_ativo.copy()

        novo_cadastro_ok = list(bd.values())[-1]

        print(f"""\nCadastro realizado com sucesso\n
            Novo Ativo: {nova_chave}
            Nome: {novo_cadastro_ok["nome"]}
            Tipo: {novo_cadastro_ok["tipo"]       }
            Valor: {novo_cadastro_ok["valor"] }
            Data de Aquisição: {novo_cadastro_ok["data_aquisicao"] }
            Localização: {novo_cadastro_ok["localizacao"]}
            Condição: {novo_cadastro_ok ["condicao"]}""")

        while True:
            print("\nDeseja Realizar um novo cadastro?\n" \
                "1 - Sim\n"
                "2 - Voltar ao Menu\n"
                "3 - Sair do sistema\n")

            try:
                Valoroperacao = int(input("\nEscolha uma opção do menu de 1 à 3:\n"))
            except (NameError, ValueError):
                continue 

            if Valoroperacao not in [1, 2, 3]:
                print("\nSó é permitido a escolha de uma das opção do menu de 1 à 3:")
                continue

            match Valoroperacao:
                case 1: 
                    break  
                case 2: menu()
             
                case 3: 
                    print("\nEncerrando o Sistema de Bens Patrimoniais. Até mais!\n")
                    exit()

Cadastrar_Bens()