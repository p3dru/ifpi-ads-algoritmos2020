def eh_par(numero):
    contador = 0
    if numero % 2 == 0:
        contador += 1
    return contador

def eh_impar(numero):
    contador = 0
    if numero % 2 != 0:
        contador += 1
    return contador

def eh_positivo(numero):
    contador = 0
    if numero >= 0:
        contador += 1
    return contador

def eh_negativo(numero):
    contador = 0
    if numero < 0:
        contador += 1
    return contador

def apresentar_media(vetor):
    total = media = 0
    for numeros in range(len(vetor)):
        total += vetor[numeros]
    media = total / len(vetor)
    print(f"A média dos valores em vetor é {media:.2f}")


casos = int(input("Digite quantos numeros pretende inserir: "))
print()
vetor = [-1] * casos
pares = impares = negativos = positivos = 0
for elemento in range(len(vetor)):
    vetor[elemento] = int(input(f"Digite o valor da posição {elemento}: "))
    pares += eh_par(vetor[elemento])
    impares += eh_impar(vetor[elemento])
    negativos += eh_negativo(vetor[elemento])
    positivos += eh_positivo(vetor[elemento])
print()
print(vetor)
print("Foram digitados:\n"
      f"{pares} números pares\n"
      f"{impares} números impares\n"
      f"{negativos} números negativos\n"
      f"{positivos} números positivos\n")

pares = impares = negativos = positivos = 0
for posicao in range(len(vetor)):
    if posicao % 2 == 0:
        vetor[posicao] = vetor[posicao] * 2
    else:
        vetor[posicao] = vetor[posicao] / 2
    pares += eh_par(vetor[posicao])
    impares += eh_impar(vetor[posicao])
    negativos += eh_negativo(vetor[posicao])
    positivos += eh_positivo(vetor[posicao])
    
print()
print(vetor)
print("Depois da transformação temos:\n"
      f"{pares} números pares\n"
      f"{impares} números impares\n"
      f"{negativos} números negativos\n"
      f"{positivos} números positivos\n")

apresentar_media(vetor)


    
    
