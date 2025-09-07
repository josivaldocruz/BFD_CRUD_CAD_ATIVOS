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
        "4 - Voltar")

        try:
            operacao = int(input("\nEscolha uma opção do menu de 1 à 4:\n"))
        except (NameError, ValueError):
            continue

        if operacao == 4:
            pass
        if operacao not in [1, 2, 3, 4]:
            print("\nSó é permitido a escolha de uma das opção do menu de 1 à 4:")
            continue

        match operacao:
              case 1:
                resultado = Cadastrar_Bens()
              case 2:
                resultado = Atualizar_Bens()
              case 3:
                resultado = Baixar_Bens()

        return
