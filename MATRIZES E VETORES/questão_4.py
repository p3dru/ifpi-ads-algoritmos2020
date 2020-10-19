def verificar_intersecção(vetor1, vetor2):
    vetor_d = []
    for elemento in range(len(vetor2)):
        if vetor1[elemento] in vetor2:
            vetor_d.append(vetor1[elemento])
    return vetor_d

vetor_a = []
vetor_b = []
quantidade = int(input("Digite a quantidade de elementos dos vetores: "))
for elemento in range(quantidade):
    vetor_a.append(input(f"Digite o elemento {elemento} do vetor a: "))
for elemento in range(quantidade):
    vetor_b.append(input(f"Digite o elemento {elemento} do vetor b: "))
vetor_c = vetor_a + vetor_b
vetor_d = verificar_intersecção(vetor_a, vetor_b)
print(f"Vetor a = {vetor_a}")
print(f"Vetor b = {vetor_b}")
print(f"Vetor c = {vetor_c}")
print(f"Vetor d = {vetor_d}")
