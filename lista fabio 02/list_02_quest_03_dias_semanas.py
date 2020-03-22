#entrada
dias = int(input("Digite uma quantidade de dias: "))
#processamento
semanas = dias // 7
dias_restantes = dias % 7
#saida
print(f"{dias} dias correspondem à {semanas} semanas e {dias_restantes} dias.")