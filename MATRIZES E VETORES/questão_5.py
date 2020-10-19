def s(vetor):
    contador_c = solucao = 0
    contador_d = 19
    while contador_c < 10:
        solucao += (vetor[contador_c] - vetor[contador_d]) ** 2
        contador_c += 1
        contador_d -= 1
    return solucao
        
    
vetor = []
for elementos in range(20):
    vetor.append(int(input(f"Digite o valor da posição {elementos+1}: ")))
soma = s(vetor)
print(f"A soma da expressão S é {soma}")
