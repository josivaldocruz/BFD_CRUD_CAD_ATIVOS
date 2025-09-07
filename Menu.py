
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
        print("Por favor, Escolha uma opção do menu de 1 à 5:")
        continue

    match operacao:
        case 1:
            resultado = somar(a, b)
        case 2:
            resultado = subtrair(a, b)
        case 3:
            resultado = multiplicar(a, b)
        case 4:
            resultado = dividir(a, b)