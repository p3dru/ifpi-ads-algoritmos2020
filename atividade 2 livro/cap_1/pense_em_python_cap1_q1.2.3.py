#tempo por milha = quantidade e milhas no mesmo período de tempo
km = 10
milhas = 10 * 1.61
minutos = 42
segundos = 42
print(f"O tempo por milha é {milhas} em {minutos} minutos e {segundos} segundos")
horas = ((minutos * 60) + segundos) / 3600
velocidade_media = milhas / horas
print(f"A velocidade media é de {velocidade_media:.2f} mph")