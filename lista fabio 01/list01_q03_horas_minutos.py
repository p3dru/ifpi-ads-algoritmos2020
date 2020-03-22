#entrada
minutos = int(input("Digite um valor em minutos: "))
#processamento
horas = minutos // 60
minutos_real = minutos % 60
#saida
print("O valor digitado em horas e minutos é: {} hora(s) e {} minuto(s)".format(horas, minutos_real))