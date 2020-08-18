lista = [] #cria lista
for volta in range(0, 5): #cria laço for de 5 vezes
    numero = int(input("Digite um número: ")) #pede números 5 vezes
    if volta == 0 or numero > lista[-1]: #avalia se é a primeira volta ou se o número é maior que o último número da lista
        lista.append(numero) #se for, insere no final
        print("Adicionado ao final da lista") #exibe que foi inserido no final
    else: #se não
        posicao = 0 #posição recebe o valor 0 de começo
        while posicao < len(lista): #enquanto a posição for menor que o tamanho total da lista
            if numero <= lista[posicao]: #se o número for menor ou igual á posição indicada por posição na lista
                lista.insert(posicao, numero) #a lista recebe na posição da volta, o número, fastando pra frente os outros
                print(f"Adicionado na posição {posicao}") #indica a posição que tá
                break #quebra o código pra não printar infinitas vezes
            posicao += 1 #posição tem valor atualizado
print("-+" * 40)
print(f"Os valores digitados em ordem foram {lista}")
