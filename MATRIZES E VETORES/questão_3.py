vetor_a = []
vetor_b = []
quantidade = int(input("Digite a quantidade de elementos dos vetores: "))
for elementos in range(quantidade):
    vetor_a.append(input(f"Digite o elemento {elementos} do vetor a: "))
for elementos in range(quantidade):
    vetor_b.append(input(f"Digite o elemento {elementos} do vetor b: "))
vetor_c = vetor_a + vetor_b
print(f"Vetor a = {vetor_a}")
print(f"Vetor b = {vetor_b}")
print(f"Vetor c = {vetor_c}")
