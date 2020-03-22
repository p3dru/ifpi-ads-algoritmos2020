dia_1 = int(input("Digite o dia: "))
mes_1 = int(input("Digite o mes: "))
ano_1 = int(input("Digite o ano: "))
dia_2 = int(input("Digite o dia: "))
mes_2 = int(input("Digite o mes: "))
ano_2 = int(input("Digite o ano: "))
dia_3 = int(input("Digite o dia: "))
mes_3 = int(input("Digite o mes: "))
ano_3 = int(input("Digite o ano: "))
total_dias_1 = dia_1 + (mes_1 * 30) + (ano_1 * 365)
total_dias_2 = dia_2 + (mes_2 * 30) + (ano_2 * 365)
total_dias_3 = dia_3 + (mes_3 * 30) + (ano_3 * 365)
if total_dias_1 > total_dias_2 > total_dias_3:
    print(f"A data mais recente é {dia_1}/{mes_1}/{ano_1}")
elif total_dias_2 > total_dias_1 > total_dias_3:
    print(f"A data mais recente é {dia_2}/{mes_2}/{ano_2}")
elif total_dias_3 > total_dias_2 > total_dias_1:
    print(f"A data mais recente é {dia_3}/{mes_3}/{ano_3}")