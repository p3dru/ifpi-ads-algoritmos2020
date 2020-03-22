#entrada
horas = float(input("Digite um valor em horas: "))
minutos = int(input("Digite um valor em minutos: "))
#processamento
min_total = (horas * 60) + minutos
#saída
print("O valor total em minutos é {:.2f}".format(min_total))
