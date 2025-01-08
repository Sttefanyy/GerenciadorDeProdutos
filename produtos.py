import json

lista_produtos = []
id_unico = 1

def salvar_dados():
    dados = {
        "id_unico": id_unico,
        "produtos": lista_produtos
    }
    with open("produtos.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("Dados salvos com sucesso!")


def carregar_dados():
    try:
        with open("produtos.json", "r") as arquivo:
            dados = json.load(arquivo)
            if isinstance(dados, dict):
                return dados["produtos"], dados["id_unico"]
            else:
                return [], 1
    except FileNotFoundError:
        return [], 1


def menu():
    global lista_produtos, id_unico
    lista_produtos, id_unico = carregar_dados()
    while True:
        print("\n--- Gerenciador de Inventário ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Buscar Produto")
        print("6. Salvar e Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            buscar_produto()
        elif opcao == "6":
            print()
            salvar_dados()
            print("Saindo do sistema. Até a próxima!")
            break
        else:
            print("Opção inválida.")


def adicionar_produto():
    global id_unico
    try:
        nome = input("\nDigite o nome do produto: ")
        if not nome:
            raise ValueError("Nome não pode estar vazio.")
        categoria = input("Digite a categoria do produto: ")
        if not categoria:
            raise ValueError("Categoria não pode estar vazio.")
        quantidade = int(input("Digite a quantidade do produto em estoque: "))
        if quantidade < 0:
            raise ValueError("Quantidade deve ser um valor positivo.")
        preco = float(input("Digite o preço do produto: "))
        if preco < 0:
            raise ValueError("Preço deve ser um valor positivo.")
        produto = {
            "id": id_unico,
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade,
            "preço": preco,
        }
        lista_produtos.append(produto)
        id_unico += 1
        print(f"Produto adicionado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def listar_produtos():
    print()

    if not lista_produtos:
        print("Não há produtos cadastrados")
        return
    for produto in lista_produtos:
        id = produto["id"]
        nome = produto["nome"]
        categoria = produto["categoria"]
        qtd = produto["quantidade"]
        preco = produto["preço"]

        print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")

    while True:
        print("\n--- Opções de filtragem ---")
        print("1. Filtrar por categoria")
        print("2. Ordenação por nome")
        print("3. Ordenação por quantidade")
        print("4. Ordenação por preço")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print()
            categoria = input("Digite a categoria que deseja ver: ")
            print()
            print(f"--- Lista de produtos da categoria {categoria} ---")
            for produto in lista_produtos:
                if categoria.lower() in produto["categoria"].lower():
                    id = produto["id"]
                    nome = produto["nome"]
                    categoria = produto["categoria"]
                    qtd = produto["quantidade"]
                    preco = produto["preço"]

                    print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")

        elif opcao == "2":
            print()
            print("Produtos ordenados por nome:")

            lista_ordenada = sorted(lista_produtos, key=lambda x: x['nome'])
            for produto in lista_ordenada:
                id = produto["id"]
                nome = produto["nome"]
                categoria = produto["categoria"]
                qtd = produto["quantidade"]
                preco = produto["preço"]

                print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")


        elif opcao == "3":
            print()
            print("Produtos ordenados por quantidade:")

            lista_ordenada = sorted(lista_produtos, key=lambda x: x['quantidade'])
            for produto in lista_ordenada:
                id = produto["id"]
                nome = produto["nome"]
                categoria = produto["categoria"]
                qtd = produto["quantidade"]
                preco = produto["preço"]

                print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")

        elif opcao == "4":
            print()
            print("Produtos ordenados por preço:")

            lista_ordenada = sorted(lista_produtos, key=lambda x: x['preço'])
            for produto in lista_ordenada:
                id = produto["id"]
                nome = produto["nome"]
                categoria = produto["categoria"]
                qtd = produto["quantidade"]
                preco = produto["preço"]

                print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")


        elif opcao == "5":
            break


        else:
            print("Opção inválida.")


def atualizar_produto():
    print()
    try:
        id_atualizar = int(input("Qual o id do produto que você deseja atualizar? "))
        for produto in lista_produtos:
            if id_atualizar == produto["id"]:
                id = produto["id"]
                nome = produto["nome"]
                categoria = produto["categoria"]
                qtd = produto["quantidade"]
                preco = produto["preço"]

                print(f"Produto atual: ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")
                print()
                print("O que você deseja atualizar deste produto?")
                while True:
                    print("1. Nome")
                    print("2. Quantidade")
                    print("3. Preço")
                    print("4. Categoria")
                    print("5. Voltar ao menu principal")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        print()
                        nome_atualizado = input("Digite o novo nome deste produto: ")
                        if not nome_atualizado:
                            raise ValueError("Nome não pode estar vazio.")
                        produto.update({"nome": nome_atualizado})

                        id = produto["id"]
                        nome = produto["nome"]
                        categoria = produto["categoria"]
                        qtd = produto["quantidade"]
                        preco = produto["preço"]

                        print(f"Nome de produto atualizado com sucesso, produto atualmente: ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")
                        return

                    elif opcao == "2":
                        print()
                        quantidade_atualizado = int(input("Digite a nova quantidade deste produto: "))
                        if quantidade_atualizado < 0:
                            raise ValueError("Quantidade deve ser um valor positivo.")
                        produto.update({"quantidade": quantidade_atualizado})

                        id = produto["id"]
                        nome = produto["nome"]
                        categoria = produto["categoria"]
                        qtd = produto["quantidade"]
                        preco = produto["preço"]

                        print(f"Quantidade de produto atualizada com sucesso, produto atualmente: ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")
                        return

                    elif opcao == "3":
                        print()
                        preco_atualizado = float(input("Digite o novo preço deste produto: "))
                        if preco_atualizado < 0:
                            raise ValueError("Preço deve ser um valor positivo.")
                        produto.update({"preço": preco_atualizado})

                        id = produto["id"]
                        nome = produto["nome"]
                        categoria = produto["categoria"]
                        qtd = produto["quantidade"]
                        preco = produto["preço"]

                        print(f"Preço de produto atualizado com sucesso, produto atualmente: ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")
                        return

                    elif opcao == "4":
                        print()
                        categoria_atualizado = input("Digite a nova categoria deste produto: ")
                        if not categoria_atualizado:
                            raise ValueError("Categoria não pode estar vazia.")
                        produto.update({"categoria": categoria_atualizado})

                        id = produto["id"]
                        nome = produto["nome"]
                        categoria = produto["categoria"]
                        qtd = produto["quantidade"]
                        preco = produto["preço"]

                        print(f"Categoria de produto atualizado com sucesso, produto atualmente: ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")
                        return

                    elif opcao == "5":
                        break

                    else:
                        print("Opção inválida. Tente novamente.")
                        print()
        print("Id não encontrado!")
    except ValueError as e:
        print(f"Erro: {e}")

def remover_produto():
    print()
    try:
        id_remover = int(input("Qual o id do produto que você deseja remover? "))

        for produto in lista_produtos:
            if id_remover == produto["id"]:

                id = produto["id"]
                nome = produto["nome"]
                categoria = produto["categoria"]
                qtd = produto["quantidade"]
                preco = produto["preço"]
                resp = input(f"Tem certeza que deseja remover o produto: ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco} \nResponda com sim ou não: ")

                if resp.lower() == "sim":
                    print()
                    lista_produtos.remove(produto)
                    print(f"Produto '{produto['nome']}' removido com sucesso!")
                    return
                else:
                    print("Produto não removido!")
                    return
        print("Id não encontrado!")
    except ValueError as e:
        print(f"Erro: {e}")

def buscar_produto():
    print()
    try:
        resp = int(input("Deseja pesquisar por ID(1) ou pelo nome(2) do produto? "))

        if resp == 1:
            id_entrada = int(input("Qual o ID do produto? "))
            print()

            for produto in lista_produtos:
                if id_entrada == produto["id"]:
                    id = produto["id"]
                    nome = produto["nome"]
                    categoria = produto["categoria"]
                    qtd = produto["quantidade"]
                    preco = produto["preço"]

                    print(f"Produto de ID {id_entrada} encontrado:")
                    print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")
                    return
            print("Nenhum produto foi encontrado a partir deste ID!")

        elif resp == 2:
            nome_entrada = input("Qual o nome do produto? ").lower()
            print()

            for produto in lista_produtos:
                if nome_entrada in produto["nome"].lower():
                    id = produto["id"]
                    nome = produto["nome"]
                    categoria = produto["categoria"]
                    qtd = produto["quantidade"]
                    preco = produto["preço"]

                    print(f"Produto de nome {nome_entrada} encontrado:")
                    print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {qtd}, Preço: {preco}")
                    return
            print("Nenhum produto foi encontrado a partir deste nome!")
        else:
            print("Opção inválida.")
    except ValueError as e:
        print(f"Erro: {e}")

produtos = carregar_dados()
menu()
