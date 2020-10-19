def inverter_vetor(vetor):
    vetor_invertido = vetor[::-1]
    return vetor_invertido


vetor_a = []
vetor_b = []
quantidade = int(input("Quantidade de elementos: "))
for elementos in range(quantidade):
    vetor_a.append(input("Digite o elemento: "))
vetor_b = inverter_vetor(vetor_a)
print(vetor_a)
print(vetor_b)
