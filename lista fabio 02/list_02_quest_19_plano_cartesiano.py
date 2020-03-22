#entrada
x_1 = int(input("Distância do ponto x1: "))
y_1 = int(input("Distância do ponto y1: "))
x_2 = int(input("Distância do ponto x2: "))
y_2 = int(input("Distância do ponto y2: "))
#processamento
d = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2) ** 0.5)
#saida
print(f"A distância dos pontos é de {d} unidades de medida")
