"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de inserir, apagar e lista.
não permita que o programa quebre com erros de indice inexistente na lista.
"""

try:
    lista_de_compras = []
    print(lista_de_compras)

    while True:
        print("\nLista de Compras:")
        for idx, item in enumerate(lista_de_compras):
            print(f"{idx}: {item}")

        print("\nOpções:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Sair")

        escolha = input("Escolha uma opção (1-3): ")

        if escolha == '1':
            item = input("Digite o nome do item para adicionar: ")
            lista_de_compras.append(item)
            print(f"{item} adicionado à lista.")

        elif escolha == '2':
            try:
                indice = int(input("Digite o índice do item para remover: "))
                item_removido = lista_de_compras.pop(indice)
                print(f"{item_removido} removido da lista.")
            except (ValueError, IndexError):
                print("Índice inválido. Tente novamente.")

        elif escolha == '3':
            print("Saindo do programa.")
            break
    
        else:
            print("Opção inválida. Tente novamente.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")