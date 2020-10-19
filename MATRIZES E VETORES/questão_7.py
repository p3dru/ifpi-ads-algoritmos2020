vetor_a = []
vetor_b = []
quantidade_de_elementos = int(input("Quantidade de elementos: "))
for elemento in range(quantidade_de_elementos):
    vetor_a.append(int(input(f"Digite o valor para a posicao {elemento + 1}: ")))
for elemento in range(len(vetor_a)):
    if vetor_a[elemento] % 2 == 0:
        vetor_b.append(0)
    else:
        vetor_b.append(1)
print(vetor_a)
print(vetor_b)
