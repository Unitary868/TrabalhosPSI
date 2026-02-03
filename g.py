nomes = list()

while True:
    print("\n--- Gestor de Nomes (modos diferentes) ---")
    print("1 - Adicionar nome")
    print("2 - Substituir um nome existente")
    print("3 - Ordenar nomes A-Z")
    print("4 - Mostrar nome com mais letras")
    print("5 - Verificar se um nome se repete")
    print("6 - Limpar todos os nomes")
    print("7 - Comparar dois nomes (qual é maior)")
    print("0 - Sair")

    op = input("Opção: ")

    # 1 - Adicionar nome
    if op == "1":
        nome = input("Nome: ")
        nomes.append(nome)
        print("Nome adicionado.")

    # 2 - Substituir nome
    elif op == "2":
        antigo = input("Nome antigo: ")
        novo = input("Novo nome: ")

        if antigo in nomes:
            pos = nomes.index(antigo)
            nomes.remove(antigo)
            nomes.insert(pos, novo)
            print("Nome substituído.")
        else:
            print("Nome não encontrado.")

    # 3 - Ordenar A-Z
    elif op == "3":
        if len(nomes) == 0:
            print("Lista vazia.")
        else:
            nomes.sort()
            print("Lista ordenada.")

    # 4 - Mostrar nome com mais letras
    elif op == "4":
        if len(nomes) == 0:
            print("Lista vazia.")
        else:
            maior = ""
            i = 0
            while i < len(nomes):
                nome = nomes.pop(0)
                nomes.append(nome)

                if len(nome) > len(maior):
                    maior = nome

                i = i + 1

            print("Nome com mais letras:", maior)

    # 5 - Verificar se um nome se repete
    elif op == "5":
        nome = input("Nome a verificar: ")

        if nomes.count(nome) > 1:
            print("Esse nome está repetido.")
        else:
            print("Esse nome não está repetido.")

    # 6 - Limpar todos os nomes
    elif op == "6":
        nomes.clear()
        print("Todos os nomes foram removidos.")

    # 7 - Comparar dois nomes
    elif op == "7":
        nome1 = input("Primeiro nome: ")
        nome2 = input("Segundo nome: ")

        if len(nome1) > len(nome2):
            print("O primeiro nome é maior.")
        elif len(nome2) > len(nome1):
            print("O segundo nome é maior.")
        else:
            print("Os nomes têm o mesmo tamanho.")

    # 0 - Sair
    elif op == "0":
        print("Programa terminado.")
        break

    else:
        print("Opção inválida.")
