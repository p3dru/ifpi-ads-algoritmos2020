expressao = input("Digite a expressão: ")
lista_expressao = lista_sad = lista_happy = []
posicao_sad = []
posicao_happy = []
contador = 0
for posicao, simbolo in enumerate(expressao):
    lista_expressao.append(simbolo)
for posicao, simbolo in enumerate(lista_expressao):
    if lista_expressao[posicao] == "(":
        posicao_sad.append(posicao)
    if lista_expressao[posicao] == ")":
        posicao_happy.append(posicao)
        
if len(posicao_sad) != len(posicao_happy):
    print("Expressão Inválida!")
else:
    for elemento in range(len(posicao_sad)):
        if posicao_sad[elemento] > posicao_happy[elemento]:
            print("Expressão Inválida!")
            break
        elif posicao_sad[elemento] < posicao_happy[elemento]:
            contador += 1
            if contador == len(posicao_sad):

                print("Expressão Válida!")

"""
print()
print(lista_expressao)
print(posicao_sad)
print(posicao_happy)
"""
