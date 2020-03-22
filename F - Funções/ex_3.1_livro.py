def right_justify(x):
    quantidade_de_espacos = 70 - len(x)
    linha = " " * quantidade_de_espacos
    print(linha + x)

palavra = input("Digite uma palavra: ")
right_justify(palavra)

