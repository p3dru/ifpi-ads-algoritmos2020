hora_inicio = int(input("Hora de inicio do jogo: "))
minuto_inicio = int(input("Minuto de inicio do jogo: "))
hora_fim = int(input("Hora de término do jogo: "))
minuto_fim = int(input("Minuto de término do jogo: "))
horas_jogadas = 0
if hora_inicio > hora_fim:
    horas_jogadas = (24 - hora_inicio) + hora_fim
else:
    hora_jogadas = hora_fim - hora_inicio
if minuto_inicio > minuto_fim:
    minutos_jogados = (60 - minuto_inicio) + minuto_fim
else:
    minutos_jogados = minuto_fim - minuto_inicio
print(f"O total jogado foi de {horas_jogadas}:{minutos_jogados}")