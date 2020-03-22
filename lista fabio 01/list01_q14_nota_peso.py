#entrada
nota_1 = float(input("Primeira nota: "))
peso_1 = int(input("Primeiro peso: "))
nota_2 = float(input("Segunda nota: "))
peso_2 = int(input("Segundo peso: "))
nota_3 = float(input("Terceira nota: "))
peso_3 = int(input("Terceiro peso: "))
#processamento
soma_de_pesos = peso_3 + peso_2 + peso_1
ponderada = (((peso_1 * nota_1) + (peso_2 * nota_2) + (peso_3 * nota_3)) / soma_de_pesos)
#saida
print(f"A media ponderada é de {ponderada:.2f}")