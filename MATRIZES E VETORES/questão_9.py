def vetor_pronto(x):
    vetor = []
    for elementos in range(x):
        vetor.append(int(input("Digite um número: ")))
    return vetor

def organizar_vetor(string):
    vetor = sorted(string)
    return vetor

tamanho = int(input("Digite o tamanho do vetor: "))
vetor = vetor_pronto(tamanho)
vetor = organizar_vetor(vetor)
print()
print(f"Vetor organizado de forma crescente: {vetor}")
