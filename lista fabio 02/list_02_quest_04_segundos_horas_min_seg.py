#entrada
segundos = int(input("Digite uma quantidade de segundos: "))
#processamento
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = (segundos % 3600) % 60
#saida
print(f"{segundos} segundos equivalem à {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")