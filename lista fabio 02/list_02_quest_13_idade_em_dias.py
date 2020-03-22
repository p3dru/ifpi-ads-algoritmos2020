#entrada
anos = int(input("Quantos anos tens? "))
meses = int(input("Quantos meses tens? "))
dias = int(input("E dias..? "))
#processamento
dias_totais = (anos * 365) + (meses * 30) + dias
#saida
print(f"Você já viveu ao todo {dias_totais} dias")