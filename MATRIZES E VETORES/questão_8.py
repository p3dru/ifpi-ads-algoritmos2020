def verificar_maior(vetor):
    maior = vetor[0]
    posicao = 0
    for elemento in range(len(vetor)):
        if vetor[elemento] > maior:
            maior = vetor[elemento]
            posicao = elemento
    print(f"O maior valor do vetor é {maior} na posição {posicao}")

def verificar_menor(vetor):
    menor = vetor[0]
    posicao = 0
    for elemento in range(len(vetor)):
        if vetor[elemento] < menor:
            menor = vetor[elemento]
            posicao = elemento
    print(f"O maior valor do vetor é {menor} na posição {posicao}")

quantidade = int(input("Digite a quantidade de elementos para o vetor: "))
vetor = []
for elementos in range(quantidade):
    vetor.append(int(input("Digite um número: ")))
print(vetor)
verificar_maior(vetor)
verificar_menor(vetor)

                 
