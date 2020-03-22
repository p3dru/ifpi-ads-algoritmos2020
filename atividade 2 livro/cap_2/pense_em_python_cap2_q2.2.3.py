#resolução unica
hora_de_saida = 6
minuto_de_saida = 52
total_de_segundos = (6 * 3600) + (52 * 60)
km_1 = (8 * 60) + 15
km_3 = ((7 * 60) + 12) * 3
segundos_totais = total_de_segundos + km_1 + km_3 + km_1
horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = (segundos_totais % 3600) % 60
print(f"Chegará em casa às {horas} horas, {minutos} minutos e {segundos} segundos")

#fiquei feliz por responder essa em pouco tempo