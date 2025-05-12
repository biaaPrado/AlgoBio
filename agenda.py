# Agenda em Python

agenda = []

while True:
    print("\n--- MENU DA AGENDA ---")
    print("1 - Adicionar contato")
    print("2 - Mostrar todos os contatos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    
    if opcao == '1':
        
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")

        contato = {
            "Nome": nome,
            "Telefone": telefone,
            "CPF": cpf,
            "Endereço": endereco
        }

        agenda.append(contato)
        print("Contato adicionado com sucesso!")

    elif opcao == '2':
        if not agenda:
            print("Nenhum contato na agenda.")
        else:
            print("\n--- Contatos da Agenda ---")
            for i, contato in enumerate(agenda, 1):
                print(f"\nContato {i}:")
                print(f"Nome: {contato['Nome']}")
                print(f"Telefone: {contato['Telefone']}")
                print(f"CPF: {contato['CPF']}")
                print(f"Endereço: {contato['Endereço']}")
                
    elif opcao == '3':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
