def inserir_valor_na_lista(lista):
    valores = int(input("Digite quantos elementos deseja inserir na lista: "))
    contador = 0
    while contador < valores:
        elemento = int(input("Digite o elemento a ser inserido: "))
        lista.append(elemento)
        contador += 1
    return lista

def mostrar_valor_na_posicao(lista):
    tamanho = len(lista) - 1
    posicao = int(input(f"Digite a posição entre 0 e {tamanho} para exibir o elemento do index: "))
    print(f"O elemento da posição {posicao} é {lista[posicao]}")

def remover_de_posicao_especifica(lista):
    posicao = int(input("Digite a posição na qual você deseja excluir: "))
    lista.pop(posicao)
    return lista

def inserir_valor_em_posicao_especifica(lista):
    tamanho = len(lista)
    algarismo = int(input("Digite o número que deseja inserir: "))
    posicao = int(input(f"Digite a posicao que deseja inserir (Limite: {tamanho + 1}): "))
    lista.insert(posicao, algarismo)
    return lista

def elementos_index_par(lista):
    pares = []
    for elementos in range(len(lista)):
        if elementos % 2 == 0:
            pares.append(lista[elementos])
    print(pares)

def elementos_index_impar(lista):
    impares = []
    for elementos in range(len(lista)):
        if elementos % 2 != 0:
            impares.append(lista[elementos])
    print(impares)

def elementos_primos(lista):
    numeros_primos = []
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for elemento in range(len(lista)):
        if lista[elemento] in primos:
            numeros_primos.append(lista[elemento])
    print(numeros_primos)

def elementos_pares(lista):
    pares = []
    for elementos in lista:
        if elementos % 2 == 0:
            pares.append(elementos)
    print(pares)

def elementos_impares(lista):
    impares = []
    for elementos in lista:
        if elementos % 2 != 0:
            impares.append(elementos)
    print(impares)

def exibir_index_de_algarismos_0(lista):
    index = []
    contador = 0
    for elementos in range(len(lista)):
        if lista[elementos] == 0:
            index.append(contador)
        contador += 1
    print(index)

def exibir_elementos_positivos(lista):
    positivos = []
    for elemento in lista:
        if elemento >= 0:
            positivos.append(elemento)
    print(positivos)

def exibir_elementos_negativos(lista):
    negativos = []
    for elemento in lista:
        if elemento < 0:
            negativos.append(elemento)
    print(negativos)

def exibir_media_de_valores(lista):
    total = 0
    elementos = len(lista)
    for numeros in range(elementos):
        total += lista[numeros]
    media = total / elementos
    print(f"A média dos valores digitados é {media:.2f}")

def quantas_vezes_o_numero_apareceu(lista):
    numero = int(input("Número que deseja pesquisar incidências: "))
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador += 1
    if contador == 1:
        print(f"A incidência do número {numero} ocorre {contador} vez")
    else:
        print(f"A incidência do número {numero} ocorre {contador} vezes")

def dobrar_valores_dos_elementos(lista):
    for elemento in range(len(lista)):
        lista[elemento] = lista[elemento] * 2
    return lista
        
def dividir_pela_metade(lista):
    for elemento in range(len(lista)):
        lista[elemento] = lista[elemento] / 2
    return lista

def multiplicar_pelo_numero_que_desejar(lista):
    numero = int(input("Digite o número: "))
    for elemento in range(len(lista)):
        lista[elemento] = lista[elemento] * numero
    return lista

def dividir_pelo_numero_que_desejar(lista):
    numero = int(input("Digite o número: "))
    for elementos in range(len(lista)):
        lista[elementos] = lista[elementos] / numero
    return lista

def multiplos_do_numero(lista):
    numero = int(input("Digite o número: "))
    multiplos = []
    for elemento in lista:
        if elemento % numero == 0 and elemento > 0:
            multiplos.append(elemento)
    print(multiplos)

def transformar_em_int(lista):
    for elementos in range(len(lista)):
        lista[elementos] = int(lista[elementos])
    return lista


print("Bem vindo usuário, abaixo teremos algumas opções para você se divertir com listas: \n"
      "\n"
      "Opções:\n"
      "1- Inserir novos valores na lista\n"
      "2- Mostrar valor na posição que desejar\n"
      "3- Remover elemento do final\n"
      "4- Remover elemento do inicio\n"
      "5- Remover elemento de uma posição específica\n"
      "6- Inserir valor em uma posição específica\n"
      "7- Exibir apenas elementos de index par\n"
      "8- Exibir apenas elementos de index ímpar\n"
      "9- Exibir apenas elementos primos\n"
      "10- Exibir apenas elementos ímpares\n"
      "11- Exibir apenas elementos pares\n"
      "12- Exibir index de elementos = 0\n"
      "13- Exibir elementos positivos\n"
      "14- Exibir elementos negatios\n"
      "15- Exibir media de valores digitados\n"
      "16- Verificar quantas vezes um número apareceu\n"
      "17- Dobrar todos os valores\n"
      "18- Dividir todos os valores pela metade\n"
      "19- Multiplicar, pelo número que você desejar, todos os valores de lista\n"
      "20- Dividir valores pelo número que você desejar\n"
      "21- Exibir todos os valores múltiplos do número que desejar\n"
      "22- Transformar todos os números em inteiros (sem arredondamento)\n"
      "23- Resetar a lista\n"
      "24- Exibir lista\n"
      "0- Para sair\n")

numeros = []
opcao = int(input("Opção desejada: "))
while opcao != 0:
    if opcao == 1:
        numeros = inserir_valor_na_lista(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 2:
        mostrar_valor_na_posicao(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 3:
        numeros.pop()
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 4:
        numeros.pop(0)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 5:
        numeros = remover_de_posicao_especifica(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 6:
        numeros = inserir_valor_em_posicao_especifica(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 7:
        elementos_index_par(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 8:
        elementos_index_impar(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 9:
        elementos_primos(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 10:
        elementos_impares(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 11:
        elementos_pares(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 12:
        exibir_index_de_algarismos_0(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 13:
        exibir_elementos_positivos(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 14:
        exibir_elementos_negativos(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 15:
        exibir_media_de_valores(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 16:
        quantas_vezes_o_numero_apareceu(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 17:
        numeros = dobrar_valores_dos_elementos(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 18:
        numeros = dividir_pela_metade(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 19:
        numeros = multiplicar_pelo_numero_que_desejar(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 20:
        numeros = dividir_pelo_numero_que_desejar(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 21:
        multiplos_do_numero(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 22:
        numeros = transformar_em_int(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 23:
        numeros = []
        print()
        opcao = int(input("Opção desejada: "))
    elif opcao == 24:
        print(numeros)
        print()
        opcao = int(input("Opção desejada: "))
    else:
        print("Opção inválida")
        print()
        opcao = int(input("Opção desejada: "))
print()
print("+=" * 14)
print("Obrigado por usar o programa")      
print("+=" * 14)
