contatos = []

while True:
    print("\nAgenda de Contatos")
    print("1 - Adicionar contato")
    print("2 - Ver contatos")
    print("3 - Editar contato")
    print("4 - Favoritar contato")
    print("5 - Deletar contato")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")

        contato = {
            "nome": nome,
            "telefone": telefone,
            "favorito": False
        }

        contatos.append(contato)
        print("Contato adicionado!")

    elif opcao == "2":
        print("\nLista de contatos:")
        for i, contato in enumerate(contatos):
            fav = "⭐" if contato["favorito"] else ""
            print(f"{i} - {contato['nome']} ({contato['telefone']}) {fav}")

    elif opcao == "3":
        indice = int(input("Digite o índice do contato para editar: "))
        if 0 <= indice < len(contatos):
            novo_nome = input("Novo nome: ")
            novo_tel = input("Novo telefone: ")
            contatos[indice]["nome"] = novo_nome
            contatos[indice]["telefone"] = novo_tel
            print("Contato atualizado!")

    elif opcao == "4":
        indice = int(input("Digite o índice do contato para favoritar: "))
        if 0 <= indice < len(contatos):
            contatos[indice]["favorito"] = True
            print("Contato marcado como favorito!")

    elif opcao == "5":
        indice = int(input("Digite o índice do contato para deletar: "))
        if 0 <= indice < len(contatos):
            contatos.pop(indice)
            print("Contato deletado!")

    elif opcao == "0":
        print("Encerrando agenda...")
        break

    else:
        print("Opção inválida!")
