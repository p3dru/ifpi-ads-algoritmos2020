#entradas
minutos = int(input("Digite uma quantidade de minutos: "))
#processamento
dias = (minutos // 60) // 24
horas = (minutos // 60) % 24
minutos_restantes = minutos % 60
#saida
print(f"{minutos} minutos correspondem à {dias} dias, {horas} horas e {minutos_restantes} minutos")