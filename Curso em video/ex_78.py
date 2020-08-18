lista = [] #cria lista
maior = menor = 0 #atribui o valor 0 à maior e menor
for valores in range(0, 5): #para os valores no alcance de 0 à 5 (5 vezes)
    lista.append(int(input("Digite um número: "))) #para cada volta, adicionar um valor dado à lista
    if valores == 0: #se a volta(valores) for igual a 0
        maior = menor = lista[valores] #maior e menor recebem o ítem contido na posição descrita [0]
    else: #se não
        if lista[valores] > maior: #se o valor contido na posição valores for maior que o maior número
            maior = lista[valores] #o valor de maior se atualiza para este valor que está na posição valores
        if lista[valores] < menor: #se o valor contido na posição valores for menor que o menor número
            menor = lista[valores] #o valor de menor se atualiza para este valor que está na posição valores
print(f"Você digitou os valores {lista}") #printa a lista
print(f"O maior valor digitado foi {maior}, nas posições ",end="") #informa o maior valor encontrado sem quebra de linha para informar outros valores
for posicao, numero in enumerate(lista): #para cada posição e números na numeração de lista
    if numero == maior: #se o número (da lista) for igual ao maior número
        print(f"{posicao}... ",end="") #printar a posicao sem quebra de linha
print() #quebra a linha
print(f"O menor valor digitado foi {menor}, nas posições ",end="") #informa o menor valor encontrado na lista sem quebra de linha para informar novos valores
for posicao, numero in enumerate(lista): #para cada posição e número na numeração de lista
    if numero == menor: #se número for igual ao menor
        print(f"{posicao}... ",end="") #printar a posição sem quebra de linha
print() #quebra de linha
