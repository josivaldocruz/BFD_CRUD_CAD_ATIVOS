from Create import Cadastrar_Bens
from Read import Consultar_Bens
from Update import Atualizar_Bens
from Delete import Baixar_Bens


print("Bem-vindo ao Sistema de Bens Patrimoniais")
while True:
    print("\nQuais Operações deseja realizar no sistema:\n" \
    "1 - Cadastrar Bens\n"
    "2 - Consultar Bens\n"
    "3 - Atualizar Bens\n"
    "4 - Baixar Bens\n"
    "5 - sair")
    operacao = int(input("\nEscolha uma opção do menu de 1 à 5:\n"))

    if operacao == 5:
        print("\nEncerrando o Sistema de Bens Patrimoniais. Até mais!\n")
        break
    if operacao not in [1, 2, 3, 4]:
        print("Por favor, Escolha uma opção do menu de 1 5:")
        continue

    match operacao:
        case 1:
            resultado = Cadastrar_Bens()
        case 2:
            resultado = Consultar_Bens()
        case 3:
            resultado = Atualizar_Bens()
        case 4:
            resultado = Baixar_Bens()