def CamelCase(palavra):
    contador = 0
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(palavra)):
        if palavra[i] in maiusculas:
            contador += 1
    print(contador + 1)


string = input()
CamelCase(string)

