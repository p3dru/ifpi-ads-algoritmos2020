def verificar_se_há_iguais(vetor):
    contador = 0
    for elemento in range(len(vetor)):
        if vetor[elemento] in vetor[elemento + 1:]:
            contador += 1
    if contador != 0:
        print("Há elementos iguais no vetor")
    else:
        print("Não há elementos iguais no vetor")
vetor_a = []
quantidade = int(input("Digite a quantidade de elementos do vetor: "))
for elementos in range(quantidade):
    vetor_a.append(input("Digite o elemento: "))
verificar_se_há_iguais(vetor_a)
    
